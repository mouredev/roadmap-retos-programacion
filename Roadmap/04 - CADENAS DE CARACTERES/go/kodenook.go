package main

import (
	"fmt"
	"strings"
)

func main() {
	/*
		String Functions
	*/

	var word string = "hello, Go"

	fmt.Println(strings.Contains(word, "hello"))
	fmt.Println(strings.Count(word, "l"))
	fmt.Println(strings.Index(word, "Go"))
	fmt.Println(strings.LastIndex(word, "Go"))
	fmt.Println(strings.Repeat(word, 2))
	fmt.Println(strings.Replace(word, "Go", "Go!", 1))
	fmt.Println(strings.ToLower(word))
	fmt.Println(strings.ToUpper(word))
	fmt.Println(strings.Trim(word, "eho"))
	fmt.Println(strings.TrimSpace(word))
}
