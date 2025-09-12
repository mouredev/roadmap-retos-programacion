package main

import (
	"fmt"
)

var global string = "global"

func main () {
	name()
	fullName("", "")
	fmt.Println(addition(5, -2.5, 1.2))
	var age uint8 = 20
	ageAddition(&age)
	fmt.Println(age)
	first()

	scope()
	// fmt.Println(local) cannot

	fmt.Printf("number of times it was a number and not words: %d", exercise("hello", "go"))
}

// The function "name" in Go language prints "kodenook" to the console.
func name() {
	fmt.Println("kodenook")
}

// The fullName function in Go takes two string parameters, fname and lname, and prints them out with
// default values if either parameter is empty.
func fullName(fname string, lname string) {
	if(fname == "") {
		fname = "my"
	}
	if(lname == "") {
		lname = "surname"
	}

	fmt.Printf("%s %s\n", fname, lname)
}

// The `addition` function in Go calculates the sum of a variable number of float32 numbers.
func addition(numbers ...float32) float32 {
	var result float32 = 0.0

	for _, value := range numbers {
		result += value
	}

	return result
}

// The function `ageAddition` takes a pointer to an unsigned 8-bit integer and adds 5 to its value.
func ageAddition(age *uint8) {
	*age += 5
}

// The function `first` prints "First" and defines an inner function `second` that prints "Second" and
// then calls it.
func first() {
	fmt.Println("First")

	// cannot
	// func second() {
	// 	fmt.Println("Second")
	// }

	// second()

	var second func() = func() {
		fmt.Println("Second")
	}

	second()
}

// The `scope` function in Go demonstrates variable scope by accessing both a global and local
// variable.
func scope() {
	var local string = "local"

	fmt.Println(global)
	fmt.Println(local)
}

/*
	Exercise
*/

// The function `exercise` takes two words as input and prints them based on certain conditions while
// counting the numbers that do not meet those conditions.
func exercise(word1 string, word2 string) uint8 {
	var i uint8
	var countNumbers uint8 = 0

	for i = 1; i < 101; i++ {
		if i % 3 == 0 && i % 5 == 0 {
			fmt.Printf("%s, %s\n", word1, word2)
		} else if i % 3  == 0 {
			fmt.Println(word1)
		} else if i % 5  == 0 {
			fmt.Println(word2)
		}else {
			countNumbers++
		}
	}

	return countNumbers
}