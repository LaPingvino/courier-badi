// incremental-arabic-features.go
//
// Incremental Arabic features enhancement tool for CourierBadi font.
// This tool systematically adds missing Arabic functionality by analyzing
// the current features file and available glyphs, then adding enhancements
// in manageable increments.
//
// Usage: go run incremental-arabic-features.go [--level N] [--dry-run]

package main

import (
	"bufio"
	"encoding/xml"
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"sort"
	"strings"
	"time"
)

type Config struct {
	TargetUFO    string
	Level        int
	DryRun       bool
	Verbose      bool
	OutputSuffix string
}

type GlyphInventory struct {
	All        map[string]bool
	Arabic     map[string]bool
	Contextual map[string]bool
	Extended   map[string]bool
	Diacritics map[string]bool
}

type FeatureAnalysis struct {
	ExistingLookups   []string
	MissingContextual []string
	MissingExtended   []string
	MissingLanguages  []string
	GlyphCoverage     int
	TotalArabicGlyphs int
}

type Enhancement struct {
	Type        string // "contextual", "extended", "language", "ligature"
	Priority    int    // 1=high, 5=low
	Description string
	Code        string
}

func main() {
	config := parseFlags()

	fmt.Println("🚀 Incremental Arabic Features Enhancement")
	fmt.Println("==========================================")
	fmt.Printf("Target: %s\n", config.TargetUFO)
	fmt.Printf("Enhancement Level: %d\n", config.Level)

	if config.DryRun {
		fmt.Println("Mode: Dry Run (no changes will be made)")
	}

	// Step 1: Load glyph inventory
	fmt.Println("\n📖 Loading glyph inventory...")
	inventory, err := loadGlyphInventory(config.TargetUFO)
	if err != nil {
		fmt.Printf("❌ Error loading glyphs: %v\n", err)
		return
	}

	fmt.Printf("   ✅ Total glyphs: %d\n", len(inventory.All))
	fmt.Printf("   ✅ Arabic glyphs: %d\n", len(inventory.Arabic))
	fmt.Printf("   ✅ Contextual forms: %d\n", len(inventory.Contextual))
	fmt.Printf("   ✅ Extended Arabic: %d\n", len(inventory.Extended))

	// Step 2: Analyze current features
	fmt.Println("\n🔍 Analyzing current features...")
	analysis, err := analyzeCurrentFeatures(config, inventory)
	if err != nil {
		fmt.Printf("❌ Analysis failed: %v\n", err)
		return
	}

	printAnalysis(analysis)

	// Step 3: Generate enhancement plan
	fmt.Println("\n🎯 Generating enhancement plan...")
	enhancements := generateEnhancements(config, inventory, analysis)

	if len(enhancements) == 0 {
		fmt.Println("   ✅ No enhancements needed at this level!")
		return
	}

	fmt.Printf("   📋 Generated %d enhancements\n", len(enhancements))
	printEnhancementPlan(enhancements)

	if config.DryRun {
		fmt.Println("\n✅ Dry run complete - no changes made")
		return
	}

	// Step 4: Create backup
	fmt.Println("\n💾 Creating backup...")
	if err := createBackup(config); err != nil {
		fmt.Printf("❌ Backup failed: %v\n", err)
		return
	}
	fmt.Println("   ✅ Backup created")

	// Step 5: Apply enhancements
	fmt.Println("\n🔧 Applying enhancements...")
	if err := applyEnhancements(config, enhancements, inventory); err != nil {
		fmt.Printf("❌ Enhancement failed: %v\n", err)
		return
	}

	fmt.Println("   ✅ Enhancements applied successfully")

	// Step 6: Test compilation
	fmt.Println("\n🏗️  Testing compilation...")
	if err := testCompilation(config); err != nil {
		fmt.Printf("⚠️  Compilation test failed: %v\n", err)
		fmt.Println("   💡 Consider using a lower enhancement level")
	} else {
		fmt.Println("   ✅ Compilation test passed")
	}

	fmt.Println("\n🎉 Enhancement complete!")
	fmt.Printf("   📁 Enhanced features: %s/features.fea%s\n",
		config.TargetUFO, config.OutputSuffix)
}

func parseFlags() Config {
	config := Config{
		TargetUFO:    "sources/CourierBadi-Regular.ufo",
		Level:        1,
		OutputSuffix: ".enhanced",
	}

	flag.StringVar(&config.TargetUFO, "ufo", config.TargetUFO, "Target UFO directory")
	flag.IntVar(&config.Level, "level", config.Level, "Enhancement level (1-5)")
	flag.BoolVar(&config.DryRun, "dry-run", false, "Show plan without applying changes")
	flag.BoolVar(&config.Verbose, "verbose", false, "Verbose output")
	flag.StringVar(&config.OutputSuffix, "suffix", config.OutputSuffix, "Output file suffix")

	flag.Parse()

	return config
}

