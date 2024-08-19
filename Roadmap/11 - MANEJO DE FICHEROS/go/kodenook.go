package main

import (
	"fmt"
	"os"
)

func main() {
	file, _ := os.Create("kodenook.txt")
	defer file.Close()

	file.WriteString("richard Ocaranza\n")
	file.WriteString("27\n")
	file.WriteString("Golang")

	file.Close()

	file, _ = os.Open(file.Name())
	defer file.Close()

	buffer := make([]byte, 26)
	n, _ := file.Read(buffer)

	fmt.Println(string(buffer[:n]))
}
