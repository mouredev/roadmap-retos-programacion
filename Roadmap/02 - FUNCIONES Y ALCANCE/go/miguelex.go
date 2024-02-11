package main

import "fmt"

func holaMundo() {
	fmt.Println("Hola mundo")
}

func saludo(name string) {
	fmt.Println("Hola", name)
}

func saludo2(name string) string {
	return "Hola " + name
}

func operaciones(a, b int) (int, int) {
	suma := func() int {
		return a + b
	}
	resta := func() int {
		return a - b
	}
	return suma(), resta()
}

func division(a, b int) (int, error) {
	if b == 0 {
		return 0, fmt.Errorf("No se puede dividir por 0")
	}
	return a / b, nil
}

func extra(param1, param2 string) int {

	var numImpreso = 0

	for i := 1; i < 101; i++ {
		if i%15 == 0 {
			fmt.Println(param1 + param2)
		} else if i%3 == 0 {
			fmt.Println(param1)
		} else if i%5 == 0 {
			fmt.Println(param2)
		} else {
			fmt.Println(i)
			numImpreso++
		}
	}

	return numImpreso
}

func main() {
	holaMundo()
	saludo("Miguel")
	fmt.Println(saludo2("Miguel"))
	fmt.Println(operaciones(10, 5))
	fmt.Println(division(10, 0))
	fmt.Println("Cantidad de numeros impresos: ", extra("Fizz", "Buzz"))
}
