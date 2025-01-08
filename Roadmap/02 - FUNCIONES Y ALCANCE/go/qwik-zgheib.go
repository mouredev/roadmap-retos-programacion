package main

import (
	"fmt"
)

// global variable
var globalVar int = 100

// function without parameters and return
func noParamsNoReturn() {
	fmt.Println("Function without parameters and return")
}

// function with one parameter
func oneParam(param int) {
	fmt.Printf("Function with one parameter: %d\n", param)
}

// function with multiple parameters
func multipleParams(param1 int, param2 string) {
	fmt.Printf("Function with multiple parameters: %d, %s\n", param1, param2)
}

// function with return
func withReturn() int {
	return 42
}

// function with multiple parameters(defined) and return
func multipleParamsWithReturn(param1 int, param2 string) string {
	return fmt.Sprintf("Function with multiple parameters and return: %d, %s", param1, param2)
}

// function with multiple parameters(undefined) and return
func multipleParamsWithReturnUndefined(numbers ...int) int {
	sum := 0
	for _, number := range numbers {
		sum += number
	}
	return sum
}

// function inside a function
func outerFunction() {
	fmt.Println("Outer function")
	innerFunction := func() {
		fmt.Println("Inner function")
	}
	innerFunction()
}

// local and global variables
func localVsGlobal() {
	localVar := 10
	fmt.Printf("Local variable: %d\n", localVar)
	fmt.Printf("Global variable: %d\n", globalVar)
}

// function extra: FizzBuzz
func fizzBuzz(str1, str2 string) int {
	count := 0
	for i := 1; i <= 100; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println(str1 + str2)
		} else if i%3 == 0 {
			fmt.Println(str1)
		} else if i%5 == 0 {
			fmt.Println(str2)
		} else {
			fmt.Println(i)
			count++
		}
	}
	return count
}

func main() {
	noParamsNoReturn()
	oneParam(10)
	multipleParams(20, "Hello")
	fmt.Println(withReturn())
	fmt.Println(multipleParamsWithReturn(30, "World"))

	fmt.Printf("Sum of numbers: %d", multipleParamsWithReturnUndefined(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
	fmt.Println("\n------")

	outerFunction()

	localVsGlobal()

	fmt.Printf("Count of numbers printed: %d\n", fizzBuzz("Fizz", "Buzz"))
}
