package main

import "fmt"

func main() {
	// 1. Bucle for básico
	for i := 1; i < 10; i++ {
		fmt.Println(i)
	}

	// 2. Bucle for con condición
	i := 1
	for i < 10 {
		fmt.Println(i)
		i++
	}

	// 3. Bucle infinito con break
	i = 1
	for {
		if i > 10 {
			break
		}
		fmt.Println(i)
		i++
	}

	// 4. Iteración sobre un Array
	numsArray := [10]int{1, 2, 3, 5, 6, 7, 8, 9, 10}
	for i, num := range numsArray {
		fmt.Printf("Índice: %v, Valor: %d\n", i, num)
	}

	// Iteración sobre un Slice
	numSlice := [10]int{1, 2, 3, 5, 6, 7, 8, 9, 10}
	for _, number := range numSlice {
		fmt.Println(number)
	}

	// 6. Iteración sobre un Map
	numsMap := map[string]int{"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10}
	for key := range numsMap {
		fmt.Println(key, numsMap[key])
	}

	//  Iteración sobre una cadena de texto
	text := "Hola Mundo"
	for i, char := range text {
		fmt.Printf("Índice: %v, Caracter: %c\n", i, char)
	}

	// 8. Iteración sobre un canal
	numsChan := make(chan int)
	go func() {
		for i := 1; i <= 10; i++ {
			numsChan <- i
		}
		close(numsChan)
	}()
	for num := range numsChan {
		fmt.Println(num)
	}

	// 9. Iteración sobre un canal con select
	numsChan1 := make(chan int)
	numsChan2 := make(chan int)
	go func() {
		for i := 1; i <= 10; i++ {
			numsChan1 <- i
			numsChan2 <- i
		}
		close(numsChan1)
		close(numsChan2)
	}()
	for {
		select {
		case num, ok := <-numsChan1:
			if !ok {
				numsChan1 = nil
			} else {
				fmt.Println("Canal 1:", num)
			}
		case num, ok := <-numsChan2:
			if !ok {
				numsChan2 = nil
			} else {
				fmt.Println("Canal 2:", num)
			}
		}
		if numsChan1 == nil && numsChan2 == nil {
			break
		}
	}

	// 9. Iteración con una función recursiva
	var recursivePrint func(int)
	recursivePrint = func(n int) {
		if n > 10 {
			return
		}
		fmt.Println(n)
		recursivePrint(n + 1)
	}
	recursivePrint(1)

	// 10. Iteración con un defer
	for i := 1; i <= 10; i++ {
		defer fmt.Println(i)
	}
	fmt.Println("Fin del programa")

	// 11. Iteración con un defer y una función anónima
	for i := 1; i <= 10; i++ {
		defer func() {
			fmt.Println(i)
		}()
	}
	fmt.Println("Fin del programa")

	// 12. Iteracion con goto (No Recomendado)
	i = 1
Loop:
	if i <= 10 {
		fmt.Println(i)
		i++
		goto Loop
	}

	/*
		El uso de goto para crear bucles no es recomendado en la mayoría de los lenguajes de programación, incluyendo Go, por varias razones:

		Legibilidad: El uso de goto puede hacer que el flujo del programa sea difícil de seguir y entender. Los bucles for y while son estructuras de control más claras y fáciles de leer.

		Mantenimiento: El código que utiliza goto puede ser más difícil de mantener y depurar. Los saltos incondicionales pueden llevar a errores difíciles de rastrear y corregir.

		Estructura: Los lenguajes modernos promueven el uso de estructuras de control más estructuradas y legibles, como los bucles for, while, y las funciones recursivas. Estas estructuras ayudan a mantener el código organizado y comprensible.

		Errores: El uso de goto puede llevar a errores como bucles infinitos o saltos a etiquetas incorrectas, lo que puede causar comportamientos inesperados en el programa.

		En resumen, aunque goto puede ser útil en casos muy específicos, generalmente es mejor evitar su uso y optar por estructuras de control más claras y seguras.
	*/
}
