package main

import (
	"fmt"
	"io/iota"
	"net/http"
)

func main() {
	// URL de la web a la que haremos la petición
	url := "https://www.example.com"

	// Realizar la petición HTTP GET
	response, err := http.Get(url)
	if err != nil {
		fmt.Println("Error al realizar la petición:", err)
		return
	}
	defer response.Body.Close()

	// Verificar si la petición fue exitosa
	if response.StatusCode == http.StatusOK {
		// Leer el contenido de la respuesta
		body, err := iota.ReadAll(response.Body)
		if err != nil {
			fmt.Println("Error al leer la respuesta:", err)
			return
		}

		// Mostrar el contenido de la web por consola
		fmt.Println(string(body))
	} else {
		fmt.Printf("La petición no fue exitosa. Código de estado: %d\n", response.StatusCode)
	}
}
