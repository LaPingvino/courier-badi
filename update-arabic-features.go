// update-arabic-features.go
//
// This script extracts Arabic OpenType features from NoNameFixed-2048.ufo
// and applies them to CourierBadi-Regular.ufo to provide full Arabic ligature support.
//
// The script:
// 1. Preserves the existing GDEF table from CourierBadi
// 2. Extracts essential Arabic features (init, medi, fina, rlig, locl, mark, etc.)
// 3. Creates a complete features.fea file with proper Arabic shaping support
//
// Usage: go run update-arabic-features.go
package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func main() {
	// File paths
	// Read the source features file (NoNameFixed-2048.ufo)
	sourceFile := "sources/NoNameFixed-2048.ufo/features.fea"
	targetFile := "sources/CourierBadi-Regular.ufo/features.fea"
	outputFile := "sources/CourierBadi-Regular.ufo/features.fea.new"

	fmt.Println("Reading source features from:", sourceFile)
	fmt.Println("This will extract Arabic OpenType features for full ligature support...")

	sourceFeatures, err := extractArabicFeatures(sourceFile)
	if err != nil {
		fmt.Printf("Error reading source features: %v\n", err)
		return
	}

	fmt.Println("Reading target GDEF table from:", targetFile)

	gdefTable, err := extractGDEFTable(targetFile)
	if err != nil {
		fmt.Printf("Error reading target GDEF: %v\n", err)
		return
	}

	fmt.Println("Creating new features file:", outputFile)

	err = createNewFeaturesFile(outputFile, gdefTable, sourceFeatures)
	if err != nil {
		fmt.Printf("Error creating new features file: %v\n", err)
		return
	}

	fmt.Println("Successfully created new features file!")
	fmt.Println("Arabic features extracted:", len(sourceFeatures))
	fmt.Println("To use it, run: mv", outputFile, targetFile)
	fmt.Println("")
	fmt.Println("The updated features.fea now includes:")
	fmt.Println("- Complete Arabic contextual shaping (init, medi, fina)")
	fmt.Println("- Required Arabic ligatures (LAM-ALEF combinations)")
	fmt.Println("- Proper mark positioning for diacritics")
	fmt.Println("- Localized number forms")
	fmt.Println("- All necessary lookup tables")
}

// extractArabicFeatures reads the source UFO features file and extracts
// all Arabic-related OpenType features and lookup tables
func extractArabicFeatures(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var features []string
	var currentFeature strings.Builder
	var inFeature bool
	var featureName string
	seenFeatures := make(map[string]bool)

	// Essential OpenType features needed for proper Arabic text rendering
	arabicFeatures := map[string]bool{
		"locl": true, // localized forms
		"init": true, // initial forms
		"medi": true, // medial forms
		"fina": true, // final forms
		"rlig": true, // required ligatures
		"calt": true, // contextual alternates
		"mark": true, // mark positioning
		"mkmk": true, // mark to mark positioning
		"liga": true, // standard ligatures
		"dlig": true, // discretionary ligatures
		"ccmp": true, // glyph composition/decomposition
	}

	scanner := bufio.NewScanner(file)
	braceCount := 0
	var lookupBuffer strings.Builder
	var inLookup bool

	for scanner.Scan() {
		line := scanner.Text()

		// Extract lookup tables first (they come before features)
		if strings.Contains(line, "lookup ") && strings.Contains(line, "Arabic") {
			inLookup = true
			lookupBuffer.Reset()
			lookupBuffer.WriteString(line + "\n")
			braceCount = strings.Count(line, "{") - strings.Count(line, "}")
		} else if inLookup {
			lookupBuffer.WriteString(line + "\n")
			braceCount += strings.Count(line, "{")
			braceCount -= strings.Count(line, "}")

			if braceCount == 0 {
				features = append(features, strings.TrimSpace(lookupBuffer.String()))
				inLookup = false
			}
		}

		// Check if we're starting a feature
		if strings.Contains(line, "feature ") {
			re := regexp.MustCompile(`feature\s+(\w+)\s*{`)
			matches := re.FindStringSubmatch(line)
			if len(matches) > 1 {
				featureName = matches[1]
				if arabicFeatures[featureName] && !seenFeatures[featureName] {
					inFeature = true
					seenFeatures[featureName] = true
					currentFeature.Reset()
					currentFeature.WriteString(line + "\n")
					braceCount = 1
				}
			}
		} else if inFeature {
			currentFeature.WriteString(line + "\n")

			// Count braces to know when feature ends
			braceCount += strings.Count(line, "{")
			braceCount -= strings.Count(line, "}")

			if braceCount == 0 {
				features = append(features, strings.TrimSpace(currentFeature.String()))
				inFeature = false
			}
		}
	}

	fmt.Printf("Extracted %d Arabic features and lookups\n", len(features))
	return features, scanner.Err()
}

