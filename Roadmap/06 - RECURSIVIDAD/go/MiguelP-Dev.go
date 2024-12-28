package main

import "fmt"

/*
Las funciones recursivas son aquellas que se llaman a si mismas dentro de su propio código.
Son útiles para resolver problemas que pueden dividirse en subproblemas más pequeños del mismo tipo.

Ventajas:
Las funciones recursivas puenden ser más fáciles de escribir y entender para problemas
que tienen una estructura repetitiva natural(como árboles y gráficos).

Desventajas:
Las funciones recursivas pueden consumir más memoria debido a las llamadas repetitivas
y el almacenamiento en la pila.

Pueden ser menos eficientes que las soluciones iterativas debido a la sobrecarga de llamas.
*/
func coutdown(n int) {
	fmt.Println(n)
	if n >= 1 {
		coutdown(n - 1)
	}
	return
}

/*
1 Calcular el factorial de un número concreto (la función recibe ese número).
Consiste en en multipllicar ese número por el factorial del número inmediatamente anterior,
reduciendolo hasta llegar a 1 y devolver el resultado.
*/
func factorialCalc(n uint) uint {
	if n == 0 {
		return 1
	} else if n == 1 {
		return 1
	}
	return n * factorialCalc(n-1)
}

/*
2 Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
Cada número en la serie de Fibonacci es a suma de los dos números anteriores, usar la recursividad aquí involucra
calcular los números previos recursivamente hasta llegar a los casos base(0, 1, 2).
*/
func fibbo(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	}
	return fibbo(n-1) + fibbo(n-2)
}

/*
3 Hanoi Towers:
Mover discos entre varillas siguiendo las reglas espesíficas se puede resolver el problema
dividiendo el problema en mover discos más pequeños recursivamente.
*/

func hanoi(n int, origin, destiny, auxiliary string) {
	if n == 1 {
		fmt.Printf("Mover disco 1 de %s a %s\n", origin, destiny)
		return
	}
	hanoi(n-1, origin, auxiliary, destiny)
	fmt.Printf("Mover disco %v de %s a %s\n", n, origin, destiny)
	hanoi(n-1, auxiliary, destiny, origin)
}

func main() {
	// Cuenta atrás
	coutdown(100)

	// Factorial
	fmt.Println("El factorial de 25 es: ", factorialCalc(25))

	// Fibbonacci
	fmt.Println("El número en la posición 25 de la sucesión es: ", fibbo(25))

	// Torre de hanoi
	hanoi(7, "A", "B", "C")
}
