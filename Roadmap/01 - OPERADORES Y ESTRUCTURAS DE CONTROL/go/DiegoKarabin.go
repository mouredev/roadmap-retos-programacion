package main

import "fmt"

func main() {
	println("Operadores Aritmeticos")
	println("suma (+): 3 + 2 =", 3 + 2)
	println("resta (-): 3 - 2 =", 3 - 2)
	println("producto (*): 3 * 2 =", 3 * 2)
	println("cociente entero (/): 3 / 2 =", 3 / 2)
	println("cociente flotante (/): 3 / 2. =", 3 / 2.)
	println("residuo (%): 3 % 2 =", 3 % 2)

	println("\nOperadores Logicos")
	println("and (&&): true && false =", true && false)
	println("or (||): true || false =", true || false)
	println("not (!): !true =", !true)

	println("\nOperadores de comparacion")
	println("es igual que (==): 2 == 2 =", 2 == 2)
	println("no es igual que / es distinto que (!=): 3 != 2 =", 3 != 2)
	println("es menor que (<): 2 < 3 =", 2 < 3)
	println("es menor o igual que (<=): 3 <= 3 =", 3 <= 3)
	println("es mayor que (>): 3 > 2 =", 3 > 2)
	println("es mayor o igual que (>=): 4 >= 4 =", 4 >= 4)

	println("\nOperadores de asignacion")
	foo := 42
	println("Para declaracion y asignacion con inferencia del tipo de dato (:=): foo := 42; foo; //", foo)
	foo = 43
	println("Asignacion (=): foo = 43; foo; //", foo)

	println("\nOperadores aritmeticos y de asignacion combinados")
	foo += 2
	println("aumentar (+=): foo += 2; foo; //", foo)
	foo -= 2
	println("disminuir (-=): foo -= 2; foo; //", foo)
	foo *= 2
	println("multiplicar (*=): foo *= 2; foo; //", foo)
	foo /= 2
	println("dividir (/=): foo /= 2; foo; //", foo)
	foo %= 2
	println("residuo (%=): foo %= 2; foo; //", foo)

	println("\nOperadores de incremento y decremento")
	foo++
	println("incremento (++): foo++; //", foo)
	foo--
	println("decremento (--): foo--; //", foo)

	println("\nOperadores a nivel de bits")
	const uint8_a uint8 = 0b0011
	const uint8_b uint8 = 0b0101
	fmt.Printf("and (&): %08b & %08b = %08b\n", uint8_a, uint8_b, uint8_a & uint8_b)
	fmt.Printf("or (|): %08b & %08b = %08b\n", uint8_a, uint8_b, uint8_a | uint8_b)
	fmt.Printf("xor (^): %08b ^ %08b = %08b\n", uint8_a, uint8_b, uint8_a ^ uint8_b)
	fmt.Printf("not (^): ^%08b = %08b\n", uint8_b, ^uint8_b)
	fmt.Printf("and not (&^): %08b &^ %08b = %08b\n", uint8_a, uint8_b, uint8_a &^ uint8_b)
	fmt.Printf("left shift (<<(uint)): %08b<<2 = %08b\n", uint8_a, uint8_a<<2)
	fmt.Printf("right shift (>>(uint)): %08b>>2 = %08b\n", uint8_a, uint8_a>>2)

	println("\nOperadores de direccion")
	var my_variable int = 123
	var pointer *int = &my_variable
	println("retorna un puntero (&): &my_variable = ", &my_variable)
	println("va al puntero y devuelve el valor al que refiere (*): *pointer = ", *pointer)


	println("\nEstructuras de control")
	println("if")

	var condition bool = true

	if condition {
		println("Se cumple la condicion y se entra al bloque if.")
	}

	other_condition := false
	println("\nif/else")

	if other_condition {
		println("Se cumple la condicion y se entra al bloque if.")
	} else {
		println("No se cumple la condicion y se entra al bloque else.")
	}

	my_value := 1
	println("\nswitch")

	switch my_value {
	case 1: println("Uno")
	case 2: println("Dos")
	case 3: println("Tres")
	default: println("Número desconocido")
	}

	println("\nfor")
	for i := 1; i <= 5; i++ {
		print(i, " ")
	}
	println()

	println("\nExtra")
	for i := 10; i <= 55; i += 2 {
		if (!(i == 16 || i % 3 == 0)) {
			println(i)
		}
	}
}
