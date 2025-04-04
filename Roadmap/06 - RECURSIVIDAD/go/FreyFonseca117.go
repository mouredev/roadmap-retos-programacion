// # #06 RECURSIVIDAD
// > #### Dificultad: Difícil | Publicación: 05/02/24 | Corrección: 12/02/24

// ## Ejercicio

// ```
// /*
//  * EJERCICIO:
//  * Entiende el concepto de recursividad creando una función recursiva que imprima
//  * números del 100 al 0.
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Utiliza el concepto de recursividad para:
//  * - Calcular el factorial de un número concreto (la función recibe ese número).
//  * - Calcular el valor de un elemento concreto (según su posición) en la
//  *   sucesión de Fibonacci (la función recibe la posición).
//  */
// ```
// #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

// Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

// > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

package main

import "fmt"

// valores que recibe la funcion.
var value1 int = 100

// funcion que recorre los valores
func recorreValores(a int) int {
	if a < 0 {
		return 0
	} else {
		fmt.Println(a)
		return recorreValores(a - 1)
	}
}

// funcion factorial
func funFactorial(a int) int {
	if a == 0 {
		return 1
	}
	return a * funFactorial(a-1)
}

// funcion de binonacci
func funFibonacci(num int) int {
	if num <= 0 {
		return 0
	} else if num == 1 {
		return 1
	}
	return funFibonacci(num-1) + funFibonacci(num-2)

}

func main() {
	recorreValores(value1)
	result := funFactorial(10)
	fmt.Println(result)
	result2 := funFibonacci(10)
	fmt.Println(result2)

}
