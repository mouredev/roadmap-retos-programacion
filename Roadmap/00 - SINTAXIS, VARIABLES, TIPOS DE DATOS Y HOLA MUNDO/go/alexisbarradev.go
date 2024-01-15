/*Crea un comentario en el código y coloca la URL del sitio web oficial del
lenguaje de programación que has seleccionado
*/

//https://golang.org/

/*Representa las diferentes sintaxis que existen de crear comentarios
en el lenguaje (en una línea, varias...).
*/

/*
un IDLE de ejemplo:
https://www.jetbrains.com/go/
*/

//Crea una variable (y una constante si el lenguaje lo soporta)

package main

import "fmt"

const dobDay = 10

var dobYear int = 1984

/*Crea variables representando todos los tipos de datos primitivos
del lenguaje (cadenas de texto, enteros, booleanos...).
*/

var numInteger int = 2024

var numFloat float32 = 3.16

var numComp complex64 = 1 + 2i

var isTrue bool = true

var xMas string = "Merry Xmas!"

var letter byte = 'Z'

var simbolo rune = '±'

//Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"//
func main() {
	fmt.Println("¡Hola, Go!...")
}
