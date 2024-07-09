package main

import "fmt"

func main() {
	recursion(100)
}

func recursion(number uint64) {
	fmt.Println(number)

	if number > 0 {
		recursion(number - 1)
	}
}
