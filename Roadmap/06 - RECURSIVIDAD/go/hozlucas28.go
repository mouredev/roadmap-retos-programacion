package main

import "fmt"

func main() {
	/*
	   Recursive function...
	*/

	fmt.Println("\nRecursive function...")

	var recursiveFn func(from int, to int, rtn *[]int)

	recursiveFn = func(from int, to int, rtn *[]int) {
		if from < to {
			return
		}

		*rtn = append(*rtn, from)
		recursiveFn(from-1, to, rtn)
	}

	fmt.Println("\nvar recursiveFn func(from int, to int, rtn *[]int)")

	fmt.Println("\nrecursiveFn = func(from int, to int, rtn *[]int) {\n  if from < to {\n    return\n  }\n\n  *rtn = append(*rtn, from)\n  recursiveFn(from-1, to, rtn)\n}")

	var recursiveRtn []int
	recursiveFn(100, 0, &recursiveRtn)

	fmt.Println("\nvar recursiveRtn []int")
	fmt.Println("recursiveFn(100, 0, recursiveRtn)")

	fmt.Printf("\nrecursiveRtn --> %d\n", recursiveRtn)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #\n")

	/*
	   Additional challenge...
	*/

	fmt.Println("Get factorial...")

	var getFactorial func(number int) int

	getFactorial = func(number int) int {
		if number < 2 {
			return 1
		}

		return number * getFactorial(number-1)
	}

	fmt.Println("\nvar getFactorial func(number int) int")

	fmt.Println("\ngetFactorial = func(number int) int {\n  if number < 2 {\n    return 1\n  }\n\n  return number * getFactorial(number-1)\n}")

	fmt.Printf("\ngetFactorial(5) --> %d\n", getFactorial(5))

	fmt.Println("\n# ---------------------------------------------------------------------------------- #\n")

	fmt.Println("Get Fibonacci value by position...")

	var getFibonacciValueByPos func(position int) int

	getFibonacciValueByPos = func(position int) int {
		if position == 1 || position == 2 {
			return 1
		}

		return getFibonacciValueByPos(position-1) + getFibonacciValueByPos(position-2)
	}

	fmt.Println("\nvar getFibonacciValueByPos func(position int) int")

	fmt.Println("\ngetFibonacciValueByPos = func(position int) int {\n  if position == 1 || position == 2 {\n    return 1\n  }\n\n  return getFibonacciValueByPos(position-1) + getFibonacciValueByPos(position-2)\n}")

	fmt.Printf("\ngetFibonacciValueByPos(8) --> %d", getFibonacciValueByPos(8))

}
