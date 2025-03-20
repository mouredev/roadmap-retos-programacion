package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	response, err := http.Get("https://httpbin.org/get")

	if err != nil {
		fmt.Println("Error al realizar la petición HTTP Get")
	}

	defer response.Body.Close()

	if response.StatusCode == 200 {
		body, err := io.ReadAll(response.Body)

		if err != nil {
			fmt.Println("Error al leer el contenido del cuerpo de la petición")
		}

		fmt.Println(string(body))
	}
}
