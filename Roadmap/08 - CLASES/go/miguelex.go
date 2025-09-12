package main

import "fmt"

// Las clases en Go son un poco diferentes a otros lenguajes, no funcionado de forma "tradicional"
type Vehiculo struct {
	nombre    string
	numRuedas int
}

// Constructor de Vehiculo
func NuevoVehiculo(nombre string, numRuedas int) *Vehiculo {
	return &Vehiculo{nombre: nombre, numRuedas: numRuedas}
}

// Método ToString para Vehiculo
func (v *Vehiculo) ToString() string {
	return fmt.Sprintf("Nombre: %s, Número de Ruedas: %d", v.nombre, v.numRuedas)
}

// Definición de la estructura Pila
type Pila struct {
	elementos []interface{}
}

// Método para agregar un elemento a la pila
func (p *Pila) Push(elemento interface{}) {
	p.elementos = append(p.elementos, elemento)
}

// Método para eliminar y devolver el último elemento agregado a la pila
func (p *Pila) Pop() interface{} {
	if len(p.elementos) == 0 {
		return nil // Devolver nil si la pila está vacía
	}
	elemento := p.elementos[len(p.elementos)-1]
	p.elementos = p.elementos[:len(p.elementos)-1]
	return elemento
}

// Método para obtener el tamaño de la pila
func (p *Pila) Size() int {
	return len(p.elementos)
}

// Método para imprimir los elementos de la pila
func (p *Pila) ToString() string {
	str := "["
	for i, elemento := range p.elementos {
		str += fmt.Sprintf("%v", elemento)
		if i < len(p.elementos)-1 {
			str += ", "
		}
	}
	str += "]"
	return str
}

// Definición de la estructura Cola
type Cola struct {
	elementos []interface{}
}

// Método para agregar un elemento a la cola
func (c *Cola) Enqueue(elemento interface{}) {
	c.elementos = append(c.elementos, elemento)
}

// Método para eliminar y devolver el primer elemento agregado a la cola
func (c *Cola) Dequeue() interface{} {
	if len(c.elementos) == 0 {
		return nil // Devolver nil si la cola está vacía
	}
	elemento := c.elementos[0]
	c.elementos = c.elementos[1:]
	return elemento
}

// Método para obtener el tamaño de la cola

func (c *Cola) Size() int {
	return len(c.elementos)
}

// Método para imprimir los elementos de la cola
func (c *Cola) ToString() string {
	str := "["
	for i, elemento := range c.elementos {
		str += fmt.Sprintf("%v", elemento)
		if i < len(c.elementos)-1 {
			str += ", "
		}
	}
	str += "]"
	return str
}

func main() {
	// Crear un nuevo Vehiculo
	coche := NuevoVehiculo("Coche", 4)
	bicicleta := NuevoVehiculo("Bicicleta", 2)

	// Imprimir los detalles del Vehiculo usando el método ToString
	fmt.Println(coche.ToString())
	fmt.Println(bicicleta.ToString())

	// Crear una nueva pila
	pila := Pila{}

	// Agregar elementos a la pila
	pila.Push(1)
	pila.Push(2)
	pila.Push(3)

	// Imprimir el tamaño de la pila
	fmt.Println("Tamaño de la pila:", pila.Size())

	// Imprimir los elementos de la pila
	fmt.Println("Elementos de la pila:", pila.ToString())

	// Eliminar un elemento de la pila
	elementoEliminado := pila.Pop()
	fmt.Println("Elemento eliminado:", elementoEliminado)

	// Imprimir el tamaño de la pila después de eliminar un elemento
	fmt.Println("Tamaño de la pila:", pila.Size())

	// Imprimir los elementos de la pila después de eliminar un elemento
	fmt.Println("Elementos de la pila:", pila.ToString())

	// Crear una nueva cola
	cola := Cola{}

	// Agregar elementos a la cola
	cola.Enqueue(1)
	cola.Enqueue(2)
	cola.Enqueue(3)

	// Imprimir el tamaño
	fmt.Println("Tamaño de la cola:", cola.Size())

	// Imprimir los elementos de la cola
	fmt.Println("Elementos de la cola:", cola.ToString())

	// Eliminar un elemento de la cola
	elementoEliminado = cola.Dequeue()
	fmt.Println("Elemento eliminado:", elementoEliminado)

	// Imprimir el tamaño de la cola después de eliminar un elemento
	fmt.Println("Tamaño de la cola:", cola.Size())

	// Imprimir los elementos de la cola después de eliminar un elemento
	fmt.Println("Elementos de la cola:", cola.ToString())
}
