package main

import "fmt"

func main() {
	// Mecanismo 1
	for i := 1; i <= 10; i++ {
		fmt.Println(i)
	}

	// Mecanismo 2
	i := 1
	for i <= 10 {
		fmt.Println(i)
		i++
	}

	// Mecanismo 3
	for _, i := range []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} {
		fmt.Println(i)
	}

	//Extra
	// Mecanismo 4
	i = 1
	for {
		fmt.Println(i)
		i++
		if i > 10 {
			break
		}
	}

	// Mecanismo 5
	i = 1
	for {
		if i > 10 {
			break
		}
		fmt.Println(i)
		i++
	}

}