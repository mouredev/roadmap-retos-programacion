package main

import (
	"fmt"
	"regexp"
)

type Validator interface {
	Validate(input string) bool
}

// NumberValidator -- -- --
type NumberValidator struct{}

func (nv NumberValidator) Validate(input string) bool {
	re := regexp.MustCompile(`\d+`)
	return re.MatchString(input)
}

func (nv NumberValidator) Extract(input string) []string {
	re := regexp.MustCompile(`\d+`)
	return re.FindAllString(input, -1)
}

// EmailValidator -- -- --
type EmailValidator struct{}

func (ev EmailValidator) Validate(input string) bool {
	re := regexp.MustCompile(`^[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$`)
	return re.MatchString(input)
}

// PhoneValidator -- -- --
type PhoneValidator struct{}

func (pv PhoneValidator) Validate(input string) bool {
	re := regexp.MustCompile(`^\+?[0-9]{1,3}?[-. ]?(\(?\d{1,4}?\)?[-. ]?)?[\d-. ]{7,10}$`)
	return re.MatchString(input)
}

// URLValidator -- -- --
type URLValidator struct{}

func (uv URLValidator) Validate(input string) bool {
	re := regexp.MustCompile(`^(https?|ftp)://[^\s/$.?#].[^\s]*$`)
	return re.MatchString(input)
}

func main() {

	text := "Hello, I'm qwik zgheib, and my phone number is +51984371244"
	email := "qwikzgheib@gmail.com"
	phone := "+51984371244"
	url := "https://www.dota2.com/hero/legioncommander"

	content := []string{
		text,
		email,
		phone,
		url,
	}

	validators := []Validator{
		NumberValidator{},
		EmailValidator{},
		PhoneValidator{},
		URLValidator{},
	}

	for i, validator := range validators {
		switch v := validator.(type) {
		case NumberValidator:
			if v.Validate(content[i]) {
				numbers := v.Extract(text)
				fmt.Println("numbers found:", numbers)
			} else {
				fmt.Println("no numbers found!")
			}
		case EmailValidator:
			fmt.Print("email: ", content[i])
			if v.Validate(content[i]) {
				fmt.Println(" - valid")
			} else {
				fmt.Println(" - invalid")
			}
		case PhoneValidator:
			fmt.Print("phone number: ", content[i])
			if v.Validate(content[i]) {
				fmt.Println(" - valid")
			} else {
				fmt.Println(" - invalid")
			}
		case URLValidator:
			fmt.Print("url: ", content[i])
			if v.Validate(content[i]) {
				fmt.Println(" - valid")
			} else {
				fmt.Println(" - invalid")
			}
		}
	}
}
