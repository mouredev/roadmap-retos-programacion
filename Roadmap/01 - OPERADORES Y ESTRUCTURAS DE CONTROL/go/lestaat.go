package main

import "fmt"

func main() {

	fmt.Println("Aritmeticos")
	fmt.Printf("suma de 1 + 2 es: %d \n", 1+2)
	fmt.Printf("resta de 2 - 1 es: %d \n", 2-1)
	fmt.Printf("multiplicacion de 2 * 2 es: %d \n", 2*2)
	fmt.Printf("division de 2 / 1 es: %d \n", 2/2)
	fmt.Printf("modulo de 7 %% 3 es: %d \n", 7%3)

	fmt.Println("Logicos")
	fmt.Println(" AND (2 >= 1) && (2 <= 3)", (2 >= 1) && (2 <= 3))
	fmt.Println(" OR (2 <= 1) && (2 <= 3)", (2 <= 1) || (2 <= 3))
	fmt.Println(" NOT (2 <=1)", !(2 <= 1))

	fmt.Println("Bit a bit")
	var x int = 8
	var y int = 4
	fmt.Printf("and de 8 & 4 es: %d \n", x&y)
	fmt.Printf("or de 8 | 4 es: %d \n", x|y)
	fmt.Printf("xor de 8 ^ 4 es: %d \n", x^y)
	fmt.Printf("izquierda de 8 << 2 es: %d \n", x<<2)
	fmt.Printf("derecha de 8 >> 2 es: %d \n", x>>2)

	fmt.Println("Comparacion")
	fmt.Printf("igual que 2 == 2 \n", 2 == 2)
	fmt.Printf("mayor que 2 > 1 \n", 2 > 1)
	fmt.Printf("menor que 2 < 4 \n", 2 < 4)
	fmt.Printf("desiguales 2 != 4 \n", 2 != 4)

	fmt.Println("Asignacion")
	var myVar int = 10
	fmt.Printf("inicializacion de %d \n", myVar)
	myVar += 10
	fmt.Printf("asignacion de %d \n", myVar)
	myVar -= 5
	fmt.Printf("resta y asignacion de %d \n", myVar)
	myVar *= 2
	fmt.Printf("multiplicacion y asignacion de %d \n", myVar)
	myVar /= 2
	fmt.Printf("division y asignacion de %d \n", myVar)
	myVar %= 4
	fmt.Printf("modulo y asignacion de %d \n", myVar)

	fmt.Println("Condicionales")
	var myNewVar int = 5
	if myNewVar > 5 {
		fmt.Println("myVar es mayor que 5")
	} else if myNewVar < 5 {
		fmt.Println("myVar es menor que 5")
	} else {
		fmt.Println("myVar es igual a 5")
	}

	switch myNewVar {
	case 1:
		fmt.Println("myVar es 1")
	case 2:
		fmt.Println("myVar es 2")
	case 3:
		fmt.Println("myVar es 3")
	default:
		fmt.Println("myVar es 5")
	}

	fmt.Println("Loops")
	i := 0
	for i < 5 {
		fmt.Println(i)
		i++
	}

	fmt.Println("Extra")
	for n := 10; n <= 55; n++ {
		if n != 16 && n%3 != 0 {
			fmt.Println(n)
		}
	}
}
