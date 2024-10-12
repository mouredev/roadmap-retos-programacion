/*
 * EXERCISE:
 * - Create examples of basic functions that represent the different
 *   possibilities of the language:
 *   Without parameters or return, with one or more parameters, with return...
 * - Check if you can create functions within functions.
 * - Use some examples of functions already created in the language.
 * - Test the concept of LOCAL and GLOBAL variables.
 * - You must print the result of all examples to the console.
 *   (and keep in mind that each language may have more or fewer possibilities)
 *
 * EXTRA DIFFICULTY (optional):
 * Create a function that receives two parameters of string type and returns a number.
 * - The function prints all numbers from 1 to 100. Taking into account that:
 *   - If the number is a multiple of 3, it shows the text string of the first parameter.
 *   - If the number is a multiple of 5, it shows the text string of the second parameter.
 *   - If the number is a multiple of 3 and 5, it shows both text strings concatenated.
 *   - The function returns the number of times the number has been printed instead of the texts.
 *
 * Pay special attention to the syntax you should use in each of the cases.
 * Each language follows conventions that you must respect for the code to be understood.
 */

package main

import "fmt"
 var globalvar = "I am global because I am outside any function or block."
 func main() {
	var localVar ="I am local because I am inside a function";
	fmt.Println(localVar);
	fmt.Println(noParams()); // No params
	fmt.Println(withParams(1,2)) // 3
	var number = 1;
	notReturn(&number);
	fmt.Println(number);  // 2
	b(a); // string
	recursive(&number,10);

	// Anonymous Functions
	anonFunc := func() {
        fmt.Println("I am an anonymous function")
    }
	anonFunc();

	// Clousures
	counter := 0
    increment := func() int {
        counter++
        return counter
    }
    fmt.Println(increment()) // 1
    fmt.Println(increment()) // 2
	fmt.Println(sum(1,2,3,4,5)) //15
	challenge("fizz","buzz");
 }

 // Without Params
 func noParams() string {
	return "No Params";
 }

 // With Params
 func withParams(num1 int, num2 int) int{
	return num1 + num2;
 }

 // Function modifying external variable
 func notReturn(num *int){
	*num += 1;
 }

 // High order Functions
 func a () string {
	return "I am func A"
 }

 func b (function func() string) {
	fmt.Println("I am in func B and I an calling this fn: " + function());
 }

 // Recursive Function
 func recursive (num *int , max int){
	if *num <= max {
		fmt.Println("This is recutsive: ")
		fmt.Println(*num)
		*num++
		recursive(num, max)
	}
 }

 // Variable number of arguments
 func sum(nums ...int) int {
    total := 0
    for _, num := range nums {
        total += num
    }
    return total
}

func challenge(str1 string, str2 string){
	for i:=0; i<100; i++{
		if(i %3 ==0 && i%5==0){
			fmt.Println(str1 +  " "+ str2)
		} else if(i % 3==0){
			fmt.Println(str1)
		} else if(i % 5==0){
			fmt.Println(str2)
		}

	}

}