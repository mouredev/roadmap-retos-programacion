package main

import "fmt"

const FROM int = 1
const TO int = 10

func recursiveFn(from int, to int) {
	fmt.Printf("\n%d", from)

	if from < to {
		recursiveFn(from+1, to)
	}
}

func main() {
	/*
		Iterations...
	*/

	fmt.Println("Additional challenge...")

	fmt.Println("\nFirst method...")
	recursiveFn(FROM, TO)

	fmt.Println("\n\nSecond method...")
	for i := FROM; i < TO+1; i++ {
		fmt.Printf("\n%d", i)
	}

	fmt.Println("\n\nThird method...")
	var j int = FROM
	for j < TO+1 {
		fmt.Printf("\n%d", j)
		j++
	}

	fmt.Println("\n\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	fmt.Println("\nFirst method...")
	recursiveFn(FROM, TO)

	fmt.Println("\n\nSecond method...")
	for i := FROM; i < TO+1; i++ {
		fmt.Printf("\n%d", i)
	}

	fmt.Println("\n\nThird method...")
	j = FROM
	for j < TO+1 {
		fmt.Printf("\n%d", j)
		j++
	}

	fmt.Println("\n\nFourth method...")
	for i := range [TO]int{} {
		fmt.Printf("\n%d", i+1)
	}
}
