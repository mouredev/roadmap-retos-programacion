package main

import "fmt"

// URL de GO => https://golang.org/

// Comentario de 1 línea

/*
Comentario de varias lineas
*/

const Constante = "Javier"

var variable = "Curto"

func main() {

	// Primitivos
	var integer uint32 = 10
	var integerNeg int32 = -10
	var numFloat32 float32 = 10.5
	var numFloat64 float64 = 10.5
	var boolTrue bool = true
	var boolFalse bool = false
	var text string = "Javier"
	var charRune rune = 'a'

	var language string = "Go"

	fmt.Println("¡Hola, " + language + "!")

	fmt.Println("Primitivos: "+Constante, variable, integer, integerNeg, numFloat32, numFloat64, boolTrue, boolFalse, text, charRune)
}
