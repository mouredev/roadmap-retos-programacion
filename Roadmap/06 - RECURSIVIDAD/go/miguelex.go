package main

import "fmt"

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

func potencia(base, exponente int) int {
	if exponente == 0 {
		return 1
	}
	return base * potencia(base, exponente-1)
}

func suma(a, b int) int {
	if b == 0 {
		return a
	}
	return 1 + suma(a, b-1)
}

func imprimirNumeros(numero int) {
	if numero >= 0 {
		fmt.Print(numero, " ")
		imprimirNumeros(numero - 1)
	}
}

func main() {
	fmt.Println("La suma de 3 + 5 usando recursividad es: ", suma(3, 5))
	fmt.Println("La potencia de 2^3 usando recursividad es: ", potencia(2, 3))
	fmt.Println("El valor de 5! es: ", factorial(5))
	fmt.Println("El valor de del 10º numero de Fibonacci es: ", fibonacci(10))
	fmt.Println("De 100 a 0 usando rercursividad: ")
	imprimirNumeros(100)
	var n int
	fmt.Println("Ingrese un número para calcular su factorial: ")
	fmt.Scan(&n)
	fmt.Println("El valor de ", n, "! es: ", factorial(n))
	fmt.Println("Ingrese un número para calcular su número de Fibonacci: ")
	fmt.Scan(&n)
	fmt.Println("El valor de del ", n, "º numero de Fibonacci es: ", fibonacci(n))

}
