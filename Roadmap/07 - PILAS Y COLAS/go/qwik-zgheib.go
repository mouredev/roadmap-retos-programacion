package main

import (
	"fmt"
)

// Stack defines the interface for a LIFO stack.
type Stack interface {
	Push(item string)
	Pop() (string, error)
	Print()
}

// Queue defines the interface for a FIFO queue.
type Queue interface {
	Enqueue(item string)
	Dequeue() (string, error)
	Print()
}

type StringStack struct {
	items []string
}

func NewStringStack() *StringStack {
	return &StringStack{items: []string{}}
}

func (s *StringStack) Push(item string) {
	s.items = append(s.items, item)
}

func (s *StringStack) Pop() (string, error) {
	if len(s.items) == 0 {
		return "", fmt.Errorf("stack is empty")
	}
	item := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return item, nil
}

func (s *StringStack) Print() {
	fmt.Println(s.items)
}

type StringQueue struct {
	items []string
}

func NewStringQueue() *StringQueue {
	return &StringQueue{items: []string{}}
}

func (q *StringQueue) Enqueue(item string) {
	q.items = append(q.items, item)
}

func (q *StringQueue) Dequeue() (string, error) {
	if len(q.items) == 0 {
		return "", fmt.Errorf("queue is empty")
	}
	item := q.items[0]
	q.items = q.items[1:]
	return item, nil
}

func (q *StringQueue) Print() {
	fmt.Println(q.items)
}

type WebNavigator struct {
	stack Stack
}

func NewWebNavigator(stack Stack) *WebNavigator {
	return &WebNavigator{stack: stack}
}

func (wn *WebNavigator) Navigate() {
	for {
		var action string
		fmt.Println("Enter a URL or type 'forward', 'back', or 'exit':")
		fmt.Scan(&action)
		switch action {
		case "exit":
			fmt.Println("Exiting web navigator.")
			return
		case "forward":
			fmt.Println("Forwarding to next page.")
			_, err := wn.stack.Pop()
			if err != nil {
				fmt.Println("No next pages.")
			}
		case "back":
			_, err := wn.stack.Pop()
			if err != nil {
				fmt.Println("No previous pages.")
			}
		default:
			wn.stack.Push(action)
		}
		wn.stack.Print()
	}
}

type SharedPrinter struct {
	queue Queue
}

func NewSharedPrinter(queue Queue) *SharedPrinter {
	return &SharedPrinter{queue: queue}
}

func (sp *SharedPrinter) PrintDocuments() {
	for {
		var action string
		fmt.Println("Add a document or type 'print' or 'exit':")
		fmt.Scan(&action)
		switch action {
		case "exit":
			return
		case "print":
			doc, err := sp.queue.Dequeue()
			if err != nil {
				fmt.Println("No documents to print.")
			} else {
				fmt.Printf("Printing: %s\n", doc)
			}
		default:
			sp.queue.Enqueue(action)
		}
		sp.queue.Print()
	}
}

func main() {
	stack := NewStringStack()
	stack.Push("1")
	stack.Push("2")
	stack.Push("3")
	stack.Print()
	item, _ := stack.Pop()
	fmt.Println("Popped item:", item)
	stack.Print()

	queue := NewStringQueue()
	queue.Enqueue("1")
	queue.Enqueue("2")
	queue.Enqueue("3")
	queue.Print()
	item, _ = queue.Dequeue()
	fmt.Println("Dequeued item:", item)
	queue.Print()

	webNavigator := NewWebNavigator(NewStringStack())
	webNavigator.Navigate()

	sharedPrinter := NewSharedPrinter(NewStringQueue())
	sharedPrinter.PrintDocuments()
}
