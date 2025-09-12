package main

import (
	"fmt"
)

func main() {

	/*
		Arithmetic Operators
	*/

	fmt.Println("\nArithmetic Operators\n")
	fmt.Printf("Addition: 1 + 1 = %d\n", 1 + 1)
	fmt.Printf("Subtraction: 1 - 1 = %d\n", 1 - 1)
	fmt.Printf("Multiplication: 1 * 1 = %d\n", 1 * 1)
	fmt.Printf("Division: 1 / 1 = %d\n", 1 / 1)
	fmt.Printf("Modulus: 1 % 1 = %d\n", 1 % 1)

	/*
		Bitwise Operators
	*/

	fmt.Println("\nBitwise Operators\n")
	fmt.Printf("&: 5 & 2 = %d\n", 5 & 2)
	fmt.Printf("|: 5 | 2 = %d\n", 5 | 2)
	fmt.Printf("^: 5 ^ 2 = %d\n", 5 ^ 2)
	fmt.Printf(">>: 5 >> 2 = %d\n", 5 >> 2)
	fmt.Printf("<<: 5 << 2 = %d\n", 5 << 2)

	/*
		Assignment Operators
	*/

	fmt.Println("\nAssignment Operators\n")
	fmt.Println("x = 5")
	fmt.Println("x += 5, x = x + 5")
	fmt.Println("x -= 5, x = x - 5")
	fmt.Println("x *= 5, x = x * 5")
	fmt.Println("x /= 5, x = x / 5")
	fmt.Println("x %= 5, x = x % 5")
	fmt.Println("x &= 5, x = x & 5")
	fmt.Println("x |= 5, x = x | 5")
	fmt.Println("x ^= 5, x = x ^ 5")
	fmt.Println("x >>= 5, x = x >> 5")
	fmt.Println("x <<= 5, x = x << 5")

	/*
	Comparison Operators
	*/

	fmt.Println("\nComparison Operators\n")
	fmt.Printf("Equal to 4 == 4, %t\n", 4 == 4)
	fmt.Printf("Not Equal to 4 != 4, %t\n", 4 != 4)
	fmt.Printf("Greater Than 4 > 5, %t\n", 4 >= 5)
	fmt.Printf("Less Than 4 < 5, %t\n", 4 <= 5)
	fmt.Printf("Greater Than Or Equal To 4 >= 5, %t\n", 4 >= 5)
	fmt.Printf("Less Than Or Equal To 4 <= 5, %t\n", 4 <= 5)

	/*
		Logical Operators
	*/

	fmt.Println("\nLogical Operators\n")
	fmt.Printf("&&, 3 < 5 && 3 < 10, %t\n", 3 < 5 && 3 < 10)
	fmt.Printf("||, 3 < 5 || 3 < 10, %t\n", 3 < 5 || 3 < 4)
	fmt.Printf("!, !(4 < 5), %t\n", !(4 < 5))

	/*
		If
	*/

	if 6 > 5 {
		fmt.Println("6 Is grater than 5")
	} else if 5 < 6 {
		fmt.Println("5 Is less than 6")
	} else {
		fmt.Println("Good Bye")
	}

	/*
		Switch
	*/

	switch 5 + 5 {
		case 2:
			fmt.Println("the case is 2")
		case 5:
			fmt.Println("the case is 5")
		case 8, 10:
			fmt.Println("the case is 8 or 10")
		default:
			fmt.Println("the case is not here")
	}

	/*
		For Loop
	*/

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	fruits := [3]string{"apple", "orange", "banana"}

	for idx, value := range fruits {
		fmt.Printf("the index is %d and the value is %s\n", idx, value)
	}

	/*
		Exercise
	*/

	for i := 10; i < 56; i += 2 {
		if i == 16 || i % 3 == 0 {
			continue;
		}
		fmt.Println(i)
	}
}