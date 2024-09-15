/*
 * Are you ready to learn or review the programming language of your choice?
 * - Remember that all participation instructions are in the
 *   GitHub repository.
 *
 * First things first... Have you already chosen a language?
 * - Not all of them are the same, but their fundamentals are usually common.
 * - This first challenge will help you familiarize yourself with how to participate
 *   by submitting your own solutions.
 *
 * EXERCISE:
 * - Create a comment in the code and place the URL of the official website of
 *   the programming language you have selected.
 * - Represent the different syntaxes that exist for creating comments
 *   in the language (single line, multiple lines...).
 * - Create a variable (and a constant if the language supports it).
 * - Create variables representing all the primitive data types
 *   of the language (strings, integers, booleans...).
 * - Print the text to the terminal: "Hello, [and the name of your language]!"
 *
 * Easy? Don't worry, remember that this is a study path and
 * we must start from the beginning.
 */

//  Documentation: https://go.dev/doc/tutorial/getting-started

package main

import (
	"fmt"
	"unsafe"
)

// Declaring a constant
const greeting = "Hello"

func main() {
      // Declaring a variable
    var name string = "World"
    fmt.Println(greeting + ", " + name + "!")

     // Modifying the variable
     name = "Go"
     fmt.Println(greeting + ", " + name + "!")

     types()
}


func types(){
     // Integer types
     var intVar int = 42
     var int8Var int8 = 127
     var int16Var int16 = 32767
     var int32Var int32 = 2147483647
     var int64Var int64 = 9223372036854775807
 
     var uintVar uint = 42
     var uint8Var uint8 = 255
     var uint16Var uint16 = 65535
     var uint32Var uint32 = 4294967295
     var uint64Var uint64 = 18446744073709551615
 
     // Floating-point types
     var float32Var float32 = 3.14159265358979323846
     var float64Var float64 = 3.14159265358979323846
 
     // Complex types
     var complex64Var complex64 = 3.14 + 2.7i
     var complex128Var complex128 = 3.14 + 2.7i
 
     // Boolean type
     var boolVar bool = true
 
     // String type
     var stringVar string = "Hello, Gabriel!"
 
     // Byte (alias for uint8) and Rune (alias for int32)
     var byteVar byte = 'A'
     var runeVar rune = '☺'

     fmt.Printf("int: %v, Type: %T, Size: %d bytes\n", intVar, intVar, unsafe.Sizeof(intVar))
     fmt.Printf("int8: %v, Type: %T, Size: %d bytes\n", int8Var, int8Var, unsafe.Sizeof(int8Var))
     fmt.Printf("int16: %v, Type: %T, Size: %d bytes\n", int16Var, int16Var, unsafe.Sizeof(int16Var))
     fmt.Printf("int32: %v, Type: %T, Size: %d bytes\n", int32Var, int32Var, unsafe.Sizeof(int32Var))
     fmt.Printf("int64: %v, Type: %T, Size: %d bytes\n", int64Var, int64Var, unsafe.Sizeof(int64Var))
 
     fmt.Printf("uint: %v, Type: %T, Size: %d bytes\n", uintVar, uintVar, unsafe.Sizeof(uintVar))
     fmt.Printf("uint8: %v, Type: %T, Size: %d bytes\n", uint8Var, uint8Var, unsafe.Sizeof(uint8Var))
     fmt.Printf("uint16: %v, Type: %T, Size: %d bytes\n", uint16Var, uint16Var, unsafe.Sizeof(uint16Var))
     fmt.Printf("uint32: %v, Type: %T, Size: %d bytes\n", uint32Var, uint32Var, unsafe.Sizeof(uint32Var))
     fmt.Printf("uint64: %v, Type: %T, Size: %d bytes\n", uint64Var, uint64Var, unsafe.Sizeof(uint64Var))
 
     fmt.Printf("float32: %v, Type: %T, Size: %d bytes\n", float32Var, float32Var, unsafe.Sizeof(float32Var))
     fmt.Printf("float64: %v, Type: %T, Size: %d bytes\n", float64Var, float64Var, unsafe.Sizeof(float64Var))
 
     fmt.Printf("complex64: %v, Type: %T, Size: %d bytes\n", complex64Var, complex64Var, unsafe.Sizeof(complex64Var))
     fmt.Printf("complex128: %v, Type: %T, Size: %d bytes\n", complex128Var, complex128Var, unsafe.Sizeof(complex128Var))
 
     fmt.Printf("bool: %v, Type: %T, Size: %d bytes\n", boolVar, boolVar, unsafe.Sizeof(boolVar))
     fmt.Printf("string: %v, Type: %T, Size: %d bytes\n", stringVar, stringVar, unsafe.Sizeof(stringVar))
 
     fmt.Printf("byte: %v, Type: %T, Size: %d bytes\n", byteVar, byteVar, unsafe.Sizeof(byteVar))
     fmt.Printf("rune: %v, Type: %T, Size: %d bytes\n", runeVar, runeVar, unsafe.Sizeof(runeVar))
}