package main

import (
	"fmt"
	"regexp"
)

type texts struct {
	text1 string
	text2 string
}

func main() {
	t := texts{
		text1: "Es4 kasd 3 234 23  text0",
		text2: `This is the ex4 roslñdfalfj 3 39 fcm10`,
	}

	// Compila el patrón de expresión regular.
	re, err := regexp.Compile(`\d+`)
	if err != nil {
		fmt.Println("Error al compilar la expresión regular:", err)
		return
	}

	// Encuentra todas las ocurrencias del patrón en el texto.
	fmt.Printf("Del texto 1: %s\n", t.text1)
	numeros1 := re.FindAllString(t.text1, -1)
	fmt.Println("Números encontrados:", numeros1)
	fmt.Printf("Del texto 2: %s\n", t.text2)
	numeros2 := re.FindAllString(t.text2, -1)
	fmt.Println("Números encontrados:", numeros2)

	// Dificutlad Extra
	// Creando los emails, número y url
	email := "example.ga@gmail.com"
	numeroPeruano := "987654321"
	url := "google.com"

	fmt.Println("-------------------")
	fmt.Println("-------------------")
	fmt.Println("-------------------")

	// Compila el patrón de expresión regular.para email
	textEmail, valid := isEmailValited(email)
	if valid {
		fmt.Println(textEmail, "valido")
	} else {
		fmt.Println(textEmail, "invalido")
	}

	textNumber, validnumber := isnumberphoneValited(numeroPeruano)
	if validnumber {
		fmt.Println(textNumber, "valido")
	} else {
		fmt.Println(textNumber, "invalido")
	}

	textUrl, validurl := isurlValited(url)
	if validurl {
		fmt.Println(textUrl, "valido")
	} else {
		fmt.Println(textUrl, "invalido")
	}

}

func isEmailValited(e string) (string, bool) {
	emailRegex := regexp.MustCompile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
	return fmt.Sprintf("El email: '%s' es:", e), emailRegex.MatchString(e)
}

func isnumberphoneValited(e string) (string, bool) {
	emailRegex := regexp.MustCompile("^[0-9]{9,9}$")
	return fmt.Sprintf("El numero: '%s' es:", e), emailRegex.MatchString(e)
}

func isurlValited(e string) (string, bool) {
	emailRegex := regexp.MustCompile(`[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)`)
	return fmt.Sprintf("La url: '%s' es:", e), emailRegex.MatchString(e)
}
