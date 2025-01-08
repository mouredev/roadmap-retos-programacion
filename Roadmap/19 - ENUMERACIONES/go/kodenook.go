package main

import "fmt"

func main() {
	const (
		monday int = iota
		tuesday
		wednesday
		thursday
		friday
		saturday
		sunday
	)

	day := 6

	switch day {
	case monday:
		fmt.Println("Monday")
	case tuesday:
		fmt.Println("Tuesday")
	case wednesday:
		fmt.Println("Wednesday")
	case thursday:
		fmt.Println("Thursday")
	case friday:
		fmt.Println("Friday")
	case saturday:
		fmt.Println("Saturday")
	case sunday:
		fmt.Println("Sunday")
	}
}
