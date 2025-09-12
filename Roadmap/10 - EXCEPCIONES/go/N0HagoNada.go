package main

import (
	"errors"
	"fmt"
)

type CustomError struct {
	Message string
}

func (e *CustomError) Error() string {
	return e.Message
}

func main() {
	// Ejemplo 1: División por cero
	result, err := divideNumbers(10, 0)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Resultado:", result)
	}

	// Ejemplo 2: Acceso a índice fuera de rango
	numbers := []int{1, 2, 3}
	value, err := getValueAtIndex(numbers, 5)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Valor:", value)
	}
	fmt.Println("****************************** Reto ***************************************")
	// Llamada a la función processParams con diferentes casos
	err = processParams(10, 2)
	handleError(err)

	err = processParams(0, 5)
	handleError(err)

	err = processParams(10, 0)
	handleError(err)

	err = processParams(-5, 3)
	handleError(err)

	err = processParams(8, 4)
	handleError(err)

	fmt.Println("Ejecución finalizada")
}

func divideNumbers(a, b int) (int, error) {
	if b == 0 {
		return 0, fmt.Errorf("No se puede dividir por cero")
	}
	return a / b, nil
}

func getValueAtIndex(numbers []int, index int) (int, error) {

	if index < 0 || index >= len(numbers) {
		return 0, fmt.Errorf("Índice fuera de rango: %d", index)
	}

	return numbers[index], nil
}

// Función que procesa parámetros y puede lanzar diferentes tipos de excepciones
func processParams(a, b int) error {
	if a == 0 {
		return errors.New("No se puede procesar con el valor 'a' igual a cero")
	}

	if b == 0 {
		return fmt.Errorf("No se puede procesar con el valor 'b' igual a cero")
	}

	if a < 0 || b < 0 {
		return &CustomError{Message: "No se pueden procesar valores negativos"}
	}

	// Procesamiento correcto
	result := a / b
	fmt.Printf("Resultado: %d\n", result)
	return nil
}

func handleError(err error) {
	if err != nil {
		fmt.Println("Tipo de error:", err)
	} else {
		fmt.Println("No se ha producido ningún error")
	}
}
