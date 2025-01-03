package main

import (
	"errors"
	"fmt"
	"strconv"
)

//De manera general, GO representa cualquier tipo de error mediante la interfaz error:

func main() {
	//División por cero
	if res, err := divideTwoNumbers(10, 0); err == nil {
		fmt.Println(res)
	} else {
		fmt.Println(err)
	}

	//Indice fuera de rango
	numbers := []int{1, 2, 3, 4, 5, 6}
	val, err := getElementByIndex(numbers, 6)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(val)

	}

	//Error personalizado
	result, err := divisionPositive(-34, 3)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(result)
	}
}

func divideTwoNumbers(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("cannot divide by zero")
	}
	return a / b, nil
}

func getElementByIndex[T any](slice []T, i int) (T, error) {
	if len(slice) >= i {
		var zeroValue T
		return zeroValue, errors.New("index of range! it must be less than " + strconv.Itoa(i))
	}
	return slice[i], nil
}

type CustomError struct {
	msg string
}

func (ce *CustomError) Error() string {
	return ce.msg
}

func divisionPositive(numerator, denominator int) (int, error) {
	if numerator < 0 || denominator < 0 {
		return 0, &CustomError{msg: "not valid numbers negatives"}
	}
	return numerator / denominator, nil
}
