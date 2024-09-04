package main

import (
	"fmt"
	"time"
)

// NOTA: Un callback es una función que se pasa como argumento a otra función.

// Definimos un tipo para la funcion callback, en este caso recibe un entero y devuelve un entero
type Callback func(int) int

// Definimos una funcion que aplique una operacion al numero que recibe y devuelve el resultado
func applyCallback(num int, callback Callback) int {
	return callback(num)
}

func main() {
	// Definimos una funcion que multiplica por 2 el numero.
	duplica := func(num int) int {
		return num * 2
	}

	// Definimos otra funcion que suma el numero con 10
	suma := func(num int) int {
		return num + 10
	}

	// Aplicamos la funcion duplicar al numero 5
	fmt.Println("Resultado de multiplicar 5 por 2:", applyCallback(5, duplica))

	// Aplicamos la funcion triplicar al numero 5
	fmt.Println("Resultado de sumar 15 con 10:", applyCallback(15, suma))

	// Extra
	simuladorPedidos()

}

func simuladorPedidos() {

	// Definimos las funciones de confirmacion, listo y entrega
	confirmacion := func(num int) int {
		fmt.Println("Pedido confirmado")
		return num
	}

	listo := func(num int) int {
		fmt.Println("Plato listo")
		return num
	}

	entrega := func(num int) int {
		fmt.Println("Pedido entregado")
		return num
	}

	// Simulamos un pedido de pizza
	procesarPedido("Pizza", confirmacion, listo, entrega)

	// Simulamos un pedido de hamburguesa
	procesarPedido("Hamburguesa", confirmacion, listo, entrega)
}

func procesarPedido(plato string, confirmacion, listo, entrega Callback) {
	fmt.Println("Procesando pedido de", plato)

	time.Sleep(time.Duration(1+time.Now().Nanosecond()%10) * time.Second) // Simulamos un tiempo aleatorio entre 1 y 10 segundos
	confirmacion(1)

	time.Sleep(time.Duration(1+time.Now().Nanosecond()%10) * time.Second)
	listo(2)

	time.Sleep(time.Duration(1+time.Now().Nanosecond()%10) * time.Second)
	entrega(3)
}