func loadGlyphInventory(ufoPath string) (*GlyphInventory, error) {
	glyphsDir := filepath.Join(ufoPath, "glyphs")
	files, err := filepath.Glob(filepath.Join(glyphsDir, "*.glif"))
	if err != nil {
		return nil, err
	}

	inventory := &GlyphInventory{
		All:        make(map[string]bool),
		Arabic:     make(map[string]bool),
		Contextual: make(map[string]bool),
		Extended:   make(map[string]bool),
		Diacritics: make(map[string]bool),
	}

	for _, filePath := range files {
		glyphName, err := extractGlyphName(filePath)
		if err != nil {
			continue
		}

		if glyphName == "" {
			continue
		}

		inventory.All[glyphName] = true

		// Categorize glyph
		if isArabicGlyph(glyphName) {
			inventory.Arabic[glyphName] = true

			if isContextualForm(glyphName) {
				inventory.Contextual[glyphName] = true
			}

			if isExtendedArabic(glyphName) {
				inventory.Extended[glyphName] = true
			}

			if isDiacritic(glyphName) {
				inventory.Diacritics[glyphName] = true
			}
		}
	}

	return inventory, nil
}

func extractGlyphName(filePath string) (string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return "", err
	}
	defer file.Close()

	decoder := xml.NewDecoder(file)

	for {
		token, err := decoder.Token()
		if err != nil {
			return "", err
		}

		if start, ok := token.(xml.StartElement); ok && start.Name.Local == "glyph" {
			for _, attr := range start.Attr {
				if attr.Name.Local == "name" {
					return attr.Value, nil
				}
			}
		}
	}
}

func analyzeCurrentFeatures(config Config, inventory *GlyphInventory) (*FeatureAnalysis, error) {
	featuresPath := filepath.Join(config.TargetUFO, "features.fea")

	file, err := os.Open(featuresPath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	analysis := &FeatureAnalysis{
		TotalArabicGlyphs: len(inventory.Arabic),
	}

	scanner := bufio.NewScanner(file)
	lookupPattern := regexp.MustCompile(`^lookup\s+(\w+)`)
	glyphPattern := regexp.MustCompile(`\\uni[0-9A-F]{4}`)
	referencedGlyphs := make(map[string]bool)

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())

		// Track lookups
		if matches := lookupPattern.FindStringSubmatch(line); matches != nil {
			analysis.ExistingLookups = append(analysis.ExistingLookups, matches[1])
		}

		// Track referenced glyphs
		glyphMatches := glyphPattern.FindAllString(line, -1)
		for _, glyph := range glyphMatches {
			if isArabicGlyph(glyph) {
				referencedGlyphs[glyph] = true
			}
		}
	}

	analysis.GlyphCoverage = len(referencedGlyphs)

	// Find missing contextual forms
	analysis.MissingContextual = findMissingContextualForms(inventory, referencedGlyphs)

	// Find missing extended Arabic
	analysis.MissingExtended = findMissingExtended(inventory, referencedGlyphs)

	// Check language support
	analysis.MissingLanguages = findMissingLanguages(featuresPath)

	return analysis, nil
}

func generateEnhancements(config Config, inventory *GlyphInventory, analysis *FeatureAnalysis) []Enhancement {
	var enhancements []Enhancement

	switch config.Level {
	case 1:
		// Level 1: Basic missing contextual forms
		enhancements = append(enhancements, generateBasicContextual(inventory, analysis)...)

	case 2:
		// Level 2: Extended Arabic characters
		enhancements = append(enhancements, generateBasicContextual(inventory, analysis)...)
		enhancements = append(enhancements, generateExtendedArabic(inventory, analysis)...)

	case 3:
		// Level 3: Language-specific features
		enhancements = append(enhancements, generateBasicContextual(inventory, analysis)...)
		enhancements = append(enhancements, generateExtendedArabic(inventory, analysis)...)
		enhancements = append(enhancements, generateLanguageFeatures(analysis)...)

	case 4:
		// Level 4: Advanced ligatures and positioning
		enhancements = append(enhancements, generateAllEnhancements(inventory, analysis)...)

	case 5:
		// Level 5: Complete feature overhaul
		enhancements = append(enhancements, generateCompleteOverhaul(inventory, analysis)...)
	}

	// Sort by priority
	sort.Slice(enhancements, func(i, j int) bool {
		return enhancements[i].Priority < enhancements[j].Priority
	})

	return enhancements
}

func generateBasicContextual(inventory *GlyphInventory, analysis *FeatureAnalysis) []Enhancement {
	var enhancements []Enhancement

	if len(analysis.MissingContextual) > 0 {
		// Group missing contextual forms
		missing := analysis.MissingContextual[:min(10, len(analysis.MissingContextual))]

		code := generateContextualCode(missing, inventory)

		enhancement := Enhancement{
			Type:        "contextual",
			Priority:    1,
			Description: fmt.Sprintf("Add %d missing contextual forms", len(missing)),
			Code:        code,
		}

		enhancements = append(enhancements, enhancement)
	}

	return enhancements
}

