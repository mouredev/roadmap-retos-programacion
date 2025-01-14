package main

import "fmt"

func main() {
	// Defer
	defer fmt.Println("\nfinal")

	x := 10
	y := 5

	// Operadores Aritméticos
	fmt.Println("Operadores Aritméticos")
	fmt.Println("Suma", x+y)
	fmt.Println("Resta", x-y)
	fmt.Println("Multiplicación", x*y)
	fmt.Println("División", x/y)
	fmt.Println("Módulo", x%y)
	x--
	fmt.Println("Decremento", x)
	x++
	fmt.Println("Incremento", x)

	// Operadores de Comparacion
	fmt.Println("\nOperadores de Comparación")
	fmt.Println("Igualdad", x == y)
	fmt.Println("Distinto a", x != y)
	fmt.Println("Mayor que", x > y)
	fmt.Println("Menor que", x < y)
	fmt.Println("Mayor o igual que", x >= y)
	fmt.Println("Menor o igual que", x <= y)

	// Operadores Logicos
	fmt.Println("\nOperadores Logicos")
	fmt.Println("AND", x == 10 && y == 5)
	fmt.Println("OR", x == 10 || y == 5)
	fmt.Println("NOT", !(x == 10))

	// Operadores de Bits
	fmt.Println("\nOperadores de Bits")
	fmt.Println("AND", x&y)
	fmt.Println("OR", x|y)
	fmt.Println("XOR", x^y)
	fmt.Println("NOT", ^x)
	fmt.Println("Desplazamiento a la izquierda", x<<1)
	fmt.Println("Desplazamiento a la derecha", x>>1)

	// Operadores de asignacion
	fmt.Println("\nOperadores de asignacion")
	z := 10
	fmt.Println("Valor inicial", z)
	z = 5
	fmt.Println("Asignacion", z)
	z += 5
	fmt.Println("Incremento y asignacion", z)
	z -= 5
	fmt.Println("Decremento y asignacion", z)
	z *= 5
	fmt.Println("Multiplicación y asignacion", z)
	z /= 5
	fmt.Println("División y asignacion", z)
	z %= 5
	fmt.Println("Módulo y asignacion", z)
	z &= 5
	fmt.Println("AND y asignacion", z)
	z |= 5
	fmt.Println("OR y asignacion", z)
	z ^= 5
	fmt.Println("XOR y asignacion", z)
	z <<= 1
	fmt.Println("Desplazamiento a la izquierda y asignacion", z)
	z >>= 1
	fmt.Println("Desplazamiento a la derecha y asignacion", z)

	// Operadores de punteros
	fmt.Println("\nOperadores de punteros")
	j := 1
	k := &j
	fmt.Println("Direccion en memoria", &k)
	fmt.Println("Puntero", *k)

	//Condicionales
	fmt.Println("\nCondicionales")
	if x == 10 {
		fmt.Println("x es igual a 10")
	} else {
		fmt.Println("x no es igual a 10")
	}

	//Iterativas
	fmt.Println("\nIterativas")
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	fmt.Println("\nFor Range")
	for indice, letra := range "hola mundo" {
		fmt.Println(indice, string(letra))
	}

	// Switch
	fmt.Println("\nSwitch")
	x = 1
	switch x {
	case 1:
		fmt.Println("x es igual a 1")
	case 2, 3:
		fmt.Println("x es igual a 2 o 3")
	default:
		fmt.Println("x no es ninguno de los valores anteriores")
	}

	printNumber()
}

func printNumber() {
	fmt.Println("\nImprime los numeros comprendidos entre 10 y 55 (pares, no 16 ni multiplos de 3)")
	for i := 10; i <= 55; i++ {
		if i%2 == 0 && i != 16 && i%3 != 0 {
			fmt.Println(i)
		}
	}
}
