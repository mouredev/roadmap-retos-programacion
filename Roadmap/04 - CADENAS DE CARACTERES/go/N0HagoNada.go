package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for {
		fmt.Println("Introduce una palabra (o escribe 'exit' para salir):")
		scanner.Scan()
		palabra := strings.TrimSpace(scanner.Text())

		if palabra == "exit" {
			break
		}

		if esPalindromo(palabra) {
			fmt.Println(palabra, "es un palíndromo.")
		} else {
			fmt.Println(palabra, "no es un palíndromo.")
		}

		if esIsograma(palabra) {
			fmt.Println(palabra, "es un isograma.")
		} else {
			fmt.Println(palabra, "no es un isograma.")
		}

		fmt.Println("Introduce otra palabra para comparar si son anagramas (o escribe 'exit' para salir):")
		scanner.Scan()
		otraPalabra := strings.TrimSpace(scanner.Text())

		if otraPalabra == "exit" {
			break
		}

		if esAnagrama(palabra, otraPalabra) {
			fmt.Println(palabra, "y", otraPalabra, "son anagramas.")
		} else {
			fmt.Println(palabra, "y", otraPalabra, "no son anagramas.")
		}
	}
	operacioneStrings()
	TestStringIterationWithRange()
	TestStringEqualsCaseInsensitive()
}

func operacioneStrings() {
	// Imprimir cadena
	fmt.Println("Let's print out this string.")
	// Concatenar
	fmt.Println("Sammy" + "Shark")
	// Aplicar mayúsculas y minúsculas
	ss := "Sammy Shark"
	fmt.Println(strings.ToUpper(ss))
	fmt.Println(strings.ToLower(ss))
	// Funciones de busqueda de cadena
	/* strings.HasPrefix 	Realiza búsquedas en la cadena desde el principio.
	strings.HasSuffix 	Realiza búsquedas en la cadena desde el final.
	strings.Contains 	Realiza búsquedas en cualquier parte de la cadena.
	strings.Count 	Cuenta la cantidad de veces que aparece la cadena.*/
	fmt.Println(strings.HasPrefix(ss, "Sammy"))
	fmt.Println(strings.HasSuffix(ss, "Shark"))
	fmt.Println(strings.Contains(ss, "Sh"))
	fmt.Println(strings.Count(ss, "S"))
	// Determina la longuitud de la cadena
	openSource := "Jhon contributes to open source."
	fmt.Println(len(openSource))
	// manipulación de Cadenas, strings.Join, strings.Split, strings.ReplaceAll
	fmt.Println(strings.Join([]string{"sharks", "crustaceans", "plankton"}, ","))
	balloon := "Sammy has a balloon."
	s := strings.Split(balloon, " ")
	fmt.Printf("%q", s)
	fmt.Println()
	// strings Filed ignora espacios en blanco
	data := "  username password   email	date"
	fields := strings.Fields(data)
	fmt.Printf("%q", fields)
	// ReplaceAll toma uan cadena original y realiza una sustitución
	fmt.Println(strings.ReplaceAll(balloon, "has", "had"))
	// Eliminar espacios en blanco
	fmt.Println(strings.TrimSpace(data)) // que pasa aqui ?
	fmt.Println(strings.TrimSpace(" \t\n Hello, Gophers \n\t\r\n"))
	// Trim retorna un slice del string quitando
	fmt.Println(strings.Trim("¡¡¡Hello, Gophers!!!", "!¡"))
	// Builder para construir un string
	words := []string{"Hola", " ", "Mundo"}

	var builder strings.Builder

	for _, w := range words {
		builder.WriteString(w)
	}

	result := builder.String()
	fmt.Println(result)
	// Comparar tamaño

	// create three strings
	string1 := "Programiz"
	string2 := "Programiz Pro"
	string3 := "Programiz"

	// compare strings
	fmt.Println(string1+" vs "+string2+":", strings.Compare(string1, string2)) // -1
	fmt.Println(string2+" vs "+string3+":", strings.Compare(string2, string3)) // 1
	fmt.Println(string1+" vs "+string3+":", strings.Compare(string1, string3)) // 0
}

// Iterar sobre un String
func TestStringIterationWithRange() {
	fmt.Println()
	namestring := "omar barra"
	for _, v := range namestring {
		fmt.Printf("%q\n", v)
	}
}

// Compara igualdad sin importar case
func TestStringEqualsCaseInsensitive() {
	got := "Go is Awesome!"
	expect := "go is awesome!"

	if !strings.EqualFold(got, expect) {
		fmt.Printf("expected %s got %s", expect, got)
	}
}

func esPalindromo(s string) bool {
	s = strings.ToLower(s)
	izquierda := 0
	derecha := len(s) - 1

	for izquierda < derecha {
		// Avanzar izquierda si no es letra o número
		for izquierda < derecha && !unicode.IsLetter(rune(s[izquierda])) && !unicode.IsNumber(rune(s[izquierda])) {
			izquierda++
		}
		// Retroceder derecha si no es letra o número
		for izquierda < derecha && !unicode.IsLetter(rune(s[derecha])) && !unicode.IsNumber(rune(s[derecha])) {
			derecha--
		}

		if s[izquierda] != s[derecha] {
			return false
		}

		izquierda++
		derecha--
	}

	return true
}

func esAnagrama(palabra1, palabra2 string) bool {
	// contienen el mismo número de ocurrencias de cada letra en orden diferente
	if len(palabra1) != len(palabra2) {
		return false
	}
	cuenta := make(map[rune]int)

	for _, letra := range strings.ToLower(palabra1) {
		if unicode.IsLetter(letra) {
			cuenta[letra]++
		}
	}

	for _, letra := range strings.ToLower(palabra2) {
		if unicode.IsLetter(letra) {
			cuenta[letra]--
			if cuenta[letra] < 0 {
				return false
			}
		}
	}

	for _, valor := range cuenta {
		if valor != 0 {
			return false
		}
	}

	return true
}
func esIsograma(palabra string) bool {
	// No tiene letras repetidas
	usado := make(map[rune]bool)
	for _, letra := range strings.ToLower(palabra) {
		if letra == '-' || letra == ' ' {
			continue
		}
		if _, ok := usado[letra]; ok {
			return false
		}
		usado[letra] = true
	}
	return true
}
func InvertirString(s string) string {
	// Convierte el string a un slice de runas para manejar adecuadamente caracteres Unicode.
	runas := []rune(s)
	for i, j := 0, len(runas)-1; i < j; i, j = i+1, j-1 {
		// Intercambia los elementos.
		runas[i], runas[j] = runas[j], runas[i]
	}
	// Convierte el slice de runas de vuelta a string.
	return string(runas)
}
