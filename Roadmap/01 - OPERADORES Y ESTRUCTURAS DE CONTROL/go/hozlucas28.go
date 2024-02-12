package main

import "fmt"

func main() {
	/*
		Type of operators...
	*/

	// Arithmetic
	const addition int = 1 + 1
	fmt.Printf("Addition: 1 + 1 --> %d\n", addition)

	const subtraction int = 1 - 1
	fmt.Printf("Subtraction: 1 - 1 --> %d\n", subtraction)

	const Multiplication int = 2 * 3
	fmt.Printf("Multiplication: 2 * 3 --> %d\n", Multiplication)

	const quotient int = 8 / 2
	fmt.Printf("Quotient: 8 / 2 --> %d\n", quotient)

	const remainder int = 13 % 3
	fmt.Printf("Remainder: 13 %% 3 --> %d\n", remainder)

	// Comparison
	const equal bool = 1 == 1
	fmt.Printf("\nEqual: 1 == 1 --> %t\n", equal)

	const notEqual bool = 1 != 2
	fmt.Printf("Not equal: 1 != 2 --> %t\n", notEqual)

	const greaterThan bool = 2 > 2
	fmt.Printf("Greater than: 2 > 2 --> %t\n", greaterThan)

	const lessThan bool = -1 < 0
	fmt.Printf("Less than: -1 < 0 --> %t\n", lessThan)

	const greaterThanOrEqualTo bool = 2 >= 2
	fmt.Printf("Greater than or equal to: 2 >= 2 --> %t\n", greaterThanOrEqualTo)

	const lessThanOrEqualTo bool = -1 <= -0.5
	fmt.Printf("Less than or equal to: -1 <= -0.5 --> %t\n", lessThanOrEqualTo)

	// Logical
	fmt.Printf("\nAnd: true && false --> %t\n", true && false)

	fmt.Printf("Or: false || true --> %t\n", false || true)

	fmt.Printf("Not: !true --> %t\n", !true)

	// Address
	var number int8 = 16
	fmt.Printf("\nAddress / Pointer: < const number int8 > --> %p\n", &number)

	/*
		Control structures...
	*/

	// < if > and < if else >
	if true {
		fmt.Printf("\nIf: True statement\n")
	}

	if false {
		fmt.Printf("If else: False --> True statement\n")
	} else {
		fmt.Printf("If else: False --> False statement\n")
	}

	// < switch >
	const letter string = "A"

	switch letter {
	case "D":
		fmt.Printf("Switch: 'A' --> Case 1 ('D')\n")

	case "C":
		fmt.Printf("Switch: 'A' --> Case 2 ('C')\n")

	case "B":
		fmt.Printf("Switch: 'A' --> Case 3 ('B')\n")

	default:
		fmt.Printf("Switch: 'A' --> Default case ('A')\n")
	}

	// < for (while version) >
	var i int8 = 5

	fmt.Println("")
	for i > 0 {
		if i == 2 {
			i--
			continue
		}

		fmt.Printf("For (while version): i > 0 --> %d iteration\n", i)
		i--
	}

	// < for >
	fmt.Println("")
	for j := 1; j < 11; j++ {
		if j == 5 {
			break
		}

		fmt.Printf("For: j > 0 --> %d iteration\n", j)
	}

	/*
	   Additional challenge...
	*/

	fmt.Println("")
	for k := 10; k < 56; k++ {
		if k != 16 && k%2 == 0 && k%3 != 0 {
			fmt.Printf("%d\n", k)
		}

	}

}
