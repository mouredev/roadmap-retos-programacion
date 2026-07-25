package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func main() {

	// Declaracion de variables
	var longString = " Esto es una cadena de texto "
	var sayHi = "Hello, World"
	var godev = "https://go.dev"
	var numericString = "1234567"
	var numbers = 567890
	var runicString rune = 'a'
	var lang = "golang"

	// Concatenación
	fmt.Println("Concatenación con paquetes: ", strings.Join([]string{"Hola", "Golang!"}, ", "))
	fmt.Println("Concatenación con siḿbolo de suma: ", "Hola "+"Mundo "+"de "+"Desarrolladores.")
	fmt.Println("concatenación de variables", sayHi+" "+" "+longString)

	// interpolación
	fmt.Printf("Esta es la página oficial del lenguaje %s: %s\n", lang, godev)
	interpolacion := fmt.Sprintf("Esta es la página oficial del lenguaje %s: %s", lang, godev)
	fmt.Println(interpolacion)

	// Búsqueda
	fmt.Println("Busca una palabra: ", strings.Contains(longString, "una"))
	fmt.Println("Busca algunos caracteres: ", strings.ContainsAny(longString, "abc"))
	fmt.Println("Busca un caracter unicode: ", strings.ContainsRune(longString, 'a'))

	// Reemplazo de una palabra
	fmt.Println("Reemplazo de palabra: ", strings.Replace(sayHi, "World", "Golang", 1))

	// Cuenta la cantidad de veces que una cadena aparece e otra
	fmt.Println("Cuenta las veces que aparece una cadena", strings.Count(longString, "a"))

	// División de Cadena
	fmt.Println("Division de cadena(Slice): ", strings.Split("Hello-Gophers-of-world", "-"))

	// Conversión a Mayúsculas
	fmt.Println("Conversión a mayúsculas: ", strings.ToUpper(sayHi))

	// Conversión a Minúsculas
	fmt.Println("Converión a minúsculas: ", strings.ToLower(longString))

	// Recorte de Espacios(Principio y fin de la cadena)
	fmt.Println("Recorte de espacios (Principio y Fin): ", strings.Trim(longString, " "))

	// Conversión de Rune a Cadena
	fmt.Println("Unicode a Cadena de texto: ", strconv.QuoteRuneToASCII(runicString))
	fmt.Println("Unicode a Cadena de texto: ", strconv.QuoteRune(runicString))
	fmt.Println("Unicode a Cadena de texto: ", strconv.QuoteRuneToGraphic(runicString))

	// Cálculo de Longitud
	fmt.Println("longitud de una cadena: ", len(longString))

	// Formateo de Cadenas: fmt Aplica formateo específico a cadenas, como sprintf.
	value := fmt.Sprintf("Tipo: %T Valor: %s Espacio de memoria: %v\n ", longString, longString, &longString)
	fmt.Println("Formateo: ", value)

	// Verificación de Prefijo
	fmt.Println("Verificar prefijo(https://): ", strings.HasPrefix(godev, "https://"))

	// Verificación de Sufijo
	fmt.Println("Verificar sufijo(.dev): ", strings.HasSuffix(godev, ".dev"))

	// Repetición de Cadena: strings Crea una nueva cadena repitiendo una existente un número específico de veces.
	fmt.Println("Repetición de cadenas: ", strings.Repeat("go ", 4))

	// Conversión de Cadena a Entero: strconv Convierte una cadena que representa un número en su valor entero.
	n, _ := strconv.Atoi(numericString)
	fmt.Printf("Conversión de cadena a entero: Tipo: %T Valor: %d\n", n, n)

	// Conversión de Entero a Cadena: strconv Convierte un valor entero en su representación de cadena.
	ITS := strconv.Itoa(numbers)
	fmt.Printf("Conversión de entero a cadena: Tipo: %T Valor: %s\n", ITS, ITS)

	// Extra: Palabras palindromas

	fmt.Println("'Somos', ¿es una palabra palindroma?: ", palindromeWord("somos"))
	fmt.Println("'Hola', ¿es una palabra palindroma?: ", palindromeWord("hola"))

	// Extra: Anagramas
	fmt.Println("'Amor y Roma', ¿son anagrama?: ", anagramWord("AmoR", "RoMa"))
	fmt.Println("'Verde y Rojo', ¿son anagrama?: ", anagramWord("Verde", "rOjo"))

	// Extra: Isogramas
	fmt.Println("'Murciélago' ¿es un isograma?: ", isogramWord("murciélago"))
	fmt.Println("'Pan' ¿es un isograma?: ", isogramWord("pan"))
	fmt.Println("'Pasta' ¿es un isograma?: ", isogramWord("pasta"))

}

func palindromeWord(word string) bool {
	if len(word) == 0 {
		return false
	} else if len(word) == 1 {
		return true
	} else {
		runes := []rune(word)
		n := len(runes)
		for i := 0; i < n/2; i++ {
			runes[i], runes[n-1-i] = runes[n-1-i], runes[i]
		}
		reversed := string(runes)

		if reversed != word {
			return false
		}
		return true
	}
}

func anagramWord(x, y string) bool {
	// Verificamos si tienen diferente longitud (por definición no pueden serlo)
	if len(x) != len(y) {
		return false
	}

	// las dividimos con Split mientras las paso a minúsculas a la vez
	splited1 := strings.Split(strings.ToLower(x), "")
	splited2 := strings.Split(strings.ToLower(y), "")

	// Las ordenamos
	sort.Strings(splited1)
	sort.Strings(splited2)

	// Iteramos sobre ellas para comparar si son iguales
	for i := 0; i < len(splited1); i++ {
		compared := splited1[i] == splited2[i]
		if !compared {
			return false
		}
	}
	return true
}

func isogramWord(s string) bool {
	word := strings.ToLower(s)

	runeCount := make(map[rune]int)

	for _, r := range word {
		runeCount[r]++
	}

	var firstCount int
	for _, count := range runeCount {
		firstCount = count
		break
	}

	for _, count := range runeCount {
		if count != firstCount {
			return false
		}
	}
	return true
}
