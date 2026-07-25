package main

import "fmt"

// Una función puede tomar cero o más argumentos y devolver cero o más valores.
func add(x int, y int) int {
	return x + y
}

// Función que no devolverá ningún valor
func printMessage(message string) {
	fmt.Println(message)
}

// Cuando dos o más parámetros de función con nombre consecutivos comparten el
// mismo tipo, se puede omitir el tipo de todos menos del último
func add2(x, y int) int {
	return x + y
}

// Múltiples argumentos de retorno
func swap(x, y int) (int, int) {
	return y, x
}

// Valores de retorno nombrados
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return // devuelve x, y
}
func calcular(a, b int) (suma int, producto int) {
	suma = a + b
	producto = a * b
	return
}

// Función que devuelve varios valores.  En este caso un error y un float64
// Esta funcionalidad es particularmente útil para devolver un valor principal y un error, lo cual es un patrón común en Go.
func dividir(dividendo, divisor float64) (float64, error) {
	if divisor == 0 {
		return 0, fmt.Errorf("división por cero")
	}
	return dividendo / divisor, nil
}

// Declaración corta de variable
// La declaración corta de variable := se puede usar para declarar y asignar
// variables dentro de una función. La declaración corta de variable no se puede
// usar en el ámbito de la función principal, ya que no se puede declarar una
// variable sin un tipo explícito. En su lugar, se puede usar la declaración
// larga var nombre tipo = valor.

func main() {
	// Declaración de función anónima
	restar := func(x, y int) int {
		return x - y
	}

	fmt.Println(restar(5, 3)) // 2

	printMessage("Hola, mundo!") // Hola, mundo!

	fmt.Println(add(1, 2))  // 3
	fmt.Println(add2(1, 2)) // 3
	a, b := swap(1, 2)
	fmt.Println(a, b)      // 2 1
	fmt.Println(split(17)) // 7 10

	resultado, err := dividir(10, 0)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Resultado:", resultado)
	}

	suma, producto := calcular(3, 4)
	fmt.Println("Suma:", suma, "Producto:", producto) // Suma: 7 Producto: 12
}
