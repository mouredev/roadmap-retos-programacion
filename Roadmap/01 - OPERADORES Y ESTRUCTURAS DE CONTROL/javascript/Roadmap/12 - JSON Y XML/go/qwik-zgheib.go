package main

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"os"
)

type Person struct {
	Name                 string
	Age                  int
	BirthDate            string
	ProgrammingLanguages []string
}

// Serializer interface
type Serializer interface {
	Serialize(data Person, filename string) error
	Deserialize(filename string) (Person, error)
}

// JSONSerializer struct implementing Serializer interface
type JSONSerializer struct{}

func (js JSONSerializer) Serialize(data Person, filename string) error {
	file, err := json.MarshalIndent(data, "", "  ")
	if err != nil {
		return err
	}
	return os.WriteFile(filename, file, 0644)
}

func (js JSONSerializer) Deserialize(filename string) (Person, error) {
	var person Person
	file, err := os.ReadFile(filename)
	if err != nil {
		return person, err
	}
	err = json.Unmarshal(file, &person)
	return person, err
}

// XMLSerializer struct implementing Serializer interface
type XMLSerializer struct{}

func (xs XMLSerializer) Serialize(data Person, filename string) error {
	file, err := xml.MarshalIndent(data, "", "  ")
	if err != nil {
		return err
	}
	return os.WriteFile(filename, file, 0644)
}

func (xs XMLSerializer) Deserialize(filename string) (Person, error) {
	var person Person
	file, err := os.ReadFile(filename)
	if err != nil {
		return person, err
	}
	err = xml.Unmarshal(file, &person)
	return person, err
}

type SerializerFactory struct{}

func (sf SerializerFactory) GetSerializer(format string) Serializer {
	switch format {
	case "json":
		return JSONSerializer{}
	case "xml":
		return XMLSerializer{}
	default:
		return nil
	}
}

func main() {
	person := Person{
		Name:                 "Qwik zgheib",
		Age:                  30,
		BirthDate:            "2002-11-09",
		ProgrammingLanguages: []string{"Go", "Java", "Python"},
	}

	factory := SerializerFactory{}

	jsonSerializer := factory.GetSerializer("json")
	xmlSerializer := factory.GetSerializer("xml")

	jsonFile := "qwik-zgheib.json"
	xmlFile := "qwik-zgheib.xml"

	// Serialize to JSON
	err := jsonSerializer.Serialize(person, jsonFile)
	if err != nil {
		fmt.Println("Err serializing to JSON:", err)
	}

	// Serialize to XML
	err = xmlSerializer.Serialize(person, xmlFile)
	if err != nil {
		fmt.Println("Err serializing to XML:", err)
	}

	// Deserialize from JSON
	jsonPerson, err := jsonSerializer.Deserialize(jsonFile)
	if err != nil {
		fmt.Println("Err deserializing JSON:", err)
	} else {
		fmt.Println("JSON deserialized:", jsonPerson)
	}

	// Deserialize from XML
	xmlPerson, err := xmlSerializer.Deserialize(xmlFile)
	if err != nil {
		fmt.Println("Err deserializing XML:", err)
	} else {
		fmt.Println("XML deserialized:", xmlPerson)
	}

	// Delete the JSON file
	err = os.Remove(jsonFile)
	if err != nil {
		fmt.Println("Err deleting JSON file:", err)
	}

	// Delete the XML file
	err = os.Remove(xmlFile)
	if err != nil {
		fmt.Println("Err deleting XML file:", err)
	}
}
