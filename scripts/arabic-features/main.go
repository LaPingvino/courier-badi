// Command arabic-features generates the OpenType feature code needed for correct
// Arabic shaping directly from a UFO source, and writes it into the UFO's
// features.fea between managed markers.
//
// Why this exists: Arabic joining is subtle and easy to get wrong by hand. The
// two classic mistakes are (1) forgetting positional forms for the "rarer"
// extended letters that DO have glyphs in the font but no rules, and (2)
// writing lam-alef ligatures against the base letters (uni0644 uni0627) even
// though HarfBuzz applies init/medi/fina BEFORE rlig, so by the time the
// ligature lookup runs the glyphs are already lam.init/alef.fina and the rule
// never matches. This tool avoids both:
//
//   - It reads the actual glyph inventory of the UFO and only emits a
//     substitution when both the source and target glyphs exist.
//   - It derives every base -> {isol,init,medi,fina} mapping and every lam-alef
//     ligature from the Unicode Character Database (see arabicdata.go), and
//     falls back to the "<base>.init/.medi/.fina" naming convention for
//     extended letters that have no Unicode presentation-form codepoint
//     (e.g. Pashto U+0681, U+0685).
//   - It writes lam-alef ligatures against the POSITIONAL forms so they fire.
//
// The generated block is delimited by markers so hand-written features around
// it are preserved. Run:
//
//	go run ./scripts/arabic-features --ufo sources/CourierBadi-Regular.ufo
//
// Use --check to fail (non-zero exit) if the file is not up to date, and
// --stdout to print the generated block without touching the file.
package main

import (
	"encoding/xml"
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"unicode"
)

const (
	beginMarker = "# >>> BEGIN GENERATED ARABIC FEATURES (scripts/arabic-features) >>>"
	endMarker   = "# <<< END GENERATED ARABIC FEATURES <<<"
)

// font is the subset of a UFO we care about: which glyph names exist and which
// codepoint each cmapped glyph carries.
type font struct {
	names map[string]bool // set of all glyph names
	cmap  map[rune]string // codepoint -> glyph name
}

func (f *font) has(name string) bool { return f.names[name] }

// glyphFor returns the glyph name for codepoint cp if a glyph with that
// codepoint exists, otherwise the conventional "uniXXXX" name if such a glyph
// exists, otherwise "".
func (f *font) glyphFor(cp rune) string {
	if n, ok := f.cmap[cp]; ok {
		return n
	}
	if n := uniName(cp); f.has(n) {
		return n
	}
	return ""
}

func uniName(cp rune) string { return fmt.Sprintf("uni%04X", cp) }

// --- UFO loading ---------------------------------------------------------

type plistDict struct {
	Keys []string `xml:"dict>key"`
	Vals []string `xml:"dict>string"`
}

type glif struct {
	Unicodes []struct {
		Hex string `xml:"hex,attr"`
	} `xml:"unicode"`
}

func loadFont(ufo string) (*font, error) {
	contents := filepath.Join(ufo, "glyphs", "contents.plist")
	data, err := os.ReadFile(contents)
	if err != nil {
		return nil, err
	}
	var d plistDict
	if err := xml.Unmarshal(data, &d); err != nil {
		return nil, fmt.Errorf("parse contents.plist: %w", err)
	}
	if len(d.Keys) != len(d.Vals) {
		return nil, fmt.Errorf("contents.plist: %d keys vs %d values", len(d.Keys), len(d.Vals))
	}
	f := &font{names: make(map[string]bool), cmap: make(map[rune]string)}
	for i, name := range d.Keys {
		f.names[name] = true
		gfile := filepath.Join(ufo, "glyphs", d.Vals[i])
		gdata, err := os.ReadFile(gfile)
		if err != nil {
			return nil, err
		}
		var g glif
		if err := xml.Unmarshal(gdata, &g); err != nil {
			return nil, fmt.Errorf("parse %s: %w", gfile, err)
		}
		for _, u := range g.Unicodes {
			var cp rune
			if _, err := fmt.Sscanf(u.Hex, "%X", &cp); err == nil {
				if _, dup := f.cmap[cp]; !dup {
					f.cmap[cp] = name
				}
			}
		}
	}
	return f, nil
}

// --- feature generation --------------------------------------------------

func isArabic(cp rune) bool {
	switch {
	case cp >= 0x0600 && cp <= 0x06FF: // Arabic
	case cp >= 0x0750 && cp <= 0x077F: // Arabic Supplement
	case cp >= 0x08A0 && cp <= 0x08FF: // Arabic Extended-A
	default:
		return false
	}
	return true
}

// positionalTarget returns the glyph name for base glyph `name` (codepoint
// `cp`) in position `pos` ("init"/"medi"/"fina"), or "" if none exists.
func positionalTarget(f *font, cp rune, name, pos string) string {
	// 1. Unicode presentation form for this base+position.
	if fs, ok := arabicForms[cp]; ok {
		var formCP rune
		switch pos {
		case "init":
			formCP = fs.Init
		case "medi":
			formCP = fs.Medi
		case "fina":
			formCP = fs.Fina
		}
		if formCP != 0 {
			if g := f.glyphFor(formCP); g != "" {
				return g
			}
		}
	}
	// 2. Naming-convention fallback for extended letters (e.g. uni0681.init).
	if cand := name + "." + pos; f.has(cand) {
		return cand
	}
	return ""
}

