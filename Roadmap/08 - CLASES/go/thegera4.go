/* 
NOTA IMPORTANTE:
Go no tiene clases como tal, pero se pueden simular con structs(estructuras) 
y métodos asociados a ellas.
En este ejemplo se simulan las estructuras de pila y cola, y se les agregan
métodos para realizar operaciones sobre ellas.
Los metodos se definen con la estructura a la que pertenecen como primer 
argumento el cual se llama receptor.
*/

package main

import "fmt"

// Simulacion de clase "Car" con métodos asociados
type Car struct {
	brand string // atributos
	model string
	year int
}

// Método asociado a la estructura "Car"
func (car Car) printInfo() string {
	return fmt.Sprintf("Marca: %s, Modelo: %s, Año: %d", car.brand, car.model, car.year)
}

// Método asociado a la estructura "Car"
func (car *Car) changeBrand(newBrand string) {
	car.brand = newBrand
}

// Estructura de pila de números (LIFO)
type Stack[T any] struct {
	data []T
}

// Saber si la pila está vacía
func (stack *Stack[T]) IsEmpty() bool {
	return len(stack.data) == 0
}

// Agrega un número a la pila
func (stack *Stack[T]) Push(element T) {
	stack.data = append(stack.data, element)
}

// Elimina y recupoera/devuelve el último número agregado a la pila. Regresa false si la pila está vacía
func (stack *Stack[T]) Pop() (T, bool) {
	if stack.IsEmpty() {
		var zeroValue T
		return zeroValue, false
	} else {
		index := len(stack.data) - 1 // Indice del último elemento
		element := stack.data[index]  // Último elemento
		stack.data = stack.data[:index] // Elimina el último elemento por su indice
		return element, true
	}
}

// Estrucutra de cola de números (FIFO)
type Queue[T any] struct {
	data []T
}

// Saber si la cola está vacía
func (queue *Queue[T]) IsEmpty() bool {
	return len(queue.data) == 0
}

// Agrega un número a la cola
func (queue *Queue[T]) Enqueue(element T) {
	queue.data = append(queue.data, element)
}

// Elimina y recupera/devuelve el primer número agregado a la cola. Regresa false si la cola está vacía
func (queue *Queue[T]) Dequeue() (T, bool) {
	if queue.IsEmpty() {
		var zeroValue T
		return zeroValue, false
	} else {
		element := queue.data[0] // Accedemos al Primer elemento
		queue.data = queue.data[1:] // Elimina el primer elemento
		return element, true
	}
}

func main () {

	// Simulacion de clase "Car"
	car1 := Car{brand: "Ford", model: "Fiesta", year: 2019}
	fmt.Println(car1.printInfo())
	car1.changeBrand("Chevrolet")
	fmt.Println(car1.printInfo())
	
	// Extra: Stack / Pila
	stack := Stack[string]{}
	fmt.Println("Pila vacía: ", stack.IsEmpty())
	stack.Push("1")
	stack.Push("2")
	stack.Push("3")
	fmt.Println("Pila:" + fmt.Sprint(stack.data))
	fmt.Println("Ahora se eliminara el ultimo elemento de la pila...")
	stack.Pop()
	fmt.Println("Pila:" + fmt.Sprint(stack.data))
	
	// Extra: Queue / Cola
	queue := Queue[int]{}
	fmt.Println("Cola vacía: ", queue.IsEmpty())
	queue.Enqueue(1)
	queue.Enqueue(2)
	queue.Enqueue(3)
	fmt.Println("Cola:" + fmt.Sprint(queue.data))
	fmt.Println("Ahora se eliminara el primer elemento de la cola...")
	queue.Dequeue()
	fmt.Println("Cola:" + fmt.Sprint(queue.data))

}