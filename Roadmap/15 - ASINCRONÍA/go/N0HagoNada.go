package main

import (
	"fmt"
	"sync"
	"time"
)

func funcionAsincrona(nombre string, duracion time.Duration, wg *sync.WaitGroup) {
	if wg != nil {
		defer wg.Done()
	}
	fmt.Printf("%s comenzó\n", nombre)
	fmt.Printf("%s tardará %s en finalizar\n", nombre, duracion)
	time.Sleep(duracion)
	fmt.Printf("%s finalizó\n", nombre)
}

func main() {
	var wg sync.WaitGroup

	// Ejecutar las funciones C, B y A en paralelo
	wg.Add(3)
	go funcionAsincrona("Función C", 3*time.Second, &wg)
	go funcionAsincrona("Función B", 2*time.Second, &wg)
	go funcionAsincrona("Función A", 1*time.Second, &wg)

	// Esperar a que las funciones C, B y A finalicen
	wg.Wait()

	// Ejecutar la función D
	funcionAsincrona("Función D", 1*time.Second, nil)

	fmt.Println("Programa finalizado")
}
