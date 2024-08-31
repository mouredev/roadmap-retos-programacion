package main

import "fmt"

// https://go.dev/

// single line comment

/*
multi line comment
*/

const PI float64 = 3.1416

func main() {
	var lenguaje string = "golang"
	otherLenguaje := "python"

	// primitive types
	var age int = 25
	var name string = "Kevin"
	var married bool = true
	var score float64 = 8.5

	fmt.Println("Hola" + " " + lenguaje)
	fmt.Println(age, name, married, score, otherLenguaje)
}
