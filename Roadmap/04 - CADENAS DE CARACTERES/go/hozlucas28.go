package main

import (
	"fmt"
	"regexp"
	"strings"
)

func main() {
	/*
	   String operations...
	*/

	// Get length of a string
	const strLength int = len("Hello World!")
	fmt.Println("Get length of a string: len(<STRING NAME>)")
	fmt.Printf("len('Hello World!') --> %d", strLength)

	// Get char of a string
	var char byte = "Hello World!"[1]
	fmt.Println("\n\nGet char of a string: <STRING NAME>[<INDEX OF THE CHAR>]")
	fmt.Printf("'Hello World!'[1] --> %c", char)

	// Get substring of a string
	var substring string = "Hello World!"[2:9]
	fmt.Println("\n\nGet substring of a string: <STRING NAME>[<START>, <END - 1>]")
	fmt.Printf("'Hello World!'[2:9] --> '%s'", substring)

	// String to uppercase
	var uppercaseStr string = strings.ToUpper("Buenos Aires")
	fmt.Println("\n\nString to uppercase: strings.ToUpper(<STRING NAME>)")
	fmt.Printf("strings.ToUpper('Buenos Aires') --> '%s'", uppercaseStr)

	// String to lowercase
	var lowercaseStr string = strings.ToLower("USA")
	fmt.Println("\n\nString to lowercase: strings.ToLower(<STRING NAME>)")
	fmt.Printf("strings.ToLower('USA') --> '%s'", lowercaseStr)

	// Repeat a string
	var repeatedStr string = strings.Repeat("Juana", 2)
	fmt.Println("\n\nRepeat a string: strings.Repeat(<STRING NAME>, <NUMBER OF REPEATS>)")
	fmt.Printf("strings.Repeat('Juana', 2) --> '%s'", repeatedStr)

	// Concat two strings
	const concatedStr01 string = "Lucas" + "Hoz"
	fmt.Println("\n\nConcat two strings: <FIRST STRING NAME> + <SECOND STRING NAME> + <'N' STRING NAME...>")
	fmt.Printf("'Lucas ' + 'Hoz' --> '%s'", concatedStr01)

	// Replace substring of a string
	var replacedStr string = strings.ReplaceAll("Hello Python!", "Python", "Golang")
	fmt.Println("\n\nReplace substring of a string: strings.ReplaceAll(<STRING NAME>, <SUBSTRING TO SEARCH>, <NEW SUBSTRING>)")
	fmt.Printf("strings.ReplaceAll('Hello Python!', 'Python', 'Golang') --> '%s'", replacedStr)

	// Compare start of a string
	var compareStart bool = strings.HasPrefix("Lucas", "ho")
	fmt.Println("\n\nCompare start of a string: strings.HasPrefix(<STRING NAME>, <SUBSTRING TO FIND>)")
	fmt.Printf("strings.HasPrefix('Lucas', 'ho') --> %t", compareStart)

	// Compare end of a string
	var compareEnd bool = strings.HasSuffix("Lucas", "as")
	fmt.Println("\n\nCompare end of a string: strings.HasSuffix(<STRING NAME>, <SUBSTRING TO FIND>)")
	fmt.Printf("strings.HasSuffix('Lucas', 'as') --> %t", compareEnd)

	// Check if a string includes a substring
	var includes bool = strings.Contains("Lucas", "c")
	fmt.Println("\n\nCheck if a string includes a substring: strings.Contains(<STRING NAME>, <SUBSTRING TO FIND>)")
	fmt.Printf("strings.Contains('Lucas', 'c') --> %t", includes)

	// Check if a string matches a regex
	regexStr, _ := regexp.MatchString(`[luc]`, "Lucas")
	fmt.Println("\n\nCheck if a string matches a regex: regexp.MatchString(<REGEX>, <STRING NAME>)")
	fmt.Printf("regexp.MatchString(`[luc]`, 'Lucas') --> %t", regexStr)

	// Check if a string is equal to another string
	var commonComparison int = strings.Compare("Lucas", "LuCaS")
	fmt.Println("\n\nCheck if a string is equal to another string: strings.Compare(<FIRST STRING NAME>, <SECOND STRING NAME>)")
	fmt.Printf("strings.Compare('Lucas', 'LuCaS') --> %d", commonComparison)

	fmt.Println("\n\n# ---------------------------------------------------------------------------------- #")

	/*
	   Additional challenge...
	*/

	arr01 := []string{"level", "hello", "racecar", "world", "madam", "programming", "deed", "javascript"}
	palindromeWords := getPalindromeWords(arr01)
	fmt.Println("\nPalindrome words of", arr01, "-->", palindromeWords)

	arr02 := [][]string{
		{"listen", "silent"},
		{"hello", "world"},
		{"good", "dog"},
	}
	anagramWords := getAnagramWords(arr02)
	fmt.Println("\nAnagram words of", arr02, "-->", anagramWords)

	arr03 := []string{"hello", "world", "isogram", "javascript", "python", "algorithm"}
	isogramWords := getIsogramWords(arr03)
	fmt.Println("\nIsogram words of", arr03, "-->", isogramWords)
}

func getPalindromeWords(words []string) []string {
	var palindromeWords []string

	for _, word := range words {
		var reversedWord strings.Builder
		for j := len(word) - 1; j >= 0; j-- {
			var char byte = word[j]
			reversedWord.WriteByte(char)
		}

		var isPalindrome bool = strings.EqualFold(word, reversedWord.String())
		if isPalindrome {
			palindromeWords = append(palindromeWords, word)
		}
	}

	return palindromeWords

}

func getAnagramWords(pairOfWords [][]string) [][]string {
	var anagramWords [][]string

	for _, words := range pairOfWords {
		word01, word02 := words[0], words[1]

		var longestWord string = word02
		if len(word01) > len(word02) {
			longestWord = word01
		}

		uniqueChars := make(map[rune]bool)
		for _, char := range longestWord {
			uniqueChars[char] = true
		}

		isAnagram := true
		for _, char := range word01 {
			if !uniqueChars[char] {
				isAnagram = false
				break
			}
		}

		if isAnagram {
			anagramWords = append(anagramWords, words)
		}
	}

	return anagramWords
}

func getIsogramWords(words []string) []string {
	var isogramsWords []string

	for _, word := range words {
		var wordFmt string = strings.ReplaceAll(word, " ", "")

		uniqueChars := make(map[rune]bool)
		for _, char := range wordFmt {
			uniqueChars[char] = true
		}

		if len(wordFmt) == len(uniqueChars) {
			isogramsWords = append(isogramsWords, word)
		}
	}

	return isogramsWords
}
