package main

import "fmt"

// types of operators
func typesOperators() {
	// aritmetics
	var a int = 10
	var b int = 20
	var c int
	c = a + b
	a += b
	fmt.Println("sum: ", c)

	// logical
	var x bool = true
	var y bool = false
	if x && y {
		println("logical: True")
	}

	// comparison
	if a == b {
		fmt.Println("comparison: True")
	}

	// assignment
	a = b
	fmt.Println("assignment: ", a)

	/* identity */
	var m int = 10
	var n int = 10
	if m == n {
		fmt.Println("identity: True")
	}

	// pertenence
	var numbers = [3]int{1, 2, 3}
	var number = 2
	for _, n := range numbers {
		if n == number {
			fmt.Println("pertenece: True")
		}
	}

	// bits
	var d int = 60
	var e int = 13
	c = d & e
	fmt.Println("bits: ", c)
}

// control structures
func controlStructures() error {
	// conditional
	var a int = 10
	if a > 5 {
		fmt.Println("conditional: True")
	}

	// iterative
	for i := 0; i < 5; i++ {
		fmt.Println("iterative: ", i)
	}

	// exception
	var b int = 0
	if b == 0 {
		return fmt.Errorf("exception: Error division by zero")
	}

	return nil
}

func exercise() {
	for i := 10; i <= 55; i++ {
		if i != 16 && i%3 != 0 {
			fmt.Println("exercise: ", i)
		}
	}
}

func main() {
	typesOperators()

	// exeption error
	err := controlStructures()
	if err != nil {
		fmt.Println(err)
	}

	exercise()
}
