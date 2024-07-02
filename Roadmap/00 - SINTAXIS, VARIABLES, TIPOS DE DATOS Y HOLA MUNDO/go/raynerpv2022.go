package main

import "fmt"

func main() {
	// comentario

	/*
		comentario
		multiples
		lineas
	*/
	const language string = "gOlAng"
	VarInt := 10
	VarFloat := 10.486485688
	VarBool := true
	VarString := "esto es un String"
	fmt.Printf("Variable Entera : %d\n", VarInt)
	fmt.Printf("Variable Float : %.2f\n", VarFloat)
	fmt.Printf("Variable Boolean : %v\n", VarBool)
	fmt.Printf("ariable String : %s\n", VarString)
	fmt.Println("Hello " + language)

}