type rule struct{ from, to string }

func joiningRules(f *font, pos string) []rule {
	var cps []rune
	for cp := range f.cmap {
		if isArabic(cp) {
			cps = append(cps, cp)
		}
	}
	sort.Slice(cps, func(i, j int) bool { return cps[i] < cps[j] })
	var rules []rule
	for _, cp := range cps {
		name := f.cmap[cp]
		to := positionalTarget(f, cp, name, pos)
		if to != "" && to != name {
			rules = append(rules, rule{name, to})
		}
	}
	return rules
}

// lamAlefRules emits ligatures against the positional forms of lam and alef,
// because rlig runs after the joining features have already substituted them.
func lamAlefRules(f *font) (isol, fina []rule) {
	lamInit := positionalTarget(f, 0x0644, glyphOr(f, 0x0644), "init")
	lamMedi := positionalTarget(f, 0x0644, glyphOr(f, 0x0644), "medi")
	if lamInit == "" && lamMedi == "" {
		return nil, nil
	}
	for _, la := range lamAlefLigs {
		alefFina := positionalTarget(f, la.Alef, glyphOr(f, la.Alef), "fina")
		if alefFina == "" {
			continue
		}
		ligIsol := f.glyphFor(la.LigIsol)
		ligFina := f.glyphFor(la.LigFina)
		if lamInit != "" && ligIsol != "" {
			isol = append(isol, rule{lamInit + " " + alefFina, ligIsol})
		}
		if lamMedi != "" && ligFina != "" {
			fina = append(fina, rule{lamMedi + " " + alefFina, ligFina})
		}
	}
	return isol, fina
}

func glyphOr(f *font, cp rune) string {
	if n, ok := f.cmap[cp]; ok {
		return n
	}
	return uniName(cp)
}

// markClass returns all glyphs whose codepoint is a non-spacing / enclosing
// mark, for the GDEF mark class. The Arabic tashkil presentation forms in
// U+FE70..U+FE7F are excluded: although Unicode gives them category Mn, they
// are standalone spacing forms, not combining marks, and fontbakery flags them
// if they appear in the GDEF mark class.
func markClass(f *font) []string {
	var marks []string
	for cp, name := range f.cmap {
		if cp >= 0xFE70 && cp <= 0xFE7F {
			continue
		}
		if unicode.In(cp, unicode.Mn, unicode.Me) {
			marks = append(marks, name)
		}
	}
	sort.Strings(marks)
	return marks
}

// simplePair emits a single-substitution list if any glyph pairs exist.
func simplePairs(f *font, pairs [][2]rune) []rule {
	var rules []rule
	for _, p := range pairs {
		from := f.glyphFor(p[0])
		to := f.glyphFor(p[1])
		if from != "" && to != "" && from != to {
			rules = append(rules, rule{from, to})
		}
	}
	return rules
}

func namePairs(f *font, pairs [][2]string) []rule {
	var rules []rule
	for _, p := range pairs {
		if f.has(p[0]) && f.has(p[1]) {
			rules = append(rules, rule{p[0], p[1]})
		}
	}
	return rules
}

func writeLookup(b *strings.Builder, name string, rules []rule) bool {
	if len(rules) == 0 {
		return false
	}
	fmt.Fprintf(b, "lookup %s {\n", name)
	for _, r := range rules {
		fmt.Fprintf(b, "    sub %s by %s;\n", ref(r.from), r.to)
	}
	fmt.Fprintf(b, "} %s;\n\n", name)
	return true
}

// ref back-slash escapes a (possibly multi-glyph) left-hand side.
func ref(s string) string {
	parts := strings.Fields(s)
	for i, p := range parts {
		parts[i] = "\\" + p
	}
	return strings.Join(parts, " ")
}

