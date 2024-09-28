package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
	"unicode"
)

type Person struct {
	Name string
	Age  int
}

// Contact struct represents a contact in the agenda
type Contact struct {
	Name  string
	Phone string
}

// Agenda struct represents the agenda of contacts
type Agenda struct {
	Contacts []Contact
}

// NewAgenda creates a new empty agenda
func NewAgenda() *Agenda {
	return &Agenda{Contacts: []Contact{}}
}

// AddContact adds a new contact to the agenda
func (a *Agenda) AddContact(name, phone string) {
	a.Contacts = append(a.Contacts, Contact{Name: name, Phone: phone})
}

// UpdateContact updates an existing contact's phone number
func (a *Agenda) UpdateContact(name, phone string) bool {
	for i, c := range a.Contacts {
		if c.Name == name {
			a.Contacts[i].Phone = phone
			return true
		}
	}
	return false
}

// DeleteContact deletes a contact by name
func (a *Agenda) DeleteContact(name string) bool {
	for i, c := range a.Contacts {
		if c.Name == name {
			a.Contacts = append(a.Contacts[:i], a.Contacts[i+1:]...)
			return true
		}
	}
	return false
}

// SearchContact searches for a contact by name
func (a *Agenda) SearchContact(name string) *Contact {
	for _, c := range a.Contacts {
		if c.Name == name {
			return &c
		}
	}
	return nil
}

// ListContacts lists all contacts sorted by name
func (a *Agenda) ListContacts() {
	sort.Slice(a.Contacts, func(i, j int) bool {
		return a.Contacts[i].Name < a.Contacts[j].Name
	})
	for _, c := range a.Contacts {
		fmt.Printf("Name: %s, Phone: %s\n", c.Name, c.Phone)
	}
}

// ValidPhoneNumber checks if the phone number is valid
func ValidPhoneNumber(phone string) bool {
	if len(phone) > 11 {
		return false
	}
	for _, c := range phone {
		if !unicode.IsDigit(c) {
			return false
		}
	}
	return true
}

// ReadInput reads input from the user
func ReadInput(prompt string) string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(prompt)
	input, _ := reader.ReadString('\n')
	return strings.TrimSpace(input)
}

func main() {
	// Arrays
	arr := [5]int{1, 2, 3, 4, 5}
	fmt.Println("Array:", arr)
	arr[2] = 10
	fmt.Println("Updated Array:", arr)
	fmt.Println("----------------------------------------")

	// Slices
	slice := []int{5, 3, 4, 1, 2}
	fmt.Println("Slice:", slice)
	slice = append(slice, 6)
	fmt.Println("Appended Slice:", slice)
	sort.Ints(slice)
	fmt.Println("Sorted Slice:", slice)
	slice = slice[:len(slice)-1]
	fmt.Println("Slice after deletion:", slice)
	fmt.Println("----------------------------------------")

	// Maps
	m := make(map[string]int)
	m["one"] = 1
	m["two"] = 2
	m["three"] = 3
	fmt.Println("Map:", m)
	m["two"] = 22
	fmt.Println("Updated Map:", m)
	delete(m, "three")
	fmt.Println("Map after deletion:", m)

	// Sorting map keys
	keys := make([]string, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	fmt.Println("Sorted Map Keys:", keys)
	fmt.Println("----------------------------------------")

	// Structs
	person := Person{"Alice", 30}
	fmt.Println("Struct:", person)
	person.Age = 31
	fmt.Println("Updated Struct:", person)

	// extra exercise
	agenda := NewAgenda()
	for {
		fmt.Println("\nChoose an option:")
		fmt.Println("1. Add contact")
		fmt.Println("2. Update contact")
		fmt.Println("3. Delete contact")
		fmt.Println("4. Search contact")
		fmt.Println("5. List contacts")
		fmt.Println("6. Exit")

		choice := ReadInput("Enter choice: ")
		switch choice {
		case "1":
			name := ReadInput("Enter name: ")
			phone := ReadInput("Enter phone number: ")
			if ValidPhoneNumber(phone) {
				agenda.AddContact(name, phone)
				fmt.Println("Contact added.")
			} else {
				fmt.Println("Invalid phone number.")
			}
		case "2":
			name := ReadInput("Enter name: ")
			phone := ReadInput("Enter new phone number: ")
			if ValidPhoneNumber(phone) {
				if agenda.UpdateContact(name, phone) {
					fmt.Println("Contact updated.")
				} else {
					fmt.Println("Contact not found.")
				}
			} else {
				fmt.Println("Invalid phone number.")
			}
		case "3":
			name := ReadInput("Enter name: ")
			if agenda.DeleteContact(name) {
				fmt.Println("Contact deleted.")
			} else {
				fmt.Println("Contact not found.")
			}
		case "4":
			name := ReadInput("Enter name: ")
			contact := agenda.SearchContact(name)
			if contact != nil {
				fmt.Printf("Contact found - Name: %s, Phone: %s\n", contact.Name, contact.Phone)
			} else {
				fmt.Println("Contact not found.")
			}
		case "5":
			agenda.ListContacts()
		case "6":
			fmt.Println("Exiting.")
			return
		default:
			fmt.Println("Invalid choice. Please try again.")
		}
	}
}
