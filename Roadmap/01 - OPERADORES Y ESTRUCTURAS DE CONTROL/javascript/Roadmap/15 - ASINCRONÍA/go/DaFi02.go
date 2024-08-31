package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup

	wg.Add(1)
	go process(&wg, "Soy un proceso y duro poco :c", 1)
	wg.Wait()

	fmt.Println("-------------------------")
	fmt.Println("Reto : Procesos en paralelo con un proceso más largo")
	fmt.Println("-------------------------")

	wg.Add(3)

	go process(&wg, "C", 3)
	go process(&wg, "B", 2)
	go process(&wg, "A", 1)

	wg.Wait()

	fmt.Println("-------------------------")

	wg.Add(1)
	go process(&wg, "D", 1)
	wg.Wait()
}

func process(wg *sync.WaitGroup, name string, seconds int) {
	defer wg.Done()
	start := time.Now()
	fmt.Printf("El proceso %s comienza a las  %s y terminará en %d segundos\n", name, start.Format(time.DateTime), seconds)
	time.Sleep(time.Duration(seconds) * time.Second)
	fmt.Printf("Proceso: %s terminó a las: %s\n", name, time.Now().Format(time.DateTime))
}
