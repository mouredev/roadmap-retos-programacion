package main

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"io"
	"os"
)

type Person struct {
	Name               string   `json:"name" xml:"name"`
	Age                int      `json:"age" xml:"age"`
	DateBorn           string   `json:"date" xml:"date"`
	ProgramingLanguage []string `json:"languages" xml:"languages"`
}

func main() {
	// Escribir JSON
	p := Person{Name: "John Doe", Age: 30, DateBorn: "09-12-2023", ProgramingLanguage: []string{"go", "c", "asm"}}
	fileJSON, _ := os.Create("person.json")

	err := json.NewEncoder(fileJSON).Encode(p)
	if err != nil {
		print(err.Error())
	}
	fileJSON.Close()
	// Escribir XML
	filexml, _ := os.Create("person.xml")

	encoder := xml.NewEncoder(filexml)
	encoder.Indent("", "  ")
	err = encoder.Encode(p)
	if err != nil {
		print(err.Error())
	}
	filexml.Close()
	jsonFile := "person.json"
	xmlFile := "person.xml"
	// Leer y decodificar JSON
	var personFromJson Person
	readAndDecode(jsonFile, &personFromJson, "json")

	// Leer y decodificar XML
	var personFromXml Person
	readAndDecode(xmlFile, &personFromXml, "xml")

	// Opcional: imprimir los datos leídos para verificación
	fmt.Println("Datos desde JSON:", personFromJson)
	fmt.Println("Datos desde XML:", personFromXml)

	// Eliminar archivos
	err = os.Remove(jsonFile)
	if err != nil {
		print(err.Error())
	}
	err = os.Remove(xmlFile)
	if err != nil {
		print(err.Error())
	}

}
func readAndDecode(fileName string, person *Person, fileType string) {
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println("Error abriendo el archivo:", err)
		return
	}
	defer file.Close()

	data, _ := io.ReadAll(file)

	switch fileType {
	case "json":
		err := json.Unmarshal(data, person)
		if err != nil {
			print(err.Error())
		}
	case "xml":
		err := xml.Unmarshal(data, person)
		if err != nil {
			print(err.Error())
		}
	}
}
