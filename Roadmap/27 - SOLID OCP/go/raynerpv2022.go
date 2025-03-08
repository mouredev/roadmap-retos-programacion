/*
#  * EJERCICIO:
#  * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
#  * y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
#  * Requisitos:
#  * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
#  * Instrucciones:
#  * 1. Implementa las operaciones de suma, resta, multiplicación y división.
#  * 2. Comprueba que el sistema funciona.
#  * 3. Agrega una quinta operación para calcular potencias.
#  * 4. Comprueba que se cumple el OCP.
#
*/
package main

import (
	"fmt"
	"math"
)

// incorrect

type Shape struct {
	a    float64
	b    float64
	area float64
	name string
}

func (s *Shape) Area() {
	if s.name == "rectangle" {
		s.area = s.a * s.b
	}
	if s.name == "triangle" {
		s.area = s.a * s.b / 2
	}
	if s.name == "square" {
		s.area = math.Pow((s.a), 2)
	}
}

func (s *Shape) Result() {
	fmt.Printf("Shape %v, Area %v\n", s.name, s.area)
}

// Correct

type AreaCalculator interface {
	Area()
	Result() // no debe serpero es como unico pincha
}

type BaseForm struct {
	area float64
	name string
}

type square struct {
	a float64
	BaseForm
}

func (s *square) Area() {
	s.area = math.Pow(s.a, 2)
}

type rectangle struct {
	a, b float64
	BaseForm
}

func (r *rectangle) Area() {
	r.area = r.a * r.b
}

type triangle struct {
	a, b float64
	BaseForm
}

func (t *triangle) Area() {
	t.area = t.a * t.b / 2
}

func (bf *BaseForm) Result() {
	fmt.Printf("Form %v, Area %v\n", bf.name, bf.area)
}

func (bf *BaseForm) Area() {
	// NO debe ser pero es como unico pincha
}

// Extra

type Operation interface {
	Execute(a, b float64) float64
}

type Sum struct{}

func (s *Sum) Execute(a, b float64) float64 {
	return a + b
}

type Rest struct{}

func (r *Rest) Execute(a, b float64) float64 {
	return a - b
}

type Mult struct{}

func (r *Mult) Execute(a, b float64) float64 {
	return a * b
}

type Dv struct{}

func (r *Dv) Execute(a, b float64) float64 {
	return a / b
}

type Pw struct{}

func (r *Pw) Execute(a, b float64) float64 {
	return math.Pow(a, b)
}

type Calculator struct {
	registry map[string]Operation
}

func (c *Calculator) Init() {
	c.registry = map[string]Operation{}

}

func (c *Calculator) Registry(key string, value Operation) {
	c.registry[key] = value

}

func (c *Calculator) Calculus(key string, a float64, b float64) float64 {
	v, ok := c.registry[key]
	if !ok {
		fmt.Printf(" Operation %v not yet allowed\n", key)
		return 0.0

	} else {
		return v.Execute(a, b)
	}

}

func main() {
	// falsch
	fmt.Println(("InCorrect"))
	shape := []Shape{
		{a: 12.0, b: 13.0, name: "rectangle"},
		{a: 11, b: 3, name: "triangle"},
		{a: 2, b: 2, name: "square"},
	}

	for _, v := range shape {
		v.Area()
		v.Result()

	}

	// Richtig
	fmt.Println(("Correct"))

	square := &square{a: 12, BaseForm: BaseForm{name: "square"}}
	triangle := &triangle{a: 2, b: 5, BaseForm: BaseForm{name: "triangle"}}
	rectangle := &rectangle{a: 5, b: 6, BaseForm: BaseForm{name: "rectangle"}}

	form := []AreaCalculator{square, triangle, rectangle}

	for _, i := range form {
		i.Area()
		i.Result()
	}

	// extra
	fmt.Println("EXTRA")
	calculator := Calculator{}
	calculator.Init()

	calculator.Registry("+", &Sum{})
	calculator.Registry("-", &Rest{})
	calculator.Registry("*", &Mult{})
	calculator.Registry("/", &Dv{})
	calculator.Registry("^", &Pw{})

	fmt.Println(calculator.Calculus("+", 20, 40))
	fmt.Println(calculator.Calculus("-", 20, 40))
	fmt.Println(calculator.Calculus("*", 20, 40))
	fmt.Println(calculator.Calculus("/", 20, 40))
	fmt.Println(calculator.Calculus("^", 20, 4))
}
