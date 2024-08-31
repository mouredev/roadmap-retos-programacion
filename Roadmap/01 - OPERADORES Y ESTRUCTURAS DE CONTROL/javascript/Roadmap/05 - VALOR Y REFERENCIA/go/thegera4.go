package main

import "fmt"

func main() {
	// Asignación por valor: es cuando se asigna un valor directamente a una variable

	a := 5 // a es una variable que almacena el valor 5
	b := a // b es una variable que almacena el valor de a, pero no es una referencia a la dirección de memoria de a
	fmt.Println(a) // 5
	fmt.Println("b antes de cambiar su valor", b) // 5
	b = 10 // b es una variable que almacena el valor 10, pero no es una referencia a la dirección de memoria de a
	fmt.Println("b después de cambiar su valor", b) // 10

	// Asignación por referencia: es cuando se asigna una dirección de memoria a una variable, 
	// la cual apunta a otra variable ya existente y que puede ser modificada

	c := &a // c es un puntero a la dirección de memoria de a
	fmt.Println(c) // 0xc0000b6010 (dirección de memoria de a)
	d := c // d es un puntero a la dirección de memoria de a (por medio de c)
	fmt.Println(d) // 0xc0000b6010 (dirección de memoria de a porque c es un puntero a la dirección de memoria de a)
	*d = 10 // d es un puntero a la dirección de memoria de a, por lo que al modificar *d, se modifica el valor de a y lo relacionado
	fmt.Println(a) // 10
	fmt.Println(*c) // 10
	fmt.Println(*d) // 10

	x, y := 5, 10

	// Ejemplo de funcion con parámetros por valor 

	fmt.Println("x antes de sumByValue", x) // 5
	fmt.Println("y antes de sumByValue", y) // 10
	resultByValue := sumByValue(x, y)
	fmt.Println("Resultado de sumByValue", resultByValue) // 30
	fmt.Println("x después de sumByValue", x) // 5
	fmt.Println("y después de sumByValue", y) // 10

	// Ejemplo de funcion con parámetros por referencia

	fmt.Println("x antes de sumByRef", x) // 5
	fmt.Println("y antes de sumByRef", y) // 10
	resultByRef := sumByRef(&x, y)
	fmt.Println("Resultado de sumByRef", resultByRef) // 30
	fmt.Println("x después de sumByRef", x) // 20
	fmt.Println("y después de sumByRef", y) // 10

	// Dificultad extra

	p1V1, p1V2 := 5, 10

	fmt.Println("p1V1 antes de intercambiar swapByValue", p1V1) // 5
	fmt.Println("p1V2 antes de intercambiar swapByValue", p1V2) // 10
	p1V1, p1V2 = swapByValue(p1V1, p1V2)
	fmt.Println("p1V1 después de intercambiar swapByValue", p1V1) // 10
	fmt.Println("p1V2 después de intercambiar swapByValue", p1V2) // 5
	fmt.Println("p1V1 antes de intercambiar swapByRef", p1V1) // 10
	fmt.Println("p1V2 antes de intercambiar swapByRef", p1V2) // 5
	p1V1, p1V2 = swapByRef(&p1V1, p1V2)
	fmt.Println("p1V1 después de intercambiar swapByRef", p1V1) // 5
	fmt.Println("p1V2 después de intercambiar swapByRef", p1V2) // 10

}

func sumByValue(a, b int) int {
	a = 20 //modificamos el valor de x, pero no afecta a la variable original si no que se crea una copia de x
	return a + b
}

func sumByRef(a *int, b int) int {
	*a = 20 //modificamos el valor de x, y afecta a la variable original al ser un puntero a la dirección de memoria de x
	return *a + b
}

func swapByValue(a, b int) (int, int) {
	return b, a
}

func swapByRef(a *int, b int) (int, int) {
	return b, *a
}