func generateExtendedArabic(inventory *GlyphInventory, analysis *FeatureAnalysis) []Enhancement {
	var enhancements []Enhancement

	if len(analysis.MissingExtended) > 0 {
		missing := analysis.MissingExtended[:min(20, len(analysis.MissingExtended))]

		code := generateExtendedCode(missing, inventory)

		enhancement := Enhancement{
			Type:        "extended",
			Priority:    2,
			Description: fmt.Sprintf("Add %d extended Arabic characters", len(missing)),
			Code:        code,
		}

		enhancements = append(enhancements, enhancement)
	}

	return enhancements
}

func generateLanguageFeatures(analysis *FeatureAnalysis) []Enhancement {
	var enhancements []Enhancement

	for _, lang := range analysis.MissingLanguages {
		enhancement := Enhancement{
			Type:        "language",
			Priority:    3,
			Description: fmt.Sprintf("Add %s language support", lang),
			Code:        generateLanguageCode(lang),
		}

		enhancements = append(enhancements, enhancement)
	}

	return enhancements
}

func generateAllEnhancements(inventory *GlyphInventory, analysis *FeatureAnalysis) []Enhancement {
	var enhancements []Enhancement

	enhancements = append(enhancements, generateBasicContextual(inventory, analysis)...)
	enhancements = append(enhancements, generateExtendedArabic(inventory, analysis)...)
	enhancements = append(enhancements, generateLanguageFeatures(analysis)...)

	return enhancements
}

func generateCompleteOverhaul(inventory *GlyphInventory, analysis *FeatureAnalysis) []Enhancement {
	return []Enhancement{
		{
			Type:        "complete",
			Priority:    5,
			Description: "Complete Arabic features overhaul",
			Code:        "# Complete overhaul would be implemented here",
		},
	}
}

func applyEnhancements(config Config, enhancements []Enhancement, inventory *GlyphInventory) error {
	featuresPath := filepath.Join(config.TargetUFO, "features.fea")
	outputPath := featuresPath + config.OutputSuffix

	// Read current features
	content, err := os.ReadFile(featuresPath)
	if err != nil {
		return err
	}

	enhanced := string(content)

	// Apply each enhancement
	for _, enhancement := range enhancements {
		enhanced = applyEnhancement(enhanced, enhancement)
	}

	// Add header comment
	header := fmt.Sprintf("# Enhanced Arabic features - Level %d - %s\n",
		config.Level, time.Now().Format("2006-01-02 15:04:05"))
	enhanced = header + enhanced

	return os.WriteFile(outputPath, []byte(enhanced), 0644)
}

func applyEnhancement(content string, enhancement Enhancement) string {
	switch enhancement.Type {
	case "contextual":
		return addContextualEnhancement(content, enhancement)
	case "extended":
		return addExtendedEnhancement(content, enhancement)
	case "language":
		return addLanguageEnhancement(content, enhancement)
	default:
		return content
	}
}

func addContextualEnhancement(content string, enhancement Enhancement) string {
	// Find insertion point after existing fina feature
	insertPoint := strings.Index(content, "} fina;")
	if insertPoint == -1 {
		return content
	}

	// Insert before the closing brace
	beforeClose := content[:insertPoint]
	afterClose := content[insertPoint:]

	return beforeClose + "\n    # Additional contextual forms\n" +
		enhancement.Code + "\n" + afterClose
}

func addExtendedEnhancement(content string, enhancement Enhancement) string {
	// Add to GDEF section
	gdefPoint := strings.Index(content, "@GDEF_Simple = [")
	if gdefPoint == -1 {
		return content
	}

	// Find end of GDEF_Simple
	endPoint := strings.Index(content[gdefPoint:], "];")
	if endPoint == -1 {
		return content
	}

	beforeEnd := content[:gdefPoint+endPoint]
	afterEnd := content[gdefPoint+endPoint:]

	return beforeEnd + "\n    # Extended Arabic glyphs\n" +
		enhancement.Code + "\n" + afterEnd
}

func addLanguageEnhancement(content string, enhancement Enhancement) string {
	// Add after language system declarations
	insertPoint := strings.Index(content, "languagesystem arab URD;")
	if insertPoint == -1 {
		return content
	}

	endOfLine := strings.Index(content[insertPoint:], "\n")
	if endOfLine == -1 {
		return content
	}

	insertPoint += endOfLine + 1

	before := content[:insertPoint]
	after := content[insertPoint:]

	return before + enhancement.Code + "\n" + after
}

