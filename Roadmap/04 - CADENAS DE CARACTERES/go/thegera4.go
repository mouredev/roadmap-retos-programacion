/*
 * EJERCICIO:
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

package main

import (
	"fmt"
	"strings"
)

func main() {

	//Algunas operaciones con strings. Para mas operaciones revisar documentacion de paquete "strings"

	// Acceso a caracteres específicos (ASCII)
	fmt.Println("***Acceso a caracteres específicos***")
	fmt.Println("Hola"[0]) // 72
	fmt.Println("Hola"[1]) // 111
	fmt.Println("Hola"[2]) // 108
	fmt.Println("Hola"[3]) // 97

	// Subcadenas
	fmt.Println("***Subcadenas***")
	fmt.Println("Hola"[0:2]) // Ho
	fmt.Println("Hola"[1:3]) // ol
	fmt.Println("Hola"[2:4]) // la

	// Longitud
	fmt.Println("***Longitud***")
	fmt.Println(len("Hola")) // 4

	//Count
	fmt.Println("***Conteo***")
	fmt.Println(strings.Count("Hola mundo", "o")) // 2

	// Concatenación
	fmt.Println("***Concatenación***")
	fmt.Println("Hola" + " mundo") // Hola mundo
	var s string = "nuevo"
	fmt.Printf("Otro string %s\n",s) // Otro string nuevo
	var s1 string = "mas"
	var s2 string = "variables"
	fmt.Printf("Otro string %s con %s %s\n",s,s1,s2) // Otra cadena doble cadena

	// Repetición
	fmt.Println("***Repetición***")
	fmt.Println(strings.Repeat("Hola", 3)) // HolaHolaHola

	// Conversión a mayúsculas y minúsculas
	fmt.Println("***Conversión a mayúsculas y minúsculas***")
	fmt.Println(strings.ToUpper("Hola")) // HOLA
	fmt.Println(strings.ToLower("Hola")) // hola

	// Reemplazo
	fmt.Println("***Reemplazo***")
	fmt.Println(strings.Replace("Hola mundo", "mundo", "gente", 1)) // Hola gente

	// División
	fmt.Println("***División***")
	fmt.Println(strings.Split("Hola mundo", " ")) // [Hola mundo]

	// Unión
	fmt.Println("***Unión***")
	slice := []string{"Hola", "mundo"}
	fmt.Println(strings.Join(slice, " ")) // Hola mundo

	// Verificación
	fmt.Println("***Verificación***")
	fmt.Println(strings.Contains("Hola mundo", "mundo")) // true
	fmt.Println(strings.Contains("Hola mundo", "gente")) // false

	//Prefijo y sufijo
	fmt.Println("***Prefijo y sufijo***")
	fmt.Println(strings.HasPrefix("Hola mundo", "Hola")) // true
	fmt.Println(strings.HasSuffix("Hola mundo", "mundo")) // true

	// Palíndromos
	fmt.Println("***Extra: Palindromos***")
	fmt.Println(isPalindrome("Anita lava la tina")) // true
	fmt.Println(isPalindrome("Roma")) // false

	// Anagramas
	fmt.Println("***Extra: Anagramas***")
	fmt.Println(isAnagram("gato", "Toga")) // true
	fmt.Println(isAnagram("Anita", "tina")) // false

	// Isogramas
	fmt.Println("***Extra: Isogramas***")
	fmt.Println(isIsogram("murcielago")) // true
	fmt.Println(isIsogram("anita")) // false

}

// Palíndromos - Palabras que se leen igual de izquierda a derecha que de derecha a izquierda
func isPalindrome(str string) bool {
	str = strings.ToLower(str) // Convierte la cadena a minúsculas
	str = strings.Replace(str, " ", "", -1)  // Elimina los espacios en blanco

	for i := 0; i < len(str)/2; i++ { // Recorre la mitad de la cadena
		if str[i] != str[len(str)-1-i] { // Compara el caracter actual con el simétrico
			return false // Si no son iguales, regresa false
		}
	}
	return true // Si no se encontraron diferencias, regresa true
}

// Anagramas
func isAnagram(s1, s2 string) bool {
	s1 = strings.ToLower(s1) // Convierte las cadenas a minúsculas
	s2 = strings.ToLower(s2)

	if len(s1) != len(s2) { // Si las cadenas no tienen la misma longitud, regresa false directamente (no pueden ser anagramas)
		return false
	}

	m := make(map[rune]int) // Crea un mapa para contar las ocurrencias de cada caracter

	for _, c := range s1 { // Recorre cada caracter de la primera cadena
		m[c]++ // Cuenta cuantas veces aparece cada caracter
	}

	for _, c := range s2 { //Recorre cada caracter de la segunda cadena
		m[c]-- // Resta 1 a la cuenta de cada caracter
	}

	for _, v := range m { // Recorre el mapa
		if v != 0 { // Si alguna cuenta no es 0,
			return false // regresa false (no son anagramas)
		}
	}

	return true // Si todas las cuentas son 0, regresa true (son anagramas)
}

// Isogramas
func isIsogram(s string) bool {
	m := make(map[rune]bool) // Crea un mapa para almacenar los caracteres únicos

	for _, c := range s { // Recorre cada caracter de la cadena
		if m[c] { // Si el caracter ya está en el mapa,
			return false // regresa false (no es un isograma)
		}
		m[c] = true // Si el caracter no está en el mapa, lo agrega
	}

	return true // Si no se encontraron caracteres repetidos, regresa true (es un isograma)
}