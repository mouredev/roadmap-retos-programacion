package main

import (
	"fmt"
	"time"
)

func main() {
	/*
		Dates...
	*/

	fmt.Println("Dates...")

	var today time.Time = time.Now()
	var bornDate time.Time = time.Date(2002, time.February, 20, 0, 0, 0, 0, time.UTC)

	fmt.Printf("\nToday is: %v\n", today)
	fmt.Printf("\nLucas Hoz born date: %v\n", bornDate)

	var yearsBetweenDates int = today.Year() - bornDate.Year()
	fmt.Printf("\nYears between today and born date: %d years\n", yearsBetweenDates)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	fmt.Printf("\nDay, month, and year: %d, %d, and %d\n", bornDate.Day(), bornDate.Month(), bornDate.Year())

	fmt.Printf("\nHours, minutes, and seconds: %d hours, %d minutes, and %d seconds\n", bornDate.Hour(), bornDate.Minute(), bornDate.Second())

	fmt.Printf("\nDay of the year: %d\n", bornDate.YearDay())

	fmt.Printf("\nDay of the week (weeks starts on sunday): %d\n", bornDate.Weekday()+1)

	fmt.Printf("\nMonth name: %s\n", bornDate.Local().Month())
}
