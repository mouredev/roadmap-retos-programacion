// https://go.dev/

package main

import "fmt"

func main() {
	// Este es un comentario de una sola línea

	// Este es un comentario
	// de múltiples líneas

	/*
	Este es un comentario
	de múltiples líneas
	*/

	const foo string = "bar"
	var baz string = "vaz"

	// boolean variables
	var boolean_variable bool = true

	// numeric variables

	// unsigned integers
	var uint_variable uint = 18446744073709551615
	var uint8_variable uint8 = 255
	var uint16_variable uint16 = 65535
	var uint32_variable uint32 = 4294967295
	var uint64_variable uint64 = 18446744073709551615

	// signed integers
	var int_variable int = -2147483648
	var int8_variable int8 = 127
	var int16_variable int16 = 32767
	var int32_variable int32 = 2147483647
	var int64_variable int64 = 9223372036854775807

	// float point numbers
	var float32_variable float32 = 1234.5
	var float64_variable float64 = 13412341212342.3434342432

	// complex numbers
	var complex64_variable complex64 = 1i
	var complex128_variable complex128 = 1e64i

	// strings
	var string_variable = "foobar"

	fmt.Println("¡Hola, Go!")

	fmt.Println(
		baz,
		boolean_variable,
		uint_variable,
		uint8_variable,
		uint16_variable,
		uint32_variable,
		uint64_variable,
		int_variable,
		int8_variable,
		int16_variable,
		int32_variable,
		int64_variable,
		float32_variable,
		float64_variable,
		complex64_variable,
		complex128_variable,
		string_variable,
	)
}
