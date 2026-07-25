/*
#  * EJERCICIO:
#  * Explora el concepto de callback en tu lenguaje creando un ejemplo
#  * simple (a tu elección) que muestre su funcionamiento.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
#  * Estará formado por una función que procesa pedidos.
#  * Debe aceptar el nombre del plato, una callback de confirmación, una
#  * de listo y otra de entrega.
#  * - Debe imprimir un confirmación cuando empiece el procesamiento.
#  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#  *   procesos.
#  * - Debe invocar a cada callback siguiendo un orden de procesado.
#  * - Debe notificar que el plato está listo o ha sido entregado.
#  */

package main

import (
	"fmt"
	"math/rand"
	"strings"
	"sync"
	"time"
)

type OrdersType func(name string) string

type MyFunction func(interface{}) interface{}

func Orders(name string, c, r, d OrdersType, w *sync.WaitGroup) {
	defer w.Done()

	waitTime := rand.Intn(10) + 1
	time.Sleep(time.Duration(waitTime) * time.Second)
	fmt.Printf("%v Wait time: %vs\n", c(name), waitTime)

	waitTime = rand.Intn(10) + 1
	time.Sleep(time.Duration(waitTime) * time.Second)
	fmt.Printf("%v Wait time: %vs\n", r(name), waitTime)

	waitTime = rand.Intn(10) + 1
	time.Sleep(time.Duration(waitTime) * time.Second)
	fmt.Printf("%v Wait time: %vs\n", d(name), waitTime)

}

func Confirm(name string) string {

	return fmt.Sprintf(" Plato %v confirmado", name)
}

func Ready(name string) string {

	return fmt.Sprintf(" Plato %v listo", name)
}

func Delivered(name string) string {

	return fmt.Sprintf(" Plato %v entregado", name)
}

func GetSum(list1 interface{}) interface{} {
	sum := 0
	for _, i := range list1.([]int) {
		sum += i
	}
	return sum
}

func GetNameUpperCase(name interface{}) interface{} {
	return strings.ToUpper(name.(string))
}

func Nothing(param interface{}, myF MyFunction) interface{} {
	return myF(param)
}

func main() {
	fmt.Println(Nothing([]int{1, 2, 3, 4, 5, 6, 7, 8, 9}, GetSum))
	fmt.Println(Nothing("resbaloso", GetNameUpperCase))

	fmt.Println("Extra")
	orders := []string{
		"Calabaza",
		"Brocoli",
		"Cebollino"}
	var w sync.WaitGroup
	fmt.Println("Precesamiento de Pedidos")
	for _, i := range orders {
		w.Add(1)
		go Orders(i, Confirm, Ready, Delivered, &w)
	}
	w.Wait()
}
