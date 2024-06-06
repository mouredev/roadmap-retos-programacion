package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	/*
	   Stack methods for insert and recover items...
	*/

	fmt.Println("Stack methods for insert and recover items...")

	var stack []int8 = []int8{1, 5, 7, 9, 8}

	fmt.Println("\nvar stack []int = []int{1, 5, 7, 9, 8}")

	fmt.Println("\nInsert an element at the end of the stack...")

	stack = append(stack, 12)

	fmt.Printf("\nstack = append(stack, 12) --> stack = %d\n", stack)

	fmt.Println("\nRecover an element of the stack...")

	var lastStackElement int8 = stack[len(stack)-1]
	stack = stack[:len(stack)-1]

	fmt.Println("\nvar lastStackElement int8 = stack[len(stack)-1]\nstack = stack[:len(stack)-1]")

	fmt.Printf("\nlastStackElement --> %d\n", lastStackElement)
	fmt.Printf("\nstack --> %d\n", stack)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
	   Queue methods for insert and recover items...
	*/

	fmt.Println("\nQueue methods for insert and recover items...")

	var queue []string = []string{"Hello", "World"}

	fmt.Println("\nvar queue []string = []string{'Hello', 'World'}")

	fmt.Println("\nInsert an element at the end of the queue...")

	queue = append(queue, "Golang")

	fmt.Printf("\nqueue = append(queue, 'Golang') --> queue = %s\n", queue)

	fmt.Println("\nRecover an element of the queue...")

	var firstQueueElement string = queue[0]
	queue = queue[1:]

	fmt.Println("\nvar firstQueueElement string = queue[0]\nqueue = queue[1:]")

	fmt.Printf("\nfirstQueueElement --> %s\n", firstQueueElement)
	fmt.Printf("\nqueue --> %s\n", queue)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
	   Additional challenge...
	*/

	// Stack exercise...
	fmt.Println("\nStack exercise...")

	var browserHistory []string = []string{}

	var shouldExit bool = false
	for !shouldExit {
		fmt.Printf("\nBrowser history --> %s\n", browserHistory)

		var operation string
		fmt.Print("\nSelect an operation ('Back', 'Forward', or 'Exit'): ")
		_, operationErr := fmt.Scanf("%s\n", &operation)

		if operationErr != nil {
			shouldExit = true
			continue
		}

		var operationFormatted string = strings.ToUpper(operation)

		switch operationFormatted {
		case "BACK":
			if len(browserHistory) > 0 {
				browserHistory = browserHistory[:len(browserHistory)-1]
			}
			break

		case "FORWARD":
			var lastPageNumber int = 0

			if len(browserHistory) > 0 {
				var lastPage string = browserHistory[len(browserHistory)-1]
				_, lastPageNumberStr, _ := strings.Cut(lastPage, " ")
				lastPageNumber, _ = strconv.Atoi(strings.TrimSpace(lastPageNumberStr))
			}

			var newPage string = fmt.Sprintf("Page %d", lastPageNumber+1)
			browserHistory = append(browserHistory, newPage)
			break

		case "EXIT":
			shouldExit = true
			break

		default:
			break
		}
	}

	// Queue exercise...
	fmt.Println("\nQueue exercise...")

	var documents []string = []string{}

	for true {
		fmt.Printf("\nDocuments --> %s\n", documents)

		var userInput string
		fmt.Print("\nAdd a document to print, or write 'Print' to print the document in the queue: ")
		_, userInputErr := fmt.Scanf("%s\n", &userInput)

		if userInputErr != nil {
			break
		}

		var userInputFormatted string = strings.ToUpper(userInput)

		if userInputFormatted == "PRINT" {
			if len(documents) > 0 {
				var printedDocument string = documents[0]
				documents = documents[1:]
				fmt.Printf("\nPrinted document --> %s\n", printedDocument)
			}
		} else {
			documents = append(documents, userInput)
		}
	}
}
