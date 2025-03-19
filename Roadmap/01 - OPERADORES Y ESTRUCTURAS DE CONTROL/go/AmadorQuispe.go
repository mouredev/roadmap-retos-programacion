package main

import (
	"fmt"
	"math/rand"
)

//#01 OPERADORES Y ESTRUCTURAS DE CONTROL

func main() {
	fmt.Println("OPERADORES ARITMÉTICOS")
	fmt.Println("--------------------")
	// Operadores aritméticos.

	var number1 = 10
	var number2 = 3
	fmt.Printf("SUMA DE %d Y %d ES %d \n", number1, number2, number1+number2)
	fmt.Printf("RESTA DE %d Y %d ES %d \n", number1, number2, number1-number2)
	fmt.Printf("DIVISIÓN DE %d Y %d ES %v \n", number1, number2, number1/number2)
	fmt.Printf("MULTIPLICACIÓN DE %d Y %d ES %d \n", number1, number2, number1*number2)
	fmt.Printf("MODULO DE %d Y %d ES %d \n", number1, number2, number1%number2)

	fmt.Println("OPERADORES DE COMPARACIÓN")
	fmt.Println("--------------------")
	//Operadores de comparación
	fmt.Printf("(==) El número %d es igual a %d ? : %v \n", number1, number2, number1 == number2)
	fmt.Printf("(!=) El número %d es diferente de %d ? : %v \n", number1, number2, number1 != number2)
	fmt.Printf("(<) El número %d es menor que %d ? : %v \n", number1, number2, number1 < number2)
	fmt.Printf("(>) El número %d es mayor que %d ? : %v \n", number1, number2, number1 > number2)
	fmt.Printf("(<=) El número %d es menor o igual que %d ? : %v \n", number1, number2, number1 <= number2)
	fmt.Printf("(>=) El número %d es mayor o igual que %d ? : %v \n", number1, number2, number1 >= number2)

	fmt.Println("OPERADORES LÓGICOS")
	fmt.Println("--------------------")
	//Operadores de comparación
	fmt.Printf("(&&) El número %d y %d es mayor a CERO ? : %v \n", number1, number2, number1 > 0 && number2 > 0)
	fmt.Printf("(||) El número %d ó %d es mayor a CERO ? : %v \n", number1, number2, number1 > 0 || number2 > 0)
	fmt.Printf("(!) El número %d es mayor a CERO (negación) ? : %v \n", number1, !(number1 > 0))

	fmt.Println("OPERADORES UNARIOS")
	fmt.Println("--------------------")
	//Operadores unarios
	fmt.Printf("(+) El número %d en positivo\n", +number1)
	fmt.Printf("(-) El número %d en negativo\n", -number1)
	number1++
	fmt.Printf("(++) El número %v\n", number1)
	number1--
	fmt.Printf("(--) El número %v\n", number1)

	fmt.Println("OPERADORES DE ASIGNACIÓN")
	fmt.Println("--------------------")
	//operadores de asignación
	//Declarar una variable
	var num1 uint
	num1 = 120
	fmt.Println("El valor asignado de la variable 'num1' es ", num1)
	num1 += 10
	fmt.Println("El valor de la variable 'num1' incrementado en 10 es ", num1)
	num1 -= 4
	fmt.Println("El valor de la variable 'num1' decrementado en 4 es ", num1)
	num1 *= 2
	fmt.Println("El valor de la variable 'num1' multiplicado por 2 es ", num1)
	num1 /= 2
	fmt.Println("El valor de la variable 'num1' dividido en 2 es ", num1)
	num1 %= 2
	fmt.Println("El resto de dividir en 2 de la variable 'num1' es ", num1)

	fmt.Println("OPERADORES LÓGICOS A NIVEL DE BITS")
	fmt.Println("--------------------")
	//operadores lógicos a nivel de Bits

	// Declarar dos variables de tipo entero
	var a int = 10
	var b int = 7

	var resultado int = a & b
	fmt.Println("El resultado de la operación AND a nivel de bits es:", resultado)

	resultado = a | b
	fmt.Println("El resultado de la operación OR a nivel de bits es:", resultado)

	resultado = a ^ b
	fmt.Println("El resultado de la operación XOR a nivel de bits es:", resultado)

	resultado = a << 2
	fmt.Println("El resultado del desplazamiento a la izquierda es:", resultado)

	resultado = a >> 2
	fmt.Println("El resultado del desplazamiento a la derecha es:", resultado)

	resultado = ^a
	fmt.Println("El resultado de la operación NOT a nivel de bits es:", resultado)

	fmt.Println("FLUJOS DE CONTROL")
	fmt.Println("-------------------")

	fmt.Println("IF ")
	fmt.Println("-------------------")
	var valor = rand.Int()
	if valor%2 == 0 {
		fmt.Println("El número ", valor, " es par")
	}

	fmt.Println("IF ELSE")
	fmt.Println("-------------------")
	if valor%2 == 0 {
		fmt.Println("El número ", valor, " es par")
	} else {
		fmt.Println("El número ", valor, " no es par")
	}

	fmt.Println("ELSE IF")
	fmt.Println("-------------------")
	qualification := 75
	if qualification >= 90 {
		fmt.Println("Excelente")
	} else if qualification >= 80 {
		fmt.Println("Muy bien")
	} else if qualification >= 70 {
		fmt.Println("Bien")
	} else {
		fmt.Println("Regular")
	}

	fmt.Println("SWITCH SIN CONDICIÓN")
	fmt.Println("-------------------")
	switch {
	case qualification >= 90:
		fmt.Println("Excelente")
	case qualification >= 80:
		fmt.Println("Muy bien")
	case qualification >= 70:
		fmt.Println("Bien")
	default:
		fmt.Println("Regular")
	}

	fmt.Println("SWITCH CASE")
	fmt.Println("-------------------")
	weekday := 2
	switch weekday {
	case 1:
		fmt.Println("Lunes")
	case 2:
		fmt.Println("Martes")
	case 3:
		fmt.Println("Miércoles")
	case 4:
		fmt.Println("Jueves")
	case 5:
		fmt.Println("Viernes")
	case 6:
		fmt.Println("Sábado")
	case 7:
		fmt.Println("Domingo")
	default:
		fmt.Println("Día no valido")
	}

	fmt.Println("FOR COMÚN")
	fmt.Println("-------------------")
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	fmt.Println("FOR ESTILO WHILE")
	fmt.Println("-------------------")
	var i = 0
	for i < 10 {
		fmt.Println(i)
		i++
	}

	fmt.Println("FOR RANGE")
	fmt.Println("-------------------")
	for i, letter := range "amsoft.dev" {
		fmt.Println(i, string(letter))
	}

	fmt.Println("FOR FOREVER (for infinito)")
	fmt.Println("-------------------")
	for {
		fmt.Print("Salir? (s/n): ")
		var c rune
		fmt.Scanf("%c\n", &c)
		if c == 'S' || c == 's' {
			break
		}
	}

	fmt.Println("EXTRA")
	/* 	* Crea un programa que imprima por consola todos los números comprendidos
	* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */
	for i := 10; i <= 55; i++ {
		if !(i == 16 || i%3 == 0) {
			fmt.Println(i)
		}
	}

}
