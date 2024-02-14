package main

import "fmt"

func pasoPorValor(x int) int {
	x = 0
	return x
}

func pasoPorReferencia(x *int) int {
	*x = 0
	return *x
}

func intercambioPorvalor(x int, y int) (int, int) {
	return y, x
}

func intercambioPorReferencia(x *int, y *int) {
	*x, *y = *y, *x
}

func main() {
	// Declaracion de variable por valor

	fmt.Println("\nDeclaracion de variable por valor")

	var num1 = 10
	var num2 = num1

	fmt.Printf("\nvar num1 %d \nvar num2 %d ", num1, num2)

	num1 = 20

	fmt.Printf("\nvar num1 %d \nvar num2 %d ", num1, num2)

	// Declaracion de variable por referencia

	fmt.Println("\nDeclaracion de variable por referencia")

	var num3 = []int{1, 2, 3, 4}
	var num4 = &num3

	fmt.Printf("\nvar num3 %d \nvar num4 %d ", num3, *num4)

	num3[1] = 56789

	fmt.Printf("\nvar num3 %d \nvar num4 %d ", num3, *num4)

	// Paso por valor

	num1 = 5
	fmt.Printf("\nValor de var num1 = %d  antes de llamar a la funcion", num1)
	num2 = pasoPorValor(num1)
	fmt.Printf("\nPaso por valor: var num1 =  %d \nvar num2 = %d ", num1, num2)
	// Paso por Referencia

	num1 = 5

	fmt.Printf("\nValor de var num1 = %d  antes de llamar a la funcion", num1)
	num2 = pasoPorReferencia(&num1)

	fmt.Printf("\nPaso por referencia: var num1 = %d \nvar num2 = %d ", num1, num2)

	num1 = 1
	num2 = 2

	fmt.Printf("\nValor de var num1 = %d \nValor de var num2 = %d  antes de llamar a la funcion", num1, num2)

	num1, num2 = intercambioPorvalor(num1, num2)

	fmt.Printf("\nIntercambio por valor: var num1 = %d \nvar num2 = %d \nvar num3 = %d \nvar num4 = %d ", num1, num2, num3, num4)

	num1 = 1
	num2 = 2

	fmt.Printf("\nValor de var num1 = %d \nValor de var num2 = %d  antes de llamar a la funcion", num1, num2)

	intercambioPorReferencia(&num1, &num2)

	fmt.Printf("\nIntercambio por referencia: var num1 = %d \nvar num2 = %d ", num1, num2, num3, num4)

}
