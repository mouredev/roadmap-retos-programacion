package main

import "fmt"

// Función de orden superior que toma otra función como argumento
func aplicarOperacion(a, b int, operacion func(int, int) int) int {
	return operacion(a, b)
}

// Función que suma dos números
func sumar(a, b int) int {
	return a + b
}

// Función que multiplica dos números
func multiplicar(a, b int) int {
	return a * b
}

// Función de orden superior que retorna una función
func crearMultiplicador(factor int) func(int) int {
	return func(num int) int {
		return num * factor
	}
}
func main() {
	// Llamar a la función de orden superior pasando diferentes funciones como argumentos
	resultado := aplicarOperacion(5, 3, sumar)
	fmt.Println("Suma: 5 + 3 =", resultado)

	resultado = aplicarOperacion(5, 3, multiplicar)
	fmt.Println("Multiplicación: 5 * 3 =", resultado)

	duplicar := crearMultiplicador(2)
	triplicar := crearMultiplicador(3)

	// Usar las funciones multiplicadoras
	fmt.Println("Duplicar 5:", duplicar(5))
	fmt.Println("Triplicar 5:", triplicar(5))
}
