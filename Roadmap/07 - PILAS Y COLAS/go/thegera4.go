package main

import "fmt"

// Estructura de pila de números (LIFO)
type StringStack struct {
	data []string
}

// Saber si la pila está vacía
func (stack *StringStack) IsEmpty() bool {
	return len(stack.data) == 0
}

// Agrega un número a la pila
func (stack *StringStack) Push(element string) {
	stack.data = append(stack.data, element)
}

// Elimina y recupoera/devuelve el último número agregado a la pila. Regresa false si la pila está vacía
func (stack *StringStack) Pop() (string, bool) {
	if stack.IsEmpty() {
		return "", false
	} else {
		index := len(stack.data) - 1 // Indice del último elemento
		element := stack.data[index]  // Último elemento
		stack.data = stack.data[:index] // Elimina el último elemento por su indice
		return element, true
	}
}

// Estrucutra de cola de números (FIFO)
type StringsQueue struct {
	data []string
}

// Saber si la cola está vacía
func (queue *StringsQueue) IsEmpty() bool {
	return len(queue.data) == 0
}

// Agrega un número a la cola
func (queue *StringsQueue) Enqueue(element string) {
	queue.data = append(queue.data, element)
}

// Elimina y recupera/devuelve el primer número agregado a la cola. Regresa false si la cola está vacía
func (queue *StringsQueue) Dequeue() (string, bool) {
	if queue.IsEmpty() {
		return "", false
	} else {
		element := queue.data[0] // Accedemos al Primer elemento
		queue.data = queue.data[1:] // Elimina el primer elemento
		return element, true
	}
}

func main () {

	// Ejemplos de Stack
	stack := StringStack{}
	fmt.Println("Pila vacía: ", stack.IsEmpty())
	stack.Push("1")
	stack.Push("2")
	stack.Push("3")
	fmt.Println("Pila:" + fmt.Sprint(stack.data))
	fmt.Println("Ahora se eliminara el ultimo elemento de la pila...")
	stack.Pop()
	fmt.Println("Pila:" + fmt.Sprint(stack.data))
	
	// Ejemplos de Queue
	queue := StringsQueue{}
	fmt.Println("Cola vacía: ", queue.IsEmpty())
	queue.Enqueue("1")
	queue.Enqueue("2")
	queue.Enqueue("3")
	fmt.Println("Cola:" + fmt.Sprint(queue.data))
	fmt.Println("Ahora se eliminara el primer elemento de la cola...")
	queue.Dequeue()
	fmt.Println("Cola:" + fmt.Sprint(queue.data))

	// Extra
	menu()
}

// Funcion auxiliar para mostrar un menu de opciones y elegir entre salir, el navegador web o la impresora compartida
func menu() {
	for {
		var input int
		fmt.Println("Bienvenido a las funcinalidades extra. Por favor, elige una opción:")
		fmt.Println("1. Navegador Web")
		fmt.Println("2. Impresora Compartida")
		fmt.Println("3. Salir")
		fmt.Scanln(&input)
		switch input {
			case 1:
				webBrowser()
			case 2:
				sharedPrinter()
			case 3:
				return
			default:
				fmt.Println("Opción no válida")
		}
	}
}

// Simula el mecanismo adelante/atrás de un navegador web
func webBrowser() {
	history := StringStack{}
	forward := StringStack{}
	current := "google.com"
	fmt.Println("Bienvenido a: " + current)
	for {
		var input string
		fmt.Println("Ingresa una página web o 'atras' o 'adelante' para navegar o 'salir' para cerrar la aplicacion:")
		fmt.Scanln(&input)
		if input == "" {
			fmt.Println("Pagina no valida")
			continue
		}
		switch input {
			case "salir":
				return
			case "atras":
				if page, ok := history.Pop(); ok { 
					forward.Push(current)
					current = page
					fmt.Println("Ahora estás en: " + current)
				} else {
					fmt.Println("No hay páginas anteriores")
				}
			case "adelante":
				if page, ok := forward.Pop(); ok {
					history.Push(current)
					current = page
					fmt.Println("Ahora estás en: " + current)
				} else {
					fmt.Println("No hay páginas siguientes")
				}
			default:
				history.Push(current)
				current = input
				fmt.Println("Ahora estás en: " + current)
			}
	}
}

// Simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica
func sharedPrinter() {
	queue := StringsQueue{}
	for {
		var input string
		fmt.Println("Ingresa un nombre de documento, 'mostrar' para ver la cola de impresion, 'imprimir' para imprimir un documento en la fila o 'salir' para cerrar la aplicacion:")
		fmt.Scanln(&input)
		if input == "" {
			fmt.Println("Instruccion no valida")
			continue
		} else if input == "salir" {
			return
		} else if input == "imprimir" {
			if doc, ok := queue.Dequeue(); ok {
				fmt.Println("Imprimiendo: " + doc)
			} else {
				fmt.Println("No hay documentos para imprimir")
			}
		} else if input == "mostrar" {
			fmt.Println("Documentos en la cola: " + fmt.Sprint(queue.data))
		} else {
			queue.Enqueue(input)
			fmt.Println("Documento agregado a la cola")
		}
	}
}