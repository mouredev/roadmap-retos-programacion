package main

import "fmt"

func main() {
	n1 := 2
	n2 := 3

	result := apply(n1, n2, add)

	fmt.Println(result)
}

func apply(n1, n2 int, operation func(int, int) int) int {
	return operation(n1, n2)
}

func add(n1, n2 int) int {
	return n1 + n2
}
