package main

import "fmt"

func main() {
	languages := []string{"golang"}

	languages = append(languages, "rust")
	languages = append([]string{"typescript"}, languages...)
	languages = append(languages, "python", "php")
	languages = append(languages[:2], append([]string{"ruby", "java"}, languages[2:]...)...)
	languages = append(languages[:5], languages[6:]...)
	languages[3] = "python"

	fmt.Printf("%v\n", languages)

	find := "golang"
	for _, v := range languages {
		if v == find {
			fmt.Printf("%v\n", true)
			break
		}
	}

	languages = []string{}
	fmt.Printf("%v\n", languages)
}
