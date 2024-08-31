// https://go.dev/

package main

import "fmt"

func main() {
	// Comentario de una sola línea

	// Comentario de
	// múltiples líneas

	/*
		Comentario de
		múltiples líneas
	*/

	const firstString string = "first"
	var secondString string = "second"

	// Otra manera de declarar variables
	thirdString := "third"

	// bool
	var trueBool bool = true
	var falseBool bool = false

	// uint integers
	var _uint uint = 4294967295
	var _uint8 uint8 = 255
	var _uint16 uint16 = 65535
	var _uint32 uint32 = 4294967295
	var _uint64 uint64 = 18446744073709551615

	// int
	var _int int = -2147483648
	var _int8 int8 = 127
	var _int16 int16 = 32767
	var _int32 int32 = 2147483647
	var _int64 int64 = 9223372036854775807

	// float
	var _float32 float32 = 123.0
	var _float64 float64 = 12345678910.12345678910

	// complex
	var _complex64 complex64 = 1i
	var _complex128 complex128 = 1e64i

	// slice
	var firstSlice []string = []string{"first", "second", "third"}
	var secondSlice []int = []int{1, 2, 3}

	// map
	var firstMap map[string]string = map[string]string{"first": "first", "second": "second", "third": "third"}
	var secondMap map[string]int = map[string]int{"first": 1, "second": 2, "third": 3}

	fmt.Println("¡Hola, Go!")

	fmt.Println(
		firstString,
		secondString,
		thirdString,
		trueBool,
		falseBool,
		_uint,
		_uint8,
		_uint16,
		_uint32,
		_uint64,
		_int,
		_int8,
		_int16,
		_int32,
		_int64,
		_float32,
		_float64,
		_complex64,
		_complex128,
		firstSlice,
		secondSlice,
		firstMap,
		secondMap,
	)

}
