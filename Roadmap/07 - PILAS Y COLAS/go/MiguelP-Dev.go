package main

import "fmt"

func main() {
	var lifo sliceStack
	var fifo sliceQueue

	for {
		var opt uint8
		fmt.Println("Selecciona uan opcion:")
		fmt.Println("1. Ejecuta las funciones de Pilas.")
		fmt.Println("2. Ejecuta las funciones de Colas.")
		fmt.Println("3. Navegador.")
		fmt.Println("4. Impresora.")
		fmt.Println("5. Salir.")
		fmt.Scan(&opt)

		switch opt {
		case 1:
			// LIFO (Last In, First Out).
			lifo.push("MiguelP-Dev")
			lifo.push("master")

			fmt.Println(lifo.pop())
			fmt.Println(lifo.pop())
			fmt.Println(lifo.pop())

		case 2:
			// FIFO (First In, First Out).

			fifo.push("0")
			fifo.push("1")
			fifo.push("2")
			fifo.push("3")

			fmt.Println(fifo.pop())
			fmt.Println(fifo.pop())
			fmt.Println(fifo.pop())
			fmt.Println(fifo.pop())
			fmt.Println(fifo.pop())

		case 3:
			webNavigator(&navigator)
		case 4:
			docPrinter(&printerv)
		case 5:
			return
		default:
			continue
		}

	}
}

// LIFO (Last In, First Out).
// sliceStack Es un slice que funcionará como una pila(Stack).
type sliceStack []string

// push Método para agregar datos a un slice que funciona como pila.
func (s *sliceStack) push(v string) {
	*s = append(*s, v)
}

// popSlice Método pop para sacar elementos de uns slice que sirve como pila(Los slices no tienen una función 'Delete', pero son ideales como pilas).
func (s *sliceStack) pop() string {
	if len(*s) == 0 {
		fmt.Println("La pila está vacía.")
		return ""
	}
	index := len(*s) - 1
	element := (*s)[index]
	*s = (*s)[:index]
	return element
}

// FIFO (First In, First Out).
// sliceQueue Es un slice que funcionará como una cola.
type sliceQueue []string

// push Método para encolar elementos
func (q *sliceQueue) push(v string) {
	*q = append(*q, v)
}

// pop Método para deencolar elementos
func (q *sliceQueue) pop() string {
	if len(*q) == 0 {
		fmt.Println("La cola está vacía.")
		return ""
	}
	pop := (*q)[0]
	*q = (*q)[1:]
	return pop
}

/*
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 */
// navStack pila para la función que simula un navegador
type navStack []string

var navigator navStack
var position = 0

func webNavigator(n *navStack) {
	for {
		var option string
		fmt.Printf("\n")
		fmt.Println("adelante", " - ", "Viajar a la página siguiente.")
		fmt.Println("atras", " - ", "Viajar a la página anterior.")
		fmt.Println("salir", " - ", "Salir de la app.")
		fmt.Println("borrar", " - ", "Borra el historial.")
		fmt.Printf("Ingresa una de las opciones: ")
		fmt.Scan(&option)

		switch option {
		case "salir":
			fmt.Println("Saliendo... Bye!")
			return
		case "adelante":
			if position < len(*n)-1 {
				position++
				fmt.Println("Viajando a:", (*n)[position])
			} else {
				fmt.Println("No hay páginas delante.")
			}
		case "atras":
			if position > 0 {
				position--
				fmt.Println("Viajando a:", (*n)[position])
			} else {
				fmt.Println("No hay páginas hacia atrás.")
			}
		case "borrar":
			*n = []string{}
			position = 0
			fmt.Println("Histarial borrado.")
		default:
			if len(*n) == 0 {
				*n = append(*n, option)
				position = 0
			} else {
				*n = append((*n)[:position+1], option)
				position++
			}
			fmt.Println("Navegando a:", (*n)[position])
		}
	}

}

type queue []string

var printerv queue

func docPrinter(q *queue) {
	var option string
	fmt.Scan(&option)

	switch option {
	case "imprimir":
		if len(*q) == 0 {
			fmt.Println("La cola de impresión está vacía.")
			return
		}
		fmt.Println("Imprimiendo: " + (*q)[0])
		*q = (*q)[1:]
	case "Salir":
		return
	default:
		*q = append(*q, option)
		fmt.Println("Documento agregado a la cola")
	}
	docPrinter(&printerv)

}
