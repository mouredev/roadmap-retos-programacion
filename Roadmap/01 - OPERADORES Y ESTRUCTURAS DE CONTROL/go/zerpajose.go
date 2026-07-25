package main

import (
	"errors"
	"fmt"
	"math"
)

func Accounting(f int, b int) (n int, err error) {
	if f < 0 {
		return 0, errors.New("Error")
	} else {
		return b, nil
	}
}

func main() {
	// EJERCICIO
	a := 1
	b := 2
	// ARIMETICOS
	fmt.Println("SUMA", a+b)
	fmt.Println("RESTA", a-b)
	fmt.Println("MULTIPLICACION", a*b)
	fmt.Println("DIVISION", a/b)
	fmt.Println("RESTO", a%b)

	// BITWISE
	fmt.Println("AND", 3&5)
	fmt.Println("OR", 3|5)
	fmt.Println("XOR", 3^5)
	fmt.Println("NOT", ^5)
	fmt.Println("AND NOT", 3&^5)
	fmt.Println("LEFT SHIFT", 53<<2)
	fmt.Println("LEFT SHIFT", 53>>2)

	// COMPARACION
	fmt.Println("IGUAL", 0 == 0)
	fmt.Println("DIFERENTE", 1 == 0)
	fmt.Println("MENOR QUE", 2 < 5)
	fmt.Println("MENOR O IGUAL", 2 <= 2)
	fmt.Println("MAYOR QUE", 5 > 2)
	fmt.Println("MAYOR O IGUAL", 5 >= 5)

	// LOGICOS
	fmt.Println("AND", true && true)
	fmt.Println("OR", true || false)
	fmt.Println("NOT", !false)

	// CONCATENACION DE STRINGS
	s := "hi " + "world"
	s += " and good bye"
	fmt.Println(s)

	// DECISION
	if s == "HI" {
		fmt.Println("HOLA")
	} else if s == "BYE" {
		fmt.Println("BYE")
	} else {
		fmt.Println("DEFAULT")
	}

	// SWITCH
	switch {
	case s == "hi world and good bye":
		fmt.Println("HOLA")
	case s == "HI":
		fmt.Println("HI")
	case s == "BYE":
		fmt.Println("BYE")
	default:
		fmt.Println("DEFAULT")
	}

	// FOR
	prints := [5]int{1, 2, 3, 4, 5}
	for i := 5; i >= 0; i-- {
		fmt.Println(i)
	}

	// FOR RANGE
	for _, p := range prints {
		fmt.Println(p)
	}

	// DIRECCION
	fmt.Println("POINTER ADDRESS", &s)
	var x *string = &s
	fmt.Println("POINTER VALUE", *x)

	// ERROR
	num1, err1 := Accounting(-1, 0)
	fmt.Println(err1, num1)
	num2, err2 := Accounting(1, 5)
	fmt.Println(err2, num2)

	// DIFICULTAD EXTRA
	fmt.Println("DIFICULTAD EXTRA")
	var count = 56

	for i := 10; i < count; i++ {
		var j float64 = float64(i)
		if (i%2 != 0) || (i == 16) || (math.Mod(j/3, 1) == 0) {
			continue
		}
		fmt.Print(i, " ")
	}
}
