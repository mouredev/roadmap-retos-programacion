package main

import (
	"fmt"
)

type Greeter interface {
	Greet(name string) string
}

type SimpleGreeter struct{}

func (g SimpleGreeter) Greet(name string) string {
	return fmt.Sprintf("Hello, %s!", name)
}

type ExcitedDecorator struct {
	Greeter Greeter
}

func (e ExcitedDecorator) Greet(name string) string {
	return e.Greeter.Greet(name) + " How are you doing today?"
}

type AddGreetingCountDecorator struct {
	Greeter   Greeter
	CallCount int
}

func (c *AddGreetingCountDecorator) Greet(name string) string {
	c.CallCount++
	return c.Greeter.Greet(name)
}

func (c *AddGreetingCountDecorator) GetCallCount() int {
	return c.CallCount
}

func main() {
	greeter := SimpleGreeter{}

	excitedGreeter := ExcitedDecorator{Greeter: greeter}

	countingGreeter := &AddGreetingCountDecorator{Greeter: excitedGreeter}

	fmt.Println(countingGreeter.Greet("qwik"))
	fmt.Println(countingGreeter.Greet("zgheib"))
	fmt.Println(countingGreeter.Greet("mossad"))

	fmt.Printf("Greet method has been called %d times\n", countingGreeter.GetCallCount())
}
