package main

import "fmt"

//Documentacipn en http://go.dev/

//Comentario en una linea
/*
Comentario
en
varias
lineas
*/

const Pi float64 = 3.1416
var language string = "Golang"

func main(){
	var age int = 39
	var name string = "Aldo"
	var isDev bool = true
	var nota float64 = 9.3
	fmt.Println("Hello, " + language)
	fmt.Printf("Hola soy %v, tengo %v años, mi nota mas alta es %v, %v!",age, name, nota, isDev)
}