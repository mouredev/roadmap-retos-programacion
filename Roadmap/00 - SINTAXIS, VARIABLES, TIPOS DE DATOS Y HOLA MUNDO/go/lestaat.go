package main

// This is the golang programing page https://go.dev/

/*
This is a multiline comment
of this beautiful program :-D
*/

import "fmt"

var myVariable = "Golang"

const myConstant = "My constant is here!"

var myString string = "String"
var myBool bool = true
var myInt int = 10
var myFloat float32 = 3.14
var myComplex complex64 = 2 + 3i
var myAliasByte byte = 65
var myAliasRune rune = '☺'

func main() {
	fmt.Println("Hola " + myVariable)
	fmt.Println(myConstant, myString, myBool, myInt, myFloat, myComplex, myAliasByte, myAliasRune)
}
