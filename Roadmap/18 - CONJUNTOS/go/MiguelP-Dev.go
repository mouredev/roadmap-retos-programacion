package main

import (
	"fmt"
	"strings"
)

// Un conjunto es una colección de elementos no repetidos.
// En Go, los conjuntos se pueden implementar utilizando mapas.
// La clave del mapa es el elemento y el valor es un booleano que indica si el elemento está presente en el conjunto.

// Set Definimos la estructura de un conjunto.
type Set struct {
	elements map[any]bool
}

// Creamos un nuevo conjunto.
func NewSet() *Set {
	return &Set{elements: make(map[any]bool)}
}

// Add Añade un elemento al conjunto.
func (s *Set) Add(element any) {
	s.elements[element] = true
}

// Remove Elimina un elemento del conjunto.
func (s *Set) Remove(element any) {
	delete(s.elements, element)
}

// Contains Comprueba si un elemento está en el conjunto.
func (s *Set) Contains(element any) bool {
	// Extra: Comprobamos si el elemento es de tipo string y lo convertimos a minúsculas para comprobar si existe en el conjunto.
	if _, ok := element.(string); ok {
		strings.ToLower(element.(string))
		return s.elements[element]
	}

	return s.elements[element]
}

// Size Devuelve el tamaño del conjunto.
func (s *Set) Size() int {
	return len(s.elements)
}

// Task1: Union de conjuntos.
// La unión de dos conjuntos es la operación que resulta en un nuevo conjunto que
// contiene todos los elementos de los conjuntos originales.
func Union(set1, set2 *Set) *Set {
	unionSet := NewSet()

	for element := range set1.elements {
		unionSet.Add(element)
	}

	for element := range set2.elements {
		unionSet.Add(element)
	}

	return unionSet
}

// Task2 : Intersección de conjuntos.
// La intersección de dos conjuntos es la operación que resulta en un nuevo conjunto que contiene solo
// los elementos que están presentes en ambos conjuntos originales.
func intersection(set1, set2 *Set) *Set {
	intersectionSet := NewSet()

	for element := range set1.elements {
		if set2.Contains(element) {
			intersectionSet.Add(element)
		}
	}

	return intersectionSet
}

// Task3 : Diferencia de conjuntos.
// La diferencia de dos conjuntos es la operación que resulta en un nuevo conjunto que contiene solo
// los elementos que están presentes en el primer conjunto original pero no en el segundo.
func difference(set1, set2 *Set) *Set {
	differenceSet := NewSet()

	for element := range set1.elements {
		if !set2.Contains(element) {
			differenceSet.Add(element)
		}
	}
	return differenceSet
}

