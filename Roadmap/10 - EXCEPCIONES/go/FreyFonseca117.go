//  * EJERCICIO:
//  * Explora el concepto de manejo de excepciones según tu lenguaje.
//  * Fuerza un error en tu código, captura el error, imprime dicho error
//  * y evita que el programa se detenga de manera inesperada.
//  * Prueba a dividir "10/0" o acceder a un índice no existente
//  * de un listado para intentar provocar un error.
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Crea una función que sea capaz de procesar parámetros, pero que también
//  * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
//  * corresponderse con un tipo de excepción creada por nosotros de manera
//  * personalizada, y debe ser lanzada de manera manual) en caso de error.
//  * - Captura todas las excepciones desde el lugar donde llamas a la función.
//  * - Imprime el tipo de error.
//  * - Imprime si no se ha producido ningún error.
//  * - Imprime que la ejecución ha finalizado.

package main

import (
	"errors"
	"fmt"
)

// manejo de errores

func dividir(a, b float32) (float32, error) {
	if b == 0 {
		return 0, errors.New("Division entre 0")
	}
	return a / b, nil

}

// Actividad opcional
func procesarParametros(a, b float32) (float32, bool, error) {
	if b == 0 {
		return 0, false, errors.New("Divison entre cero")
	} else if a == 0 {
		return 0, true, errors.New("el numerador es cero")
	} else {
		return a / b, true, nil
	}
}

func main() {
	result, err := dividir(10, 0)
	if err != nil {
		fmt.Println("Se ha producido un error", err)
	} else {
		fmt.Println("El resultado es", result)
	}
	result, err = dividir(10, 4)
	if err != nil {
		fmt.Println("Se ha producido un error", err)
	} else {
		fmt.Println("El resultado es", result)
	}
	result, ok, err := procesarParametros(10, 0)
	if err != nil {
		fmt.Println("Error en procesarParametros:", err)
	} else {
		fmt.Println("Resultado de procesarParametros:", result, "¿Es válido?:", ok)
	}
	result, ok, err = procesarParametros(8, 4)
	if err != nil {
		fmt.Println("Error en procesarParametros:", err)
	} else {
		fmt.Println("Resultado de procesarParametros:", result, "¿Es válido?:", ok)
	}
	fmt.Println("Ejecución finalizada.")
}
