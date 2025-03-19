package main

import "fmt"

// /*
//  * EJERCICIO:
//  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
//  * operaciones (debes utilizar una estructura que las soporte):
//  * - Añade un elemento al final.
//  * - Añade un elemento al principio.
//  * - Añade varios elementos en bloque al final.
//  * - Añade varios elementos en bloque en una posición concreta.
//  * - Elimina un elemento en una posición concreta.
//  * - Actualiza el valor de un elemento en una posición concreta.
//  * - Comprueba si un elemento está en un conjunto.
//  * - Elimina todo el contenido del conjunto.
//  *

/* DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */

func main() {

	data := []int{1, 2, 3, 4}
	fmt.Printf("Original DATA  %v\n", data)
	data = append(data, 5)
	fmt.Printf("add items at the end %v\n", data)

	// append(data[:1], data[0:]...) en este ejemplo, da como resultado [1, 1, 2, 3, 4].
	// Aquí, el primer elemento [1] se duplica, pero se está agregando un espacio adicional para el nuevo elemento.
	data = append(data[:1], data[0:]...)
	data[0] = 0
	fmt.Printf("add item at the Start %v\n", data)

	data = append(data, []int{6, 7, 8}...)
	fmt.Printf("add several items at the end %v\n", data)

	// Crear una nueva slice con espacio para los valores adicionales
	// y concatenar las partes del slice con los nuevos valores
	// es decir parto desde 0 hasta 4, conacteno el nuevo slice, y pego de 5 hasta final
	data = append(data[:5], append([]int{-1, -2, -3}, data[5:]...)...)
	fmt.Printf("add several items at index position  %v\n", data)

	// creo primer slice hasta posicion deseada a eliminar y el segundo slice desde la posicion siguente,
	// eliinando el elemento
	data = append(data[:3], data[4:]...)
	fmt.Printf("add several items at index position  %v\n", data)

	data[3] = 100
	fmt.Printf("Update  item at index position  %v\n", data)

	found := false
	for _, v := range data {
		if v == 100 {
			fmt.Printf("  %v is in  slice  %v\n", 100, data)
			found = true
			break
		}
	}
	if !found {
		fmt.Printf("  %v is NOT in  slice  %v\n", 100, data)
	}
	data = []int{}
	fmt.Printf("  Data empty  %v\n", data)

	// EXTRA

	set1 := map[int]bool{0: true, 2: true, 4: true, 6: true, 8: true, 10: true}
	set2 := map[int]bool{1: true, 2: true, 3: true, 4: true, 5: true, 6: true, 7: true, 8: true, 9: true, 10: true}

	// Interseccion
	interseccion := map[int]bool{}
	for i, _ := range set1 {

		intValue := set2[i]
		if intValue {
			interseccion[i] = true
		}
	}
	fmt.Printf("  INTERSECCION  %v\n", interseccion)

	// diferencia set 1 con set2

	diferencia1 := map[int]bool{}
	for i, _ := range set1 {
		dif := set2[i]
		if !dif {
			diferencia1[i] = true
		}
	}

	fmt.Printf("  Diferencia Set1 con Set2 %v\n", diferencia1)

	// diferencia set 1 con set2

	diferencia2 := map[int]bool{}
	for i, _ := range set2 {
		dif := set1[i]
		if !dif {
			diferencia2[i] = true
		}
	}

	fmt.Printf("  Diferencia Set2 con Set1 %v\n", diferencia2)

	// diferencia simetrica

	for i, _ := range diferencia1 {

		diferencia2[i] = true

	}

	fmt.Printf("  Diferencia simetrica %v\n", diferencia2)

	// union

	for i, _ := range set1 {
		set2[i] = true
	}
	fmt.Printf("  UNION  %v\n", set2)

}
