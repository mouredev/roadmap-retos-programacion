// # #07 PILAS Y COLAS
// > #### Dificultad: Media | Publicación: 12/02/24 | Corrección: 19/02/24

// ## Ejercicio

// ```
// /*
//  * EJERCICIO:
//  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
//  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
//  * o lista (dependiendo de las posibilidades de tu lenguaje).
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
//  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
//  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
//  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
//  *   el nombre de una nueva web.
//  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
//  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
//  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
//  *   interpretan como nombres de documentos.
//  */
// ```
// #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

// Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

// > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

package main

import (
	"fmt"
	"strings"
)

// Stack (Pila - LIFO)
type Stack struct {
	items []string
}

func (s *Stack) Push(item string) {
	s.items = append(s.items, item)
}

func (s *Stack) Pop() (string, bool) {
	if len(s.items) == 0 {
		return "", false
	}
	item := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return item, true
}

func (s *Stack) Peek() (string, bool) {
	if len(s.items) == 0 {
		return "", false
	}
	return s.items[len(s.items)-1], true
}

// Queue (Cola - FIFO)
type Queue struct {
	items []string
}

func (q *Queue) Enqueue(item string) {
	q.items = append(q.items, item)
}

func (q *Queue) Dequeue() (string, bool) {
	if len(q.items) == 0 {
		return "", false
	}
	item := q.items[0]
	q.items = q.items[1:]
	return item, true
}

func navegadorWeb() {
	historial := Stack{}
	adelante := Stack{}
	currentPage := ""

	for {
		fmt.Printf("\nPágina actual: [%s]\n", currentPage)
		fmt.Println("1. Ingresar URL")
		fmt.Println("2. Atrás")
		fmt.Println("3. Adelante")
		fmt.Println("4. Salir")
		fmt.Print("Seleccione opción: ")

		var input string
		fmt.Scanln(&input)

		switch strings.ToLower(input) {
		case "1", "url":
			fmt.Print("Ingrese URL: ")
			fmt.Scanln(&input)
			if currentPage != "" {
				historial.Push(currentPage)
			}
			currentPage = input
			adelante = Stack{} // Resetear pila adelante

		case "2", "atrás":
			if page, ok := historial.Pop(); ok {
				adelante.Push(currentPage)
				currentPage = page
			} else {
				fmt.Println("No hay páginas anteriores")
			}

		case "3", "adelante":
			if page, ok := adelante.Pop(); ok {
				historial.Push(currentPage)
				currentPage = page
			} else {
				fmt.Println("No hay páginas siguientes")
			}

		case "4", "salir":
			return

		default:
			fmt.Println("Opción no válida")
		}
	}
}

func main() {
	navegadorWeb()
}
