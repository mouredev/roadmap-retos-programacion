package main

import "fmt"

func main() {
	var animal Animal = Animal{"bob"}
	var dog Dog = Dog{animal, "black"}

	animal.MakeSound()
	dog.MakeSound()
}

type Animal struct {
	Name string
}

func (a *Animal) MakeSound() {
	fmt.Println("Some generic animal sound")
}

type Dog struct {
	Animal
	color string
}

type Cat struct {
	Animal
	color string
}
