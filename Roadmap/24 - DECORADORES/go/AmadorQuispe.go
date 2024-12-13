package main

import "fmt"

type ICoffee interface {
	getPrice() uint
}

type CoffeeSimple struct{}

func (c *CoffeeSimple) getPrice() uint {
	return 25
}

type CoffeeWithMilk struct {
	coffee ICoffee
}

func (c *CoffeeWithMilk) getPrice() uint {
	additional := 5
	return c.coffee.getPrice() + uint(additional)
}

type CoffeeWithSugar struct {
	coffee ICoffee
}

func (c *CoffeeWithSugar) getPrice() uint {
	additional := 2
	return c.coffee.getPrice() + uint(additional)
}

//EXTRA
type CoffeeWithCounting struct {
	coffee ICoffee
	count  uint
}

func (c *CoffeeWithCounting) getPrice() uint {
	c.count++
	return c.coffee.getPrice()
}

func main() {
	//Coffee Simple
	coffee := &CoffeeSimple{}
	fmt.Println("Price coffee normal", coffee.getPrice())
	//Add Milk
	coffeeWithMilk := CoffeeWithMilk{
		coffee: coffee,
	}
	fmt.Println("Price coffee with milk", coffeeWithMilk.getPrice())
	//Add sugar
	coffeeWithSugar := CoffeeWithSugar{
		coffee: &coffeeWithMilk,
	}
	fmt.Println("Price coffee with milk and sugar", coffeeWithSugar.getPrice())
	//Add  counting calls
	coffeeWithCounting := CoffeeWithCounting{
		coffee: &coffeeWithSugar,
	}
	coffeeWithCounting.getPrice()
	coffeeWithCounting.getPrice()
	coffeeWithCounting.getPrice()
	fmt.Println("getPrice method has been called ", coffeeWithCounting.count)

}
