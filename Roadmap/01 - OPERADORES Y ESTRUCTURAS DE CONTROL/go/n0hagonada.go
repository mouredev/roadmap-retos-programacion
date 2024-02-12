package main

import "fmt"

func main() {
	// Operadores Aritméticos
	a := 5 + 3  // Suma
	b := 10 - 4 // Resta
	c := 7 * 3  // Multiplicación
	d := 20 / 4 // División
	e := 9 % 4  // Módulo
	fmt.Println(a, b, c, d, e)
	// Operadores Lógicos
	x := true
	y := false
	fmt.Println(x && y) // AND lógico
	fmt.Println(x || y) // OR lógico
	fmt.Println(!x)     // NOT lógico
	// Operadores de Comparación
	fmt.Println(a == b) // Igual a
	fmt.Println(a != b) // Diferente de
	fmt.Println(a > b)  // Mayor que
	fmt.Println(a < b)  // Menor que
	// Operadores de Asignación
	a += 2 // Equivalente a a = a + 2
	b -= 3 // Equivalente a b = b - 3
	// Operadores de bits
	f := 3 << 2  // Desplazamiento a la izquierda
	g := 16 >> 2 // Desplazamiento a la derecha
	h := 5 & 2   // AND de bits
	i := 5 | 2   // OR de bits
	j := 5 ^ 2   // XOR de bits
	k := ^5      // NOT de bits
	fmt.Println(f, g, h, i, j, k)
	// Condicionales
	if a > 5 {
		fmt.Println("a es mayor que 5")
	} else if a == 5 {
		fmt.Println("a es igual a 5")
	} else {
		fmt.Println("a es menor que 5")
	}
	// iterativas
	for i := 70; i < 75; i++ {
		fmt.Println(i)
	}
	fmt.Println("*************************** Extra ******************************************")
	extra()
}
func extra() {
	for i := 10; i <= 55; i++ {
		if i != 16 && i%2 == 0 && 1%3 != 0 {
			fmt.Println(i)
		}
	}
}
