// # #05 VALOR Y REFERENCIA
// > #### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

// ## Ejercicio

// ```
// /*
//  * EJERCICIO:
//  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
//  *   su tipo de dato.
//  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
//  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
//  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
//  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
//  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
//  *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
//  *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
//  *   Comprueba también que se ha conservado el valor original en las primeras.
//  */
// ```
// #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

// Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

// > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

package main

import "fmt"

// Función con parámetro por valor
func duplicarValor(num int) {
	num *= 2
	fmt.Println("Dentro de duplicarValor:", num)
}

// Función con parámetro por referencia (usando puntero)
func duplicarReferencia(num *int) {
	*num *= 2
	fmt.Println("Dentro de duplicarReferencia:", *num)
}

// Intercambio por valor (no afecta a las variables originales)
func intercambioPorValor(a, b int) (int, int) {
	return b, a
}

// Intercambio por referencia (afecta a las variables originales)
func intercambioReferencia(a, b *int) {
	*a, *b = *b, *a
}

func main() {
	// Asignación por valor (tipos primitivos)
	a := 10
	b := a // b recibe una COPIA del valor de a
	b = 20
	fmt.Println("Por valor - a:", a, "b:", b) // a sigue siendo 10

	// Asignación por referencia (slices, maps, channels, pointers)
	slice1 := []int{1, 2, 3}
	slice2 := slice1 // slice2 apunta al MISMO slice subyacente
	slice2[0] = 99
	fmt.Println("Por referencia - slice1:", slice1, "slice2:", slice2) // ambos muestran [99 2 3]

	// Usando punteros para referencia explícita
	ptrVal := 5
	ptr := &ptrVal // ptr es un puntero a ptrVal
	*ptr = 15
	fmt.Println("Con punteros - ptrVal:", ptrVal, "*ptr:", *ptr) // ambos son 15

	// Pruebas de paso por valor y por referencia
	numero := 10

	// Paso por valor
	duplicarValor(numero)
	fmt.Println("Después de duplicarValor:", numero) // sigue siendo 10

	// Paso por referencia
	duplicarReferencia(&numero)
	fmt.Println("Después de duplicarReferencia:", numero) // ahora es 20

	// Variables originales para intercambio
	original1, original2 := 5, 10
	fmt.Println("\nOriginales para intercambio - original1:", original1, "original2:", original2)

	// Intercambio por valor
	nuevo1, nuevo2 := intercambioPorValor(original1, original2)
	fmt.Println("Intercambio por valor:")
	fmt.Println("Originales - original1:", original1, "original2:", original2) // no han cambiado
	fmt.Println("Nuevas - nuevo1:", nuevo1, "nuevo2:", nuevo2)                 // valores intercambiados

	// Intercambio por referencia
	intercambioReferencia(&original1, &original2)
	fmt.Println("Intercambio por referencia:")
	fmt.Println("Originales modificadas - original1:", original1, "original2:", original2) // ahora están intercambiadas
}
