package main

import (
	"fmt"
	"sync"
	"time"
)

func AsyncT(name string, duration int, wg *sync.WaitGroup) {
	if wg != nil {
		defer wg.Done()
	}

	startTime := time.Now()
	fmt.Printf("Task \"%s\" started at %s\n", name, startTime.Format("15:04:05"))
	fmt.Printf("Task \"%s\" will last %d seconds\n", name, duration)

	time.Sleep(time.Duration(duration) * time.Second)

	endTime := time.Now()
	fmt.Printf("Task \"%s\" finished at %s\n", name, endTime.Format("15:04:05"))
}

func main() {
	fmt.Println("Starting program...")

	// Creamos un Grupo de espera para syncronizar las gorutinas
	var wg sync.WaitGroup

	// Añadimos 3 tareas al grupo
	wg.Add(3)

	// Ejecutamos las tareas A, B y C en paralelo mediante goroutines
	go AsyncT("C", 3, &wg)
	go AsyncT("B", 2, &wg)
	go AsyncT("A", 1, &wg)

	// Esperamos a que funalizen las todas las tareas
	wg.Wait()

	// Una vez finalizadas todas las tareas ejecutamos la tarea D
	AsyncT("D", 1, nil)

	fmt.Println("Program Finished")
}
