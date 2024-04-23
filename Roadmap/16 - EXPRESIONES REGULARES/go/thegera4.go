package main

import (
	"fmt"
	"regexp"
)

func main() {
	text := "Hola, mi nombre es Juan y tengo 25 años. Mi número de teléfono es 1234567890 y mi email es juan@email.com. Puedes visitar mi sitio web en https://juan.com";
	// Creamos la expresión regular
	re := regexp.MustCompile(`\d+`)
	// Buscamos todas las coincidencias en el texto
	matches := re.FindAllString(text, -1)
	// Imprimimos los resultados
	fmt.Println("Números encontrados:")
	for _, match := range matches {
		fmt.Println(match)
	}

	// EXTRA

	// Expresión regular para validar un email
	emailRegex := regexp.MustCompile(`[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`)
	emailOK := "thegera4@hotmail.com"
	emailNotOK := "pepe4356hotmail.com"
	emailNotOK2 := "pepe4356@hotmailco"
	emailNotOK3 := "renata@.com"
	emailNotOK4 := "gerardo@hotmail.c"
	fmt.Printf("Email válido?: %v\n", emailRegex.MatchString(emailOK))
	fmt.Printf("Email válido?: %v\n", emailRegex.MatchString(emailNotOK))
	fmt.Printf("Email válido?: %v\n", emailRegex.MatchString(emailNotOK2))
	fmt.Printf("Email válido?: %v\n", emailRegex.MatchString(emailNotOK3))
	fmt.Printf("Email válido?: %v\n", emailRegex.MatchString(emailNotOK4))

	// Expresión regular para validar un número de teléfono
	phoneRegex := regexp.MustCompile(`^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$`)
	phoneOK := "+1 123-456-7890"
	phoneNotOK := "123456789"
	phoneOK2 := "+528712345678"
	phoneNotOK2 := "12345678a0"
	fmt.Printf("Teléfono válido?: %v\n", phoneRegex.MatchString(phoneOK))
	fmt.Printf("Teléfono válido?: %v\n", phoneRegex.MatchString(phoneNotOK))
	fmt.Printf("Teléfono válido?: %v\n", phoneRegex.MatchString(phoneOK2))
	fmt.Printf("Teléfono válido?: %v\n", phoneRegex.MatchString(phoneNotOK2))

	// Expresión regular para validar una URL
	urlOK := "https://www.google.com"
	urlOK2 := "www.google.com"
	urlNotOK := "google."
	urlRegex := regexp.MustCompile(`^(https?:\/\/)?(www\.)?([a-zA-Z0-9-]+)\.([a-zA-Z]{2,})(\/[a-zA-Z0-9#]+\/?)*$`)
	fmt.Printf("URL válida?: %v\n", urlRegex.MatchString(urlOK))
	fmt.Printf("URL válida?: %v\n", urlRegex.MatchString(urlOK2))
	fmt.Printf("URL válida?: %v\n", urlRegex.MatchString(urlNotOK))

}