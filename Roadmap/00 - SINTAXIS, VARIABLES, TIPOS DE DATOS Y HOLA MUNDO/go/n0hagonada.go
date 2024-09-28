package main

import "fmt"

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
// https://go.dev/doc/effective_go

func main() {
	const Pi float64 = 3.14159
	var nombre string = "Go"
	var edad int = 30
	var esVerdadero bool = true
	var altura float64 = 1.75
	var b byte = 0x41
	var letra rune = 'ñ'
	var puntero *int = &edad
	var g map[string]int = map[string]int{"uno": 1, "dos": 2}
	type MiInterface interface{ MiMetodo() string }
	var f []int = []int{1, 2, 3}
	type H struct{ Campo string }
	fmt.Println("!Hola, " + nombre)
	imprimirDatos := fmt.Sprintf("Entero: %d\nCadena de Texto: %s\nBooleano: %t\nFlotante: %f\nByte: %c\nRuna: %c\nPuntero: %p\nMapa: %v\nArray: %v", edad, nombre, esVerdadero, altura, b, letra, puntero, g, f)
	fmt.Println(imprimirDatos)
}
