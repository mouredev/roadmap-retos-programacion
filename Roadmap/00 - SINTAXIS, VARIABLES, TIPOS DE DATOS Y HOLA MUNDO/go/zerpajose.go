// https://go.dev/
/*
Comentarios multilinea
otra linea
otra linea
*/
package main

import "fmt"

func main() {
	var nombre string = "GO"
	edad := 25
	isLanguage := true
	fmt.Println("Hola", nombre)

	// GO no permite dejar variables sin usar
	fmt.Println(edad, isLanguage)
}
