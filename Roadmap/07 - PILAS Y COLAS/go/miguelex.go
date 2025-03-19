package main

import (
	"fmt"
)

func main() {

	var pila [10]int
	indice := 0

	pila[indice] = 3
	indice++

	fmt.Println("Contenido de la pila")
	for i := 0; i < indice; i++ {
		fmt.Println(pila[i])
	}

	fmt.Println("--------------------")

	pila[indice] = 4
	indice++
	pila[indice] = 1
	indice++

	fmt.Println("Contenido de la pila")
	for i := 0; i < indice; i++ {
		fmt.Println(pila[i])
	}

	fmt.Println("--------------------")

	// desapilamos

	indice--

	fmt.Println("Contenido de la pila")
	for i := 0; i < indice; i++ {
		fmt.Println(pila[i])
	}

	fmt.Println("--------------------")

	pila[indice] = 5
	indice++

	fmt.Println("Contenido de la pila")
	for i := 0; i < indice; i++ {
		fmt.Println(pila[i])
	}

	fmt.Println("--------------------")

	fmt.Println("Cola:")

	var cola [10]int
	indice = 0

	cola[indice] = 3
	indice++

	fmt.Println("Contenido de la cola")
	for i := 0; i < indice; i++ {
		fmt.Println(cola[i])
	}

	fmt.Println("--------------------")

	cola[indice] = 4
	indice++
	cola[indice] = 1
	indice++

	fmt.Println("Contenido de la cola")

	for i := 0; i < indice; i++ {
		fmt.Println(cola[i])
	}

	fmt.Println("--------------------")

	// desencolamos

	for i := 0; i < indice; i++ {
		cola[i] = cola[i+1]
	}
	indice--

	fmt.Println("Contenido de la cola")

	for i := 0; i < indice; i++ {
		fmt.Println(cola[i])
	}

	fmt.Println("--------------------")

}
