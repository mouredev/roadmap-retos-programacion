package main

import (
	"errors"
	"fmt"
)

func prueba() (string, error) {
	return "", errors.New("Ha ocurrido un error")
}

func main() {
	// Operadore aritméticos
	fmt.Println("Sean a = 10, b = 3 y c = 20.0")
	a := 10
	b := 3
	c := 20.0
	suma := a + b
	fmt.Println("Suma de a + b: ", suma)
	resta := a - b
	fmt.Println("Resta de a - b: ", resta)
	multiplicacion := a * b
	fmt.Println("Multiplicación de a * b: ", multiplicacion)
	divisionEntera := a / b
	fmt.Println("División entera de a / b: ", divisionEntera)
	division := c / 3
	fmt.Println("División de a / c: ", division)
	modulo := a % 2
	fmt.Println("Módulo de a % 2: ", modulo)

	// Operadores lógicos
	fmt.Println("Sean x = true and y = false")
	x := true
	y := false
	fmt.Println("AND lógico x && y: ", x && y)
	fmt.Println("OR lógico x || y: ", x || y)
	fmt.Printf("NOT lógico !x = %t y !y = %t\n", !x, !y)

	// Operadores relacionales
	fmt.Println("Sean num1 = 5 y num2 = 10")
	num1 := 5
	num2 := 10
	esIgual := num1 == num2
	fmt.Println("Es igual num1 == num2: ", esIgual)
	esDiferente := num1 != num2
	fmt.Println("Es diferente num1 != num2: ", esDiferente)
	esMayor := num1 > num2
	fmt.Println("Es mayor num1 > num2: ", esMayor)
	esMenorIgual := num1 <= num2
	fmt.Println("Es menor num1 <= num2: ", esMenorIgual)

	// Alterar el orden de evaluación con el uso de parentesis
	resultado1 := num1 + num2*num1 - num2
	fmt.Println("Resultado usando precedencia de operadores: ", resultado1)
	resultado2 := (num1 + num2) * (num1 - num2)
	fmt.Println("Resultado realizando primero la suma y la resta y luego la multiplicación: ", resultado2)

	// Estructuras de Control

	// Estructura if - else if - else
	if num1 < num2 && num1 != 0 {
		fmt.Println("num1 es menor que num2 y num1 es diferente de cero")
	}

	if num1 > num2 {
		fmt.Println("El número uno es mayor que el dos")
	} else if num1 == num2 {
		fmt.Println("Los números son iguales")
	} else {
		fmt.Println("El número dos es mayor que el uno")
	}

	if _, err := prueba(); err != nil {
		fmt.Println(err)
	}

	// Estructura Switch
	opcion := '1'
	switch opcion {
	case '1':
		fmt.Println("Valor seleccionado 1")
	case '2':
		fmt.Println("Valor seleccionado 2")
	default:
		fmt.Println("Valor seleccionado no válido")
	}

	// Bucle for

	// for clásico
	for i := 0; i < 10; i++ {
		fmt.Printf("%d\t", i)
	}
	fmt.Printf("\n")

	// for como bucle while
	j := 0
	for j < 10 {
		fmt.Printf("%d\t", j)
		j++
	}
	fmt.Printf("\n")

	// Bucle infinito
	for {
		// Tareas a ejecutar
		break
	}

	// for para iterar sobre secuencias
	numeros := []int{10, 20, 30}
	for indice, valor := range numeros {
		fmt.Printf("Índice: %d, Valor: %d\n", indice, valor)
	}
	// El índice puede ser descartado usando el identificador de blanco _
	for _, valor := range numeros {
		fmt.Println(valor)
	}
	// Uso de for en strings
	text := "Hola, mundo"
	for index, runeValue := range text {
		fmt.Printf("Índice: %d, Runa: %c\n", index, runeValue)
	}
	// Uso de for en mapas
	edades := map[string]int{"Juan": 30, "Ana": 25}
	for clave, valor := range edades {
		fmt.Printf("%s tiene %d años\n", clave, valor)
	}

	// RETO EXTRA
	fmt.Println("RETO EXTRA")
	for i := 10; i <= 55; i += 2 {
		if i != 16 && i%3 != 0 {
			fmt.Println(i)
		}
	}
}
