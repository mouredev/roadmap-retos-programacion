package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Función que simula el procesamiento de un pedido
func procesarPedido(nombrePlato string, confirmar, listo, entregar func()) {

	confirmar()
	fmt.Printf("Procesando pedido: %s\n", nombrePlato)

	tiempo := rand.Intn(10) + 1
	fmt.Printf("Tiempo de procesamiento estimado: %d segundos\n", tiempo)
	time.Sleep(time.Duration(tiempo) * time.Second)

	listo()
	fmt.Printf("El plato %s está listo\n", nombrePlato)

	tiempo = rand.Intn(5) + 1
	fmt.Printf("Tiempo de entrega estimado: %d segundos\n", tiempo)
	time.Sleep(time.Duration(tiempo) * time.Second)

	entregar()
	fmt.Printf("El plato %s ha sido entregado\n", nombrePlato)
}

func main() {
	// Callbacks para las diferentes etapas del procesamiento
	confirmar := func() {
		fmt.Println("Confirmando pedido...")
	}

	listo := func() {
		fmt.Println("El plato está listo para ser entregado")
	}

	entregar := func() {
		fmt.Println("El plato ha sido entregado al cliente")
	}

	procesarPedido("Ensalada César", confirmar, listo, entregar)
	fmt.Println()
	procesarPedido("Pasta Carbonara", confirmar, listo, entregar)
}
