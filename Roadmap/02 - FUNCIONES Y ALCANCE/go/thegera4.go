package main

import (
	"fmt"
	"strconv"
)

var global = "Soy una variable global"

func main() {

	Sayhi()

	fmt.Println(Outputname("Gera"))

	fmt.Println(Twoparams(1, 2))

	fmt.Println(Doubleamounts(2))

	fmt.Println(Comporobartipo(2))

	Scope()

	extra := Extra("Fizz", "Buzz")

	fmt.Println("El numero de veces que se imprimieron numeros fue: ", extra)

}

// Funcion basica, sin parametros ni retorno
func Sayhi() {
	fmt.Println("Hola mundo")
}

// Funcion con un parametro con retorno
func Outputname(name string) string {
	//return a string with the name injected
	return "Hola usuario " + name
}

// Funcion con parametros y retorno
func Twoparams(param1 int, param2 int) int {
	return param1 + param2
}

// Funcion adentro de otra funcion
func Doubleamounts(amount1 int) int {
	//funcion anonima
	Multiplyby := func (number int) int {
		return number * 2
	}
	return Multiplyby(amount1)
}

// Funcion ya creada en el lenguaje
func Comporobartipo(param int) string {
	return `El valor de param es ` + strconv.Itoa(param) + ` y el tipo es ` + fmt.Sprintf("%T", param)
}

// Funcion para probar el scope de las variables
func Scope() {
	//variable local
	var local = "Soy una variable local"
	fmt.Println(local)
	fmt.Println(global)
}

// Dificultad extra
func Extra(str1 string, str2 string) int {
	count := 0
	for i := 1; i <= 100; i++ {
		if i % 3 == 0 && i % 5 == 0 {
			fmt.Println(str1 + str2)
		} else if i % 3 == 0 {
			fmt.Println(str1)
		} else if i % 5 == 0 {
			fmt.Println(str2)
		} else {
			fmt.Println(i)
			count++
		}
	}
	return count
}