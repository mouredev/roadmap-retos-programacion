/*
		Ejercicio
		Crea ejemplos de funciones básicas que representen las diferentes
	    posibilidades del lenguaje:
	    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
		Comprueba si puedes crear funciones dentro de funciones.
		Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
		Pon a prueba el concepto de variable LOCAL y GLOBAL.
		Debes hacer print por consola del resultado de todos los ejemplos.
	    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
*/
package main

import "fmt"

func main(){
	greetUser1()
	greetUser2("Aldo")
	fmt.Printf("%v,\n",greetUser3("Emmanuel"))
	fmt.Println(operations(3,4))
	extra("Fizz","Buzz")
}

func greetUser1(){
	fmt.Println("Welcome to this language")
}

func greetUser2(name string){
	fmt.Printf("Hola, %v \n", name)
}

func greetUser3(name string)(string){
	return "Hola "+ name
}

func operations(a, b int)(int,int){
	add := func()int{
		return a+b
	}
	sub := func()int{
		return a-b
	}
	return add(), sub()
}

func extra(param1, param2 string)int{
	var numImpreso = 0
	for i:=1; i<101; i++{
		if i%5==0{
			fmt.Println(param1,param2)
		} else if i%3==0{
			fmt.Println(param1)
		}else if i%5 ==0{
			fmt.Println(param2)
		}else{
			fmt.Println(i)
			numImpreso++
		}
	}
	return numImpreso
}