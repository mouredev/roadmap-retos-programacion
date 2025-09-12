package main

import (
	"fmt"
	"sort"
	"strings"
)

type WordAnalyzer interface {
	IsPalindrome(word string) bool
	IsAnagram(word1, word2 string) bool
	IsIsogram(word string) bool
}

type SimpleWordAnalyzer struct{}

func NewSimpleWordAnalyzer() *SimpleWordAnalyzer {
	return &SimpleWordAnalyzer{}
}

func (wa *SimpleWordAnalyzer) IsPalindrome(word string) bool {
	for i := 0; i < len(word)/2; i++ {
		if word[i] != word[len(word)-1-i] {
			return false
		}
	}
	return true
}

func (wa *SimpleWordAnalyzer) IsAnagram(word1, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}
	word1 = strings.ToLower(word1)
	word2 = strings.ToLower(word2)
	word1 = SortString(word1)
	word2 = SortString(word2)
	return word1 == word2
}

func (wa *SimpleWordAnalyzer) IsIsogram(word string) bool {
	letters := make(map[rune]bool)
	for _, char := range word {
		if char != ' ' && letters[char] {
			return false
		}
		letters[char] = true
	}
	return true
}

func SortString(s string) string {
	sChars := strings.Split(s, "")
	sort.Strings(sChars)
	return strings.Join(sChars, "")
}

func main() {
	// Acceso a caracteres específicos
	word := "Hello"
	fmt.Println("Character at index 1:", word[1])

	// Longitud de la cadena
	fmt.Println("Length of the word:", len(word))

	// Concatenación de cadenas
	otherWord := "World"
	fmt.Println("Concatenated:", word+otherWord)

	// Conversión a mayúsculas y minúsculas
	fmt.Println("Uppercase:", strings.ToUpper(word))
	fmt.Println("Lowercase:", strings.ToLower(word))

	// Reemplazo de caracteres
	fmt.Println("Replaced:", strings.Replace(word, "e", "E", -1))

	// Verificación de una subcadena
	fmt.Println("Contains 'lo'?", strings.Contains(word, "lo"))

	// Subcadenas
	fmt.Println("Substring:", word[1:4])

	// División de una cadena
	fmt.Println("Split:", strings.Split("one,two,three", ","))

	// Unión de cadenas
	parts := []string{"one", "two", "three"}
	fmt.Println("Join:", strings.Join(parts, ", "))

	// Recorrido de la cadena
	for _, char := range word {
		fmt.Printf("%c ", char)
	}
	fmt.Println()

	// extra exercise
	wa := NewSimpleWordAnalyzer()

	word1 := "radar"
	word2 := "listen"
	word3 := "evil"
	word4 := "Debit card"
	word5 := "Bad credit"

	fmt.Printf("%s is a palindrome: %t\n", word1, wa.IsPalindrome(word1))
	fmt.Printf("%s is a palindrome: %t\n", word2, wa.IsPalindrome(word2))

	fmt.Printf("%s and %s are anagrams: %t\n", word3, word4, wa.IsAnagram(word3, word4))
	fmt.Printf("%s and %s are anagrams: %t\n", word4, word5, wa.IsAnagram(word4, word5))

	fmt.Printf("%s is an isogram: %t\n", word3, wa.IsIsogram(word3))
	fmt.Printf("%s is an isogram: %t\n", word4, wa.IsIsogram(word4))
}
