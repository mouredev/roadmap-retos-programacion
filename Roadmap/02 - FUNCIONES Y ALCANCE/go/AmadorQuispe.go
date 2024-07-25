package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

var user = "Amador" //Esto es una variable global

/*EXTRA*/
func fizzBuzz(s1, s2 string) int {
	var count int
	for i := 1; i <= 100; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println(i, s1, s2)
		} else if i%3 == 0 {
			fmt.Println(i, s1)
		} else if i%5 == 0 {
			fmt.Println(i, s2)
		} else {
			fmt.Println(i)
			count++
		}
	}
	return count
}

func main() {
	fmt.Println("(variable global) Hola !👋", user)
	fmt.Println("Se ha impreso número: ", fizzBuzz("fizz", "buzz"), "veces")
	welcomeSystem()
	printMessage("El sistema puede hacer estos trabajos")
	printMessage("[A] Operación simple (+,-,* y / de dos números) ")
	printMessage("[B] Operación multiple (+, - y * de varios números) ")
	printMessage("[C] Factorial de un número")
	fmt.Print("Ingresa la opción :")
	var option string
	fmt.Scanf("%s", &option)
	printMessage("La opción que seleccionaste es " + option)

	if option == "A" {
		printMessage("Dentro de las operaciones simples tenemos :")
		printMessage("(1) Suma")
		printMessage("(2) Resta")
		printMessage("(3) Multiplicación")
		printMessage("(4) División")
		printMessage("(5) Potencia")
		fmt.Print("Ingrese el número de la operación :")
		var opSelect string
		var num1, num2 float64
		fmt.Scan(&opSelect)
		printMessage("Haz seleccionado " + operationSelected(opSelect) + ", ahora ingresa los números.")
		fmt.Print("Ingrese el número 1 :")
		fmt.Scan(&num1)
		fmt.Print("Ingrese el número 2 :")
		fmt.Scan(&num2)
		result := operation(opSelect, num1, num2)
		printMessage("El resultado de la operación " + operationSelected(opSelect) + " :")
		fmt.Printf("%v y %v es %v \n", num1, num2, result)
	} else if option == "B" {
		printMessage("Dentro de las operaciones multiples tenemos :")
		printMessage("(1) Suma")
		printMessage("(2) Resta")
		printMessage("(3) Multiplicación")
		fmt.Print("Ingrese el número de la operación :")
		var opSelect string
		var input string
		fmt.Scan(&opSelect)
		printMessage("Haz seleccionado " + operationSelected(opSelect) + ", ahora ingresa los números.")
		fmt.Print("Ingresa los números separado por una coma (,) ejemplo 1,2,3 : ")
		fmt.Scan(&input)
		numbers := stringToSlice(input)
		result := operationsMultipleNumbers(opSelect, numbers...)
		printMessage("El resultado de la operación " + operationSelected(opSelect) + " :")
		fmt.Println(""+input+" es: ", result)
	} else if option == "C" {
		printMessage("Factorial de un número :")
		fmt.Print("Ingresa un número positivo :")
		var number int = 5
		fmt.Scan(&number)
		result := factorial(number)
		fmt.Println("El factorial de ", number, " es ", result)
	} else {
		printMessage("La opción que seleccionaste no existe")
	}

	var msg = exitSystem()
	fmt.Println(msg)

	//En go se puede asignar una función a una variable
	var fn = greeting
	fn("Amador")

	//Función anónima
	fn1 := func() {
		fmt.Println("Hello")
	}
	fn1()

}

/*Función sin parámetro ni retorno.*/
func welcomeSystem() {
	fmt.Println("------------------------------")
	fmt.Println("----Bienvenido al sistema-----")
	fmt.Println("------------------------------")
}

/*Función que recibe un parámetro pero no retorna ningún valor.*/
func printMessage(message string) {
	fmt.Println(message)
}

/*Función sin parámetro y con retorno.*/
func exitSystem() string {
	return "Gracias por usar el sistema regresa pronto."
}

/* Función que recibe un parámetro y retorna un valor.*/
func operationSelected(input string) string {
	var operation string
	switch input {
	case "1":
		operation = "(1) Suma"
	case "2":
		operation = "(2) Resta"
	case "3":
		operation = "(3) Multiplicación"
	case "4":
		operation = "(4) División"
	case "5":
		operation = "(5) Potencia"

	default:
		operation = "No soportado"
	}
	return operation
}

/*Función que recibe varios parámetros y retorna un valor.*/
func operation(operator string, number1, number2 float64) float64 {
	switch operator {
	case "1":
		return number1 + number2
	case "2":
		return number1 - number2
	case "3":
		return number1 * number2
	case "4":
		return number1 / number2
	case "5":
		// Aquí usamos una función propio del lenguaje
		return math.Pow(number1, number2)

	default:
		return 0
	}
}

/*Función que recibe varios parámetros (incluido rest parameter) y retorna un valor.*/
func operationsMultipleNumbers(operator string, numbers ...float64) float64 {
	var accumulator float64
	switch operator {
	case "1":
		for _, v := range numbers {
			accumulator += v
		}
	case "2":
		for _, v := range numbers {
			accumulator -= v
		}
	case "3":
		for _, v := range numbers {
			accumulator *= v
		}
	default:
		accumulator = 0

	}
	return accumulator
}

func factorial(num int) int {
	if num <= 1 {
		return 1
	}
	return num * factorial(num-1)
}

func stringToSlice(s string) []float64 {
	var numbers []float64
	stringSplit := strings.Split(s, ",")

	for _, v := range stringSplit {
		if fv, err := strconv.ParseFloat(v, 64); err == nil {
			numbers = append(numbers, fv)
		}
	}
	return numbers
}

func greeting(name string) {
	fmt.Println(name)
}
