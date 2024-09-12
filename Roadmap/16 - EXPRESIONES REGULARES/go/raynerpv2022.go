// #  * DIFICULTAD EXTRA (opcional):
// #  * Crea 3 expresiones regulares (a tu criterio) capaces de:
// #  * - Validar un email.
// #  * - Validar un número de teléfono.
// #  * - Validar una url.
// #  */

package main

import (
	"fmt"
	"regexp"
)

func check_mail(email string) string {
	p := `^[\w.]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$`

	re := regexp.MustCompile(p)
	if re.MatchString(email) {
		return email
	} else {
		return email + " NO VALIDO"
	}

}
func emailsValidate() {
	emails := []string{
		"user@example.com",
		"firstname.lastname@example.co.uk",
		"user+name@example.com",
		"user_name@example.org",
		"user.name123@example.info",
		"user123@example.org",
		"user.name+label@example.com",
		"username@subdomain.example.com",
		"user@example.travel",
		"user@example.name",
		"user@.com",
		"@example.com",
		"user@com",
		"user@exam_ple.com",
		"user@ex-ample.com",
		"user@.example.com",
		"user@example.c",
		"user@-example.com",
		"user@example..com",
		"user@exa_mple.com",
	}

	for _, e := range emails {
		fmt.Println(check_mail(e))
	}
}

func checkPhone(number string) string {
	ps := `^(\+34\s)?[\d]{3}\s[\d]{3}\s[\d]{3}$`
	result := regexp.MustCompile(ps)
	if result.MatchString(number) {
		return number
	} else {
		return number + " NO VALIDO"
	}

}

func telephonNUmber() {
	telefonos := []string{
		"+34 612 345 678",
		"612 345 678",
		"912 345 678",
		"(912) 345 678",
		"612345678",
		"+34 (612) 345 678",
		"612 34 56",
		"612-345-678",
		"123 456 789",
		"9123456789",
		"(612)345678",
		"612 345678",
	}

	for _, n := range telefonos {
		fmt.Println(checkPhone(n))
	}

}

func checkUrl(url string) string {

	ps := `^https?://[\w.]+\.[a-zA-Z]{2,}$`
	result := regexp.MustCompile(ps)
	if result.MatchString(url) {
		return url
	} else {
		return url + " NO VALIDA"
	}

}

func Urls() {

	urls := []string{
		"http://www.example.com",
		"https://subdomain.example.org",
		"http://example.co.uk",
		"http://example.com2",
		"http://www.example.c",
		"https://www.example.edu",
		"http://example",
		"ftp://example.com",
		"https://example.com/path",
		"http://123.456.789.0",
	}

	for _, l := range urls {
		fmt.Println(checkUrl(l))
	}

}
func main() {
	emailsValidate()
	Urls()
	telephonNUmber()
}
