package main

import (
	"errors"
	"fmt"
)

/* -------------------------------------------------------------------------- */
/*                                PHONE (CLASS)                               */
/* -------------------------------------------------------------------------- */

// Attributes
type Phone struct {
	_brand string
	_name  string
	_price float32
}

// Constructor
func NewPhone(brand string, name string, price float32) *Phone {
	var phone Phone = Phone{
		_brand: brand,
		_name:  name,
		_price: price,
	}

	return &phone
}

// Setters
func (phone *Phone) setBrand(brand string) *Phone {
	phone._brand = brand
	return phone
}

func (phone *Phone) setName(name string) *Phone {
	phone._name = name
	return phone
}

func (phone *Phone) setPrice(price float32) *Phone {
	phone._price = price
	return phone
}

// Getters
func (phone *Phone) getBrand() string {
	return phone._brand
}

func (phone *Phone) getName() string {
	return phone._name
}

func (phone *Phone) getPrice() float32 {
	return phone._price
}

// Methods
func (phone *Phone) printAttributes() {
	fmt.Printf("\nBrand --> %s\n", phone._brand)
	fmt.Printf("Name --> %s\n", phone._name)
	fmt.Printf("Price --> $%0.2f\n", phone._price)
}

/* -------------------------------------------------------------------------- */
/*                                STACK (CLASS)                               */
/* -------------------------------------------------------------------------- */

type Stack[T any] struct {
	_lastElement T
	_length      int
	_stack       []T
}

func newStack[T any](stack []T) *Stack[T] {
	var nStack Stack[T] = Stack[T]{
		_length:      len(stack),
		_lastElement: stack[len(stack)-1],
		_stack:       stack,
	}

	return &nStack
}

func (stack *Stack[T]) getLastElement() (T, error) {
	var lastElementError error
	if stack.getLength() <= 0 {
		lastElementError = errors.New("Stack empty")
	}

	return stack._lastElement, lastElementError
}

func (stack *Stack[T]) getLength() int {
	return stack._length
}

func (stack *Stack[T]) getStack() []T {
	return stack._stack
}

func (stack *Stack[T]) appendElement(element T) *Stack[T] {
	stack._stack = append(stack._stack, element)
	stack._lastElement = element
	stack._length = len(stack._stack)
	return stack
}

func (stack *Stack[T]) deleteLastElement() *Stack[T] {
	var stackLength int = stack.getLength()

	if stackLength == 1 {
		stack._length = stackLength - 1
		stack._stack = []T{}
	} else if stackLength > 1 {
		stack._lastElement = stack._stack[stackLength-2]
		stack._length = stackLength - 1
		stack._stack = stack._stack[:stackLength-1]
	}

	return stack
}

func (stack *Stack[T]) printAttributes() *Stack[T] {
	fmt.Printf("\nLast element --> %v\n", stack._lastElement)
	fmt.Printf("Length --> %d\n", stack._length)
	fmt.Printf("Stack --> %v\n", stack._stack)
	return stack
}

/* -------------------------------------------------------------------------- */
/*                                QUEUE (CLASS)                               */
/* -------------------------------------------------------------------------- */

type Queue[T any] struct {
	_firstElement T
	_length       int
	_queue        []T
}

func newQueue[T any](queue []T) *Queue[T] {
	var nQueue Queue[T] = Queue[T]{
		_firstElement: queue[0],
		_length:       len(queue),
		_queue:        queue,
	}

	return &nQueue
}

func (queue *Queue[T]) getFirstElement() (T, error) {
	var firstElementError error
	if queue.getLength() <= 0 {
		firstElementError = errors.New("Queue empty")
	}

	return queue._firstElement, firstElementError
}

func (queue *Queue[T]) getLength() int {
	return queue._length
}

func (queue *Queue[T]) getQueue() []T {
	return queue._queue
}

func (queue *Queue[T]) appendElement(element T) *Queue[T] {
	queue._queue = append(queue._queue, element)
	queue._length = len(queue._queue)
	return queue
}

func (queue *Queue[T]) deleteFirstElement() *Queue[T] {
	var queueLength int = queue.getLength()
	if queueLength == 1 {
		queue._length = 0
		queue._queue = []T{}
	} else if queueLength > 1 {
		queue._queue = queue._queue[1:]
		queue._firstElement = queue._queue[0]
		queue._length = queue._length - 1
	}

	return queue
}

func (queue *Queue[T]) printAttributes() *Queue[T] {
	fmt.Printf("\nLength --> %d\n", queue._length)
	fmt.Printf("First element --> %v\n", queue._firstElement)
	fmt.Printf("Queue --> %v\n", queue._queue)
	return queue

}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
	   Classes...
	*/

	fmt.Println("Classes in TypeScript...")

	var phone *Phone = NewPhone("Samsung", "A5 2015", 150000)

	fmt.Println("\nPhone attributes...")
	phone.printAttributes()

	phone.setBrand("Apple").setName("iPhone 15 Pro Max").setPrice(300000)

	fmt.Println("\nPhone attributes...")
	phone.printAttributes()

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
	   Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	// Stack exercise...
	var stack *Stack[string] = newStack[string]([]string{"Lucas", "Hoz", "Buenos Aires"})

	fmt.Println("\nStack attributes...")
	stack.printAttributes()

	stack.appendElement("Argentina")

	fmt.Println("\nStack attributes...")
	stack.printAttributes()

	stack.deleteLastElement().deleteLastElement()

	fmt.Println("\nStack attributes...")
	stack.printAttributes()

	stack.deleteLastElement().deleteLastElement()

	fmt.Println("\nStack attributes...")
	stack.printAttributes()

	// Queue exercise...
	var queue *Queue[string] = newQueue[string]([]string{"América", "América Latina", "América del Sur"})

	fmt.Println("\nQueue attributes...")
	queue.printAttributes()

	queue.appendElement("Argentina")

	fmt.Println("\nQueue attributes...")
	queue.printAttributes()

	queue.deleteFirstElement().deleteFirstElement()
	fmt.Println("\nQueue attributes...")
	queue.printAttributes()

	queue.deleteFirstElement().deleteFirstElement().deleteFirstElement()

	fmt.Println("\nQueue attributes...")
	queue.printAttributes()

}
