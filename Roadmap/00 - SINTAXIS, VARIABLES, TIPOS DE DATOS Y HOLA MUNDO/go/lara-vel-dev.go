// https://go.dev/doc/

package main

import "fmt"

func main() {
	// This is a single line comment

	/* This is a
	   multiline comment
	*/

	// Declaring variables
	var myVar string = "I'm a variable"
	const myConst string = "I'm a constant"
	shorthandVar := "I'm a shorthand syntax variable"

	// Print variables
	fmt.Printf("Var: %s, Const: %s, Shorthand: %s ", myVar, myConst, shorthandVar)

	/* D A T A    T Y P E S
	* int
		* int8
		* int16
		* int32
		* int64
	* uint
		* uint8
		* uint16
		* uint32
		* uint64
	* byte
	* float32
	* float64
	* string
	* bool
	* rune
	* complex
	*/

	var number int = -56
	var unsignedNumber uint = 24
	var floating float32 = 2.25
	var text string = "hola"
	var myByte byte = 'a'
	var isActive bool = true
	var myRune rune = 'Ś'
	var complexNum complex64 = 2.5 + 3.5i

	fmt.Printf("number: %d \nunsigned number: %d \nfloat: %f\ntext: %s"+
		"\nbyte: %T \nboolean: %T \nrune: %T \ncomplex: %T", number, unsignedNumber,
		floating, text, myByte, isActive, myRune, complexNum)

	// Print hello go
	fmt.Println("Hello, Go!")

}
