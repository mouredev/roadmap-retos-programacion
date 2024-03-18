package main

import (
	"errors"
	"fmt"
)

func divide(a int, b int) (int, error) {
	if b == 0 {
		var errorMessage string = fmt.Sprintf("Can't divide %d by %d value!", a, b)
		return 0, errors.New(errorMessage)
	}

	return a / b, nil
}

func at[T any](array *[]T, index int) (T, error) {
	var arrayLength int = len(*array)
	if arrayLength <= index {
		var emptyValue T
		var errorMessage string = fmt.Sprintf("Index out of range! It must be less than %d.", index)
		return emptyValue, errors.New(errorMessage)
	}

	return (*array)[index], nil
}
func main() {

	result, err := divide(10, 0)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(result)
	}

	// Ejemplo de acceso fuera de rango
	var array []int = []int{1, 2, 3, 4, 5}
	result, err = at(&array, 10)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(result)
	}
}
