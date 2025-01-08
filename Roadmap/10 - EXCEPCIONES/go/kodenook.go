package main

import (
	"fmt"
)

func main() {
	var err error
	x := 4
	y := 0

	defer func() {
		if r := recover(); r != nil {
			err = fmt.Errorf("error: %v", r)
			fmt.Println(err)
		}
	}()
	out := x / y
	fmt.Println(out)
}
