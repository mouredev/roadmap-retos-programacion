package main

import (
	"fmt"
	"time"
)

// /*
//  * EJERCICIO:
//  * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
//  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
//  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
//  * Calcula cuántos años han transcurrido entre ambas fechas.
//  *

func main() {
	now := time.Now()
	fmt.Printf("Date of today %v:\n", now)
	birthDate := time.Date(1979, time.December, 26, 19, 00, 00, 00, time.UTC)
	fmt.Printf("Date of my Birthday %v:\n", birthDate)
	dif := now.Year() - birthDate.Year()
	fmt.Printf("How many years since I was born %v:\n", dif)

	//  * DIFICULTAD EXTRA (opcional):
	//  * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
	//  * 10 maneras diferentes. Por ejemplo:
	//  * - Día, mes y año.
	//  * - Hora, minuto y segundo.
	//  * - Día de año.
	//  * - Día de la semana.
	//  * - Nombre del mes.
	//  * (lo que se te ocurra...)
	//  */

	// date := birthDate.Format("Dia/Mes/Ano")
	fmt.Printf(" Date : %v/%v/%v \n", birthDate.Day(), birthDate.Month(), birthDate.Year())
	fmt.Printf(" Time : %v:%v:%v \n", birthDate.Hour(), birthDate.Minute(), birthDate.Second())
	fmt.Printf(" Date of the year: %v \n", birthDate.YearDay())
	fmt.Printf(" MOnth: %v \n", birthDate.Month())

}
