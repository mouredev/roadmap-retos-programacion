package main

import "fmt"

func main() {
	/*
	   Variable assignment by value...
	*/

	fmt.Println("\nVariable assignment by value...")

	var a int8 = 8
	var b int8 = a

	fmt.Println("\nvar a int8 = 8\nvar b int8 = a")
	fmt.Printf("\nValue of 'a' = %d\nValue of 'b' = %d\n", a, b)

	a = a * 4

	fmt.Println("\na = a * 4")
	fmt.Printf("\nValue of 'a' = %d\nValue of 'b' = %d\n", a, b)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
	   Variable assignment by reference...
	*/

	fmt.Println("\nVariable assignment by reference...")

	c := []int{1, 2, 3, 4}
	d := &c

	fmt.Println("\nc := []int{1, 2, 3, 4}\nd := &c")
	fmt.Printf("\nValue of 'c' = %d\nValue of 'd' = %d\n", c, *d)

	c = append(c, 5)

	fmt.Println("\nc = append(c, 5)")
	fmt.Printf("\nValue of 'c' = %d\nValue of 'd' = %d\n", c, *d)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
	   Function with an argument passed by value...
	*/

	fmt.Println("\nFunction with an argument passed by value...")

	const value int8 = 2
	fnWithParamenterByValue := func(x int8) {
		x += 3
	}

	fmt.Println("\nconst value int8 = 2")
	fmt.Println("fnWithParamenterByValue := func(x int8) { x += 3 }")

	fnWithParamenterByValue(value)
	fmt.Println("\nfnWithParamenterByValue(value)")

	fmt.Printf("\nValue of 'value' = %d\n", value)

	/*
		Function with an argument passed by reference...
	*/

	fmt.Println("\nFunction with an argument passed by reference...")

	reference := []int{12}
	fnWithParamenterByReference := func(x *[]int) {
		*x = append(*x, (*x)[0]/2)
	}

	fmt.Println("\nreference := []int{12}")
	fmt.Println("fnWithParamenterByReference := func(x *[]int) { *x = append(*x, (*x)[0]/2) }")

	fnWithParamenterByReference(&reference)
	fmt.Println("\nfnWithParamenterByReference(&reference)")

	fmt.Printf("\nValue of 'reference' = %d\n", reference)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
	   Additional challenge...
	*/

	firstProgram := func(a int8, b int8) (int8, int8) {
		var aux int8 = a
		a = b
		b = aux

		return a, b
	}

	secondProgram := func(a **[]int8, b **[]int8) (**[]int8, **[]int8) {
		aux := *a
		*a = *b
		*b = aux

		return a, b
	}

	const arg01 int8 = 12
	const arg02 int8 = 34
	arg03 := []int8{1, 2, 3, 4, 5}
	arg04 := []int8{6, 7, 8, 9, 10}
	arg03Pointer := &arg03
	arg04Pointer := &arg04

	newArg01, newArg02 := firstProgram(arg01, arg02)
	newArg03, newArg04 := secondProgram(&arg03Pointer, &arg04Pointer)

	fmt.Printf("\nOriginal:\n	arg01 = %d\n	arg02 = %d", arg01, arg02)
	fmt.Printf("\nNew:\n	newArg01 = %d\n	newArg02 = %d", newArg01, newArg02)

	fmt.Printf("\n\nOriginal:\n	arg03 = %d\n	arg04 = %d", *arg03Pointer, *arg04Pointer)
	fmt.Printf("\nNew:\n	newArg03 = %d\n	newArg04 = %d", **newArg03, **newArg04)
}
