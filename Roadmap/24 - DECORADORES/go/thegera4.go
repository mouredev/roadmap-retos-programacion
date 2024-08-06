package main

import (
	"fmt"
)

// El patrón de diseño Decorador es una forma elegante de agregar funcionalidad a un objeto existente 
// sin modificar su estructura. El Decorador permite envolver un objeto con otros objetos que agregan 
// responsabilidades adicionales.

type Drink interface {
    Cost() float64
    Description() string
}

type BlackCoffee struct{}

func (coffee *BlackCoffee) Cost() float64 {
    return 2.0
}

func (coffee *BlackCoffee) Description() string {
    return "Café negro"
}

// Decorador: Leche
type Milk struct {
    beverage Drink
}

func (milk *Milk) Cost() float64 {
    return milk.beverage.Cost() + 1.0
}

func (milk *Milk) Description() string {
    return milk.beverage.Description() + ", con leche"
}

// Decorador: Azúcar
type Sugar struct {
    beverage Drink
}

func (sugar *Sugar) Cost() float64 {
    return sugar.beverage.Cost() + 0.5
}

func (sugar *Sugar) Description() string {
    return sugar.beverage.Description() + ", con azúcar"
}

// Uso:
func main() {
    café := &BlackCoffee{}
    caféConLeche := &Milk{beverage: café}
    caféConLecheYAzúcar := &Sugar{beverage: caféConLeche}

	fmt.Println(café.Description())
	fmt.Println("Costo:", café.Cost())
	fmt.Println(caféConLeche.Description())
	fmt.Println("Costo:", caféConLeche.Cost())
    fmt.Println(caféConLecheYAzúcar.Description())
    fmt.Println("Costo total:", caféConLecheYAzúcar.Cost())

	// Extra:
	saludoConContador := NewFunctionCounter(Saludar)
	saludoConContador.Increment()
	saludoConContador.Increment()
	fmt.Println("Número de veces que se llama a Saludar:", saludoConContador.GetCount())

}

// Extra:
type Counter interface {
    Increment()
    GetCount() int
}

type FunctionCounter struct {
    fn    func()
    count int
}

func NewFunctionCounter(fn func()) *FunctionCounter {
    return &FunctionCounter{
        fn: fn,
    }
}

func (fc *FunctionCounter) Increment() {
    fc.count++
    fc.fn()
}

func (fc *FunctionCounter) GetCount() int {
    return fc.count
}

func Saludar() {
    fmt.Println("¡Hola, mundo!")
}