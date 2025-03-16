package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Callback func(int) int

// process is a function that takes an integer n and a Callback function as parameters.
// It executes the Callback function with the provided integer n and prints the result.
//
// Parameters:
// - n: An integer value that will be passed to the Callback function.
// - callback: A Callback function that takes an integer as a parameter and returns an integer.
//
// Return values:
// - None
func process(n int, callback Callback) {
	result := callback(n)
	fmt.Println("result: ", result)
}

func multiplyByTwo(n int) int {
	return n * 2
}

// -- extra challenge

type ConfirmCallback func(orderID int, dish string)
type ReadyCallback func(orderID int, dish string)
type DeliverCallback func(orderID int, dish string)

type OrderProcessor struct{}

func NewOrderProcessor() *OrderProcessor {
	return &OrderProcessor{}
}

func (op *OrderProcessor) ProcessOrder(orderID int, dish string, confirm ConfirmCallback, ready ReadyCallback, deliver DeliverCallback) {
	confirm(orderID, dish)
	time.Sleep(time.Duration(rand.Intn(10)+1) * time.Second)

	ready(orderID, dish)
	time.Sleep(time.Duration(rand.Intn(10)+1) * time.Second)

	deliver(orderID, dish)
}

func main() {
	number := 5
	process(number, multiplyByTwo)
	process(number, func(n int) int {
		return n + 10
	})

	// -- extra challenge
	rand.New(rand.NewSource(time.Now().UnixNano()))

	// Callbacks
	confirm := func(orderID int, dish string) {
		fmt.Printf("Order #%d: Confirmed dish %s\n", orderID, dish)
	}

	ready := func(orderID int, dish string) {
		fmt.Printf("Order #%d: Dish %s is ready\n", orderID, dish)
	}

	deliver := func(orderID int, dish string) {
		fmt.Printf("Order #%d: Dish %s has been delivered\n", orderID, dish)
	}

	orderProcessor := NewOrderProcessor()

	orderProcessor.ProcessOrder(1, "Pizza Margherita", confirm, ready, deliver)
	orderProcessor.ProcessOrder(2, "Spaghetti Carbonara", confirm, ready, deliver)
}