// Task4 : Diferencia simétrica de conjuntos.
// La diferencia simétrica de dos conjuntos es la operación que resulta en un nuevo conjunto que contiene solo
// los elementos que están presentes en uno de los conjuntos originales, pero no en ambos.
func symmetricDifference(set1, set2 *Set) *Set {
	symmetricDifferenceSet := NewSet()

	for element := range set1.elements {
		if !set2.Contains(element) {
			symmetricDifferenceSet.Add(element)
		}
	}

	for element := range set2.elements {
		if !set1.Contains(element) {
			symmetricDifferenceSet.Add(element)
		}
	}

	return symmetricDifferenceSet
}
func main() {
	// Creamos un nuevo conjunto.
	set := NewSet()

	// Añadimos elementos al conjunto.
	set.Add(1)
	set.Add("hello")
	set.Add(3)

	// Comprobamos si un elemento está en el conjunto.
	fmt.Println(set.Contains(1))       // true
	fmt.Println(set.Contains(2))       // false
	fmt.Println(set.Contains(3))       // true
	fmt.Println(set.Contains("hello")) // true

	// Eliminamos un elemento del conjunto.
	set.Remove(1)

	// Comprobamos si el elemento ha sido eliminado.
	fmt.Println(set.Contains(1)) // false

	// Mostramos el tamaño del conjunto.
	fmt.Println(set.Size()) // 2

	// Nota: Los conjuntos no permiten elementos duplicados. En Golang trabajamos con mapas para los conjuntos y las claves no pueden ser duplicadas.
	// Por lo tanto, si intentamos añadir un elemento que ya existe en el conjunto, no se añadirá. También al ser un mapa, los elementos no tienen un orden específico.
	// Por lo tanto, no podemos garantizar el orden de los elementos en el conjunto. Solo podemos usar trucos para insertar elemtos al principio o al final.
	// Para mantener el orden de los elementos, podemos usar una lista enlazada o una lista doblemente enlazada.

	// Añade un elemento al principio.
	set.Add(0)
	fmt.Println(set.Size()) // 4
	fmt.Println(set.elements)

	// Añade un elemento al final.
	set.Add(4)
	fmt.Println(set.Size()) // 3
	fmt.Println(set.elements)

	// Añade varios elementos en bloque al final.
	set.Add(5)
	set.Add(6)
	set.Add(7)
	fmt.Println(set.Size()) // 7
	fmt.Println(set.elements)

	// Añade varios elementos en bloque en una posición concreta.
	// Actualiza el valor de un elemento en una posición concreta.
	set.Add(8)
	set.Add(9)
	set.Add(10)
	fmt.Println(set.Size()) // 10
	fmt.Println(set.elements)

	// Actualiza el valor de un elemento en una posición concreta.
	set.Add(10)
	fmt.Println(set.Size()) // 10
	fmt.Println(set.elements)

	// Elimina todo el contenido del conjunto.
	set = NewSet()
	fmt.Println(set.Size()) // 0
	fmt.Println(set.elements)

	// Extra: Ejemplos de operaciones de conjuntos.
	// Unión de conjuntos.
	// Creamos dos conjuntos.
	set1 := NewSet()
	set2 := NewSet()

	// Añadimos elementos a los conjuntos.
	set1.Add(1)
	set1.Add(2)
	set1.Add(3)

	set2.Add(4)
	set2.Add(5)
	set2.Add(6)

	// Unimos los conjuntos.
	unionSet := Union(set1, set2)
	fmt.Println("UnionSets:")
	fmt.Println(unionSet.Size()) // 6
	fmt.Println(unionSet.elements)

	// Intersección de conjuntos.
	// Creamos dos conjuntos.
	set3 := NewSet()
	set4 := NewSet()

	// Añadimos elementos a los conjuntos.
	set3.Add(1)
	set3.Add(2)
	set3.Add(3)

	set4.Add(2)
	set4.Add(3)
	set4.Add(4)

	// Obtenemos la intersección de los conjuntos.
	intersectionSet := intersection(set3, set4)
	fmt.Println("IntersectionSet:")
	fmt.Println("Size: ", intersectionSet.Size()) // 2
	fmt.Println("Elements: ", intersectionSet.elements)

	// Diferencia de conjuntos.
	// Creamos dos conjuntos.
	set5 := NewSet()
	set6 := NewSet()

	// Añadimos elementos a los conjuntos.
	set5.Add(1)
	set5.Add(2)
	set5.Add(3)

	set6.Add(2)
	set6.Add(3)
	set6.Add(4)

	// Obtenemos la diferencia de los conjuntos.
	differenceSet := difference(set5, set6)
	fmt.Println("DifferenceSet:")
	fmt.Println("Size: ", differenceSet.Size()) // 1
	fmt.Println("Elements: ", differenceSet.elements)

	// Diferencia simétrica de conjuntos.
	// Creamos dos conjuntos.
	set7 := NewSet()
	set8 := NewSet()

	// Añadimos elementos a los conjuntos.
	set7.Add(1)
	set7.Add(2)
	set7.Add(3)

	set8.Add(2)
	set8.Add(3)
	set8.Add(4)

	// Obtenemos la diferencia simétrica de los conjuntos.
	symmetricDifferenceSet := symmetricDifference(set7, set8)
	fmt.Println("SymmetricDifferenceSet:")
	fmt.Println("Size: ", symmetricDifferenceSet.Size()) // 2
	fmt.Println("Elements: ", symmetricDifferenceSet.elements)
}
