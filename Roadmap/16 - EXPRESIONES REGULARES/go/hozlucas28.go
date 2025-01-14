package main

import (
	"fmt"
	"regexp"
	"strings"
)

type RegularExpressions struct {
	email       *regexp.Regexp
	phoneNumber *regexp.Regexp
	url         *regexp.Regexp
}

func main() {
	/*
		Regular expressions...
	*/

	fmt.Println("Regular expressions...")

	const text string = "¡Hola Mundo! Hoy es 15/04/2024. Quedan 263 días para terminar el año 2024."

	var regularExpression *regexp.Regexp = regexp.MustCompile(`[0-9]`)
	var numbers string = strings.Join(regularExpression.FindAllString(text, -1), "")

	fmt.Printf("\n`text` = '%s'\n", text)
	fmt.Printf("\nNumbers inside `text` --> %s\n", numbers)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	var regularExpressions RegularExpressions = RegularExpressions{
		email:       regexp.MustCompile(`^[a-zA-Z0-9]*@[a-zA-Z0-9]*\.[a-zA-Z]{2,3}$`),
		phoneNumber: regexp.MustCompile(`^\+[0-9]{1,4} [0-9]{4} [0-9]{4}$`),
		url:         regexp.MustCompile(`^https?://([a-zA-Z0-9]*\.)?[a-zA-Z0-9]*\.[a-zA-Z]{2,3}/?$`),
	}

	var emails []string = []string{"hozlucas28@gmail.com",
		"hozlucas28@dev.com",
		"hozlucas-28@hotmail.com",
		"hozlucas28@melí.com",
		"hozlucas28@edu.com",
	}

	var phoneNumbers []string = []string{"+12 3456 7890",
		"+1 1234 5890",
		"+1234 1234 5690",
		"+123456789",
		"+123456789 1234 5678",
	}

	var urls []string = []string{"https://www.example.cóm",
		"http://example.com",
		"https://subdomain.example.com",
		"http://www.example.c2.uk",
		"https://www.example.org",
	}

	fmt.Println("\nEmails...")
	for _, email := range emails {
		var isValid bool = regularExpressions.email.MatchString(email)
		fmt.Printf("Is '%s' a valid email? %t\n", email, isValid)
	}

	fmt.Println("\nPhone numbers...")
	for _, phoneNumber := range phoneNumbers {
		var isValid bool = regularExpressions.phoneNumber.MatchString(phoneNumber)
		fmt.Printf("Is '%s' a valid phone number? %t\n", phoneNumber, isValid)
	}

	fmt.Println("\nUrls...")
	for _, url := range urls {
		var isValid bool = regularExpressions.url.MatchString(url)
		fmt.Printf("Is '%s' a valid url? %t\n", url, isValid)
	}
}
