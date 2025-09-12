package main

import (
	"reflect"
	"testing"
	"time"
)

func sum(a, b int) int {
	return a + b
}

func TestSum(t *testing.T) {
	testCases := []struct {
		a, b     int
		expected int
	}{
		{1, 2, 3},
		{5, 7, 12},
		{-3, 3, 0},
		{0, 0, 0},
	}

	for _, tc := range testCases {
		result := sum(tc.a, tc.b)
		if result != tc.expected {
			t.Errorf("sum(%d, %d) = %d; expected %d", tc.a, tc.b, result, tc.expected)
		}
	}
}

/************************************** RETO ******************************************************/
func TestPersonDictionary(t *testing.T) {
	person := map[string]interface{}{
		"name":                  "John Doe",
		"age":                   30,
		"birth_date":            "1990-01-01",
		"programming_languages": []string{"Go", "Python", "JavaScript"},
	}

	// Primer test: verificar la existencia de todos los campos
	expectedFields := []string{"name", "age", "birth_date", "programming_languages"}
	for _, field := range expectedFields {
		if _, exists := person[field]; !exists {
			t.Errorf("El campo '%s' no existe en el diccionario", field)
		}
	}

	// Segundo test: verificar que los datos introducidos son correctos
	if name, ok := person["name"].(string); !ok || name == "" {
		t.Error("El campo 'name' no es una cadena válida")
	}

	if age, ok := person["age"].(int); !ok || age <= 0 {
		t.Error("El campo 'age' no es un entero válido")
	}

	if birthDate, ok := person["birth_date"].(string); !ok {
		t.Error("El campo 'birth_date' no es una cadena")
	} else {
		_, err := time.Parse("2006-01-02", birthDate)
		if err != nil {
			t.Error("El campo 'birth_date' no tiene un formato válido (YYYY-MM-DD)")
		}
	}

	if languages, ok := person["programming_languages"].([]string); !ok {
		t.Error("El campo 'programming_languages' no es un slice de cadenas")
	} else if len(languages) == 0 {
		t.Error("El campo 'programming_languages' está vacío")
	}
}

func TestPersonDictionaryValues(t *testing.T) {
	person := map[string]interface{}{
		"name":                  "John Doe",
		"age":                   30,
		"birth_date":            "1990-01-01",
		"programming_languages": []string{"Go", "Python", "JavaScript"},
	}

	expectedPerson := map[string]interface{}{
		"name":                  "John Doe",
		"age":                   30,
		"birth_date":            "1990-01-01",
		"programming_languages": []string{"Go", "Python", "JavaScript"},
	}

	if !reflect.DeepEqual(person, expectedPerson) {
		t.Errorf("Los valores del diccionario no coinciden con los esperados")
	}
}
