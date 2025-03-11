package main

import (
	"encoding/json"
	"encoding/xml"
	"errors"
	"fmt"
	"os"
	"strings"
)

var errorDecode = errors.New("Error: no se pudo decodificar el archivo")
var errorOpen = errors.New("Error: no se pudo abrir el archivo")
var errorCreate = errors.New("Error: no se pudo crear el archivo")
var errorDelete = errors.New("Error: no se pudo eliminar el archivo")

// En go, tenemos el paquete "encoding", para tranajar con archivos como:
// encoding/xml: Codificación y decodificación en XML.
// encoding/json: Codificación y decodificación en JSON.
// encoding/base64: Codificación y decodificación en Base64.
// encoding/csv: Lectura y escritura de archivos CSV.
// encoding/gob: Codificación y decodificación en formato GOB de go.
// encoding/hex: Codificación y decodificación en formato hexadecimal.
// encoding/ascii85: Codificación y decodificación en formato ASCII85
// cada uno de estos subpaquetes proporciona herraientas para manejar distintos formatos en go.

type People struct {
	XMLName xml.Name `xml:"people"`
	People  []Person `xml:"person" json:"person"`
}

type Person struct {
	Name                 string   `xml:"name" json:"name"`
	Age                  uint8    `xml:"age" json:"age"`
	BirthDate            string   `xml:"birthDate" json:"birthDate"`
	ProgrammingLanguajes []string `xml:"proLang" json:"proLang"`
}

var xmlFile = "MiguelP-Dev.xml"
var jsonFile = "MiguelP-Dev.json"

var data = Person{Name: "Miguel", Age: uint8(31), BirthDate: "13/10/1993", ProgrammingLanguajes: []string{"Go", "JavaScript"}}

func main() {
	makeFile(xmlFile)
	makeFile(jsonFile)
	viewFile(jsonFile)
	viewFile(xmlFile)

	// Extra
	makeFile(xmlFile)
	makeFile(jsonFile)

	json := NewPerson(jsonFile)
	xml := NewPerson(xmlFile)

	fmt.Println("Json Class", json)
	fmt.Println("Xml Class", xml)

}

func makeFile(filename string) {
	file, err := os.Create(filename)
	if err != nil {
		fmt.Println("Error al crear el archivo:", err)
		return
	}
	defer file.Close()

	createdFileMessage := "Archivo creado con éxito: " + filename

	if strings.HasSuffix(filename, ".json") {
		people := []Person{
			data,
		}

		encoderJson := json.NewEncoder(file)
		encoderJson.SetIndent("", "	")
		if err := encoderJson.Encode(people); err != nil {
			fmt.Println("Error al codificar el archivo:", err)
			return
		}

		fmt.Println(createdFileMessage)

	} else if strings.HasSuffix(filename, ".xml") {
		people := People{
			People: []Person{
				data,
			}}

		encoder := xml.NewEncoder(file)
		encoder.Indent("", "	")
		if err = encoder.Encode(people); err != nil {
			fmt.Println("Error al codificar el archivo: ", err)
			return
		}

		fmt.Println(createdFileMessage)
	} else {
		err := os.Remove(filename)
		if err != nil {
			fmt.Println("Error al eliminar el archivo: ", err)
			return
		}
		return
	}

}

func viewFile(filename string) {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println(errorOpen, err)
		return
	}
	defer file.Close()

	if strings.HasSuffix(filename, ".xml") {
		var people People
		decoder := xml.NewDecoder(file)
		if err := decoder.Decode(&people); err != nil {
			fmt.Println(errorDecode, err)
			return
		}

		for _, person := range people.People {
			fmt.Printf("Name: %s, Age: %v, BirthDate: %s, Languajes: %s\n", person.Name, person.Age, person.BirthDate, person.ProgrammingLanguajes)
			err := os.Remove(filename)
			if err != nil {
				fmt.Println(errorDelete, err)
			}
		}

	} else if strings.HasSuffix(filename, ".json") {
		var people []Person
		decoder := json.NewDecoder(file)
		if err := decoder.Decode(&people); err != nil {
			fmt.Println(errorDecode, err)
		}

		for _, person := range people {
			fmt.Printf("Name: %s, Age: %v, BirthDate: %s, Languajes: %s\n", person.Name, person.Age, person.BirthDate, person.ProgrammingLanguajes)
			err := os.Remove(filename)
			if err != nil {
				fmt.Println(errorDelete, err)
			}
		}

	} else {
		err := os.Remove(filename)
		if err != nil {
			fmt.Println(errorDelete, err)
			return
		}
	}
	return
}

// Extra
/*
 DIFICULTAD EXTRA (opcional):
 Utilizando la lógica de creación de los archivos anteriores, crea un
 programa capaz de leer y transformar en una misma clase custom de tu
 lenguaje los datos almacenados en el XML y el JSON.
 Borra los archivos.
*/

func NewPerson(file string) []Person {
	f, err := os.Open(file)
	if err != nil {
		fmt.Println(errorOpen, err)
		return []Person{}
	}

	defer f.Close()

	var data []Person

	if strings.HasSuffix(file, ".json") {
		decoder := json.NewDecoder(f)
		if err := decoder.Decode(&data); err != nil {
			fmt.Println(errorDecode, err)
		}
	} else if strings.HasSuffix(file, ".xml") {
		var people People
		decoder := xml.NewDecoder(f)
		if err := decoder.Decode(&people); err != nil {
			fmt.Println(errorDecode, err)
		}

		for _, person := range people.People {
			data = append(data, person)
		}

	} else {
		return []Person{}
	}
	err = os.Remove(file)
	if err != nil {
		fmt.Println(errorDelete, err)
		return []Person{}
	}
	return data

}
