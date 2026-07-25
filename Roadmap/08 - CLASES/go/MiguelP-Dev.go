package main

import "fmt"

// Golang no posee clases pero si posee estructuras, que son similares.
// programmer es una estructura que contiene los atributos de un programador.
type programmer struct {
	name      string
	age       uint8
	languages []string
}

func newProgrammer(name string, age uint8, languages []string) *programmer {
	return &programmer{
		name:      name,
		age:       age,
		languages: languages,
	}
}

func printLanguages(p programmer) {
	text := "Languages used: "
	for _, lang := range p.languages {
		text += lang + ", "
	}
	fmt.Println(text[:len(text)-2])
}

func (p *programmer) updateAge(newAge uint8) {
	p.age = newAge
}

var one = programmer{}

// Extra : Stack and Queue
type stack struct {
	items []int
}

func (s *stack) push(item int) {
	s.items = append(s.items, item)
}

func (s *stack) pop() int {
	if len(s.items) == 0 {
		fmt.Println("Stack is empty")
		return -1
	}

	item := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return item
}

type queue struct {
	items []int
}

func (s *queue) push(item int) {
	s.items = append(s.items, item)
}

func (s *queue) pop() int {
	if len(s.items) == 0 {
		fmt.Println("Queue is empty")
		return -1
	}

	item := s.items[0]
	s.items = s.items[1:]
	return item
}

func main() {
	one.languages = append(one.languages, "golang")
	one.name = "miguel"
	one.age = 31
	fmt.Println("First: ", one)
	one.age = 32
	fmt.Println("Updated: ", one)
	printLanguages(one)
	fmt.Println("Programmer: ", newProgrammer("Miguel", 31, []string{"golang"}))
	one.updateAge(33)
	fmt.Println("Updating age with method: ", one.age)

	// Example about stack and queue using structures instead of classes.
	// stack
	myStack := new(stack)
	myStack.push(1)
	myStack.push(2)
	myStack.push(3)
	fmt.Println("Stack: ", myStack)
	myStack.pop()
	myStack.pop()
	myStack.pop()
	myStack.pop()
	fmt.Println("Stack: ", myStack)

	// queue
	myQueue := new(queue)
	myQueue.push(1)
	myQueue.push(2)
	myQueue.push(3)
	fmt.Println("Queue: ", myQueue)
	myQueue.pop()
	myQueue.pop()
	myQueue.pop()
	myQueue.pop()
	fmt.Println("Queue: ", myQueue)

}
