package main

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"io"
	"os"
)

// # * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
// #  *
// #  * EJERCICIO:
// #  * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
// #  * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
// #  * - Nombre
// #  * - Edad
// #  * - Fecha de nacimiento
// #  * - Listado de lenguajes de programación
// #  * Muestra el contenido de los archivos.
// #  * Borrarlo despues

// # XML

type Languages struct {
	Item []string `xml: "item"`
}

type Programer struct {
	XMLName  xml.Name  `xml: "Programer"`
	Name     string    `xml:"name"`
	Age      string    `xml:"age"`
	Cumple   string    `xml:"cumple"`
	Language Languages `xml:"language"`
}

func ReadXML(fileName string) *Programer {
	file, _ := os.Open(fileName)
	defer file.Close()
	reader, _ := io.ReadAll(file)
	var programer *Programer
	xml.Unmarshal(reader, &programer)
	return programer

}

func WriteXML(fileName string, programer Programer) {

	file, _ := os.Create(fileName)
	defer file.Close()
	output, e := xml.MarshalIndent(programer, "", " ")
	if e != nil {
		fmt.Println(e)
	}
	file.Write([]byte(xml.Header))
	file.Write(output)

}

//JSON

type LanguagesJ struct {
	Item []string `json: "item"`
}

type ProgramerJ struct {
	Name     string    `json:"name"`
	Age      string    `json:"age"`
	Cumple   string    `json:"cumple"`
	Language Languages `json:"language"`
}

func ReadJson(file string) *ProgramerJ {
	f, _ := os.Open(file)
	reader, _ := io.ReadAll(f)
	defer f.Close()
	var programer *ProgramerJ
	json.Unmarshal(reader, &programer)
	return programer

}

func WriteJson(file string, programer *ProgramerJ) {
	f, _ := os.Create(file)
	defer f.Close()
	salida, _ := json.MarshalIndent(programer, "", " ")
	_, err := f.Write(salida)
	if err != nil {
		fmt.Println((err))
	}
}

func main() {
	fileName := "programer.xml"
	fileNamej := "programer.json"
	programer := Programer{
		Name:   "juana",
		Age:    "23",
		Cumple: "1.1.1900",
		Language: Languages{
			[]string{"Python", "GO", "HTML"},
		},
	}
	programerj := ProgramerJ{
		Name:   "Petra",
		Age:    "23",
		Cumple: "1.1.1900",
		Language: Languages{
			[]string{"Python", "PASCAL", "JAVA"},
		},
	}

	WriteXML(fileName, programer)
	var NewProgramer *Programer
	NewProgramer = ReadXML(fileName)
	fmt.Printf("XML NAME : %v, \n Nombre : %v \n Edad : %v\n Cumle : %v\n Language :  %v\n", NewProgramer.XMLName, NewProgramer.Name, NewProgramer.Age, NewProgramer.Cumple, NewProgramer.Language)
	WriteJson(fileNamej, &programerj)
	var NewProgramerj *ProgramerJ
	NewProgramerj = ReadJson(fileNamej)
	fmt.Printf("JSON FILE  \n Nombre : %v \n Edad : %v\n Cumple : %v\n Language :  %v\n", NewProgramerj.Name, NewProgramerj.Age, NewProgramerj.Cumple, NewProgramerj.Language)

}
