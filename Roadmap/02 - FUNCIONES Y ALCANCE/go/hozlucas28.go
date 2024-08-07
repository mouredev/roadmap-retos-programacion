package main

import "fmt"

/*
   Types of functions (1)...
*/

// Common function
func commonFn() {
	fmt.Print("\nCommon function: func <FUNCTION NAME>(<PARAMETERS...>) {<INTRUCTIONS...>}")
}

// With parameter
func fnWithParameter(name string) {
	fmt.Printf("\nCommon function (with parameter): func <FUNCTION NAME>(name string) {<INTRUCTIONS...>} --> Hello %s!", name)
}

// With pointer parameter
func fnWithPointerParameter(lastName *string) {
	fmt.Printf("\nCommon function (with pointer parameter): func <FUNCTION NAME>(lastName *string) {<INTRUCTIONS...>} --> Hello %s!", *lastName)
}

// Without parameter
func fnWithoutParameter() {
	fmt.Print("\nCommon function (without parameter): func <FUNCTION NAME>() {<INTRUCTIONS...>} --> Hello!")
}

// With rest parameter
func fnWithRestParameter(numbers ...int) {
	fmt.Printf("\nCommon function (with rest parameter): func <FUNCTION NAME>(numbers ...int) {<INTRUCTIONS...>} --> %d!", numbers)
}

// With return
func fnWithReturn() int8 {
	return 10
}

// With multiple returns
func fnWithMultipleReturn() (string, int8) {
	return "Age", 21
}

// Without return
func fnWithoutReturn() {
	fmt.Printf("\nCommon function (without return): func <FUNCTION NAME>() {<INTRUCTIONS (return not included)...>} --> return void")
}

/*
   Function definition inside another function...
*/
func main() {
	/*
	   Types of functions (2)...
	*/

	// IIFE
	func() {
		fmt.Print("IFE (Immediately-Invoked Function Expression): func(){<INTRUCTIONS...>}()")
	}()

	// Function associated with a variable
	fn := func() {
		fmt.Print("\nFunction associated with a variable: <VARIABLE NAME> := func(<PARAMETERS...>) {<INTRUCTIONS...>}")
	}

	fn()
	commonFn()
	fnWithParameter("Lucas")

	var lastName string = "Hoz"
	fnWithPointerParameter(&lastName)

	fnWithoutParameter()
	fnWithRestParameter(1, 3, 5, 6, 7, 9)

	fmt.Printf("\nCommon function (with return): func <FUNCTION NAME>() int8 {<INTRUCTIONS (with return definition included)...>} --> return %d", fnWithReturn())

	var ageStr, ageInt = fnWithMultipleReturn()
	fmt.Printf("\nCommon function (with multiple returns): func <FUNCTION NAME>() (string, int8) {<INTRUCTIONS (with return definition included)...>} --> return %s, %d", ageStr, ageInt)

	fnWithoutReturn()

	/*
	   Native functions...
	*/

	array01 := [5]int{1, 2, 3, 4, 5}
	fmt.Printf("\n\nNative functions: len(%d) --> %d", array01, len(array01))

	var array02 []int
	array02 = append(array02, 4)
	fmt.Printf("\nNative functions: append([], 4) --> %d", array02)

	/*
	   Global and local variables...
	*/

	const food string = "Meat"

	showFood := func() string {
		const drink string = "Coca Cola"
		return "function call with a global variable --> food = " + food
	}

	fmt.Printf("\n\nGlobal variable: %s", showFood())
	// fmt.Printf("\nLocal variable: variable defined inside a function but called outside it --> drink = %s", drink) // Throw an undefined error.
	fmt.Printf("\nLocal variable: variable defined inside a function but called outside it --> drink = undefined")

	/*
	   Additional challenge...
	*/

	additionalChallenge := func(str01 *string, str02 *string) int8 {
		var counter int8 = 0

		fmt.Println("")
		for i := 1; i < 101; i++ {
			var multipleOfFive bool = i%5 == 0
			var multipleOfThree bool = i%3 == 0

			if multipleOfFive && multipleOfThree {
				fmt.Printf("\n%s", *str01+*str02)
				continue
			}

			if multipleOfFive {
				fmt.Printf("\n%s", *str02)
				continue
			}

			if multipleOfThree {
				fmt.Printf("\n%s", *str01)
				continue
			}

			fmt.Printf("\n%d", i)
			counter++
		}

		return counter
	}

	var str01 string = "fizz"
	var str02 string = "buzz"
	fmt.Printf("\n\n%d numbers was printed instead of 'fizz' or 'buzz' (function arguments)!", additionalChallenge(&str01, &str02))
}
