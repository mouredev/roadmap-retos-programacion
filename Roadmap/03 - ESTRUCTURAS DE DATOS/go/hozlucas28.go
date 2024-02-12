package main

import (
	"errors"
	"fmt"
	"regexp"
	"strings"
)

type Product struct {
	name  string
	price float32
}

type Form interface {
	Area() float64
	Perimeter() float64
}

type Contact struct {
	name        string
	phoneNumber string
}

func getContactName(msg string, msgOnInvalid string, shouldExist bool, contacts *[]Contact) (string, error) {
	var name string

	fmt.Printf(msg)
	fmt.Scan(&name)
	if name == "" {
		return "", errors.New("Input omitted")
	}

	condition := func(name *string) bool {
		if shouldExist {
			return !contactExist(name, contacts)
		}

		return contactExist(name, contacts)
	}

	for condition(&name) {
		fmt.Printf(msgOnInvalid)
		fmt.Scan(&name)
		if name == "" {
			return "", errors.New("Input omitted")
		}
	}

	return name, nil
}

func getPhoneNumber(msg string, msgOnInvalid string) (string, error) {
	var phoneNumber string

	fmt.Printf(msg)
	fmt.Scan(&phoneNumber)
	if phoneNumber == "" {
		return "", errors.New("Input omitted")
	}

	for !isValidPhoneNumber(&phoneNumber) {
		fmt.Printf(msgOnInvalid)
		fmt.Scan(&phoneNumber)
		if phoneNumber == "" {
			return "", errors.New("Input omitted")
		}
	}

	return phoneNumber, nil
}

func isValidPhoneNumber(phoneNumber *string) bool {
	match, _ := regexp.MatchString(`[^0-9]`, *phoneNumber)
	return len(*phoneNumber) <= 11 && !match

}

func contactExist(name *string, contacts *[]Contact) bool {
	var exist bool = false
	for i := 0; i < len(*contacts); i++ {
		if strings.ToUpper((*contacts)[i].name) == strings.ToUpper(*name) {
			return true
		}
	}

	return exist
}

func showContacts(contacts *[]Contact) {
	fmt.Print("[ ")
	for i := 0; i < len(*contacts); i++ {
		if i == len(*contacts)-1 {
			fmt.Printf("%s / %s", (*contacts)[i].name, (*contacts)[i].phoneNumber)
		} else {
			fmt.Printf("%s / %s, ", (*contacts)[i].name, (*contacts)[i].phoneNumber)
		}
	}
	fmt.Print(" ]")
}

func findContactIndex(name *string, contacts *[]Contact) (int, error) {
	for i := 0; i < len(*contacts); i++ {
		if strings.ToUpper((*contacts)[i].name) == strings.ToUpper(*name) {
			return i, nil
		}
	}

	return -1, errors.New("The contact doesn't exists")
}

