package main

// Comentario de una línea - comienza con // y van hasta el final de la línea
/*
   Comentarios generales - comienzan con /* y terminan con
*/

// Sitio oficial: https://go.dev/

import (
	"fmt"
)

var lenguaje = "Go" // Tipo implicito string

func main() {
	/*
	   Declaración de variables

	   var nombreVariable Tipo
	   var nombreVariable Tipo = valor

	   Declaración corta de variables - solo funciona dentro de funciones

	   nombreVariable := valor  // El tipo es implicito
	*/
	variable := 0
	fmt.Println(variable)

	// Booleanas
	var verdadero, falso bool = true, false
	fmt.Println(verdadero)
	fmt.Println(falso)

	// Numéricas
	/*
				uint
		        uint8       the set of all unsigned  8-bit integers (0 to 255)
			    uint16      the set of all unsigned 16-bit integers (0 to 65535)
				uint32      the set of all unsigned 32-bit integers (0 to 4294967295)
				uint64      the set of all unsigned 64-bit integers (0 to 18446744073709551615)

				byte // alias for uint8

				int
				int8        the set of all signed  8-bit integers (-128 to 127)
				int16       the set of all signed 16-bit integers (-32768 to 32767)
				int32       the set of all signed 32-bit integers (-2147483648 to 2147483647)
				int64       the set of all signed 64-bit integers (-9223372036854775808 to 9223372036854775807)

				rune // alias for int32
				     // represents a Unicode code point

			    float32     the set of all IEEE-754 32-bit floating-point numbers
				float64     the set of all IEEE-754 64-bit floating-point numbers

				complex
				complex64   the set of all complex numbers with float32 real and imaginary parts
			    complex128  the set of all complex numbers with float64 real and imaginary parts
	*/
	var entero int8 = -5
	fmt.Println(entero)

	var enteroSinSigno uint8 = 0
	fmt.Println(enteroSinSigno)

	var flotante float32 = 1.2525
	fmt.Println(flotante)

	var complejo complex64 = 4 + 1i
	fmt.Println(complejo)

	// Cadenas
	var saludo string = "Hola"
	fmt.Println(saludo)

	// Arrays
	arreglo := [3]int{1, 2, 3}
	var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
	fmt.Println(arreglo)
	fmt.Println(pow)

	// Constantes
	const pi float64 = 3.14159265
	fmt.Println(pi)

	// Punteros
	var p *int
	i := 42
	p = &i
	fmt.Println(*p)

	fmt.Printf("!%s, %s!", saludo, lenguaje)
}
