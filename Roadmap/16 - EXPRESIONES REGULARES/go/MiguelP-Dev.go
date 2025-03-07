package main

import (
	"fmt"
	"regexp"
)

func main() {
	text := "Hola, mi número de teléfono es 1234567890 y mi email es miguelportillo2475@gmail.com"
	re := regexp.MustCompile(`\d+`)
	numbers := re.FindAllString(text, -1)
	for _, number := range numbers {
		println(number)
	}

	fmt.Printf("Tipo: %T, Valor0: %s, Valor1: %s\n", numbers, numbers[0], numbers[1])

	// Validación de correo electrónico
	email := "miguelportillo2475@gmail.com"
	emailRegExp, err := regexp.Compile(`^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`)
	if err != nil {
		fmt.Println("Error al compilar la expresión regular")
	}
	if emailRegExp.MatchString(email) {
		fmt.Println("Correo electrónico válido")
	} else {
		fmt.Println("Correo electrónico inválido")
	}

	// Validación de número de teléfono
	phone := "1234567890"
	phoneRegExp, err := regexp.Compile(`^\d{10}$`)
	if err != nil {
		fmt.Println("Error al compilar la expresión regular")
	}
	if phoneRegExp.MatchString(phone) {
		fmt.Println("Número de teléfono válido")
	} else {
		fmt.Println("Número de teléfono inválido")
	}

	// Validación de URL
	url := "https://ed.team"
	urlRegExp, err := regexp.Compile(`^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`)
	if err != nil {
		fmt.Println("Error al compilar la expresión regular")
	}
	if urlRegExp.MatchString(url) {
		fmt.Print("URL válida")
	} else {
		fmt.Println("URL inválida")
	}
}
