package main

import (
	"fmt"
	"time"
)

func main() {
	// Ejercicio regular:
	asyncFunction("Prueba", 5, nil)

	// Ejercicio EXTRA:
	// Primero, creamos un canal de tipo booleano (un canal es una estructura de datos que permite la comunicación entre goroutines)
	doneChan := make(chan bool) 
	defer close(doneChan)

	// Luego, ejecutamos las goroutines / funciones de forma concurrente
	go asyncFunction("C", 3, doneChan) // goroutines son funciones que se ejecutan de forma concurrente (al mismo tiempo / paralelas)
	go asyncFunction("B", 2, doneChan) // solo agregamos la palabra "go" antes de la llamada a la función, asi se ejecuta de forma concurrente
	go asyncFunction("A", 1, doneChan) // y le pasamos el canal para que las goroutines puedan indicar que han finalizado

	// Esperamos a que las funciones finalicen (se envíe un valor al canal)
	for i := 0; i < 3; i++ {
		<-doneChan
	}

	// Luego continuamos con la ejecución del programa. En este caso, ejecutamos una función de forma secuencial.
	asyncFunction("D", 1, nil)

}

func asyncFunction(name string, seconds int, doneChan chan bool) {
	fmt.Printf("La función %s comienza a las %s\n", name, time.Now().Format("15:04:05"))
	fmt.Printf("La función %s durará %d segundos\n", name, seconds)
	time.Sleep(time.Duration(seconds) * time.Second)
	fmt.Printf("La función %s finaliza a las %s\n", name, time.Now().Format("15:04:05"))
	if doneChan != nil{ 
		doneChan <- true // Enviamos un valor al canal para indicar que la función ha finalizado
	}
}