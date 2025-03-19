package main

import (
	"errors"
	"fmt"
)

func main() {
	//operadores aritmeticos
	var a, b int = 10, 5
	var c int = a + b
	fmt.Println("suma: ", c)
	c = a - b
	fmt.Println("resta: ", c)
	c = a * b
	fmt.Println("multiplicacion: ", c)
	c = a / b
	fmt.Println("division: ", c)
	c = a % b
	fmt.Println("modulo: ", c)
	a++
	fmt.Println("incremento: ", a)
	b--
	fmt.Println("decremento: ", b)

	//operadores de asignacion
	var d int = 10
	d += 5
	fmt.Println("suma: ", d)
	d -= 5
	fmt.Println("resta: ", d)
	d *= 5
	fmt.Println("multiplicacion: ", d)
	d /= 5
	fmt.Println("division: ", d)
	d %= 5
	fmt.Println("modulo: ", d)

	//operadores de comparacion
	var e, f int = 10, 5
	fmt.Println("e == f: ", e == f)
	fmt.Println("e != f: ", e != f)
	fmt.Println("e > f: ", e > f)
	fmt.Println("e < f: ", e < f)
	fmt.Println("e >= f: ", e >= f)
	fmt.Println("e <= f: ", e <= f)

	//operadores logicos
	var g, h bool = true, false
	fmt.Println("g && h: ", g && h)
	fmt.Println("g || h: ", g || h)
	fmt.Println("!g: ", !g)
	fmt.Println("!h: ", !h)

	//operadores de bits
	var i, j uint8 = 10, 5
	fmt.Println("i & j: ", i&j)
	fmt.Println("i | j: ", i|j)
	fmt.Println("i ^ j: ", i^j)
	fmt.Println("i << 1: ", i<<1)
	fmt.Println("i >> 1: ", i>>1)

	//operadores de punteros
	var k int = 10
	var l *int
	l = &k
	fmt.Println("k: ", k)
	fmt.Println("l: ", l)
	fmt.Println("*l: ", *l)

	//operadores de canales
	var m chan int = make(chan int, 1)
	m <- 10
	fmt.Println("m: ", m)
	fmt.Println("<-m: ", <-m)

	//condicionales
	if(10 > 5) {
		fmt.Println("10 es mayor que 5")
	} else if (10 < 5) {
		fmt.Println("10 es menor que 5")
	} else {
		fmt.Println("10 es igual a 5")
	}

	var n int = 10
	switch n {
		case 10:
			fmt.Println("n es igual a 10")
		case 5:
			fmt.Println("n es igual a 5")
		default:
			fmt.Println("n no es igual a 10 ni a 5")
	}

	//ciclos
	for i := 0; i < 10; i++ {
		fmt.Println("i: ", i)
	}

	var o int = 0
	for o < 10 {
		fmt.Println("o: ", o)
		o++
	}

	var p int = 0
	for {
		if p == 10 {
			break
		}
		fmt.Println("p: ", p)
		p++
	}

	var q int = 0
	for q < 10 {
		if q == 5 {
			q++
			continue
		}
		fmt.Println("q: ", q)
		q++
	}

	var r int = 0
	for r < 10 {
		if r == 5 {
			errors.New("r es igual a 5")
		}
		fmt.Println("r: ", r)
		r++
	}

	dificultadExtra()
}

func dificultadExtra() {
	for i := 10; i <= 55; i++ {
		if i % 3 == 0 {
			continue
		} else if i == 16 {
			continue
		} else {
			fmt.Println(i)
		}
	}
}