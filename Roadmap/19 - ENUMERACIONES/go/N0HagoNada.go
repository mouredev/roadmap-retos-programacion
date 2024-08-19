package main

import "fmt"

type DayOfWeek int

const (
	Lundi DayOfWeek = iota
	Mardi
	Mercredi
	Jeudi
	Vendredi
	Samedi
	Dimanche
)

func main() {
	fmt.Println("Ingrese un número del 1 al 7 para obtener el día de la semana correspondiente:")
	var numero int
	fmt.Scanln(&numero)

	dia := obtenerDia(DayOfWeek(numero))
	if dia != "" {
		fmt.Printf("El número %d corresponde al día %s\n", numero, dia)
	} else {
		fmt.Println("Número no válido. Debe estar entre 1 y 7.")
	}
}

// Función que devuelve el nombre del día correspondiente al número
func obtenerDia(d DayOfWeek) string {
	switch d {
	case Lundi:
		return "Lundi"
	case Mardi:
		return "Mardi"
	case Mercredi:
		return "Mercredi"
	case Jeudi:
		return "Jeudi"
	case Vendredi:
		return "Vendredi"
	case Samedi:
		return "Samedi"
	case Dimanche:
		return "Dimanche"
	default:
		return ""
	}
}
