package main

import "fmt"

func main() {

	//stack
	stack := []string{"javascript", "php"}

	stack = append([]string{"go"}, stack...)
	fmt.Println(stack)

	stack = stack[1:]
	fmt.Println(stack)

	// queue

	queue := []string{"mongo", "mysql"}

	queue = append(queue, "postgres")
	fmt.Println(queue)

	queue = queue[1:]
	fmt.Println(queue)
}
