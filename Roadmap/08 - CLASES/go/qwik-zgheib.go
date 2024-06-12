package main

import (
	"fmt"
)

/* -- exercise */
type Programmer struct {
	Name      string
	Surname   string
	Age       int
	Languages []string
}

func NewProgrammer(name string, age int, languages []string) *Programmer {
	return &Programmer{
		Name:      name,
		Age:       age,
		Languages: languages,
	}
}

func (p *Programmer) Print() {
	fmt.Printf("Name: %s | Surname: %s | Age: %d | Languages: %v\n", p.Name, p.Surname, p.Age, p.Languages)
}

/* -- stack */
type Stack struct {
	items []string
}

func NewStack() *Stack {
	return &Stack{items: []string{}}
}

func (s *Stack) Push(item string) {
	s.items = append(s.items, item)
}

func (s *Stack) Pop() string {
	if s.Count() == 0 {
		return ""
	}
	item := s.items[s.Count()-1]
	s.items = s.items[:s.Count()-1]
	return item
}

func (s *Stack) Count() int {
	return len(s.items)
}

func (s *Stack) Print() {
	for i := len(s.items) - 1; i >= 0; i-- {
		fmt.Println(s.items[i])
	}
}

/* queue */
type Queue struct {
	items []string
}

func NewQueue() *Queue {
	return &Queue{items: []string{}}
}

// Enqueue adds an item to the queue.
func (q *Queue) Enqueue(item string) {
	q.items = append(q.items, item)
}

func (q *Queue) Dequeue() string {
	if q.Count() == 0 {
		return ""
	}
	item := q.items[0]
	q.items = q.items[1:]
	return item
}

func (q *Queue) Count() int {
	return len(q.items)
}

func (q *Queue) Print() {
	for _, item := range q.items {
		fmt.Println(item)
	}
}
func main() {
	myProgrammer := NewProgrammer("Qwik", 36, []string{"Go", "Python", "Typescript"})
	myProgrammer.Print()
	myProgrammer.Surname = "Zgheib"
	myProgrammer.Print()
	myProgrammer.Age = 37
	myProgrammer.Print()

	myStack := NewStack()
	myStack.Push("A")
	myStack.Push("B")
	myStack.Push("C")
	fmt.Println(myStack.Count())
	myStack.Print()
	myStack.Pop()
	fmt.Println(myStack.Count())
	fmt.Println(myStack.Pop())
	fmt.Println(myStack.Pop())
	fmt.Println(myStack.Pop())
	fmt.Println(myStack.Pop())
	fmt.Println(myStack.Count())

	myQueue := NewQueue()
	myQueue.Enqueue("A")
	myQueue.Enqueue("B")
	myQueue.Enqueue("C")
	fmt.Println(myQueue.Count())
	myQueue.Print()
	myQueue.Dequeue()
	fmt.Println(myQueue.Count())
	fmt.Println(myQueue.Dequeue())
	fmt.Println(myQueue.Dequeue())
	fmt.Println(myQueue.Dequeue())
	fmt.Println(myQueue.Dequeue())
	fmt.Println(myQueue.Count())
}
