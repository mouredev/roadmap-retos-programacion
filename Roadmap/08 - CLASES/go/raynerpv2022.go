// # /*
// #  * EJERCICIO:
// #  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
// #  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
// #  * de tu lenguaje).
// #  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
// #  * utilizando su función.
// #  *
// #  * DIFICULTAD EXTRA (opcional):
// #  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
// #  * en el ejercicio número 7 de la ruta de estudio)
// #  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
// #  *   retornar el número de elementos e imprimir todo su contenido.
// #  *
// #  */
package main

import "fmt"

type Pila_o_Cola struct {
	listValue []string
}

func (pc *Pila_o_Cola) Initt(init_value ...string) {
	pc.listValue = []string{}
	if init_value != nil {
		pc.listValue = append(pc.listValue, init_value...)
	}

}

func (pc *Pila_o_Cola) add() {
	fmt.Println(" A rellenar , entra un elemento : ")
	var value string
	fmt.Scanln(&value)
	pc.listValue = append(pc.listValue, value)
}

func (pc *Pila_o_Cola) is_empty() bool {
	if len(pc.listValue) == 0 {

		return true

	} else {

		return false
	}
}

func (pc *Pila_o_Cola) items_count() {
	if !pc.is_empty() {
		fmt.Printf("There are  %d Items \n", len(pc.listValue))
		return
	}

	fmt.Println("Empty List... Add first")
}

func (pc *Pila_o_Cola) print_items() {
	if !pc.is_empty() {
		fmt.Println(" Mostrando elementos ... : ")
		fmt.Println(pc.listValue)
		return
	}
	fmt.Println("Empty List... Add first")
}

func (pc *Pila_o_Cola) delete_one_value(index int) (string, bool) {
	if !pc.is_empty() {
		var deleteItem string
		if index == 0 {
			deleteItem = pc.listValue[0]
			pc.listValue = pc.listValue[1:]
		} else {
			deleteItem = pc.listValue[len(pc.listValue)-1]
			pc.listValue = pc.listValue[:len(pc.listValue)-1]
		}
		return deleteItem, false
	}
	fmt.Println("Empty List... Add first")
	return "", true

}

type Pila struct {
	Pila_o_Cola
}

func (p *Pila) delete_lifo() {
	value, ok := p.delete_one_value(-1)
	if !ok {
		fmt.Println(" Deleting  LIFO  ... : ")
		fmt.Printf("Item %v  deleted succesfully \n", value)
		return
	}
	return

}

type Cola struct {
	Pila_o_Cola
}

func (c *Cola) delete_fifo() {
	value, ok := c.delete_one_value(0)
	if !ok {
		fmt.Println(" Deleting  FIFO  ... : ")
		fmt.Printf("Item %v  deleted succesfully ", value)
		return
	}

}

func main() {
	pila := Pila{}
	cola := Cola{}

	poc := ""
	for {
		fmt.Println("PIla (P)  o  COLA (C)  Quit (Q) ?")
		pc := ""
		fmt.Scanln(&pc)
		switch pc {
		case "P":
			poc = "Pila"
		case "C":
			poc = "Cola"
		case "Q":
			return
		default:

			fmt.Println("Enter only P, C or Q")
			continue
		}
		for {

			fmt.Printf(" What do you want to do with %v : \n", poc)
			fmt.Println("1 -  ADD")
			fmt.Println("2 -  PRINT")
			fmt.Println("3 -  How many Items are there")
			fmt.Println("4 -  REMOVE")
			fmt.Println("5 -  EXIT")
			var op string
			fmt.Scanln(&op)
			switch op {
			case "1":

				if pc == "P" {
					pila.add()
				} else {
					cola.add()
				}
			case "2":
				if pc == "P" {
					pila.print_items()
				} else {
					cola.print_items()
				}
			case "3":
				if pc == "P" {
					pila.items_count()
				} else {
					cola.items_count()
				}
			case "4":
				if pc == "P" {
					pila.delete_lifo()
				} else {
					cola.delete_fifo()
				}
			case "5":
				fmt.Println("EXIT now.. ... ")
				return
			default:
				fmt.Println("Enter number between 1 and 5 , try again")

				{

				}
			}
		}

	}
}
