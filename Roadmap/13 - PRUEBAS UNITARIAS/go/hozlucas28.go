package main

import (
	"reflect"
	"strings"
	"testing"
)

/*
	Tests...
*/

func add(a int, b int) int {
	return a + b
}

/*
	Additional challenge...
*/

var author map[string]interface{} = map[string]interface{}{
	"name":                  "Lucas",
	"age":                   "22",
	"born_date":             "2002-02-20",
	"programming_languages": []string{"TypeScript", "Python", "Go (Golang)"},
}

/*
	Toda declaración, debajo del presente comentario, debe ser extraida a un archivo con el mismo nombre
	que el actual, pero finalizando con `*_test.go`, por ejemplo: `hozlucas28_test.go`. Caso contrario los
	tests no podrán ejecutarse.
*/

/*
	Tests...
*/

func TestAddWithPositiveArguments(test *testing.T) {
	var result int = add(1, 8)
	var expected int = 9

	if result != expected {
		test.Errorf("Test failed! add(1, 8) = %d, but expected to be %d", result, expected)
	}
}

func TestAddWithNegativeArguments(test *testing.T) {
	var result int = add(-5, -5)
	var expected int = -10

	if result != expected {
		test.Errorf("Test failed! add(-5, -5) = %d, but expected to be %d", result, expected)
	}
}

/*
	Additional challenge...
*/

func TestAuthorSchema(test *testing.T) {
	_, hasAge := author["age"]
	_, hasBornDate := author["born_date"]
	_, hasName := author["name"]
	_, hasProgrammingLanguages := author["programming_languages"]

	var errorMessage []string = []string{}

	if !hasAge {
		errorMessage = append(errorMessage, "age")
	}

	if !hasBornDate {
		errorMessage = append(errorMessage, "born_date")
	}

	if !hasName {
		errorMessage = append(errorMessage, "name")
	}

	if !hasProgrammingLanguages {
		errorMessage = append(errorMessage, "programming_languages")
	}

	if len(errorMessage) > 0 {
		var message string = strings.Join(errorMessage, ", ")
		test.Errorf("Author schema is invalid! The following properties are missing: %s", message)
	}
}

func TestAuthorDataTypes(test *testing.T) {
	isValidAge := reflect.ValueOf(author["age"]).Kind() == reflect.String
	isValidBornDate := reflect.ValueOf(author["born_date"]).Kind() == reflect.String
	isValidName := reflect.ValueOf(author["name"]).Kind() == reflect.String
	isValidProgrammingLanguages := reflect.ValueOf(author["programming_languages"]).Kind() == reflect.Slice

	var errorMessage []string = []string{}

	if !isValidAge {
		errorMessage = append(errorMessage, "age: string")
	}

	if !isValidBornDate {
		errorMessage = append(errorMessage, "born_date: string")
	}

	if !isValidName {
		errorMessage = append(errorMessage, "name: string")
	}

	if !isValidProgrammingLanguages {
		errorMessage = append(errorMessage, "programming_languages: []string")
	}

	if len(errorMessage) > 0 {
		var message string = strings.Join(errorMessage, ", ")
		test.Errorf("Data types of the properties inside author are invalid! Data types of the properties should be: { %s }", message)
	}

}
