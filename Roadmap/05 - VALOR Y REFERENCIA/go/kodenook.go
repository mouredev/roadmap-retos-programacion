package main

import "fmt"

func main() {

	/*
		Assignment by value
	*/

	var var1 uint = 3
	var var2 uint = var1

	var1 = 4

	fmt.Println(var1)
	fmt.Println(var2)

	/*
		Assignment by reference
	*/

	var var3 uint = 3
	var var4 *uint = &var3

	var3 = 5

	fmt.Println(var3)
	fmt.Println(*var4)
}
