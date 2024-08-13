package main

import (
	"fmt"
	"time"
)

func main() {
	timeTrack(func() { fmt.Println("Hello, Go") })
}

func timeTrack(callback func()) {
	start := time.Now()

	callback()

	fmt.Printf("time: %v", time.Since(start))
}
