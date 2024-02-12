package main

import "fmt"

// https://go.dev/

func main() {

	// Comentario de una sola linea

	/* Comentario de
	multiples lineas*/

	// Declaración de una Variable
	var myVariable string = "Sergio"

	// Declaración de una Constante
	const myConstant string = "Colombia"

	// Tipos de datos primitivos
	// Datos enteros
	var myInt int = 10
	var myInt8 int8 = 20
	var myInt16 int16 = 30
	var myInt32 int32 = 40
	var myInt64 int64 = 50

	var myUint uint = 60
	var myUint8 uint8 = 70
	var myUint16 uint16 = 80
	var myUint32 uint32 = 90
	var myUint64 uint64 = 100

	// Datos flotantes
	var myFloat32 float32 = 123.45
	var myFloat64 float64 = 1.2e+345

	// Datos caracter
	var myRune rune = 'Ӂ'
	var myByte byte = 'A'

	// Dato booleano
	var myBooleano bool = true

	// Imprimir texto
	fmt.Println("¡Hola, Go!")
}
