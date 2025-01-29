package main

import (
	"fmt"
	"time"
)

// now Hora actual
var now = time.Now()

// birthDate Fecha de naciemiento
var birthDate = time.Date(1993, 10, 13, 14, 35, 50, 0, time.UTC)

// datePassed Tiempo trasncurrido entre ambas fechas.
var datePassed = now.Sub(birthDate)

func main() {
	fmt.Printf("Horas Transcurridas: %v, Minutos Trasncurridos: %v, Tipo de dato: %T.\n", datePassed.Hours(), datePassed.Minutes(), datePassed)

	// Extra
	// "2006-01-02 15:04:05" Esta es la fecha de nacimiento de golang y es la fecha que se usa como
	//  una plantilla a la hora de dar formato a las fechas.

	exampleOne := now.Format("2006/01/02")
	fmt.Println("Date formatted in reversed order:", exampleOne)

	exampleTwo := now.Format("02/01/2006")
	fmt.Println("Date formatted with slash as separators:", exampleTwo)

	exampleThree := now.Format("15:04:05")
	fmt.Println("Formatted Time Clock:", exampleThree)

	exampleFour := now.Year()
	fmt.Println("Actual Year:", exampleFour)

	Madrid, _ := time.LoadLocation("Europe/Madrid")
	exampleFive := now.In(Madrid)
	fmt.Println("Time in Spesific Location(Madrid):", exampleFive)

	exampleSix := now.YearDay()
	fmt.Println("Day of the year:", exampleSix)

	exampleSeven := now.Month()
	fmt.Println("Month of year:", exampleSeven)

	exampleEith, week := now.ISOWeek()
	fmt.Printf("ISO 8601 formatted year: %v, and week number: %v\n", exampleEith, week)

	exampleNine, integer := now.Zone()
	fmt.Println("exampleNine: ", exampleNine, integer)

	exampleTen := now.Location()
	fmt.Println("Location returns the time zone information: ", exampleTen)

	// Obtengo los valores de Now por separado Primero con la fecha y luego con el reloj
	year, month, day := now.Date()
	hour, minute, second := now.Clock()
	fmt.Printf("Day: %v, Month: %v, Year: %v\n", day, month, year)
	fmt.Printf("Hour: %v, Minute: %v, Second: %v\n", hour, minute, second)

	twoHoursLater := now.Add(2 * time.Hour)
	fmt.Println("Adding two hours to actual date hour", twoHoursLater)

	fromHoursBefore := now.Add(-2 * time.Hour)
	fmt.Println("Substracting two hours to actual date hour", fromHoursBefore)

}
