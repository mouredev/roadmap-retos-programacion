package main

import (
	"errors"
	"fmt"
)

func divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("cannot divide by zero")
	}
	return a / b, nil
}

func accessElement(arr []int, index int) (int, error) {
	if index < 0 || index >= len(arr) {
		return 0, fmt.Errorf("index %d out of range", index)
	}
	return arr[index], nil
}

/* extra */
var (
	ErrDivideByZero    = errors.New("cannot divide by zero")
	ErrIndexOutOfRange = errors.New("index out of range")
	ErrCustom          = errors.New("custom error occurred")
)

type CustomError struct {
	Msg string
}

func (e *CustomError) Error() string {
	return e.Msg
}

func process(value int) error {
	if value == 0 {
		return ErrDivideByZero
	} else if value < 0 {
		return ErrIndexOutOfRange
	} else if value > 100 {
		return &CustomError{Msg: "value exceeds 100"}
	}
	return nil
}

func main() {
	result, err := divide(10, 0)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Result:", result)
	}
	fmt.Println("Execution finished.")

	arr := []int{1, 2, 3}
	element, err := accessElement(arr, 5)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Element:", element)
	}
	fmt.Println("Execution finished.")

	/* extra */
	values := []int{0, -1, 150, 50}

	for _, value := range values {
		err := process(value)
		if err != nil {
			switch err {
			case ErrDivideByZero:
				fmt.Println("Caught error:", err)
			case ErrIndexOutOfRange:
				fmt.Println("Caught error:", err)
			default:
				if customErr, ok := err.(*CustomError); ok {
					fmt.Println("Caught custom error:", customErr)
				} else {
					fmt.Println("Caught error:", err)
				}
			}
		} else {
			fmt.Println("No error occurred for value:", value)
		}
		fmt.Println("Execution finished for value:", value)
	}
}
