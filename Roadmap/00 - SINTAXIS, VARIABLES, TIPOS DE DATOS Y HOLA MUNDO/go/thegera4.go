// Web oficial de "GO" -> https://go.dev/
/* 
Comentario
en varias lineas 
*/

package main

import "fmt"

var isVariable bool = true 

const gravity float64 = 9.8

func main() {
	//hay muchos mas, pero estos son los mas comunes
	var nickname string = "thegera4"
	var age int = 36
	var weight float64 = 80.5
	
	/* 
	Alternativamente, se puede hacer lo siguiente:

	nickname := "thegera4"
	age := 36
	weight := 80.5
	
	Con esto GO infiere el tipo de dato de la variable, en este caso, string, int y float64
	y tambien inicializa la variable con el valor asignado
	*/

	fmt.Println("¡Hola, GO!")
	fmt.Printf("Mi nombre es %s, tengo %d años y peso %.2f kg\n", nickname, age, weight)

}