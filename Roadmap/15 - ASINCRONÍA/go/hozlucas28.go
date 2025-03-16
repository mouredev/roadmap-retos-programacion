package main

import (
	"fmt"
	"sync"
	"time"
)

func fn(fnName string, delay int8) {
	fmt.Printf("\n%s start...\n", fnName)
	var startTime time.Time = time.Now()

	time.Sleep(time.Duration(delay))

	var endTime time.Time = time.Now()
	fmt.Printf("%s: %v\n", fnName, endTime.Sub(startTime))
	fmt.Printf("%s end!\n", fnName)
}

func main() {
	/*
	   Asynchrony...
	*/
	var startTime time.Time = time.Now()

	fmt.Println("Asynchrony...")

	var wg sync.WaitGroup

	fmt.Println("\n> Instructions executed before calling `asyncFn` (asynchrony function)")

	wg.Add(1)
	go func() {
		defer wg.Done()
		fn("asyncFn", 5)
	}()

	fmt.Println("\n> Instructions executed after called `asyncFn` (asynchrony function)")

	wg.Wait()

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
	   Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	wg.Add(3)
	go func() {
		for range 3 {
			defer wg.Done()
		}

		fn("A", 1)
		fn("B", 2)
		fn("C", 3)
	}()

	wg.Wait()
	fn("D", 1)

	fmt.Printf("\nTotal time of execution: %v", time.Now().Sub(startTime))
}
