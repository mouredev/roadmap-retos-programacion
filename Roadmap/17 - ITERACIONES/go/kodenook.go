package main

import "fmt"

func main() {
	// This Go code snippet is using a `for` loop to iterate over the numbers from 1 to 10.
	for i := 1; i < 11; i++ {
		fmt.Printf("%d\n", i)
	}

	// This code snippet in Go is creating an array named `loop` with a length of 10, where each element
	// is of type `uint` (unsigned integer).
	loop := [10]uint{}
	for i, _ := range loop {
		fmt.Printf("%d\n", i+1)
	}

	// The code snippet you provided is using a `for` loop with a condition to iterate over the numbers
	// from 1 to 10. Here's a breakdown of what it does:
	index := 1
	for index < 11 {
		fmt.Printf("%d\n", index)
		index++
	}

	// The code snippet `index = 1
	// for ; index < 11; index++ {
	//     fmt.Printf("%d\n", index)
	// }` is using a `for` loop in Go to iterate over the numbers from 1 to 10. Here's a breakdown of what
	// it does:
	index = 1
	for ; index < 11; index++ {
		fmt.Printf("%d\n", index)
	}
}
