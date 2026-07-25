// # #04 CADENAS DE CARACTERES
// > #### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

// ## Ejercicio

// ```
// /*
//  * EJERCICIO:
//  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
//  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
//  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
//  *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
//  * para descubrir si son:
//  * - Palíndromos
//  * - Anagramas
//  * - Isogramas
//  */
// ```
// #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

// Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

// > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

package main

import (
	"fmt"
	"sort"
	"strings"
)

// palindromo verifica si una palabra es un palíndromo.
func palindromo(s string) bool {
	s = strings.ToLower(s)
	runes := []rune(s)
	i, j := 0, len(runes)-1
	for i < j {
		if runes[i] != runes[j] {
			return false
		}
		i++
		j--
	}
	return true
}

// anagrama verifica si dos palabras son anagramas.
func anagrama(a, b string) bool {
	a = strings.ReplaceAll(strings.ToLower(a), " ", "")
	b = strings.ReplaceAll(strings.ToLower(b), " ", "")

	if len(a) != len(b) {
		return false
	}
	aRunes := []rune(a)
	bRunes := []rune(b)

	// Ordenar los caracteres para comparar
	sort.Slice(aRunes, func(i, j int) bool { return aRunes[i] < aRunes[j] })
	sort.Slice(bRunes, func(i, j int) bool { return bRunes[i] < bRunes[j] })

	return string(aRunes) == string(bRunes)
}

// isograma verifica si una palabra es un isograma (no tiene letras repetidas).
func isograma(s string) bool {
	s = strings.ToLower(s)
	seen := make(map[rune]bool)
	for _, r := range s {
		if r < 'a' || r > 'z' { // Ignorar caracteres que no sean letras
			continue
		}
		if seen[r] {
			return false
		}
		seen[r] = true
	}
	return true
}

func main() {
	// OPERACIONES CON CADENAS (STRINGS)
	s := "Hello, GoLang!"

	fmt.Println("=== OPERACIONES CON STRINGS ===")

	// 1. Acceso a caracteres específicos
	fmt.Println("Primer carácter:", string(s[0]))

	// 2. Subcadenas
	fmt.Println("Subcadena (índices 7 a 13):", s[7:13])

	// 3. Longitud de la cadena
	fmt.Println("Longitud:", len(s))

	// 4. Concatenación
	s2 := " Welcome!"
	fmt.Println("Concatenado:", s+s2)

	// 5. Repetición
	fmt.Println("Repetido:", strings.Repeat("Go! ", 3))

	// 6. Recorrido (iterar sobre cada carácter)
	fmt.Print("Recorrido: ")
	for _, ch := range s {
		fmt.Printf("%c ", ch)
	}
	fmt.Println()

	// 7. Conversión a mayúsculas y minúsculas
	fmt.Println("Mayúsculas:", strings.ToUpper(s))
	fmt.Println("Minúsculas:", strings.ToLower(s))

	// 8. Reemplazo
	fmt.Println("Reemplazado:", strings.Replace(s, "GoLang", "Go", 1))

	// 9. División y unión
	dividido := strings.Split(s, " ")
	fmt.Println("Dividido:", dividido)
	fmt.Println("Unido:", strings.Join(dividido, " | "))

	// 10. Interpolación
	fmt.Println("Interpolado:", fmt.Sprintf("La cadena '%s' tiene longitud %d.", s, len(s)))

	// 11. Verificación de contenido
	fmt.Println("Contiene 'Go':", strings.Contains(s, "Go"))
	fmt.Println("Empieza con 'Hello':", strings.HasPrefix(s, "Hello"))
	fmt.Println("Termina con '!':", strings.HasSuffix(s, "!"))

	// -------------------------------------------------------------------
	// DIFICULTAD EXTRA: Análisis de palabras (palíndromos, anagramas, isogramas)
	fmt.Println("\n=== ANÁLISIS DE PALABRAS ===")

	// Ejemplo para palíndromo
	word1, word2 := "racecar", "hello"
	fmt.Printf("'%s' es palíndromo? %v\n", word1, palindromo(word1))
	fmt.Printf("'%s' es palíndromo? %v\n", word2, palindromo(word2))

	// Ejemplo para anagramas
	word3, word4 := "listen", "silent"
	fmt.Printf("'%s' y '%s' son anagramas? %v\n", word3, word4, anagrama(word3, word4))

	// Ejemplo para isograma
	word5, word6 := "machine", "programming"
	fmt.Printf("'%s' es isograma? %v\n", word5, isograma(word5))
	fmt.Printf("'%s' es isograma? %v\n", word6, isograma(word6))
}
