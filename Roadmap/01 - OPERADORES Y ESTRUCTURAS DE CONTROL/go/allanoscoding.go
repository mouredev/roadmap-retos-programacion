/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

package main

import "fmt"

func defer_example() {
	defer fmt.Println("Mundo!")
	fmt.Println("Hola")
	return
}
func is_multiple_of(num int, multiple int) bool {
	return num % multiple == 0
}

func main() {
	// Operadores aritmeticos
	my_sum := 3 + 4
	my_diff := 5 - 3
	my_mult := 2 * 2
	my_division := 6 / 3
	my_modulo := 10 % 2

	fmt.Printf("Suma: 3 + 4 = %d \n", my_sum)
	fmt.Printf("Resta: 5 - 3 = %d \n", my_diff)
	fmt.Printf("Multiplicacion: 2 * 2 = %d \n", my_mult)
	fmt.Printf("Division: 6 / 3 = %d \n", my_division)
	fmt.Printf("Resto: 10 %% 2 = %d \n", my_modulo)

	// Operadores relacionales
	my_op_1 := 5 == 3
	my_op_2 := 5 != 3
	my_op_3 := 5 < 3
	my_op_4 := 5 <= 3
	my_op_5 := 5 > 3
	my_op_6 := 5 >= 3

	fmt.Printf("Operador ==: 5 == 3 -> %t \n", my_op_1)
	fmt.Printf("Operador !=: 5 != 3 -> %t \n", my_op_2)
	fmt.Printf("Operador <: 5 < 3 -> %t \n", my_op_3)
	fmt.Printf("Operador <=: 5 <= 3 -> %t \n", my_op_4)
	fmt.Printf("Operador >: 5 > 3 -> %t \n", my_op_5)
	fmt.Printf("Operador >=: 5 >= 3 -> %t \n", my_op_6)

	// Operadores logicos
	my_op_7 := my_op_5 && my_op_1
	my_op_8 := my_op_6 || my_op_3
	my_op_9 := !my_op_2

	fmt.Printf("Resultado: (5 > 3) && (5 == 3) = %t \n", my_op_7)
	fmt.Printf("Resultado: (5 >= 3) && (5 < 3) = %t \n", my_op_8)
	fmt.Printf("Resultado: !(5 != 3) = %t \n", my_op_9)

	// Operadores bit a bit
	a := 55
	b := 11

	fmt.Printf("Bitwise AND: a & b = %d \n", a & b)
	fmt.Printf("Bitwise OR: a | b = %d \n", a | b)
	fmt.Printf("Bitwise XOR: a ^ b = %d \n", a ^ b)
	fmt.Printf("Desplazamiento a la izq: a << 1 = %d \n", a << 1)
	fmt.Printf("Desplazamiento a la dcha: a >> 1 = %d \n", a >> 1)
	fmt.Printf("Bitwise AND NOT(clear): a &^ b = %d \n", a &^ b)

	// Operadores miscelaneos
	c := 22
	d := &c

	fmt.Printf("La direccion en memoria de c es %v \n", &c)
	fmt.Printf("El valor de c es %v \n", *d)

	// Estructuras de control
	if e := a + b; e > c {
		fmt.Println("e > a + b")
	} else {
		fmt.Println("e < a + b")
	}

	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	switch name := "Angel"; name {
	case "Angel":
		fmt.Println("Es Angel")
	default:
		fmt.Println("Es otra persona")
	}

	defer_example()

	// PROBLEMA EXTRA
	fmt.Println("Problema EXTRA")
	fmt.Println("-------------------------------")
	for i := 10; i <= 55; i++ {
		if is_multiple_of(i, 2) && !is_multiple_of(i, 3) && i != 16 {
			fmt.Println(i)
		}
	}
}