func main() {
	/*
	   Structures...
	*/

	// Array
	array := [3]int{1, 2, 3}
	fmt.Printf("Array structure: <ARRAY NAME> := [<LENGTH>]<DATA TYPE>{<ELEMENTS...>}")
	fmt.Printf("\narray := [3]int{1, 2, 3} --> array = %d", array)

	// Matrix
	matrix := [3][2]int{{1, 2}, {3, 4}, {5, 6}}
	fmt.Printf("\n\nMatrix structure: <MATRIX NAME> := [<LENGTH OF ROWS>][<LENGTH OF COLUMNS>]<DATA TYPE>{<ROWS WITH ELEMENTS (COLUMNS)...>}")
	fmt.Printf("\nmatrix := [3][2]int{{1, 2}, {3, 4}, {5, 6}} --> matrix = ")
	fmt.Print(matrix)

	// Slice - Array with a length defined by the elements
	slice := []string{"Lucas", "Hoz"}
	fmt.Printf("\n\nSlice structure: <SLICE NAME> := []<DATA TYPE>{<ELEMENTS...>}")
	fmt.Printf("\nslice := []string{'Lucas', 'Hoz'} --> slice = ")
	fmt.Print(slice)

	// Map
	myMap := map[string]string{"firstName": "Lucas", "lastName": "Hoz"}
	fmt.Printf("\n\nMap structure: <MAP NAME> := map[<DATA TYPE OF KEYS>]<DATA TYPE OF VALUES>{PROPERTIES...}")
	fmt.Printf("\nmyMap := map[string]string{'firstName': 'Lucas', 'lastName': 'Hoz'} --> myMap = ")
	fmt.Print(myMap)

	// Struct
	fmt.Printf("\n\nStruct structure: type <STRUCT NAME> struct {<PARAMETERS...>}")
	fmt.Print("\ntype Product struct { name string; price float32 }")

	// Interface
	fmt.Printf("\n\nInterface structure: type <INTERFACE NAME> interface {<METHODS...>}")
	fmt.Print("\ntype Form interface { Area() float64; Perimeter() float64 }")

	fmt.Printf("\n\n# ---------------------------------------------------------------------------------- #")

	/*
	   Insert, delete, update, and sort operations
	*/

	mySlice := []int{1, 2, 3}
	myMap02 := map[string]string{"firstName": "Lucas", "lastName": "Hoz"}

	// Insert element/s at the end of a slice structure
	mySlice = append(mySlice, 4, 5)
	fmt.Printf("\n\nInsert element/s at the end of a slice structure: <SLICE NAME> = append(<SLICE NAME>, <ELEMENTS...>)")
	fmt.Printf("\n[1, 2, 3] = append([1, 2, 3], 4, 5) --> mySlice = ")
	fmt.Print(mySlice)

	// Delete an element of a slice structure
	mySlice = append(mySlice[:2], mySlice[2+1:]...)
	fmt.Printf("\n\nDelete an element of a slice structure: <SLICE NAME> = append(<SLICE NAME>[:<INDEX OF THE ELEMENT TO DELETE>], <SLICE NAME>[<INDEX OF THE ELEMENT TO DELETE> + 1:]...)")
	fmt.Printf("\n[1, 2, 3, 4, 5] = append([1, 2, 3, 4, 5][:2], [1, 2, 3, 4, 5][2 + 1:]...) --> mySlice = ")
	fmt.Print(mySlice)

	// Update an element of a slice structure
	mySlice[0] = 1 * 10
	fmt.Printf("\n\nUpdate an element of a slice structure: <SLICE NAME>[<INDEX OF THE ELEMENT TO UPDATE>] = <NEW VALUE>")
	fmt.Printf("\n[1, 2, 4, 5][0] = 1 * 10 --> mySlice = ")
	fmt.Print(mySlice)

	// Insert element in a map structure
	myMap02["country"] = "Argentina"
	fmt.Printf("\n\nInsert element in a map structure: <MAP NAME>[<KEY OF THE NEW ELEMENT>] = <VALUE>")
	fmt.Printf("\n{ 'firstName': 'Lucas', 'lastName': 'Hoz' }['country'] = 'Argentina' --> myMap02 = ")
	fmt.Print(myMap02)

	// Delete an element of a map structure
	delete(myMap02, "lastName")
	fmt.Printf("\n\nDelete an element of a map structure: delete(<MAP NAME>, <KEY OF THE PROPERTY TO DELETE>)")
	fmt.Printf("\ndelete({ 'country': 'Argentina', 'firstName': 'Lucas', 'lastName': 'Hoz' }, 'lastName') --> myMap02 = ")
	fmt.Print(myMap02)

	// Update an element of a map structure
	myMap02["firstName"] = "Nahuel"
	fmt.Printf("\n\nUpdate an element of a map structure: <MAP NAME>[<KEY OF THE ELEMENT TO UPDATE>] = <NEW VALUE>")
	fmt.Printf("\n{ 'country': 'Argentina', 'firstName': 'Lucas' }['firstName'] = 'Nahuel' --> myMap02 = ")
	fmt.Print(myMap02)

	fmt.Printf("\n\n# ---------------------------------------------------------------------------------- #")

	/*
	   Additional challenge...
	*/

	contacts := []Contact{
		{
			name:        "Juan",
			phoneNumber: "1115616",
		},
	}

	var operation string
	var exit bool = false
	for !exit {
		fmt.Printf("\n\n> Select an operation ('Show', 'Find', 'Insert', 'Update', 'Delete' or 'Exit'): ")
		fmt.Scan(&operation)

		switch strings.ToUpper(operation) {
		case "SHOW":
			if len(contacts) > 0 {
				fmt.Printf("Contacts: ")
				showContacts(&contacts)
			} else {
				fmt.Printf("There are no contacts listed!")
			}
			break

		case "FIND":
			name, nameError := getContactName("> Enter the name of the contact: ", "> The contact doesn't exists! Enter another name: ", true, &contacts)
			if nameError != nil {
				continue
			}

			index, _ := findContactIndex(&name, &contacts)
			fmt.Printf("Contact info: %s / %s", contacts[index].name, contacts[index].phoneNumber)
			break

		case "INSERT":
			name, nameError := getContactName("Enter the name of the new contact: ", "The contact already exists! Try with another name: ", false, &contacts)
			if nameError != nil {
				continue
			}

			phoneNumber, phoneNumberError := getPhoneNumber("Enter the phone number of new contact: ", "Invalid phone number! Enter a valid one: ")
			if phoneNumberError != nil {
				continue
			}

			contacts = append(contacts, Contact{name: name, phoneNumber: phoneNumber})

			fmt.Printf("Contact inserted!")
			break

		case "UPDATE":
			contactNameToUpdate, contactNameToUpdateError := getContactName("Enter the name of the contact to update: ", "The contact doesn't exists! Enter another name: ", true, &contacts)
			if contactNameToUpdateError != nil {
				continue
			}

			name, nameError := getContactName("Enter the new name:", "There is a contact with this name! Try another one: ", false, &contacts)
			if nameError != nil {
				continue
			}

			phoneNumber, phoneNumberError := getPhoneNumber("Enter the new phone number: ", "Invalid phone number! Enter a valid one: ")
			if phoneNumberError != nil {
				continue
			}

			contactIndex, _ := findContactIndex(&contactNameToUpdate, &contacts)
			contacts[contactIndex].name = name
			contacts[contactIndex].phoneNumber = phoneNumber

			fmt.Printf("Contact updated!")
			break

		case "DELETE":
			contactNameToDelete, contactNameToDeleteError := getContactName("Enter the name of the contact to delete: ", "The contact doesn't exists! Enter another name: ", true, &contacts)
			if contactNameToDeleteError != nil {
				continue
			}

			contactIndex, _ := findContactIndex(&contactNameToDelete, &contacts)
			contacts = append(contacts[:contactIndex], contacts[contactIndex+1:]...)

			fmt.Printf("Contact deleted!")
			break

		case "EXIT":
			fmt.Printf("Program finished!")
			exit = true
			break

		default:
			break
		}
	}
}
