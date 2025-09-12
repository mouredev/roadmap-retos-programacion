package main

import (
	"fmt"
	"time"
)

type root_function func()

func func_1(f root_function) root_function {
	stunden := 0
	return func() {
		f()
		time.Sleep(time.Duration(stunden) * time.Second)
		stunden += 1
		fmt.Printf("Stunden %v\n", stunden)

	}
}

func qq() {
	fmt.Print("function qq")
}

func cc() {
	fmt.Print("function cc")
}

func aa() {
	fmt.Print("function aa")
}

func main() {
	qqq := func_1(qq)
	ccc := func_1(cc)
	aaa := func_1(aa)
	qqq()
	ccc()
	aaa()
	ccc()
	ccc()
	ccc()
	ccc()
	ccc()
	qqq()
	qqq()
	aaa()
}
