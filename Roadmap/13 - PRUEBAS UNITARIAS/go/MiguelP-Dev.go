package main

import (
	"slices"
	"strings"
	"testing"
	"time"
)

func Sum(a, b float64) float64 {
	total := a + b
	return total
}

// Nota: En go los test se hacen mediante archivos con el mismo nombre del archivo a testear con el sufijo "_test.go"
// Test Simple
func TestSum(t *testing.T) {
	result := Sum(23, 24)
	spected := 47

	if result != float64(spected) {
		t.Errorf("Resultado incorrecto: obtuve %v, esperaba: %v", result, spected)
	}
}

// Go permite organizar los tests en subtests
// y usar un enfoque basado en tablas para probar
// múltiples casos con menos código repetitivo.
func TestSum2(t *testing.T) {
	type casesTemplate []struct {
		name          string
		a, b, spected float64
	}

	cases := casesTemplate{{"NegativeAndPositive", 15, -12, 3}, {"TwoTypes", 12.2, 12, 24.2}, {"Positive", 3, 4, 7}, {"Negative", -1, -2, -3}}

	for _, testCase := range cases {
		t.Run(testCase.name, func(t *testing.T) {
			result := Sum(testCase.a, testCase.b)
			if result != testCase.spected {
				t.Errorf("Para: %s, obtuve: %v, esperaba: %v", testCase.name, result, testCase.spected)
			}
		})
	}
}

// Extra

var Dictionary = map[string]any{
	"name":                  "Miguel",
	"age":                   31,
	"birth_date":            time.Date(1993, 10, 13, 0, 0, 0, 0, time.UTC),
	"Programming_languajes": []string{"Go", "Python"},
}

func testExistsFieldsDict(t *testing.T) {
	fieldsSpected := []string{"name", "age", "Programming_languajes", "birth_date"}
	fieldsObtained := []string{}

	for field, _ := range Dictionary {
		fieldsObtained = append(fieldsObtained, field)
	}

	slices.Sort(fieldsSpected)
	slices.Sort(fieldsObtained)

	t.Run("TestExistsFieldsDict", func(t *testing.T) {
		for i := 0; i <= len(fieldsSpected)-1; i++ {
			if !strings.Contains(fieldsObtained[i], fieldsSpected[i]) {
				t.Errorf("El campo %s no existe en el diccionario", fieldsSpected[i])
				return
			}
		}
	})
}

func testCorrectDataDict(t *testing.T) {
	type casesTemplate []struct {
		name    string
		spected any
	}

	cases := casesTemplate{
		{"Name", "Miguel"},
		{"Age", 31},
		{"Programming_languajes", []string{"Go", "Python"}},
		{"Birth_date", time.Date(1993, 10, 13, 0, 0, 0, 0, time.UTC)},
	}

	for _, testCase := range cases {
		t.Run(testCase.name, func(t *testing.T) {
			result := Dictionary[testCase.name]
			if result != testCase.spected {
				t.Errorf("Para: %s, obtuve: %v, esperaba: %v", testCase.name, result, testCase.spected)
			}
		})
	}
}
