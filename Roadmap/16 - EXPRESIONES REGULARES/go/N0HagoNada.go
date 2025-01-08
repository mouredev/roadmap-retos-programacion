package main

import (
	"fmt"
	"regexp"
)

func main() {

	texto := "Hola, mi número de teléfono es 123456789 y mi edad es 30 años."

	// Expresión regular para encontrar números
	re := regexp.MustCompile(`\d+`)

	// Encontrar todos los números en el texto
	numeros := re.FindAllString(texto, -1)

	fmt.Println("Números encontrados:", numeros)

	// Expresión regular para validar un email
	emailRegex := regexp.MustCompile(`^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`)

	email1 := "example@example.com"
	email2 := "invalid.email"

	fmt.Println("Email válido:", emailRegex.MatchString(email1))
	fmt.Println("Email inválido:", emailRegex.MatchString(email2))

	// Expresión regular para validar un número de teléfono
	telefonoRegex := regexp.MustCompile(`^\d{10}$`)

	telefono1 := "1234567890"
	telefono2 := "123-456-7890"

	fmt.Println("Teléfono válido:", telefonoRegex.MatchString(telefono1))
	fmt.Println("Teléfono inválido:", telefonoRegex.MatchString(telefono2))

	// Expresión regular para validar una URL
	urlRegex := regexp.MustCompile(`^(http|https)://[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,})(/.*)?$`)

	url1 := "https://www.example.com"
	url2 := "invalid.url"

	fmt.Println("URL válida:", urlRegex.MatchString(url1))
	fmt.Println("URL inválida:", urlRegex.MatchString(url2))
}
