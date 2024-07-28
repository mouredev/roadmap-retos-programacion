package main

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"os"
)

func main() {
	u := Person{"kodenook", 27, "27-07", []string{"go", "rust"}}
	data, _ := json.MarshalIndent(u, "", "\t")

	err := os.WriteFile("person.json", data, 0644)
	if err != nil {
		fmt.Println("Error al escribir el archivo JSON:", err)
		return
	}

	fmt.Println(string(data))

	data2, _ := xml.MarshalIndent(u, "", "\t")

	err = os.WriteFile("person.xml", data2, 0644)
	if err != nil {
		fmt.Println("Error al escribir el archivo XML:", err)
		return
	}

	fmt.Println(string(data2))
	os.Remove("person.json")
	os.Remove("person.xml")
}

type Person struct {
	Name                 string
	Age                  uint
	Birthdate            string
	ProgrammingLenguages []string
}
