package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	message := `Hola como estas`
	otherMessage := "amigo programador"
	//# Concatenación
	fmt.Println(message + ", " + otherMessage + ".")
	//# Longitud de la cadena
	fmt.Println("Longitud de la cadena es :", len(message))
	//# Repetición
	fmt.Println(strings.Repeat(message, 2))
	//# búsqueda
	fmt.Println("Empieza con 'Ho'?:", strings.HasPrefix(message, "Ho"))
	fmt.Println("Termina con 'as'?:", strings.HasSuffix(message, "s"))
	fmt.Println("Veces que se repite la letra 'o':", strings.Count(message, "o"))
	//# conversión a mayúsculas y minúsculas
	fmt.Println("Conversión a mayúsculas:", strings.ToUpper(message))
	fmt.Println("Conversión a minúsculas:", strings.ToLower(message))
	//# reemplazo
	fmt.Println("Reemplazar 'r' por 'T':", strings.ReplaceAll(otherMessage, "r", "T"))
	//# división
	fmt.Println("Dividir por espacio :", strings.Split(message, " "))
	//# unión
	splitString := strings.Fields(message)
	fmt.Println("Unir palabras de ", splitString, " :", strings.Join(splitString, " "))
	//# verificación
	fmt.Println("Contiene 'mo'?:", strings.Contains(message, "mo"))
	//# interpolación
	fmt.Printf("Mensaje :%s\n", message)
	//# Acceso a carácter por el indice
	fmt.Printf("Carácter en el indice 3 de %s : es '%s'\n", message, string(message[3]))
	//# sub cadenas
	fmt.Println("sub cadena :", message[1:4])
	result := isPalindrome("radar")
	fmt.Println(result)
	//# EXTRA
	//Palindrome, si al revertir se lee lo mismo
	fmt.Printf("¿'radar' es palindrome? : %v \n", isPalindrome("radar"))
	fmt.Printf("¿'hola' es palindrome? : %v \n", isPalindrome("hola"))
	//Anagrama, si ambas tienen las mismas letras
	fmt.Printf("¿'roma' y 'amor' son anagramas ? :%v\n", isAnagram("roma", "amor"))
	//Isograma, palabra o frase en la que cada letra aparece el mismo número de veces Vivienne
	fmt.Printf("¿'escritura' es Isograma ? :%v\n", isIsogram("escritura"))
	fmt.Printf("¿'Dermatoglyphics' es Isograma ? :%v\n", isIsogram("Dermatoglyphics"))
	fmt.Printf("¿'vivienne ss' es Isograma ? :%v\n", isIsogram("vivienne ss"))
}

func isPalindrome(s string) bool {
	if len(s) <= 1 {
		return true
	}
	iLeft := 0
	iRight := len(s) - 1

	for iLeft < iRight {
		if s[iLeft] != s[iRight] {
			return false
		}
		iLeft++
		iRight--
	}

	return true
}
func isAnagram(s1, s2 string) bool {
	if len(s1) != len(s2) {
		return len(s1) != len(s2)
	}
	charCount := make(map[int32]int)
	for _, char := range s1 {
		charCount[char]++
	}
	for _, char := range s2 {
		charCount[char]--
		if charCount[char] < 0 {
			return false
		}
	}
	for _, count := range charCount {
		if count != 0 {
			return false
		}
	}
	return true
}

func isIsogram(s string) bool {
	if len(s) <= 2 {
		return true
	}

	charCount := make(map[rune]int)
	for _, char := range s {
		if !unicode.IsLetter(char) {
			continue
		}
		charCount[char]++
	}
	var lenIsogram int
	for _, v := range charCount {
		lenIsogram = v
		break
	}
	for _, v := range charCount {
		if lenIsogram != v {
			return false
		}
	}
	return true
}
