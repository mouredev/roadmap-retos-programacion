package main

import "fmt"

// Golang language documentation: https://go.dev/doc/

func main() {
	// comment line

	/*
	   multi-line comment
	*/

	// primitive data types
	var number int = 10
	var decimal float64 = 10.2
	var text string = "Hello, World!"
	var boolean bool = true

	// arrays
	var numbers [5]int = [5]int{number, 2, 3, 4, 5}

	// slices
	var numbersSlice []int = []int{numbers[1], 2, 3, 4, 5}
	numbersSlice = append(numbersSlice, 6)

	// maps
	var person map[string]string = map[string]string{
		"name":    "qwik zgheib",
		"gender":  "male",
		"address": "hanac wichay",
	}

	// structs
	type Person struct {
		Name    string
		Gender  string
		Address string
	}

	var personStruct Person = Person{
		Name:    person["name"],
		Gender:  person["gender"],
		Address: person["address"],
	}

	// print variables
	fmt.Println("number:", numbersSlice)
	fmt.Println("decimal:", decimal)
	fmt.Println("text:", text)
	fmt.Println("boolean:", boolean)

	// print personStruct
	fmt.Println("personStruct:", personStruct)

	/* --- */
	fmt.Println("Hello, go!")
}
