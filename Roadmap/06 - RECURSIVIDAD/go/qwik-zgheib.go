package main

import "fmt"

/* example */
type RecursivePrinter interface {
	PrintNumbers(n int)
}

type NumberPrinter struct{}

func NewNumberPrinter() *NumberPrinter {
	return &NumberPrinter{}
}

func (np *NumberPrinter) PrintNumbers(n int) {
	if n < 0 {
		return
	}
	fmt.Println(n)
	np.PrintNumbers(n - 1)
}

/* extra - i */
type FactorialCalculator interface {
	Factorial(n int) int
}

type SimpleFactorialCalculator struct{}

func NewSimpleFactorialCalculator() *SimpleFactorialCalculator {
	return &SimpleFactorialCalculator{}
}

func (fc *SimpleFactorialCalculator) Factorial(n int) int {
	if n <= 1 {
		return 1
	}
	return n * fc.Factorial(n-1)
}

type SimpleFibonacciCalculator struct{}

/* extra - ii */
type FibonacciCalculator interface {
	Fibonacci(n int) int
}

func NewSimpleFibonacciCalculator() *SimpleFibonacciCalculator {
	return &SimpleFibonacciCalculator{}
}

func (fc *SimpleFibonacciCalculator) Fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return fc.Fibonacci(n-1) + fc.Fibonacci(n-2)
}

func main() {
	numberPrinter := NewNumberPrinter()
	factorialCalculator := NewSimpleFactorialCalculator()
	fibonacciCalculator := NewSimpleFibonacciCalculator()

	fmt.Println("Printing numbers from 100 to 0:")
	numberPrinter.PrintNumbers(100)

	fmt.Println("\nFactorial of 5:")
	fmt.Println(factorialCalculator.Factorial(5))

	fmt.Println("\nFibonacci number at position 10:")
	fmt.Println(fibonacciCalculator.Fibonacci(10))
}
