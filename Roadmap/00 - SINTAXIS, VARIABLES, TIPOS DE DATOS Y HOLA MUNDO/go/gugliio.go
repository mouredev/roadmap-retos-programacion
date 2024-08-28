package main

import "fmt"

/* Crea un comentario en el código y coloca la URL del sitio web oficial del
lenguaje de programación que has seleccionado. */

// https://go.dev/

/* Representa las diferentes sintaxis que existen de crear comentarios
en el lenguaje (en una línea, varias...). */

// Single line

/*
MultiLine 1
MultiLine 2
*/

// Crea una variable (y una constante si el lenguaje lo soporta).
var lang = "go"

const fixedValue = "constant"

/* Crea variables representando todos los tipos de datos primitivos del
lenguaje (cadenas de texto, enteros, booleanos...) */

var enteros int = 40
var flotantes float64 = 0.5
var booleanos bool = false
var cadenaDeTexto string = "nombre"

func main() {
	// Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
	fmt.Println("¡Hola, Go!")
}