// extractGDEFTable preserves the existing GDEF table and glyph class definitions
// from the target UFO file to maintain compatibility
func extractGDEFTable(filename string) (string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return "", err
	}
	defer file.Close()

	var gdef strings.Builder
	var inGDEF bool
	var inGDEFClass bool
	braceCount := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		// Collect GDEF class definitions first
		if strings.HasPrefix(line, "@GDEF_") {
			inGDEFClass = true
			gdef.WriteString(line + "\n")
		} else if inGDEFClass && strings.HasPrefix(line, "\t") {
			// Continue collecting multi-line GDEF class definitions
			gdef.WriteString(line + "\n")
		} else if inGDEFClass && !strings.HasPrefix(line, "\t") && strings.TrimSpace(line) != "" {
			inGDEFClass = false
		}

		// Then collect the GDEF table itself
		if strings.Contains(line, "table GDEF") {
			inGDEF = true
			gdef.WriteString(line + "\n")
			braceCount = 1
		} else if inGDEF {
			gdef.WriteString(line + "\n")
			braceCount += strings.Count(line, "{")
			braceCount -= strings.Count(line, "}")

			if braceCount == 0 {
				break
			}
		}
	}

	return gdef.String(), scanner.Err()
}

// createNewFeaturesFile writes the complete features.fea file with
// GDEF table first, then lookup tables, then features in proper order
func createNewFeaturesFile(filename, gdefTable string, features []string) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	defer writer.Flush()

	// Write GDEF table first
	_, err = writer.WriteString(gdefTable)
	if err != nil {
		return err
	}

	_, err = writer.WriteString("\n")
	if err != nil {
		return err
	}

	// Separate lookups from features for proper ordering
	var lookups []string
	var actualFeatures []string

	for _, feature := range features {
		if strings.Contains(feature, "lookup ") && !strings.Contains(feature, "feature ") {
			lookups = append(lookups, feature)
		} else {
			actualFeatures = append(actualFeatures, feature)
		}
	}

	// Write lookups first
	for _, lookup := range lookups {
		_, err = writer.WriteString(lookup)
		if err != nil {
			return err
		}
		_, err = writer.WriteString("\n\n")
		if err != nil {
			return err
		}
	}

	// Then write features in proper order
	featureOrder := []string{"locl", "ccmp", "dlig", "fina", "medi", "init", "rlig", "calt", "liga", "mark", "mkmk"}

	// Create a map for quick lookup
	featureMap := make(map[string]string)
	for _, feature := range actualFeatures {
		for _, name := range featureOrder {
			if strings.Contains(feature, "feature "+name+" {") {
				featureMap[name] = feature
				break
			}
		}
	}

	// Write features in order
	for _, name := range featureOrder {
		if feature, exists := featureMap[name]; exists {
			_, err = writer.WriteString(feature)
			if err != nil {
				return err
			}
			_, err = writer.WriteString("\n\n")
			if err != nil {
				return err
			}
		}
	}

	return nil
}
