package main

import "fmt"

func main() {
	numbers := []int{1, 2, 3, 4, 5}

	process(numbers, printNumber)
}

func process(numbers []int, callback func(int)) {
	for _, num := range numbers {
		callback(num)
	}
}

func printNumber(num int) {
	fmt.Println(num)
}
