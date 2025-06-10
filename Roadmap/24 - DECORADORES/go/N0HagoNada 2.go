package main

import (
	"fmt"
	"reflect"
	"runtime"
)

// Explorando el concepto de Decorador

// Interfaz del componente
type IPizza interface {
	getPrice() int
}

// Componente concreto
type VeggieMania struct {
}

func (p *VeggieMania) getPrice() int {
	return 12
}

// Decorador concreto
type TomatoTopping struct {
	pizza IPizza
}

func (c *TomatoTopping) getPrice() int {
	pizzaPrice := c.pizza.getPrice()
	return pizzaPrice + 7
}

// Decorador 2
type CheeseTopping struct {
	pizza IPizza
}

func (c *CheeseTopping) getPrice() int {
	pizzaPrice := c.pizza.getPrice()
	return pizzaPrice + 10
}

func main() {

	pizza := &VeggieMania{}

	//Añadir queso
	pizzaWithCheese := &CheeseTopping{
		pizza: pizza,
	}
	//Añadir tomate
	pizzaWithCheeseAndTomato := &TomatoTopping{
		pizza: pizzaWithCheese,
	}

	fmt.Printf("Price of veggeMania with tomato and cheese topping is %d\n", pizzaWithCheeseAndTomato.getPrice())
	fmt.Println("-------------------------------------- RETO ------------------------------------------------")
	// Aplicamos el decorador CountCalls a nuestra función de ejemplo ExampleFunction
	DecoratedFunction := CountCalls(ExampleFunction)

	// Llamamos a la función decorada varias veces para ver el conteo en acción
	DecoratedFunction(2, 3)
	DecoratedFunction(5, 7)
	DecoratedFunction(1, 1)
}

// **************** RETO **********************//

// Definimos un tipo de función que toma dos enteros y devuelve un entero
type ExampleFunc func(a, b int) int

// Definimos un tipo de función decoradora que también toma dos enteros y devuelve un entero
type DecoratedFunc func(a, b int) int

type AnyFunc func(...interface{}) []interface{}

func CountCalls(fn ExampleFunc) DecoratedFunc {
	callCount := make(map[string]int)

	// Devolvemos una nueva función que envuelve la función original
	return func(a, b int) int {
		// Obtenemos el nombre de la función original usando reflexión
		fnName := runtime.FuncForPC(reflect.ValueOf(fn).Pointer()).Name()

		// Incrementamos el contador de llamadas para esta función
		callCount[fnName]++

		// Imprimimos el mensaje de conteo
		fmt.Printf("Llamada a %s: %d veces\n", fnName, callCount[fnName])

		// Llamamos a la función original y devolvemos el resultado
		return fn(a, b)
	}
}

// Función de ejemplo a la cual aplicaremos el decorador
func ExampleFunction(a, b int) int {
	return a + b
}
