// https://go.dev/

// Single line comment.

/*
	Multi line comment...
*/

package main

import "fmt"

func main() {
	// Variable declarations
	var number01 int = 1
	const number02 int = 2

	number01 = 3
	// number02 = 2 // Throw an error because It's a constant.

	// Primitive data types
	const byteVar byte = 0

	const integerVar int = -1
	const integer8Var int8 = -12
	const integer16Var int16 = -123
	const integer32Var int32 = -1234
	const integer64Var int64 = -12345

	const uIntegerVar uint = 1
	const uInteger8Var uint8 = 12
	const uInteger16Var uint16 = 123
	const uInteger32Var uint32 = 1234
	const uInteger64Var uint64 = 12345

	const float32Var float32 = 3.141592
	const float64Var float64 = 3.141592

	const booleanVar bool = true

	const stringVar string = "¡Hello World!"

	// Outputs
	fmt.Printf("number01: %d\nnumber02: %d\n\n", number01, number02)

	fmt.Printf("> byteVar: %d --> %T\n\n", byteVar, byteVar)

	fmt.Printf("> integerVar: %d --> %T\n", integerVar, integerVar)
	fmt.Printf("> integer8Var: %d --> %T\n", integer8Var, integer8Var)
	fmt.Printf("> integer16Var: %d --> %T\n", integer16Var, integer16Var)
	fmt.Printf("> integer32Var: %d --> %T\n", integer32Var, integer32Var)
	fmt.Printf("> integer64Var: %d --> %T\n\n", integer64Var, integer64Var)

	fmt.Printf("> uIntegerVar: %d --> %T\n", uIntegerVar, uIntegerVar)
	fmt.Printf("> uInteger8Var: %d --> %T\n", uInteger8Var, uInteger8Var)
	fmt.Printf("> uInteger16Var: %d --> %T\n", uInteger16Var, uInteger16Var)
	fmt.Printf("> uInteger32Var: %d --> %T\n", uInteger32Var, uInteger32Var)
	fmt.Printf("> uInteger64Var: %d --> %T\n\n", uInteger64Var, uInteger64Var)

	fmt.Printf("> float32Var: %f --> %T\n", float32Var, float32Var)
	fmt.Printf("> float64Var: %f --> %T\n\n", float64Var, float64Var)

	fmt.Printf("> booleanVar: %t --> %T\n\n", booleanVar, booleanVar)

	fmt.Printf("> stringVar: %s --> %T\n\n", stringVar, stringVar)

	fmt.Printf("¡Hello, %s!", "Go")
}
