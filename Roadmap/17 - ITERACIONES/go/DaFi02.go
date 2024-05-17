package main

import "fmt"

func count(n int, limit int) {
	if n <= limit {
		fmt.Println(n)
		count(n+1, limit)
	}
}

func main() {

	limit := 10
	i := 1

	// First Method
	fmt.Println("First Method...")
	for ; i <= limit; i++ {
		fmt.Println(i)
	}

	i = 1

	fmt.Println("----------------------------------------------------------------------------------")
	// Second Method
	fmt.Println("\nSecond Method...")
	fmt.Println("Recursive Function...")

	count(i, limit)

	fmt.Println("----------------------------------------------------------------------------------")
	// Third Mehtod
	fmt.Println("\nThird Method")
	fmt.Println("Anonymous Recursive Function")

	var countAnon func(n int, limit int)
	countAnon = func(n int, limit int) {
		if n <= limit {
			fmt.Println(n)
			countAnon(n+1, limit)
		}
	}
	countAnon(i, limit)

}