func generate(f *font) string {
	var b strings.Builder
	b.WriteString(beginMarker + "\n")
	b.WriteString("# Generated by scripts/arabic-features. Do not edit by hand;\n")
	b.WriteString("# edit the tool and regenerate. Base<->form mapping and lam-alef\n")
	b.WriteString("# ligatures come from the Unicode Character Database.\n\n")

	b.WriteString("languagesystem DFLT dflt;\n")
	b.WriteString("languagesystem arab dflt;\n")
	b.WriteString("languagesystem arab ARA;\n")
	b.WriteString("languagesystem arab FAR;\n")
	b.WriteString("languagesystem arab URD;\n\n")

	// GDEF mark class.
	marks := markClass(f)
	if len(marks) > 0 {
		b.WriteString("@GDEF_Marks = [\n")
		for i, m := range marks {
			if i%8 == 0 {
				b.WriteString("    ")
			}
			b.WriteString("\\" + m + " ")
			if i%8 == 7 {
				b.WriteString("\n")
			}
		}
		b.WriteString("\n];\n\n")
		b.WriteString("table GDEF {\n")
		b.WriteString("    GlyphClassDef , , @GDEF_Marks, ;\n")
		b.WriteString("} GDEF;\n\n")
	}

	// Joining features. HarfBuzz applies these per glyph based on joining state.
	initRules := joiningRules(f, "init")
	mediRules := joiningRules(f, "medi")
	finaRules := joiningRules(f, "fina")

	var lookups strings.Builder
	hasInit := writeLookup(&lookups, "arabicInit", initRules)
	hasMedi := writeLookup(&lookups, "arabicMedi", mediRules)
	hasFina := writeLookup(&lookups, "arabicFina", finaRules)

	// Required lam-alef ligatures against positional forms.
	ligIsol, ligFina := lamAlefRules(f)
	ligRules := append(append([]rule{}, ligIsol...), ligFina...)
	hasRlig := writeLookup(&lookups, "arabicLamAlef", ligRules)

	// Small extras carried over from the project, guarded by glyph existence.
	loclRules := namePairs(f, [][2]string{
		{"uni06F4", "uni06F4.urdu"},
		{"uni06F7", "uni06F7.urdu"},
	})
	loclRules = append(loclRules, simplePairs(f, [][2]rune{{0x06F6, 0x0666}})...)
	hasLocl := writeLookup(&lookups, "arabicLoclUrdu", loclRules)

	dligRules := namePairs(f, [][2]string{
		{"period", "period.arabic"},
		{"colon", "colon.arabic"},
		{"exclam", "exclam.arabic"},
	})
	hasDlig := writeLookup(&lookups, "arabicDligPunct", dligRules)

	b.WriteString(lookups.String())

	// Feature blocks referencing the lookups (arab script only; that is what
	// the Arabic shaper selects).
	featBlock := func(tag string, names ...string) {
		fmt.Fprintf(&b, "feature %s {\n", tag)
		fmt.Fprintf(&b, "    script arab;\n")
		for _, n := range names {
			fmt.Fprintf(&b, "    lookup %s;\n", n)
		}
		fmt.Fprintf(&b, "} %s;\n\n", tag)
	}
	if hasInit {
		featBlock("init", "arabicInit")
	}
	if hasMedi {
		featBlock("medi", "arabicMedi")
	}
	if hasFina {
		featBlock("fina", "arabicFina")
	}
	if hasRlig {
		featBlock("rlig", "arabicLamAlef")
	}
	if hasLocl {
		fmt.Fprintf(&b, "feature locl {\n    script arab;\n    language URD exclude_dflt;\n    lookup arabicLoclUrdu;\n} locl;\n\n")
	}
	if hasDlig {
		featBlock("dlig", "arabicDligPunct")
	}

	b.WriteString(endMarker + "\n")
	return b.String()
}

// --- splice into features.fea -------------------------------------------

func splice(existing, block string) string {
	begin := strings.Index(existing, beginMarker)
	end := strings.Index(existing, endMarker)
	if begin >= 0 && end > begin {
		end += len(endMarker)
		// Trim a trailing newline right after the end marker to avoid growth.
		tail := existing[end:]
		return existing[:begin] + strings.TrimRight(block, "\n") + tail
	}
	// No markers yet: append.
	sep := ""
	if len(existing) > 0 && !strings.HasSuffix(existing, "\n\n") {
		sep = "\n"
	}
	return existing + sep + block
}

func main() {
	ufo := flag.String("ufo", "sources/CourierBadi-Regular.ufo", "path to the UFO source")
	toStdout := flag.Bool("stdout", false, "print generated block to stdout, do not modify the UFO")
	check := flag.Bool("check", false, "exit non-zero if features.fea is not up to date")
	flag.Parse()

	f, err := loadFont(*ufo)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
	block := generate(f)

	if *toStdout {
		fmt.Print(block)
		return
	}

	feaPath := filepath.Join(*ufo, "features.fea")
	existing, err := os.ReadFile(feaPath)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
	updated := splice(string(existing), block)

	if *check {
		if updated != string(existing) {
			fmt.Fprintln(os.Stderr, feaPath, "is out of date; run: go run ./scripts/arabic-features")
			os.Exit(1)
		}
		fmt.Println(feaPath, "is up to date")
		return
	}

	if updated == string(existing) {
		fmt.Println(feaPath, "already up to date")
		return
	}
	if err := os.WriteFile(feaPath, []byte(updated), 0o644); err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
	// Report a small summary.
	nInit := len(joiningRules(f, "init"))
	nMedi := len(joiningRules(f, "medi"))
	nFina := len(joiningRules(f, "fina"))
	i, fi := lamAlefRules(f)
	fmt.Printf("wrote %s\n  init=%d medi=%d fina=%d lam-alef=%d marks=%d\n",
		feaPath, nInit, nMedi, nFina, len(i)+len(fi), len(markClass(f)))
}
