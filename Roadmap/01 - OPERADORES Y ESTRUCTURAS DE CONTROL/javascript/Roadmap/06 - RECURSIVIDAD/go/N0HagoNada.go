package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Println("Introduce una numero (o escribe 'exit' para salir):")
		scanner.Scan()
		input := strings.TrimSpace(scanner.Text())

		if strings.ToLower(input) == "exit" {
			break
		}
		// Convertir la entrada de string a int
		numero, err := strconv.Atoi(input)
		if err != nil {
			fmt.Println("Por favor, introduce un número válido.")
			continue
		}
		resutaldoFibo := CalcularFibonacci(numero)
		resultadoFact := factorial(numero)
		fmt.Printf("El valor en Fibonnaci de %d es: %d\n", numero, resutaldoFibo)
		fmt.Printf("El factorial de %d es: %d\n", numero, resultadoFact)
		if err := scanner.Err(); err != nil {
			fmt.Fprintln(os.Stderr, "Error leyendo entrada:", err)
		}
	}
	fmt.Println("El valor en la secuencia fibonacci para 11 es", CalcularFibonacci(11))
	fmt.Println("El factorial de 5 es", factorial(5))
	ImprimirNumero(100)
}
func ImprimirNumero(n int) {
	if n < 0 {
		os.Exit(0)
	}
	fmt.Println(n)
	ImprimirNumero(n - 1)
}

// Función recursiva para calcular el factorial de un número
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

// Funcion para  Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).+
func CalcularFibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return CalcularFibonacci(n-1) + CalcularFibonacci(n-2)
}
