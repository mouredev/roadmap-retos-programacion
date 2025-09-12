
// https://go.dev

/*
	Comments
*/

// single-line comment

/*
	this is a
	multi-line comment
*/

package main

import "fmt"

/*
	Vars And Constants
*/

var word string = "string"
/*
	word2 := "string2" // the type is inferred and just inside functions
*/
const constant string = "constant"

/*
	Primitive Types
*/

var number int = 1 // can be unsigned(uint) and have different ranges(int, int8, int16, int32, int64 or uint versions)
var decimal float32 = 3.5 // float32 or float64
var txt string = "word"
var boolean bool = true

/*
	Print
*/

// The main function in Go prints "¡Hello, Go!" to the console.
func main() {
	fmt.Println("¡Hello, Go!")
}