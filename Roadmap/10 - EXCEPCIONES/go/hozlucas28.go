package main

import (
	"errors"
	"fmt"
)

/* -------------------------------------------------------------------------- */
/*                                ERROR (CLASS)                               */
/* -------------------------------------------------------------------------- */

type Error struct {
	errorMessage  string
	errorSeverity string
}

func (error *Error) Error() string {
	var errorSeverity string = fmt.Sprintf("Error severity: %s", error.errorSeverity)
	var errorMessage string = fmt.Sprintf("\nError message: %s", error.errorMessage)
	return errorSeverity + errorMessage
}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

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

func fn(a int, b int) (int, error) {
	if a == 0 {
		return 0, errors.New("First parameter mustn't be zero!")
	}

	if b == 0 {
		return 0, errors.New("Second parameter mustn't be zero!")
	}

	if a < 0 || b < 0 {
		return 0, &Error{errorMessage: "First parameter and second parameter must be greater than zero!", errorSeverity: "high"}
	}

	return a + b, nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Exceptions...
	*/

	fmt.Println("Exceptions...")

	division, divisionError := divide(10, 0)
	if divisionError != nil {
		fmt.Printf("\n%s\n", divisionError.Error())
	} else {
		fmt.Printf("\n%d / %d --> %d\n", 10, 0, division)
	}

	var array []string = []string{"Hello", "World", "!"}
	element, elementError := at(&array, 3)
	if elementError != nil {
		fmt.Printf("\n%s\n", elementError.Error())
	} else {
		fmt.Printf("\narray[3] --> %s\n", element)
	}

	fmt.Println("\n# ---------------------------------------------------------------------------------- #\n")

	/*
		Additional challenge...
	*/

	fmt.Println("Additional challenge...")

	// Custom error
	result01, result01Error := fn(-2, -2)
	if result01Error != nil {
		fmt.Printf("\n%s\n", result01Error.Error())
	} else {
		fmt.Printf("\nFirst result --> %d\n", result01)
	}

	// First parameter error
	result02, result02Error := fn(0, 5)
	if result02Error != nil {
		fmt.Printf("\n%s\n", result02Error.Error())
	} else {
		fmt.Printf("\nSecond result --> %d\n", result02)
	}

	// No error
	result03, result03Error := fn(5, 10)
	if result03Error != nil {
		fmt.Printf("\n%s\n", result03Error.Error())
	} else {
		fmt.Printf("\nThird result --> %d\n", result03)
	}

	// Second parameter error
	result04, result04Error := fn(8, 0)
	if result04Error != nil {
		fmt.Printf("\n%s\n", result04Error.Error())
	} else {
		fmt.Printf("\nFourth result --> %d\n", result04)
	}

	fmt.Println("\nAdditional challenge finished!")
}
