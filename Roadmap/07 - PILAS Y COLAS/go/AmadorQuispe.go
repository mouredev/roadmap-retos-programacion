package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	//stack -> LIFO
	//Push
	stackStudents := []string{}
	stackStudents = append(stackStudents, "Amador")
	stackStudents = append(stackStudents, "Pedro", "Alex")
	fmt.Println(stackStudents)
	//Pop
	itemPop := stackStudents[len(stackStudents)-1]
	stackStudents = stackStudents[:len(stackStudents)-1]
	fmt.Println("Pop element :", itemPop)
	fmt.Println(stackStudents)

	//Queue -> FIFO
	//enqueue
	queueNumbers := []int{}
	queueNumbers = append(queueNumbers, 1)
	queueNumbers = append(queueNumbers, 2, 3, 4, 5)
	fmt.Println(queueNumbers)

	//dequeue
	itemDequeue := queueNumbers[0]
	queueNumbers = queueNumbers[1:]
	fmt.Println("Dequeue element :", itemDequeue)
	fmt.Println(queueNumbers)
	sharedPrinting()
	webNavigation()
}

func sharedPrinting() {
	jobPrints := []string{}
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print("Añade un documento o selecciona imprimir/salir: ")
		action, _ := reader.ReadString('\n')
		action = strings.TrimSpace(action)
		if action == "salir" {
			fmt.Println("Saliendo...")
			os.Exit(0)
		} else if action == "imprimir" {
			if len(jobPrints) > 0 {
				p := jobPrints[len(jobPrints)-1]
				jobPrints = jobPrints[:len(jobPrints)-1]
				fmt.Println("Imprimiendo :", p)
			}
		} else {
			jobPrints = append(jobPrints, action)
			fmt.Println("Trabajo impresión agregada a la cola")
		}
		fmt.Println("Cola de impresión", jobPrints)
	}
}

func webNavigation() {
	history := []string{}
	reader := bufio.NewReader(os.Stdin)
	for {
		if len(history) > 0 {
			fmt.Print("Añade una url o interactúa con palabras adelante/atrás/salir:")
		} else {
			fmt.Print("Añade una url:")
		}
		command, _ := reader.ReadString('\n')
		command = strings.TrimSpace(command)
		switch command {
		case "salir":
			fmt.Println("Saliendo del navegador")
			os.Exit(0)
		case "adelante":
			fmt.Println("No hay historial hacia adelante")
		case "atrás":
			if len(history) == 0 {
				fmt.Println("No hay mas historial hacia atrás")
			}
			history = history[:len(history)-1]

		default:
			history = append(history, command)
		}
		if len(history) > 0 {
			lastItem := history[len(history)-1]
			fmt.Printf("Has navegado a la web: %s.\n", lastItem)
		} else {
			fmt.Println("Estás en la página de inicio.")
		}

	}
}
