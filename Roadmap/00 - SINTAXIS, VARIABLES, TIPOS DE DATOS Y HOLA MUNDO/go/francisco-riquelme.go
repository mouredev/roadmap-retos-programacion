// Este es la resolución del reto 00 - Sintaxis, variables, tipos de datos y Hola Mundo de mouredev

package main

import "fmt"

func main()

{
	// URL oficial de go https://golang.org/

	// Este es un comentario de una línea
	/*
		Este es un comentario de varias líneas
	*/

	// Declaración de variables
	var nombre string = "Francisco Riquelme"
	edad := 30

	// Constantes
	const pi float64 = 3.1416

	// Variables con tipos de datos primitivos en go
	var verdadero bool = true
	var falso bool = false
	var numeroEntero int8 = -127
	var numeroSinSigno uint8 = 255
	var otroNumeroEntero int = 100 // Dependiente de cpu
	var numeroFlotante float64 = 3.14
	var numeroComplejo complex128 = complex(1, 2) // 1 + 2i

	fmt.Println("¡Hola, Go!")
}