/*
   EJERCICIO:
   1) Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
   2) Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
   3) Crea una variable (y una constante si el lenguaje lo soporta).
   4) Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
   5) Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

// 1) https://go.dev/doc/

// 2) Comentario de una linea y varias

/*
Comentario de varias lineas
*/
package main

import "fmt"

func main() {
	// 3) Variable y constante
	const pi float64 = 3.1416
	var variable string = "Go"
	otra_variable := "otra manera de declarar variable"

	// 4) Tipos de variables primitivas https://go.dev/learn/
	//Tipos numericos
	// unsigned integers
	var _uint uint = 18446744073709551615
	var _uint8 uint8 = 255
	var _uint16 uint16 = 65535
	var _uint32 uint32 = 4294967295
	var _uint64 uint64 = 18446744073709551615
	// signed integers
	var _int int = -2147483648
	var _int8 int8 = 127
	var _int16 int16 = 32767
	var _int32 int32 = 2147483647
	var _int64 int64 = 9223372036854775807
	// float point numbers
	var _float32 float32 = 1234.5
	var _float64 float64 = 13412341212342.3434342432
	// complex numbers
	var _complex64 complex64 = 1i
	var _complex128 complex128 = 1e64i

	// Tipos boleanos
	var _true bool = true
	var _false bool = false

	//Tipos lista o slice
	var _slice_string []string = []string{"1", "2", "3"}
	var _slice_int []int = []int{1, 2, 3}

	// Tipo de dato
	var _map_string_string map[string]string = map[string]string{"1": "first", "2": "second", "3": "third"}
	var _map_string_int map[string]int = map[string]int{"first": 1, "second": 2, "third": 3}

	// 5) print() hola Go
	fmt.Println("¡Hola, Go!")
	fmt.Println(
		pi,
		variable,
		otra_variable,
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
		_true,
		_false,
		_slice_string,
		_slice_int,
		_map_string_string,
		_map_string_int)
}
