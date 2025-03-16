//package main

// Go official website: https://go.dev

// This is a single line comment

/*This is
  a multiple line comment
  for this tutorial
*/

package main

import (
	"fmt"
	"math/cmplx"
)

// Variable
var my_name = "CB"

// Constant
const Pi = 3.1416

// Primitive types
var my_other_name string = "Rafael"
var my_number int = 8
var my_decimal float64 = 12.41
var my_bulb bool = false
var my_complex128 complex128 = cmplx.Sqrt(-5 + 12i)
var my_uint uint64 = 1<<64 - 1
var my_rune rune = 2147483647

func main() {
	//Print on Terminal name of used programming language
	fmt.Println("¡Hello, Go!")

	//Additional to know what type of variable is ->
	fmt.Printf("The type of %v is %T", my_complex128, my_complex128)
}
