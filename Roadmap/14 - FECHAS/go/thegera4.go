package main

import (
	"fmt"
	"time"
)

func main() {
	today := time.Now()
	birthDate := time.Date(1987, time.July, 3, 12, 38, 45, 0, time.UTC)
	passedYears := today.Year() - birthDate.Year()

	if today.YearDay() < birthDate.YearDay() {
		passedYears--
	}
	fmt.Printf("Han transcurrido %d años desde mi nacimiento\n", passedYears)

	// Extra: Formateo de la fecha de nacimiento
	fmt.Printf("Fecha de nacimiento 1: %s\n", birthDate.Format("02/01/2006 15:04:05"))
	fmt.Printf("Fecha de nacimiento 2: %s\n", birthDate.Format("02/01/2006 03:04:05 PM"))
	fmt.Printf("Fecha de nacimiento 3: %s\n", birthDate.Format("2 de julio de 2006 a las 15:04:05"))
	fmt.Printf("Fecha de nacimiento 4: %s\n", birthDate.Format("viernes 2 de julio de 2006"))
	fmt.Printf("Fecha de nacimiento 5: %s\n", birthDate.Format("2/julio/2006"))
	fmt.Printf("Fecha de nacimiento 6: %s\n", birthDate.Format("02-01-2006"))
	fmt.Printf("Fecha de nacimiento 7: %s\n", birthDate.Format("02-01-06"))
	fmt.Printf("Fecha de nacimiento 8: %s\n", birthDate.Format("02-01-06 15:04:05"))
	fmt.Printf("Fecha de nacimiento 9: %s\n", birthDate.Format("02-01-06 03:04:05 PM"))
	fmt.Printf("Fecha de nacimiento 10: %s\n", birthDate.Format("02-01-06 03:04 PM"))
}