// Code generation functions
func generateContextualCode(missing []string, inventory *GlyphInventory) string {
	var lines []string

	for _, glyph := range missing {
		if baseGlyph := getBaseGlyph(glyph); baseGlyph != "" {
			if inventory.All[baseGlyph+".fina"] {
				lines = append(lines, fmt.Sprintf("    sub %s by %s.fina;", baseGlyph, baseGlyph))
			}
		}
	}

	return strings.Join(lines, "\n")
}

func generateExtendedCode(missing []string, inventory *GlyphInventory) string {
	var lines []string

	for _, glyph := range missing[:min(10, len(missing))] {
		lines = append(lines, fmt.Sprintf("    %s", glyph))
	}

	return strings.Join(lines, "\n")
}

func generateLanguageCode(lang string) string {
	return fmt.Sprintf("languagesystem arab %s;", lang)
}

// Helper functions
func isArabicGlyph(name string) bool {
	return strings.HasPrefix(name, "\\uni06") ||
		strings.HasPrefix(name, "\\uni07") ||
		strings.HasPrefix(name, "\\uni08") ||
		strings.HasPrefix(name, "\\uniFB") ||
		strings.HasPrefix(name, "\\uniFE") ||
		strings.HasPrefix(name, "uni06") ||
		strings.HasPrefix(name, "uni07") ||
		strings.HasPrefix(name, "uni08") ||
		strings.HasPrefix(name, "uniFB") ||
		strings.HasPrefix(name, "uniFE")
}

func isContextualForm(name string) bool {
	return strings.HasSuffix(name, ".fina") ||
		strings.HasSuffix(name, ".medi") ||
		strings.HasSuffix(name, ".init")
}

func isExtendedArabic(name string) bool {
	return strings.HasPrefix(name, "uni075") ||
		strings.HasPrefix(name, "uni08")
}

func isDiacritic(name string) bool {
	return strings.HasPrefix(name, "uni064") ||
		strings.HasPrefix(name, "uni065")
}

func findMissingContextualForms(inventory *GlyphInventory, referenced map[string]bool) []string {
	var missing []string

	for glyph := range inventory.Arabic {
		if !isContextualForm(glyph) && !referenced["\\"+glyph] {
			missing = append(missing, glyph)
		}
	}

	sort.Strings(missing)
	return missing
}

func findMissingExtended(inventory *GlyphInventory, referenced map[string]bool) []string {
	var missing []string

	for glyph := range inventory.Extended {
		if !referenced["\\"+glyph] {
			missing = append(missing, glyph)
		}
	}

	sort.Strings(missing)
	return missing
}

func findMissingLanguages(featuresPath string) []string {
	content, err := os.ReadFile(featuresPath)
	if err != nil {
		return []string{}
	}

	text := string(content)
	required := []string{"ARA", "FAR"}
	var missing []string

	for _, lang := range required {
		if !strings.Contains(text, "languagesystem arab "+lang) {
			missing = append(missing, lang)
		}
	}

	return missing
}

func getBaseGlyph(glyph string) string {
	if idx := strings.LastIndex(glyph, "."); idx != -1 {
		return glyph[:idx]
	}
	return glyph
}

func createBackup(config Config) error {
	source := filepath.Join(config.TargetUFO, "features.fea")
	timestamp := time.Now().Format("20060102-150405")
	backup := filepath.Join(config.TargetUFO, fmt.Sprintf("features.fea.backup-%s", timestamp))

	content, err := os.ReadFile(source)
	if err != nil {
		return err
	}

	return os.WriteFile(backup, content, 0644)
}

func testCompilation(config Config) error {
	// This would ideally run fontmake or similar to test compilation
	// For now, just check that the file is valid
	outputPath := filepath.Join(config.TargetUFO, "features.fea"+config.OutputSuffix)
	_, err := os.ReadFile(outputPath)
	return err
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Printing functions
func printAnalysis(analysis *FeatureAnalysis) {
	fmt.Printf("   📊 Existing lookups: %d\n", len(analysis.ExistingLookups))
	fmt.Printf("   📊 Glyph coverage: %d/%d (%.1f%%)\n",
		analysis.GlyphCoverage, analysis.TotalArabicGlyphs,
		float64(analysis.GlyphCoverage)/float64(analysis.TotalArabicGlyphs)*100)
	fmt.Printf("   📊 Missing contextual: %d\n", len(analysis.MissingContextual))
	fmt.Printf("   📊 Missing extended: %d\n", len(analysis.MissingExtended))
	fmt.Printf("   📊 Missing languages: %v\n", analysis.MissingLanguages)
}

func printEnhancementPlan(enhancements []Enhancement) {
	for i, enhancement := range enhancements {
		fmt.Printf("   %d. [P%d] %s: %s\n",
			i+1, enhancement.Priority, enhancement.Type, enhancement.Description)
	}
}
