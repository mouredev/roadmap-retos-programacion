package main

import (	
	"encoding/json"
	"encoding/xml"
	"fmt"
	"os"
	"time"
)

type Datos struct {
	Nombre string
	Edad int
	FechaNacimiento time.Time
	Lenguajes []string
}

var datosGerardo = Datos{
	Nombre: "Gerardo",
	Edad: 36,
	FechaNacimiento: time.Date(1987, time.July, 3, 0, 0, 0, 0, time.UTC),
	Lenguajes: []string{"Go", "Python", "JavaScript", "Java", "TypeScript", "Kotlin", "Dart"},
}

var datosJuan = Datos{
	Nombre: "Juan",
	Edad: 37,
	FechaNacimiento: time.Date(1986, time.July, 3, 0, 0, 0, 0, time.UTC),
	Lenguajes: []string{"Rust", "C", "C++", "C#", "Swift", "Objective-C", "Ruby"},
}

func main() {
	if _, err := os.Stat("thegera4.xml"); err == nil {

		file, err := os.Open("thegera4.xml")
		if err != nil {
			fmt.Println("Error al abrir el archivo:", err)
			return
		}

		readAndShowXML(file)

		file.Close()

		err = os.Remove("thegera4.xml")
		if err != nil {
			fmt.Println("Error al borrar el archivo:", err)
			return
		}

		return
	}

	file := createFile("thegera4.xml")

	err := writeToXML(file, datosGerardo)
	if err != nil { 
		fmt.Println("Error al escribir en el archivo:", err)
		return
	}

	err = writeToXML(file, datosJuan)
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return
	}
	
	file.Close()

	file, err = os.Open("thegera4.xml")
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}
	readAndShowXML(file)
	file.Close()

	time.Sleep(2 * time.Second)
	err = os.Remove("thegera4.xml")
	if err != nil {
		fmt.Println("Error al borrar el archivo:", err)
		return
	}

	// Dificultad extra
	if _, err := os.Stat("thegera4.json"); err == nil {

		file, err := os.Open("thegera4.json")
		if err != nil {
			fmt.Println("Error al abrir el archivo:", err)
			return
		}

		readAndShowJSON(file)

		file.Close()

		err = os.Remove("thegera4.json")
		if err != nil {
			fmt.Println("Error al borrar el archivo:", err)
			return
		}

		return
	}

	datos := []Datos{datosGerardo, datosJuan}
	
	file = createFile("thegera4.json")

	err = writeToJSON(file, datos)
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return
	}

	file.Close()

	file, err = os.Open("thegera4.json")
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}

	readAndShowJSON(file)
	file.Close()

	time.Sleep(2 * time.Second)
	err = os.Remove("thegera4.json")
	if err != nil {
		fmt.Println("Error al borrar el archivo:", err)
		return
	}

}

func createFile(name string) *os.File {
	file, err := os.Create(name)
	if err != nil {
		fmt.Println("Error al crear el archivo:", err)
		return nil
	}
	return file
}

func writeToXML(file *os.File, data Datos) error {
	xmlData, err := xml.MarshalIndent(data, "", "    ")
	if err != nil {
		fmt.Println("Error al convertir a XML:", err)
		return err
	}

	_, err = file.Write(xmlData)
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return err
	}

	_, err = file.WriteString("\n")
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return err
	}
	return nil
}

func writeToJSON(file *os.File, data []Datos) error {
	jsonData, err := json.MarshalIndent(data, "", "    ")
	if err != nil {
		fmt.Println("Error al convertir a JSON:", err)
		return err
	}

	_, err = file.Write(jsonData)
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return err
	}

	_, err = file.WriteString("\n")
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return err
	}

	return nil
}

func readAndShowXML(file *os.File) {
	fileInfo, err := file.Stat()
	if err != nil {
		fmt.Println("Error al obtener información del archivo:", err)
		return
	}

	fileData := make([]byte, fileInfo.Size())
	_, err = file.Read(fileData)
	if err != nil {
		fmt.Println("Error al leer el archivo:", err)
		return
	}

	fmt.Println(string(fileData))
	file.Close()
}

func readAndShowJSON(file *os.File) {
	fileInfo, err := file.Stat()
	if err != nil {
		fmt.Println("Error al obtener información del archivo:", err)
		return
	}

	fileData := make([]byte, fileInfo.Size())
	_, err = file.Read(fileData)
	if err != nil {
		fmt.Println("Error al leer el archivo:", err)
		return
	}

	var datos []Datos
	err = json.Unmarshal(fileData, &datos)
	if err != nil {
		fmt.Println("Error al convertir de JSON:", err)
		return
	}

	for _, dato := range datos {
		fmt.Println("Nombre:", dato.Nombre)
		fmt.Println("Edad:", dato.Edad)
		fmt.Println("Fecha de nacimiento:", dato.FechaNacimiento)
		fmt.Println("Lenguajes:")
		for _, lenguaje := range dato.Lenguajes {
			fmt.Println("    -", lenguaje)
		}
	}
	file.Close()
}