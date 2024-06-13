package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func swapByValue(x, y int) {
	x, y = y, x
}

func swapByReference(a, b *int) {
	*a, *b = *b, *a
}

func incrementByValue(num int) {
	num += 10
}

func changeNameByReference(p *Person) {
	p.Name = "qwik"
}

func main() {
	x := 10
	y := x
	y = 20

	fmt.Println("variables by value:")
	fmt.Println("x:", x)
	fmt.Println("y:", y)

	slice1 := []int{1, 2, 3}
	slice2 := slice1

	slice2[0] = 100

	fmt.Println("\nvariables by reference:")
	fmt.Println("slice1:", slice1)
	fmt.Println("slice2:", slice2)

	num := 5
	incrementByValue(num)
	fmt.Println("\nafter calling incrementByValue:", num)

	/* Extra exercise */
	person := Person{Name: "Abdul", Age: 30}
	changeNameByReference(&person)
	fmt.Println("\nafter calling changeNameByReference:", person)
	p, q := 10, 20
	swapByValue(p, q)
	fmt.Println("exchange for value:")
	fmt.Println("p:", p)
	fmt.Println("q:", q)

	a, b := 30, 40
	swapByReference(&a, &b)
	fmt.Println("\nexchange by reference:")
	fmt.Println("a:", a)
	fmt.Println("b:", b)
}
