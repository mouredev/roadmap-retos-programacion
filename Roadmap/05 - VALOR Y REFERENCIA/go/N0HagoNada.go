package main

import "fmt"

type Persona struct {
	Nombre string
}

func main() {
	// Tipos Básicos (Por Valor)
	x := 5
	y := x
	fmt.Println(y)
	// Por referencia
	a := []int{1, 2, 3}
	b := a // b y a apuntan al mismo slice
	fmt.Println(a, b)
	// Estructuras (Por Valor)
	p1 := Persona{Nombre: "Alice"}
	p2 := p1 // Copia los valores de p1 en p2
	fmt.Println(p2)
	// punteros (por Referencia)
	py := &x // y apunta a la dirección de memoria de x
	fmt.Println(py)

	// Probar la función por Valor
	var pValor1 float32 = 3.1821
	var pValor2 float32 = -1121.1
	pValor3, pValor4 := porValor(pValor1, pValor2)
	fmt.Printf("Variables originales: %f y %f \n", pValor1, pValor2)
	fmt.Printf("Variables nuevas %f, y %f \n", pValor3, pValor4)
	// Probar pasar por referencia
	porRef1 := float32(5.5)
	porRef2 := float32(10.1)

	// Intercambiar valores por referencia
	porReferencia(&porRef1, &porRef2)

	// Imprimir valores modificados
	// Nota: En este caso, x e y ya han sido modificados directamente.
	fmt.Printf("Modificados: x = %f, y = %f\n", porRef1, porRef2)
}

func porValor(param1, param2 float32) (result1, result2 float32) {
	var tmpValue float32
	tmpValue = param1
	param1 = param2
	param2 = tmpValue
	return param1, param2
}
func porReferencia(a, b *float32) {
	*a, *b = *b, *a
}
