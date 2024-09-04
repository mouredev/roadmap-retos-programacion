package main

import "fmt"

func ClassicForLoop() {
	for i := 1; i <= 10; i++ {
		fmt.Println(i)
	}
}

func ConditionalForLoop() {
	i := 1
	for i <= +10 {
		fmt.Println(i)
		i++
	}
}

func RangeForLoop() {
	s := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	for _, v := range s {
		fmt.Println(v)
	}
}

func RecursiveForLoop(n int) {
	if n > 10 {
		return
	}
	fmt.Println(n)
	RecursiveForLoop(n + 1)
}

func AnonymousForLoop() {
	(func(i int) {
		for i := 1; i <= 10; i++ {
			fmt.Println(i)
		}
	})(1)
}

func main() {
	fmt.Println("classic for loop")
	ClassicForLoop()

	fmt.Println("conditional for loop")
	ConditionalForLoop()
	
	fmt.Println("range for loop")
	RangeForLoop()
	
	fmt.Println("recursive for loop")
	RecursiveForLoop(1)
	
	fmt.Println("anonymous for loop")
	AnonymousForLoop()
}
