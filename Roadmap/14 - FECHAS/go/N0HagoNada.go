package main

import (
	"fmt"
	"time"
)

func main() {
	// Fecha actual
	fechaActual := time.Now()

	// Fecha de nacimiento (ejemplo: 1 de enero de 1990 a las 10:30 AM)
	fechaNacimiento := time.Date(1990, time.January, 1, 10, 30, 0, 0, time.Local)

	// Cálculo de la diferencia entre las fechas
	diferencia := fechaActual.Sub(fechaNacimiento)
	years := int(diferencia.Hours() / 24 / 365)

	fmt.Printf("Fecha actual: %s\n", fechaActual.Format("2006-01-02 15:04:05"))
	fmt.Printf("Fecha de nacimiento: %s\n", fechaNacimiento.Format("2006-01-02 15:04:05"))
	fmt.Printf("Años transcurridos: %d\n", years)

	/***************************** RETO ************************************************/
	// Formatos diferentes para la fecha de nacimiento
	fmt.Println("\nFormatos diferentes para la fecha de nacimiento:")
	fmt.Printf("1. Día, mes y año: %d-%d-%d\n", fechaNacimiento.Day(), fechaNacimiento.Month(), fechaNacimiento.Year())
	fmt.Printf("2. Hora, minuto y segundo: %02d:%02d:%02d\n", fechaNacimiento.Hour(), fechaNacimiento.Minute(), fechaNacimiento.Second())
	fmt.Printf("3. Día del año: %d\n", fechaNacimiento.YearDay())
	fmt.Printf("4. Día de la semana: %s\n", fechaNacimiento.Weekday())
	fmt.Printf("5. Nombre del mes: %s\n", fechaNacimiento.Month().String())
	fmt.Printf("6. Formato personalizado: %d/%d/%d %02d:%02d\n", fechaNacimiento.Day(), int(fechaNacimiento.Month()), fechaNacimiento.Year(), fechaNacimiento.Hour(), fechaNacimiento.Minute())
	fmt.Printf("7. RFC 3339: %s\n", fechaNacimiento.Format(time.RFC3339))
	fmt.Printf("8. RFC 1123: %s\n", fechaNacimiento.Format(time.RFC1123))
	fmt.Printf("9. RFC 822: %s\n", fechaNacimiento.Format(time.RFC822))
	fmt.Printf("10. Stamp: %d\n", fechaNacimiento.Unix())
}
