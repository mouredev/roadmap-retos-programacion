/*
 * EXERCISE:
 * - Show examples of creating all the structures supported by default
 *   in your language.
 * - Use operations of insertion, deletion, updating, and sorting.
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

func main(){
	dataStructures()
	challenge()
}

func dataStructures() {
    fmt.Println("Array: Fixed size of elements of the same type")
    var arr [5]int
    fmt.Println(arr)

    fmt.Println("Slices: Dynamic resizable Arrays of the same type")
    slice := []int{1, 2, 3, 4}
    fmt.Println(slice)
	slice = append(slice, 152)
    fmt.Println("After insertion:", slice)
	// Inserting in a specific index. The function is quite complex in this way
	index := 1
    slice = append(slice[:index], append([]int{10}, slice[index:]...)...)
    fmt.Println("After inserting 10 at index 1:", slice)

    fmt.Println("Maps: Implementation of hash tables / dictionaries")
    m := map[string]int{"apple": 1, "banana": 2}
    fmt.Println(m)
	// add
	m["orange"] = 3
    fmt.Println("After adding 'orange':", m)
	// edit
    m["banana"] = 4
    fmt.Println("After editing 'banana':", m)
	// delete
	delete(m, "apple")
    fmt.Println("After deleting 'apple':", m)
	// Check if key exists
	if value, exists := m["orange"]; exists {
        fmt.Println("The value of 'orange' is:", value)
    }

    fmt.Println("Structs: User-defined types that groups variables of different types")
    type Person struct {
        name string
        age  int
    }
    p := Person{
        name: "pepe",
        age:  45,
    }
    fmt.Println(p)

    fmt.Println("Pointers: Holds the memory address of a value")
    var point *int = &p.age
    fmt.Println(point)

    fmt.Println("Interface: Define a set of method signatures")
    type Animal interface {
        Feed()
        Play()
    }
	// Use of the Interface outside this function.
	d.Feed()

	fmt.Println("Channels: Used for communication between go routines")
	ch := make(chan int)

    var wg sync.WaitGroup
    wg.Add(2) // We're waiting for 2 goroutines

    go sender(ch, &wg)
    go receiver(ch, &wg)

    wg.Wait() // Wait for both goroutines to finish
}

// U se of the interface Animal
type Dog struct {
	name string
}
var d = Dog{
	name: "pepe",
}
func (d Dog) Feed() { // Implementing Feed method for Dog
	fmt.Println(d.name, "is eating dog food.")
}


// Brief Explanation about Channels
// A goroutine is a lightweight thread of execution that runs concurrently within a Go program.
// Channels are a type-safe mechanism for communicating between goroutines. 

func sender(ch chan int, wg *sync.WaitGroup) {
    defer wg.Done() // Signal that this goroutine is done when the function returns
    for i := 0; i < 5; i++ {
        ch <- i
    }
    close(ch)
}

func receiver(ch chan int, wg *sync.WaitGroup) {
    defer wg.Done() // Signal that this goroutine is done when the function returns
    for {
        value, ok := <-ch
        if !ok {
            fmt.Println("Channel closed")
            break
        }
        fmt.Println("Received:", value)
    }
}

////////////////////// CHALLENGE //////////////////////
 /*
 * EXTRA DIFFICULTY (optional):
 * Create a contact book via terminal.
 * - You must implement functionalities for searching, inserting, updating,
 *   and deleting contacts.
 * - Each contact must have a name and a phone number.
 * - The program first asks what operation you want to perform,
 *   and then the necessary data to carry it out.
 * - The program cannot allow the input of non-numeric phone numbers and with more
 *   than 11 digits (or the number of digits you want).
 * - An operation to end the program should also be proposed.
 */

 func challenge(){
     type Contact struct {
         Name     string
         Phone    string
     }
     
    agenda := make(map[string]Contact)

    fmt.Println("======== AGENDA ========")
    fmt.Println("1. Add Contact")
    fmt.Println("2. Find Contact")
    fmt.Println("3. Update Contact")
    fmt.Println("4. Delete Contact")
    fmt.Println("5. Exit")
    fmt.Println("========================")
    for{

		input := getInput("Enter Option: ")
		option, err := strconv.Atoi(input)

		if err != nil {
			fmt.Println("Invalid input. Please enter a number.")
			continue
		}

        switch option{
        case 1:
            addContact(agenda)
        case 2:
            fmt.Printf("Find contact")
        case 3:
            fmt.Printf("Update contact")
        case 4:
            fmt.Printf("Delete contact")
        case 5:
            fmt.Printf("Good Bye\n")
            return
        }

    }
}

func getInput(prompt string) string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(prompt)
	input, _ := reader.ReadString('\n')
	return strings.TrimSpace(input)
}



func addContact(agenda map[string]Contact) {
	name := getInput("Enter contact name: ")
	phone :=  getInput("Enter phone: ")
    if len(phone) > 11 && !isNumeric(phone) {
        fmt.Println("Invalid input. Please enter a number.")
	    return
    }

	agenda[name] = Contact{name: name, phoneNumber: phone}
	fmt.Println("Contact added successfully!")
}

func isNumeric(s string) bool {
	_, err := strconv.Atoi(s)
	return err == nil
}