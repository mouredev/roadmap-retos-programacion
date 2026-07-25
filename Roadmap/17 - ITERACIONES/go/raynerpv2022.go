package main

import "fmt"

/*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
#  */

func main() {

	for i := 1; i < 11; i++ {
		fmt.Println(i)
	}

	// for like while
	i := 1
	for i < 11 {
		fmt.Println(i)
		i++

	}

	// EXTRA
	// / Slice of cryptocurrency names
	cryptocurrencies := []string{"Bitcoin", "Ethereum", "Tether", "Binance Coin", "Solana", "USD Coin", "XRP", "Dogecoin", "TRON", "Toncoin"}

	// Slice of corresponding values
	prices := []float64{57732.00, 2341.66, 1.00, 543.83, 134.33, 1.00, 0.57, 0.10, 0.09, 5.40}

	for k, i := range cryptocurrencies {
		fmt.Printf(" Index %v : Crypto: %v\n", k+1, i)
	}

	// crear mapacon los dos slice
	cryptoMap := map[string]float64{}

	for k, i := range cryptocurrencies {
		cryptoMap[i] = prices[k]
	}

	for k, v := range cryptoMap {
		fmt.Printf(" Crypto %v : Value: %v\n", k, v)
	}
}
