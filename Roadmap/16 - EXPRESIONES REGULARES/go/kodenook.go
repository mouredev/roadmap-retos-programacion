package main

import (
	"fmt"
	"regexp"
)

func main() {
	fmt.Printf("%v\n", ExtractNumber("There are 3 apples, 5 oranges, and 12 bananas."))
}

func ExtractNumber(word string) []string {
	pattern := `\d+`
	re := regexp.MustCompile(pattern)
	return re.FindAllString(word, -1)
}
