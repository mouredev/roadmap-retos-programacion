/*
 * EXERCISE:
 * - Create examples using all types of operators in your language:
 *   Arithmetic, logical, comparison, assignment, identity, membership, bitwise...
 *   (Keep in mind that each language may have different ones)
 * - Using operations with operators of your choice, create examples
 *   that represent all types of control structures that exist
 *   in your language:
 *   Conditionals, iterative, exceptions...
 * - You must print the result of all examples to the console.
 *
 * EXTRA DIFFICULTY (optional):
 * Create a program that prints to the console all numbers between
 * 10 and 55 (inclusive), even, and that are neither 16 nor multiples of 3.
 *
 * Surely by carefully reviewing the possibilities you have discovered something new.
 */

package main

import (
	"fmt"
	"os"
)


func main() {
	operators()
	structuresControl()
	exceptionsHandling()
	panichHandling()
	challenge()
}

func operators(){
	a := 10
	b := 5
	
	// Arithmetic Operators:
	var addition = a+b
	var substraction = addition-1;
	var multiplication= substraction *10;
	var division= multiplication/2;
	var module = division %2;
	module++
	module--

	// Logical Operators:
	fmt.Println(a > 0 && b > 0)   // Output: true
	fmt.Println(a > 0 || b < 0)   // Output: true

	// Assignment Operators:
	a += b
	fmt.Println(a)   // Output: 15
	a -= b
	fmt.Println(a)   // Output: 10
	a /= b
	fmt.Println(a)   // Output: 2
	a*=b
	fmt.Println(a)   // Output: 10
	a |= b
	fmt.Println(a)  // Output: 15
	a ^= b
	fmt.Println(a)  // Output: 10

	 // Identity operators
	 c := a
	 fmt.Println(a == c)   // Output: true
	 d := &a
	 e := &a
	 fmt.Println(d == e) 
	 fmt.Println(&a) // This is the memory address 

	  // Membership operators
	  fruits := []string{"apple", "banana", "orange"}
	  fmt.Println("apple" == fruits[0])   // Output: true
	  fmt.Println("grape" == fruits[0])   // Output: false

	    // Bitwise operators
        x := 10
        y := 5
        fmt.Println(x & y)   // Output: 2
        fmt.Println(x | y)   // Output: 15
        fmt.Println(x ^ y)   // Output: 13
        fmt.Println(^x)   // Output: -11
        fmt.Println(x << 2)   // Output: 40
        fmt.Println(x >> 2)   // Output: 2
}

func structuresControl(){
	x:=0;

	// if-else
	if x > 0 {
		fmt.Println("x is positive")
	} else if x == 0 {
		fmt.Println("x is zero")
	} else {
		fmt.Println("x is negative")
	}

	// switch
	day:= "Monday"
	switch day {
	case "Monday", "Tuesday", "Wednesday", "Thursday", "Friday":
		fmt.Println("Weekday")
	case "Saturday", "Sunday":
		fmt.Println("Weekend")
	default:
		fmt.Println("Invalid day")
	}

	// for loop
	for i := 0; i < 2; i++ {
		fmt.Println(i)
	}

	// Range loop
	fruits := []string{"apple", "banana", "orange"}
	for index, fruit := range fruits {
		fmt.Println(index, fruit)
	}

	// While loop
	i := 0
	for i < 3 {
		fmt.Println(i)
		i++
	}
}

func divide(a, b int) int {
    if b == 0 {
        panic("Division by zero")
    }
    return a / b
}

func exceptionsHandling(){
	file, err := os.Open("file.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()
}

func panichHandling(){
	// this function in defer would recover from the error of ttrying dividing by 0
	defer func() {
        if err := recover(); err != nil {
            fmt.Println("Recovered  from panic:", err)
        }
    }()
    result := divide(10, 0)
    fmt.Println(result)
}

func challenge(){
	fmt.Println("================ CHALLENGE ================")
	// Create a program that prints to the console all numbers between
	// 10 and 55 (inclusive), even, and that are neither 16 nor multiples of 3.

	i := 10
	for i < 56 {
		if(i%2 ==0 && i != 16 && i%3 !=0){
			fmt.Println(i)
		}
		i++
	}
}