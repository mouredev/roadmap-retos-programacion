package main

import "fmt"

// Definimos una estructura de datos slice como nuestro conjunto
type mySet []interface{}

func main() {
	// Creamos un nuevo conjunto vacío
	set := mySet{}

	// Añadimos un elemento al final
	set = append(set, 1)
	fmt.Println("Añadimos 1 al final:", set)

	// Añadimos un elemento al principio
	set = append(mySet{2}, set...)
	fmt.Println("Añadimos 2 al principio:", set)

	// Añadimos varios elementos en bloque al final
	set = append(set, 3, 4, 5)
	fmt.Println("Añadimos 3, 4, 5 al final:", set)

	// Añadimos varios elementos en bloque en una posición concreta
	set = append(set[:2], append(mySet{6, 7}, set[2:]...)...)
	fmt.Println("Añadimos 6, 7 en la posición 2:", set)

	// Eliminamos un elemento en una posición concreta
	set = append(set[:3], set[4:]...)
	fmt.Println("Eliminamos el elemento en la posición 3:", set)

	// Actualizamos el valor de un elemento en una posición concreta
	set[1] = 8
	fmt.Println("Actualizamos el valor del segundo elemento a 8:", set)

	// Comprobamos si un elemento está en un conjunto
	fmt.Println("¿El elemento 6 está en el conjunto?", containsElement(set, 6))

	// Eliminamos todo el contenido del conjunto
	set = mySet{}
	fmt.Println("Conjunto vacío:", set)
}

// Función auxiliar para comprobar si un elemento está en el conjunto
func containsElement(set mySet, val interface{}) bool {
	for _, v := range set {
		if v == val {
			return true
		}
	}
	return false
}
