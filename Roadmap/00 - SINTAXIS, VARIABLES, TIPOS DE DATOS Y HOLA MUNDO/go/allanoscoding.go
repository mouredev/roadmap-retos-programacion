/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// https://go.dev

package main

import (
	"fmt"
	"math/cmplx"
)

// Constantes numericas
const (
	Big   = 10000000000000
	Small = 0.0000000001
)

func main() {
	// Este es un comentario normal

	/*
		Este es un comentario multilinea del estilo del lenguaje C
	*/

	// Inicialización de variables
	var my_int int
	var my_int_2 int = 2
	my_int_3 := 2

	fmt.Printf("Variable entera 1: %d \n", my_int)
	fmt.Printf("Variable entera 2: %d \n", my_int_2)
	fmt.Printf("Variable entera 3: %d \n", my_int_3)

	// Constantes
	const Verdad = true

	fmt.Println(Verdad)
	fmt.Println(Big)
	fmt.Println(Small)

	// Tipos primitivos
	var my_int_4 int = 19
	var my_uint uint = 1
	var my_string string = "String"
	var my_byte byte = 5
	var my_rune rune = 1599
	var my_float float32 = 1.0
	var my_float_2 float64 = 3.5
	var my_complex complex64 = 5i
	var my_complex_2 complex128 = cmplx.Sqrt(5 + 3i)
	var my_bool bool = true

	fmt.Printf("Variable entera 4: %d \n", my_int_4)
	fmt.Printf("Variable entera sin signo: %d \n", my_uint)
	fmt.Printf("Variable cadena de texto: %s \n", my_string)
	fmt.Printf("Variable byte (uint8): %d \n", my_byte)
	fmt.Printf("Variable rune (int32): %d \n", my_rune)
	fmt.Printf("Variable flotante 1: %f \n", my_float)
	fmt.Printf("Variable flotante 2: %f \n", my_float_2)
	fmt.Printf("Variable compleja 1: %v \n", my_complex)
	fmt.Printf("Variable compleja 2: %v \n", my_complex_2)
	fmt.Printf("Variable booleana: %v \n", my_bool)


	/*
		Tambien existen los tipos int8, int16, int32, int64 al igual
		que los enteros sin signo uint8, uint16, uint32, uint64, uintptr.

		int, uint y uintptr dependen de la arquitectura del sistema (32-bits o 64-bits) por
		lo que si no hay un motivo concreto se recomienda usar int de forma generalizada.
	*/

	fmt.Printf("Hola, Go!")
}
