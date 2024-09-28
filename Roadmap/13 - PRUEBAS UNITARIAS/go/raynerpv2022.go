package main

import (
	"testing"
)

/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 */

func SumaValue(a, b int) int {
	return a + b
}

func TestSumaValue(t *testing.T) {
	result := SumaValue(12, 2)

	expected := 14
	if result != expected {
		t.Errorf("SumeValue(12, 2) = %d; want %d", result, expected)
	}
}

func TestSumaVAleustruct(t *testing.T) {
	sume := []struct {
		a int
		b int
		r int
	}{
		{2, 3, 5},
		{3, 5, 8},
		{89, 10, 99},
		{-1, 0, -1},
	}
	for _, i := range sume {
		result := SumaValue(i.a, i.b)
		if result != i.r {
			t.Errorf("SumeValue(%d, %d) = %d; want %d", i.a, i.b, result, i.r)
		}
	}

}

/*
* DIFICULTAD EXTRA (opcional):
* Crea un diccionario con las siguientes claves y valores:
* "name": "Tu nombre"
* "age": "Tu edad"
* "birth_date": "Tu fecha de nacimiento"
* "programming_languages": ["Listado de lenguajes de programación"]
* Crea dos test:
* - Un primero que determine que existen todos los campos.
* - Un segundo que determine que los datos introducidos son correctos.
 */

var dev = []map[string]interface{}{
	{
		"name":                  "Alice",
		"age":                   25,
		"birth_date":            "15-06-1997",
		"programming_languages": []string{"Python", "C++", "Rust"},
	},
	{
		"name":                  "Bob",
		"age":                   30,
		"birth_date":            "15-06-1997",
		"programming_languages": []string{"JavaScript", "Ruby"},
	},
	{
		"name":                  "Charlie",
		"age":                   22,
		"birth_date":            "15-06-1997",
		"programming_languages": []string{},
	},
}
var field = []string{"name", "age", "birth_date", "programming_languages"}

func TestField(t *testing.T) {

	for i, d := range dev {
		for _, k := range field {
			if _, isPresent := d[k]; !isPresent {
				t.Errorf("falta field %v en caso %v\n", k, i+1)
			}
		}
	}

}

func TestValue(t *testing.T) {
	for i, d := range dev {
		if _, ok := d["name"].(string); !ok {
			t.Errorf("en case %v, el field `name` no tiene valor valido para string", i+1)

		}
		if _, ok := d["age"].(int); !ok {
			t.Errorf("en case %v, el field `age` no tiene valor valido para Int", i+1)

		}
		if _, ok := d["birth_date"].(string); !ok {
			t.Errorf("en case %v, el field `birth_date` no tiene valor valido para string", +1)

		}
		if _, ok := d["programming_languages"].([]string); !ok {
			t.Errorf("en case %v, el field `programming_languages` no tiene valor valido para slice de string", i+1)

		}

	}
}
