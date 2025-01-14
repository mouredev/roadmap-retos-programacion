package main

import (
    "fmt"
    "regexp"
)

func regExpr(cadena string) {
    patron := `-?\d+(\.\d+)?`
    regex := regexp.MustCompile(patron)
    numeros := regex.FindAllString(cadena, -1)

    fmt.Println("Números encontrados:")
    for _, numero := range numeros {
        fmt.Println(numero)
    }
    fmt.Println()
}

func main() {
    texto := "Este es un texto con números como 123, 45.6, -7 y 1000."
    fmt.Println("Vamos a analizar el siguiente texto:")
    fmt.Println("'" + texto + "'\n")
    regExpr(texto)

    texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456"
    fmt.Println("Vamos a analizar el siguiente texto:")
    fmt.Println("'" + texto + "'\n")
    regExpr(texto)

    emailValidation := func(email string) {
        patron := `^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$`
        regex := regexp.MustCompile(patron)
        if regex.MatchString(email) {
            fmt.Println("El email", email, "es válido.")
        } else {
            fmt.Println("El email", email, "no es válido.")
        }
    }

    phoneValidation := func(phone string) {
        patron := `^\+?(\d{2,3})?[-. ]?\d{9}$`
        regex := regexp.MustCompile(patron)
        if regex.MatchString(phone) {
            fmt.Println("El teléfono", phone, "es válido.")
        } else {
            fmt.Println("El teléfono", phone, "no es válido.")
        }
    }

    urlValidation := func(url string) {
        patron := `^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}`
        regex := regexp.MustCompile(patron)
        if regex.MatchString(url) {
            fmt.Println("La URL", url, "es válida.")
        } else {
            fmt.Println("La URL", url, "no es válida.")
        }
    }

    emailValidation("correo@correo.com")
    emailValidation("correo@correo")

    phoneValidation("+34 123456789")
    phoneValidation("123456789")

    urlValidation("http://www.google.com")
    urlValidation("www.google.com")
}
