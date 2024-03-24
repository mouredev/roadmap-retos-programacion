package main

import (
	"bufio"
	"encoding/json"
	"encoding/xml"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

type JsonAuthor struct {
	Age                  int8      `json:"age"`
	BornDate             time.Time `json:"bornDate"`
	Name                 string    `json:"name"`
	ProgrammingLanguages []string  `json:"programmingLanguages"`
}

type XmlAuthor struct {
	XMLName              xml.Name  `xml:"author"`
	Age                  int8      `xml:"age"`
	BornDate             time.Time `xml:"born-date"`
	Name                 string    `xml:"name"`
	ProgrammingLanguages []string  `xml:"programming-languages>programming-language"`
}

/* -------------------------------------------------------------------------- */
/*                              JSON FILE (CLASS)                             */
/* -------------------------------------------------------------------------- */

type JsonFile struct {
	path      string
	isDeleted bool
}

func newJsonFile(path string, initialContent JsonAuthor) (*JsonFile, error) {
	var jsonFile JsonFile = JsonFile{path: path, isDeleted: false}

	file, createErr := os.Create(jsonFile.path)
	if createErr != nil {
		return nil, createErr
	}

	file.Close()
	jsonFile.writeContent(initialContent)

	return &jsonFile, nil
}

func (jsonFile *JsonFile) getContent() (JsonAuthor, error) {
	content, openErr := os.ReadFile(jsonFile.path)
	if openErr != nil {
		return JsonAuthor{}, openErr
	}

	var jsonAuthor JsonAuthor
	unmarshalErr := json.Unmarshal(content, &jsonAuthor)
	if unmarshalErr != nil {
		return JsonAuthor{}, unmarshalErr
	}

	return jsonAuthor, nil
}

func (jsonFile *JsonFile) appendLanguage(programmingLanguage string) error {
	content, contentErr := jsonFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	content.ProgrammingLanguages = append(content.ProgrammingLanguages, programmingLanguage)

	var writeErr error = jsonFile.writeContent(content)
	if writeErr != nil {
		return writeErr
	}

	return nil
}

func (jsonFile *JsonFile) deleteFile() error {
	var removeErr error = os.Remove(jsonFile.path)
	if removeErr != nil {
		return removeErr
	}
	jsonFile.isDeleted = true

	return nil
}

func (jsonFile *JsonFile) removeLanguage(programmingLanguage string) error {
	var sanitizedProgrammingLanguage string = strings.ToUpper(programmingLanguage)

	content, contentErr := jsonFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	var sanitizedProgrammingLanguages []string = []string{}
	for _, language := range content.ProgrammingLanguages {
		if strings.ToUpper(language) != sanitizedProgrammingLanguage {
			sanitizedProgrammingLanguages = append(sanitizedProgrammingLanguages, language)
		}
	}
	content.ProgrammingLanguages = sanitizedProgrammingLanguages

	var writeErr error = jsonFile.writeContent(content)
	if writeErr != nil {
		return writeErr
	}

	return nil
}

func (jsonFile *JsonFile) updateAge(age int8) error {
	content, contentErr := jsonFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	content.Age = age
	jsonFile.writeContent(content)

	return nil
}

func (jsonFile *JsonFile) updateBornDate(bornDate time.Time) error {
	content, contentErr := jsonFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	content.BornDate = bornDate
	jsonFile.writeContent(content)

	return nil
}

func (jsonFile *JsonFile) updateName(name string) error {
	content, contentErr := jsonFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	content.Name = name
	jsonFile.writeContent(content)

	return nil
}

func (jsonFile *JsonFile) writeContent(content JsonAuthor) error {
	stringifiedContent, marshalIndentErr := json.MarshalIndent(content, "", "\t")
	if marshalIndentErr != nil {
		return marshalIndentErr
	}

	var writeErr error = os.WriteFile(jsonFile.path, stringifiedContent, os.ModeAppend)
	if writeErr != nil {
		return writeErr
	}

	return nil
}

/* -------------------------------------------------------------------------- */
/*                              XML FILE (CLASS)                              */
/* -------------------------------------------------------------------------- */

type XmlFile struct {
	path      string
	isDeleted bool
}

func newXmlFile(path string, initialContent XmlAuthor) (*XmlFile, error) {
	var xmlFile XmlFile = XmlFile{path: path, isDeleted: false}

	file, createErr := os.Create(xmlFile.path)
	if createErr != nil {
		return nil, createErr
	}

	file.Close()
	xmlFile.writeContent(initialContent)

	return &xmlFile, nil
}

func (xmlFile *XmlFile) getContent() (XmlAuthor, error) {
	content, openErr := os.ReadFile(xmlFile.path)
	if openErr != nil {
		return XmlAuthor{}, openErr
	}

	fmt.Printf("\n%s\n", string(content))

	var xmlAuthor XmlAuthor
	unmarshalErr := xml.Unmarshal(content, &xmlAuthor)
	if unmarshalErr != nil {
		return XmlAuthor{}, unmarshalErr
	}

	fmt.Printf("\n%v\n", xmlAuthor)

	return xmlAuthor, nil
}

func (xmlFile *XmlFile) appendLanguage(programmingLanguage string) error {
	content, contentErr := xmlFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	content.ProgrammingLanguages = append(content.ProgrammingLanguages, programmingLanguage)

	var writeErr error = xmlFile.writeContent(content)
	if writeErr != nil {
		return writeErr
	}

	return nil
}

func (xmlFile *XmlFile) deleteFile() error {
	var removeErr error = os.Remove(xmlFile.path)
	if removeErr != nil {
		return removeErr
	}
	xmlFile.isDeleted = true

	return nil
}

func (xmlFile *XmlFile) removeLanguage(programmingLanguage string) error {
	content, contentErr := xmlFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	var sanitizedProgrammingLanguages []string = []string{}
	for _, language := range content.ProgrammingLanguages {
		if strings.ToUpper(language) != strings.ToUpper(programmingLanguage) {
			sanitizedProgrammingLanguages = append(sanitizedProgrammingLanguages, language)
		}
	}
	content.ProgrammingLanguages = sanitizedProgrammingLanguages

	var writeErr error = xmlFile.writeContent(content)
	if writeErr != nil {
		return writeErr
	}

	return nil
}

func (xmlFile *XmlFile) updateAge(age int8) error {
	content, contentErr := xmlFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	content.Age = age
	xmlFile.writeContent(content)

	return nil
}

func (xmlFile *XmlFile) updateBornDate(bornDate time.Time) error {
	content, contentErr := xmlFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	content.BornDate = bornDate
	xmlFile.writeContent(content)

	return nil
}

func (xmlFile *XmlFile) updateName(name string) error {
	content, contentErr := xmlFile.getContent()
	if contentErr != nil {
		return contentErr
	}

	content.Name = name
	xmlFile.writeContent(content)

	return nil
}

func (xmlFile *XmlFile) writeContent(content XmlAuthor) error {
	stringifiedContent, marshalIndentErr := xml.MarshalIndent(content, "", "\t")
	if marshalIndentErr != nil {
		return marshalIndentErr
	}

	var writeErr error = os.WriteFile(xmlFile.path, stringifiedContent, os.ModeAppend)
	if writeErr != nil {
		return writeErr
	}

	return nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		JSON and XML files...
	*/

	fmt.Println("JSON and XML files...")

	const jsonFilePath string = "author.json"
	const xmlFilePath string = "author.xml"

	// Delete files if exist
	if _, err := os.Stat(jsonFilePath); err != nil {
		if removeErr := os.Remove(jsonFilePath); removeErr == nil {
			log.Fatal(removeErr)
		}
	}

	if _, err := os.Stat(xmlFilePath); err != nil {
		if removeErr := os.Remove(xmlFilePath); removeErr == nil {
			log.Fatal(removeErr)
		}
	}

	// Create files and append content
	jsonFile, jsonCreateErr := os.Create(jsonFilePath)
	if jsonCreateErr != nil {
		log.Fatal(jsonCreateErr)
	}

	xmlFile, xmlCreateErr := os.Create(xmlFilePath)
	if xmlCreateErr != nil {
		log.Fatal(xmlCreateErr)
	}

	authorJsonData := JsonAuthor{
		Age:                  22,
		BornDate:             time.Date(2002, time.February, 20, 0, 0, 0, 0, time.UTC),
		Name:                 "Lucas",
		ProgrammingLanguages: []string{"TypeScript", "Python", "Go"},
	}

	var authorXmlData XmlAuthor = XmlAuthor{
		Age:                  22,
		BornDate:             time.Date(2002, time.February, 20, 0, 0, 0, 0, time.UTC),
		Name:                 "Lucas",
		ProgrammingLanguages: []string{"TypeScript"},
	}

	jsonFileNewContent, jsonFileNewContentErr := json.MarshalIndent(authorJsonData, "", "\t")
	if jsonFileNewContentErr != nil {
		log.Fatal(jsonFileNewContentErr)
	}

	xmlFileNewContent, xmlFileNewContentErr := xml.MarshalIndent(authorXmlData, "", "\t")
	if xmlFileNewContentErr != nil {
		log.Fatal(xmlFileNewContentErr)
	}

	jsonFile.Write(jsonFileNewContent)
	xmlFile.Write(xmlFileNewContent)

	jsonFile.Close()
	xmlFile.Close()

	// Print files content
	jsonFileContent, jsonFileContentErr := os.ReadFile(jsonFilePath)
	if jsonFileContentErr != nil {
		log.Fatal(jsonFileContentErr)
	}

	xmlFileContent, xmlFileContentErr := os.ReadFile(xmlFilePath)
	if xmlFileContentErr != nil {
		log.Fatal(xmlFileContentErr)
	}

	fmt.Printf("\n%s\n", string(jsonFileContent))
	fmt.Printf("\n%s\n", string(xmlFileContent))

	// Delete files
	os.Remove(jsonFilePath)
	os.Remove(xmlFilePath)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #\n")

	/*
		Additional files...
	*/

	fmt.Println("Additional files...")

	var jsonInitialContent JsonAuthor = JsonAuthor{
		Age:                  22,
		BornDate:             time.Date(2002, time.February, 20, 0, 0, 0, 0, time.UTC),
		Name:                 "Lucas",
		ProgrammingLanguages: []string{"Go"},
	}

	jsonFileObj, jsonFileErr := newJsonFile("additional-challenge.json", jsonInitialContent)
	if jsonFileErr != nil {
		log.Fatal(jsonFileErr)
	}

	var shouldExit bool = false
	reader := bufio.NewReader(os.Stdin)

	for !shouldExit {
		fmt.Print("\nSelect an operation ('Append language', 'Print', 'Remove language', 'Update age', 'Update born date', 'Update name', or 'Exit'): ")
		operation, readErr := reader.ReadString('\n')
		if readErr != nil {
			operation = ""
		}

		var operationFmt string = strings.ToUpper(strings.TrimSpace(operation))

	jsonActions:
		switch operationFmt {
		case "APPEND LANGUAGE":
			fmt.Print("\nNew programming language: ")
			programmingLanguage, readErr := reader.ReadString('\n')
			if readErr != nil {
				break jsonActions
			}

			programmingLanguage = strings.TrimSpace(programmingLanguage)
			jsonFileObj.appendLanguage(programmingLanguage)

		case "PRINT":
			content, contentErr := jsonFileObj.getContent()
			if contentErr != nil {
				log.Fatal(contentErr)
			}

			fmt.Printf("\nAge: %d", content.Age)
			fmt.Printf("\nBorn date: %s", content.BornDate)
			fmt.Printf("\nName: %s", content.Name)
			fmt.Printf("\nProgramming languages: %s\n", content.ProgrammingLanguages)

		case "REMOVE LANGUAGE":
			fmt.Print("\nProgramming language: ")
			programmingLanguage, readErr := reader.ReadString('\n')
			if readErr != nil {
				break jsonActions
			}

			programmingLanguage = strings.TrimSpace(programmingLanguage)
			jsonFileObj.removeLanguage(programmingLanguage)

		case "UPDATE AGE":
			var newAge int8

			fmt.Print("\nNew age: ")
			_, scanErr := fmt.Scanf("%d\n", &newAge)
			if scanErr != nil {
				break jsonActions
			}

			jsonFileObj.updateAge(newAge)

		case "UPDATE BORN DATE":
			fmt.Print("\nNew born date (year-month-day): ")
			newBornDate, readErr := reader.ReadString('\n')
			if readErr != nil {
				break jsonActions
			}

			newBornDate = strings.TrimSpace(newBornDate)

			var dateInfo []string = strings.Split(newBornDate, "-")
			if len(dateInfo) != 3 {
				break jsonActions
			}

			year, atoiErr := strconv.Atoi(dateInfo[0])
			if atoiErr != nil {
				break jsonActions
			}

			month, atoiErr := strconv.Atoi(dateInfo[1])
			if atoiErr != nil {
				break jsonActions
			}

			day, atoiErr := strconv.Atoi(dateInfo[2])
			if atoiErr != nil {
				break jsonActions
			}

			jsonFileObj.updateBornDate(time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.UTC))

		case "UPDATE NAME":
			fmt.Print("\nNew name: ")
			newName, readErr := reader.ReadString('\n')
			if readErr != nil {
				break jsonActions
			}

			newName = strings.TrimSpace(newName)
			jsonFileObj.updateName(newName)

		case "EXIT":
			var deleteFileErr error = jsonFileObj.deleteFile()
			if deleteFileErr != nil {
				log.Fatal(deleteFileErr)
			}

			shouldExit = true

		default:
			fmt.Println("\nInvalid operation! Try again...")
		}
	}

	var xmlInitialContent XmlAuthor = XmlAuthor{
		Age:                  22,
		BornDate:             time.Date(2002, time.February, 20, 0, 0, 0, 0, time.UTC),
		Name:                 "Lucas",
		ProgrammingLanguages: []string{"Go (Golang)"},
	}

	xmlFileObj, xmlFileErr := newXmlFile("additional-challenge.xml", xmlInitialContent)
	if xmlFileErr != nil {
		log.Fatal(xmlFileErr)
	}

	shouldExit = false

	for !shouldExit {
		fmt.Print("\nSelect an operation ('Append language', 'Print', 'Remove language', 'Update age', 'Update born date', 'Update name', or 'Exit'): ")
		operation, readErr := reader.ReadString('\n')
		if readErr != nil {
			operation = ""
		}

		var operationFmt string = strings.ToUpper(strings.TrimSpace(operation))

	xmlActions:
		switch operationFmt {
		case "APPEND LANGUAGE":
			fmt.Print("\nNew programming language: ")
			programmingLanguage, readErr := reader.ReadString('\n')
			if readErr != nil {
				break xmlActions
			}

			programmingLanguage = strings.TrimSpace(programmingLanguage)
			xmlFileObj.appendLanguage(programmingLanguage)

		case "PRINT":
			content, contentErr := xmlFileObj.getContent()
			if contentErr != nil {
				log.Fatal(contentErr)
			}

			fmt.Printf("\nAge: %d", content.Age)
			fmt.Printf("\nBorn date: %s", content.BornDate)
			fmt.Printf("\nName: %s", content.Name)
			fmt.Printf("\nProgramming languages: %s\n", content.ProgrammingLanguages)

		case "REMOVE LANGUAGE":
			fmt.Print("\nProgramming language: ")
			programmingLanguage, readErr := reader.ReadString('\n')
			if readErr != nil {
				break xmlActions
			}

			programmingLanguage = strings.TrimSpace(programmingLanguage)
			xmlFileObj.removeLanguage(programmingLanguage)

		case "UPDATE AGE":
			var newAge int8

			fmt.Print("\nNew age: ")
			_, scanErr := fmt.Scanf("%d\n", &newAge)
			if scanErr != nil {
				break xmlActions
			}

			xmlFileObj.updateAge(newAge)

		case "UPDATE BORN DATE":
			fmt.Print("\nNew born date (year-month-day): ")
			newBornDate, readErr := reader.ReadString('\n')
			if readErr != nil {
				break xmlActions
			}

			newBornDate = strings.TrimSpace(newBornDate)

			var dateInfo []string = strings.Split(newBornDate, "-")
			if len(dateInfo) != 3 {
				break xmlActions
			}

			year, atoiErr := strconv.Atoi(dateInfo[0])
			if atoiErr != nil {
				break xmlActions
			}

			month, atoiErr := strconv.Atoi(dateInfo[1])
			if atoiErr != nil {
				break xmlActions
			}

			day, atoiErr := strconv.Atoi(dateInfo[2])
			if atoiErr != nil {
				break xmlActions
			}

			xmlFileObj.updateBornDate(time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.UTC))

		case "UPDATE NAME":
			fmt.Print("\nNew name: ")
			newName, readErr := reader.ReadString('\n')
			if readErr != nil {
				break xmlActions
			}

			newName = strings.TrimSpace(newName)
			xmlFileObj.updateName(newName)

		case "EXIT":
			var deleteFileErr error = xmlFileObj.deleteFile()
			if deleteFileErr != nil {
				log.Fatal(deleteFileErr)
			}

			shouldExit = true

		default:
			fmt.Println("\nInvalid operation! Try again...")
		}
	}
}
