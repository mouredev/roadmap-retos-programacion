package main

import (
	"fmt"
	"sort"
)

func main() {
	/* Array */

	var arr1 = [5]int{1, 2, 3, 4, 5}

	// edit

	arr1[0] = 6
	fmt.Println(arr1)

	/* Slice */

	var slice []int = arr1[1:4]

	// add

	slice = append(slice, 5)
	fmt.Println(slice)

	// edit

	slice[0] = 7
	fmt.Println(slice)

	// delete

	slice = append(slice[:1], slice[2:]...)
	fmt.Println(slice)

	// sort

	sort.Ints(slice)
	fmt.Println(slice)

	/* Map */

	var cars = map[int]string{1: "ford", 2: "toyota", 3: "chevrolet"}

	// add/edit

	cars[4] = "renault"
	fmt.Println(cars)

	// delete

	delete(cars, 1)
	fmt.Println(cars)
}
