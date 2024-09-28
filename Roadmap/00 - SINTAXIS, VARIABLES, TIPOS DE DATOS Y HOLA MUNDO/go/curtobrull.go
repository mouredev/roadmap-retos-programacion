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

	var (
		// Primitivos
		integerPos   uint32    = 10
		integerNeg   int32     = -10
		numFloat32   float32   = 10.5
		numFloat64   float64   = 10.5
		numComplex64 complex64 = 3 + 4i
		boolTrue     bool      = true
		boolFalse    bool
		text         string = "Javier"
		charRune     rune   = 'a'
		language     string = "Go"
	)

	fmt.Println("¡Hola, " + language + "!")

	fmt.Println("Primitivos: "+Constante, variable, integerPos, integerNeg, numFloat32, numFloat64, numComplex64, boolTrue, boolFalse, text, charRune)
}
