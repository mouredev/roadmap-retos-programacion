package main

import "fmt"

// Documentacion en https://go.dev/

// Comentario de una sola linea

/*
Comentario de
multiples lineas
*/

const PI float64 = 3.1416

var lenguaje string = "Go"

func main() {
	// Tipos de datos primitivos
	var edad int = 25
	var nombre string = "Miguel"
	var isDev bool = true
	var nota float64 = 8.5

	// Imprimir por consola
	fmt.Println("Hola " + lenguaje)
	fmt.Println(edad, nombre, isDev, nota)
}
