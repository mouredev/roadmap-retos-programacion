package main

import "fmt"

func main() {
	countDownRecursive(2)
	f2 := factorialN(7)
	fmt.Println("Factorial de 7 es", f2)
	result := factorial(5)
	fmt.Println("Factorial de 5 es :", result)
	f1 := fibonacci(7)
	fmt.Println("Fibonacci de 7 es :", f1)

}

func countDownRecursive(n int) {
	if n < 0 {
		fmt.Println("La cuenta terminó")
		return
	}
	fmt.Println("Count : ", n)
	countDownRecursive(n - 1)

}

func factorialN(n int) int {
	if n == 0 {
		return 1
	}
	accumulator := 1
	for i := 1; i <= n; i++ {
		accumulator *= i
	}
	return accumulator
}

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

//Función para calcular el n-ésimo número de Fibonacci
func fibonacci(n int) int {
	if n <= 1 {
		return 0
	} else if n == 2 {
		return 1
	}
	return fibonacci(n-1) + fibonacci(n-2)
}
