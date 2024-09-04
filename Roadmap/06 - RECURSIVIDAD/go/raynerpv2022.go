package main

import "fmt"

// * EJERCICIO:
// * Entiende el concepto de recursividad creando una función recursiva que imprima
// * números del 100 al 0.
// *
// * DIFICULTAD EXTRA (opcional):
// * Utiliza el concepto de recursividad para:
// * - Calcular el factorial de un número concreto (la función recibe ese número).
// * - Calcular el valor de un elemento concreto (según su posición) en la
// *   sucesión de Fibonacci (la función recibe la posición).

func number100To0(number int) {
	if number >= 0 {

		fmt.Println(number)
		number100To0((number - 1))
	}

}

func factorial(number int) int {
	if number <= 0 {
		return 0
	} else if number <= 1 {
		return 1
	} else {
		return factorial(number-1) * number
	}

}

func fibonacci(index int) int {
	if index <= 1 {
		return 0
	} else if index == 2 {
		return 1
	} else {
		return fibonacci((index - 1)) + fibonacci((index - 2))
	}

}
func main() {
	number100To0((100))
	fmt.Println(factorial(6))
	fmt.Println(fibonacci(8))
}
