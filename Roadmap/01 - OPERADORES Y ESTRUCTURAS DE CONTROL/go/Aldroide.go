package main

import "fmt"

func main(){
	// Operadores aritmeticos
	fmt.Printf("La suma de 2 + 3 es: %d \n", 2+3)
	fmt.Printf("La suma de 2 - 3 es: %d \n", 2-3)
	fmt.Printf("La suma de 2 * 3 es: %d \n", 2*3)
	fmt.Printf("La suma de 6 / 3 es: %d \n", 2/3)
	fmt.Printf("La suma de 6 %% 3 es: %d \n", 2%3)
	
	// Operaciones relacionales
	fmt.Printf("5 == 4\n", 5==4)
	fmt.Printf("5 != 4\n", 5!=4)
	fmt.Printf("5 < 4\n", 5<4)
	fmt.Printf("5 <= 4\n", 5<=4)
	fmt.Printf("5 > 4\n", 5>4)
	fmt.Printf("5 >= 4\n", 5>=4)

	// Operadores logicos
	fmt.Printf("(5 > 4) && (5 == 3) es: %t \n", (5 > 3) && (5 == 3))
	fmt.Printf("(5 >= 4) || (5 < 3) es: %t \n", (5 >= 3) || (5 < 3))
	fmt.Printf("!(5 != 4) es: %t \n", !(5 != 3))

	// Operadores bit a bit
	var x int = 8
	var y int = 4

	fmt.Printf("El resultado de 8 & 4 es: %d \n", x&y)
	fmt.Printf("El resultado de 8 | 4 es: %d \n", x|y)
	fmt.Printf("El resultado de 8 ^ 4 es: %d \n", x^y)
	fmt.Printf("El resultado de 8 << 2 es: %d \n", x<<2)
	fmt.Printf("El resultado de 8 >> 2 es: %d \n", x>>2)

	// Estructuras de Control

	// Ejemplo de if.. else

	if 5 > 3 {
		fmt.Println("5 es mayor que 3")
	} else {
		fmt.Println("5 no es mayor que 3")
	}

	// Ejemplo de switch

	switch 5 {
	case 1:
		fmt.Println("El numero es 1")
	case 2:
		fmt.Println("El numero es 2")
	case 3:
		fmt.Println("El numero es 3")
	case 4:
		fmt.Println("El numero es 4")
	case 5:
		fmt.Println("El numero es 5")
	default:
		fmt.Println("El numero es mayor que 5")
	}

	// Ejemplo de for

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	// Ejemplo de for con range

	my_array := []int{1, 2, 3, 4, 5}

	for index, value := range my_array {
		fmt.Printf("El valor en la posicion %d es %d \n", index, value)
	}

	// while

	j := 0
	for j < 5 {
		fmt.Println(j)
		j++
	}

	// do while

	k := 0
	for {
		fmt.Println(k)
		k++
		if k == 5 {
			break
		}
	}

	// Extra

	for i := 10; i <= 55; i++ {
		if i%2 == 0 && i != 16 && i%3 != 0 {
			fmt.Println(i)
		}
	}

}