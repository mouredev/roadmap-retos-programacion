package main

import "fmt"

func main() {
	fmt.Println(cuentaRegresiva(100))
	fmt.Println(factorial(5)) //120
	fmt.Println(fibonacci(10)) //55
}

func cuentaRegresiva(number int) int{
	if number == 0 { return 0 }
	fmt.Println(number)
	return cuentaRegresiva(number - 1)
}

//Dificultad extra
func factorial(number int) int{
	if number == 0 { return 1 }
	return number * factorial(number - 1)
}

//Dificultad extra
func fibonacci(position int) int{
	if position == 0 { return 0 }
	if position == 1 { return 1 }
	return fibonacci(position - 1) + fibonacci(position - 2)
}