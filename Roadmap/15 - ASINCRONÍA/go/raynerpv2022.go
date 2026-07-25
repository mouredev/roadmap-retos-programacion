package main

import (
	"fmt"
	"sync"
	"time"
)

// /*
//   - EJERCICIO:
//   - Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
//   - asíncrona una función que tardará en finalizar un número concreto de
//   - segundos parametrizables. También debes poder asignarle un nombre.
//   - La función imprime su nombre, cuándo empieza, el tiempo que durará
//   - su ejecución y cuando finaliza.
//     *
//   - DIFICULTAD EXTRA (opcional):
//   - Utilizando el concepto de asincronía y la función anterior, crea
//   - el siguiente programa que ejecuta en este orden:
//   - - Una función C que dura 3 segundos.
//   - - Una función B que dura 2 segundos.
//   - - Una función A que dura 1 segundo.
//   - - Una función D que dura 1 segundo.
//   - - Las funciones C, B y A se ejecutan en paralelo.
//   - - La función D comienza su ejecución cuando las 3 anteriores han
//   - finalizado.
//     */

func my_task(duration int, name string, wg *sync.WaitGroup) {
	if wg != nil {
		defer wg.Done()
	}
	start := time.Now()
	fmt.Printf(" Task: %v Start: %v\n", name, start)
	time.Sleep(time.Duration(duration) * time.Second)
	end := time.Now()
	fmt.Printf(" Task: %v End: %v  Duration%v\n", name, end, duration)
}

func main() {
	var wg sync.WaitGroup
	wg.Add(3)
	go my_task(10, "TAsk A", &wg)
	go my_task(8, "TAsk B", &wg)
	go my_task(4, "TAsk c", &wg)
	wg.Wait()
	my_task(1, "TAsk D", nil)

}
