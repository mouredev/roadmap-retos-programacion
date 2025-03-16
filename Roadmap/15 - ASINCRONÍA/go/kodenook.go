package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup

	wg.Add(2)

	go MyFunc("async 1", &wg)
	go MyFunc("async 2", &wg)

	wg.Wait()
}

func MyFunc(name string, wg *sync.WaitGroup) {
	start := time.Now()
	defer wg.Done()

	fmt.Printf("name execution : %v\n", name)
	fmt.Printf("start %v execution : %v\n", name, start)

	fmt.Printf("duration %v execution : 5 milliseconds\n", name)
	time.Sleep(5 * time.Millisecond)

	fmt.Printf("execution %v finalized at: %v\n", name, time.Now())
}
