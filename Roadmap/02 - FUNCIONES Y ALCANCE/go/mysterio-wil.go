package main

import (
	"fmt"
)

/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

// --- Variable Global ---
var globalVar = "Soy una variable global"

func main() {
	fmt.Println("===> Funciones básicas <===")

	// Sin parámetros ni retorno
	greet()

	// Con un parámetro
	greetPerson("Wilmer")

	// Con varios parámetros
	add(5, 3)

	// Con retorno
	result := multiply(5, 3)
	fmt.Printf("El resultado de la multiplicación es %d\n", result)

	// Con múltiples retornos (una característica de Go)
	quotient, remainder := divide(10, 3)
	fmt.Printf("10 dividido por 3 es %d con un resto de %d\n", quotient, remainder)

	// Go no tiene parámetros por defecto, se puede simular con structs o sobrecarga.
	fmt.Println("Go no soporta parámetros por defecto.")

	// Con parámetros de longitud variable (variadic)
	fmt.Println("Argumentos variables (variadic):")
	printArgs(1, "texto", true, 15.5)


	fmt.Println("\n===> Funciones dentro de funciones (Anonymous Functions) <===")
	outerFunction()


	fmt.Println("\n===> Funciones del lenguaje (built-in) <===")
	myList := []int{1, 2, 3, 4, 5}
	fmt.Printf("Usando la función len() en un slice: El slice tiene %d elementos.\n", len(myList))
	
	// No hay una función max() para slices en la librería estándar, se debe implementar.
	fmt.Printf("El valor máximo del slice es %d\n", findMax(myList))


	fmt.Println("\n===> Variable LOCAL y GLOBAL <===")
	myFunctionScope()

	// Modificar una variable global
	fmt.Printf("Antes de modificar: %s\n", globalVar)
	modifyGlobal()
	fmt.Printf("Después de modificar: %s\n", globalVar)


	/*
	 * DIFICULTAD EXTRA (opcional):
	 */
	fmt.Println("\n====> DIFICULTAD EXTRA <====")
	timesPrintedNumber := fizzBuzzExtra("Fizz", "Buzz")
	fmt.Printf("\nEl número se imprimió un total de %d veces.\n", timesPrintedNumber)
}

// --- Definiciones de funciones ---

func greet() {
	fmt.Println("Hola, Go!")
}

func greetPerson(name string) {
	fmt.Printf("Hola, %s!\n", name)
}

func add(a, b int) {
	fmt.Printf("La suma de %d y %d es %d\n", a, b, a+b)
}

func multiply(a, b int) int {
	return a * b
}

func divide(a, b int) (int, int) {
	return a / b, a % b
}

func printArgs(args ...interface{}) {
	for _, arg := range args {
		fmt.Printf("- %v\n", arg)
	}
}

func outerFunction() {
	fmt.Println("Esta es la función externa.")
	// Go usa funciones anónimas para un comportamiento similar a funciones anidadas.
	innerFunction := func() {
		fmt.Println("Esta es una función anónima (interna).")
	}
	innerFunction()
}

func findMax(numbers []int) int {
	if len(numbers) == 0 {
		return 0 // o retornar un error
	}
	maxVal := numbers[0]
	for _, number := range numbers[1:] {
		if number > maxVal {
			maxVal = number
		}
	}
	return maxVal
}

func myFunctionScope() {
	localVar := "Soy una variable local"
	fmt.Println(globalVar) // Acceso a la variable global
	fmt.Println(localVar)
}

func modifyGlobal() {
	globalVar = "He modificado la variable global"
}

func fizzBuzzExtra(text1, text2 string) int {
	count := 0
	for i := 1; i <= 100; i++ {
		isMultipleOf3 := (i%3 == 0)
		isMultipleOf5 := (i%5 == 0)

		if isMultipleOf3 && isMultipleOf5 {
			fmt.Println(text1 + text2)
		} else if isMultipleOf3 {
			fmt.Println(text1)
		} else if isMultipleOf5 {
			fmt.Println(text2)
		} else {
			fmt.Println(i)
			count++
		}
	}
	return count
}
