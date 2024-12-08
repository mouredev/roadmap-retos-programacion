/*
#  * EJERCICIO:
#  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  * o lista (dependiendo de las posibilidades de tu lenguaje).
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.
#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.
#
*/
package main

import "fmt"

type Pila struct {
	item []string
}

type Cola struct {
	item []string
}

func (p *Pila) set_pila(items string) {
	p.item = append(p.item, items)
}

func (p *Pila) get_pila() string {
	last := p.item[len(p.item)-1]
	p.item = append(p.item[:len(p.item)-1])
	return last
}

func (c *Cola) set_cola(items string) {
	c.item = append(c.item, items)
}

func (c *Cola) get_cola() string {
	last := c.item[0]
	c.item = append(c.item[1:])
	return last
}

func pila_func(pilita *Pila) {
	op_pila := ""
	fmt.Println(" PILA, Set (1) o Get (2)")
	fmt.Scanln(&op_pila)
	switch op_pila {
	case "1":
		print("Items a introducir : ")
		it := ""
		fmt.Scanln(&it)
		pilita.set_pila(it)
	case "2":
		fmt.Println("Sacando ultimo elemento pila")
		fmt.Println("Pila completa ", pilita.item)
		fmt.Println(pilita.get_pila())
		fmt.Println("Pila actualizada ", pilita.item)

	}

}

func cola_func(colita *Cola) {
	op_cola := ""
	fmt.Println(" Cola, Set (1) o Get (2)")
	fmt.Scanln(&op_cola)
	switch op_cola {
	case "1":
		it := ""
		fmt.Println("Items a introducir : ")
		fmt.Scanln(&it)
		colita.set_cola(it)
	case "2":
		fmt.Println("Sacando ultimo elemento cola")
		fmt.Println("COla completa ", colita.item)
		fmt.Println(colita.get_cola())
		fmt.Println("Cola actualizada ", colita.item)

	}

}

func ex1() {
	pilita := Pila{
		[]string{"11", "2", "3", "4", "5", "6"},
	}
	colita := Cola{
		[]string{"1", "2", "3", "4", "5", "6"},
	}
	var op string
	for {
		fmt.Println(" Pila (1) o  Cola (2) Salir (3):")
		fmt.Scanln(&op)
		switch op {
		case "1":
			pila_func(&pilita)
		case "2":
			cola_func(&colita)
		case "3":
			return
		default:
			fmt.Println("OPcion no valida")
		}

	}
}

// ******* EXTRA ******
func isEmpty(list1 []string, cad string) bool {
	if len(list1) == 0 {
		fmt.Println(cad)
		return true
	} else {
		return false
	}
}
func TOR() {
	web_list := []string{}
	index := 0
	for {
		op := ""
		fmt.Println("atras, adelante, url, salir :")
		fmt.Scanln(&op)
		switch op {
		case "atras":
			if !(isEmpty(web_list, "Listado de web vacio")) {
				if index > 0 {
					index--
				}
				fmt.Printf("navegando a  : %v indice %d \n", web_list[index], index)
			}
		case "adelante":
			if !(isEmpty(web_list, "Listado de web vacio")) {
				if index < len(web_list)-1 {
					index++
				}
				fmt.Printf("navegando a  : %v indice %d \n", web_list[index], index)
			}
		case "url":
			if !(isEmpty(web_list, "Listado de web vacio")) {
				fmt.Printf("TAB de WEB : %v indice %d \n", web_list, index)
			}
		case "salir":
			return
		default:

			web_list = append(web_list, op)
			index = len(web_list) - 1
			fmt.Printf("navegando a  : %v indice %d \n", web_list[index], index)

		}
	}
}

func printer() {
	printerQ := []string{}

	for {
		op := ""
		fmt.Println("imprimir o salir :")
		fmt.Scanln(&op)
		switch op {
		case "imprimir":
			fmt.Println(" IMprimiendo :", printerQ[0])
			printerQ = append(printerQ[1:])
			fmt.Println(" Tareas a imprimir :", printerQ)
		case "salir":
			return
		default:
			printerQ = append(printerQ, op)
			fmt.Println(" Tareas a imprimir :", printerQ)

		}

	}

}

func extra() {
	TOR()
	printer()
}

func main() {
	ex1()
	extra()

}
