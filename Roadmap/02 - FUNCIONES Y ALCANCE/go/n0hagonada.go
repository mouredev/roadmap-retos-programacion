package main

import (
	"fmt"
)

// funciones declarada como tipo
type First func(int) int // declare type

func getFunction() First { // use it
	return func(val int) int {
		return val * 5
	}
}
func main() {
	// funcionanonima
	getMod := func(a, b int) int { // declare it
		return a % b
	}
	fmt.Println(getMod(12, 5))
	//invocaicon Inmediata
	func(name string) {
		fmt.Printf("Hello, %s", name)
	}("John") // prints "Hello, John"
	numeroDeVeces := reto("Fizz", "Buzz")
	fmt.Println("Se imprimieron números en lugar de texto:", numeroDeVeces, "veces")

}
func reciboargumentosTipado(saludo string, numero int) {
	fmt.Printf("%s is %d years old.\n", saludo, numero)
}
func multipleRetorno(x, y float64) (float64, float64) {
	return (x + y) * (x - y), (x + y) / (x - y)
}
func retornoNombrado(num int) (res int) {
	res = num / 10
	return res
}
func llamadoporReferencia(num *int) {
	*num = 142
}
func reto(num1, num2 string) int {
	contador := 0
	for i := 1; i <= 100; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println(num1 + num2)
		} else if i%3 == 0 {
			fmt.Println(num1)
		} else if i%5 == 0 {
			fmt.Println(num2)
		} else {
			fmt.Println(i)
			contador++
		}
	}
	return contador
}
