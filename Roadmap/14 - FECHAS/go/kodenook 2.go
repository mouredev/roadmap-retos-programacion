package main

import (
	"fmt"
	"time"
)

func main() {
	birthday := time.Date(1996, 7, 27, 14, 30, 0, 0, time.Local)
	diff := time.Now().Sub(birthday)

	fmt.Printf("difference: %.2f years", diff.Hours()/24/365)
}
