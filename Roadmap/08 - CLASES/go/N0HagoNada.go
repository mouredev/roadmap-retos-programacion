package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Stack struct {
	elements []string
}

func (s *Stack) Push(elem string) {
	s.elements = append(s.elements, elem)
}

func (s *Stack) Pop() (string, bool) {
	if len(s.elements) == 0 {
		return "", false
	}
	lastIndex := len(s.elements) - 1
	elem := s.elements[lastIndex]
	s.elements = s.elements[:lastIndex]
	return elem, true
}

type WebBrowser struct {
	history Stack
	forward Stack
	current string
}

func (wb *WebBrowser) Visit(page string) {
	if wb.current != "" {
		wb.history.Push(wb.current)
	}
	wb.current = page    // Set the current page
	wb.forward = Stack{} // Clear forward stack
}

func (wb *WebBrowser) Back() (string, bool) {
	if page, ok := wb.history.Pop(); ok {
		wb.forward.Push(wb.current)
		wb.current = page
		return page, true
	}
	return "", false
}

func (wb *WebBrowser) Forward() (string, bool) {
	if page, ok := wb.forward.Pop(); ok {
		wb.history.Push(wb.current)
		wb.current = page
		return page, true
	}
	return "", false
}

func (wb *WebBrowser) CurrentPage() string {
	return wb.current
}

func main() {
	wb := WebBrowser{}
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Web Browser Simulator")
	for {
		fmt.Print("Enter a URL, 'atras', 'adelante', or 'exit' to navigate: ")
		scanner.Scan()
		input := strings.TrimSpace(scanner.Text())

		switch input {
		case "atras":
			if page, ok := wb.Back(); ok {
				fmt.Println("Moved back to:", page)
			} else {
				fmt.Println("No more history.")
			}
		case "adelante":
			if page, ok := wb.Forward(); ok {
				fmt.Println("Moved forward to:", page)
			} else {
				fmt.Println("No pages to move forward to.")
			}
		case "exit":
			fmt.Println("Exiting Web Browser Simulator.")
			return
		default:
			wb.Visit(input)
			fmt.Println("Visited:", wb.CurrentPage())
		}
	}
}
