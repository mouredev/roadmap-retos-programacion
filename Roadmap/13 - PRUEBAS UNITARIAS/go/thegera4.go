package main

import (
	"testing"
	"errors"
	"fmt"
)

type T interface{}

// Función que recibe dos parámetros de tipo T (int o float) y devuelve la suma de los mismos
func Suma(a, b T) (T, error) {
	switch a.(type) {
		case int:
			switch b.(type) {
			case int:
				return a.(int) + b.(int), nil
			case float64:
				return float64(a.(int)) + b.(float64), nil
			}
		case float64:
			switch b.(type) {
			case int:
				return a.(float64) + float64(b.(int)), nil
			case float64:
				return a.(float64) + b.(float64), nil
			}
		}
		return 0, errors.New("error: al menos uno de los parametros recibidos no es un numero")
}

func main() {
	
	res, err := Suma(1,2)
	if err == nil { fmt.Println(res) } else { fmt.Println(err) }

	res, err = Suma(5.5, 4.3)
	if err == nil { fmt.Println(res) } else { fmt.Println(err)}

	res, err = Suma(5.5, 4)
	if err == nil { fmt.Println(res) } else { fmt.Println(err) }

	res, err = Suma("1", 2)
	if err == nil { fmt.Println(res) } else { fmt.Println(err) }
}

// Los tests en go deben de ir en otro archivo separado (ver info en internet), se agrega aqui el test para efectos practicos
func TestSuma(t *testing.T) {
	// Caso de prueba 1: Suma de dos enteros
	resultado, err := Suma(1, 2)
	if err != nil {
		t.Errorf("Error inesperado: %v", err)
	}
	expected := 3
	if resultado != expected {
		t.Errorf("Suma(1, 2) = %v; esperado %v", resultado, expected)
	}

	// Caso de prueba 2: Suma de dos números de punto flotante
	resultado, err = Suma(5.5, 4.3)
	if err != nil {
		t.Errorf("Error inesperado: %v", err)
	}
	expectedFloat := 9.8
	if resultado != expectedFloat {
		t.Errorf("Suma(5.5, 4.3) = %v; esperado %v", resultado, expectedFloat)
	}

	// Caso de prueba 3: Suma de un número de punto flotante y un entero
	resultado, err = Suma(5.5, 4)
	if err != nil {
		t.Errorf("Error inesperado: %v", err)
	}
	if resultado != expectedFloat {
		t.Errorf("Suma(5.5, 4) = %v; esperado %v", resultado, expectedFloat)
	}

	// Caso de prueba 4: Suma con un parámetro no numérico
	_, err = Suma("1", 2)
	expectedError := "error: al menos uno de los parametros recibidos no es un numero"
	if err == nil || err.Error() != expectedError {
		t.Errorf("Error inesperado: %v; esperado %v", err, expectedError)
	}
}

// Extra

//Creamos una estructura para almacenar los datos
type Persona struct {
	Name 		string
	Age 		int
	BirthDate 	string
	Languages	[]string
}

//Creamos una funcion que recibe un string y un slice de strings y verifica si el string esta en el slice
func TestPersona(t *testing.T) {
	p := Persona{
		Name:                 "Gerardo",
		Age:                  30,
		BirthDate:            "03/07/1987",
		Languages: 				[]string{"Go", "Python", "JavaScript"},
	}

	// Prueba 1: Verificar que todos los campos existen
	if p.Name == "" || p.Age == 0 || p.BirthDate == "" || len(p.Languages) == 0 {
		t.Errorf("No todos los campos existen")
	}

	// Prueba 2: Verificar que los datos introducidos son correctos
	if p.Name != "Gerardo" || p.Age != 30 || p.BirthDate != "03/07/1987" || !contains(p.Languages, "Go") {
		t.Errorf("Los datos introducidos no son correctos")
	}
}

func contains(s []string, str string) bool {
	for _, v := range s {
		if v == str {
			return true
		}
	}
	return false
}