package main

import "fmt"

func main() {
	// Utilizando lopp
	for i := 1; i <= 10; i++ {
		fmt.Println(i)
	}
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	for _, num := range nums {
		fmt.Println(num)
	}
	i := 1
	for i <= 10 {
		fmt.Println(i)
		i++
	}
}
