package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strings"
	"time"
)

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* ------------------------------ Task Manager ------------------------------ */

type Task struct {
	description string
	title       string
}

type TaskManager struct {
	tasks           []Task
	shouldPrintLogs bool
}

func (taskManager *TaskManager) addTask(newTask Task) error {
	var startTime time.Time = time.Now()

	if taskManager.shouldPrintLogs {
		fmt.Println()
		log.Println("addTask (method) start execution...")
	}

	taskManager.tasks = append(taskManager.tasks, newTask)

	if taskManager.shouldPrintLogs {
		log.Println("addTask (method) ends execution!")
		log.Printf("addTask: %v\n", time.Since(startTime))
	}

	return nil
}

func (taskManager *TaskManager) deleteTaskByTitle(title string) error {
	var startTime time.Time = time.Now()

	if taskManager.shouldPrintLogs {
		fmt.Println()
		log.Println("deleteTaskByTitle (method) start execution...")
	}

	var uppercasedTitle string = strings.ToUpper(title)

	var sanitizedTasks []Task

	for _, task := range taskManager.tasks {
		var uppercasedTaskTitle string = strings.ToUpper(task.title)

		if uppercasedTaskTitle != uppercasedTitle {
			sanitizedTasks = append(sanitizedTasks, task)

		}
	}

	if len(taskManager.tasks) == len(sanitizedTasks) {
		return errors.New("The task title was not found!")
	}

	taskManager.tasks = sanitizedTasks

	if taskManager.shouldPrintLogs {
		log.Printf("deleteTaskByTitle (method) ends execution!\n")
		log.Printf("deleteTaskByTitle: %v\n", time.Since(startTime))
	}

	return nil
}

func (taskManager *TaskManager) printTasks() {
	var startTime time.Time = time.Now()

	if taskManager.shouldPrintLogs {
		log.Printf("printTasks (method) start execution...\n\n")
	}

	for _, task := range taskManager.tasks {
		fmt.Printf("%+v\n", task)
	}

	if taskManager.shouldPrintLogs {
		fmt.Println()
		log.Printf("printTasks (method) ends execution!\n")
		log.Printf("printTasks: %v", time.Since(startTime))
	}
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Logging...
	*/

	fmt.Println("Logging...")

	fmt.Printf("\nlog.Print(<MESSAGE>)...\n\n")

	log.Print("logger message!")

	fmt.Printf("\nlog.Printf(<MESSAGE>)...\n\n")

	log.Printf("Formatted logger message!")

	fmt.Printf("\nlog.Println(<MESSAGE>)...\n\n")

	log.Println("Logger message with line break at the end!")

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Printf("\nAdditional challenge...\n")

	var taskManager TaskManager = TaskManager{shouldPrintLogs: true}

	var exit bool = false
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)

	for !exit {
		fmt.Print("\nWrite an operation ('Add task', 'Delete task by title', 'Print tasks', or 'Exit'): ")
		operation, readerErr := reader.ReadString('\n')
		if readerErr != nil {
			continue
		}

		operation = strings.TrimSpace(operation)
		operation = strings.ToUpper(operation)

	operationActions:
		switch operation {
		case "ADD TASK":
			fmt.Print("\nTask title: ")
			taskTitle, readerErr := reader.ReadString('\n')
			if readerErr != nil {
				break operationActions
			}

			fmt.Print("Task description: ")
			taskDescription, readerErr := reader.ReadString('\n')
			if readerErr != nil {
				break operationActions
			}

			taskManager.addTask(Task{
				description: strings.TrimSpace(taskDescription),
				title:       strings.TrimSpace(taskTitle),
			})

		case "DELETE TASK BY TITLE":
			fmt.Print("\nTask title: ")
			taskTitle, readerErr := reader.ReadString('\n')
			if readerErr != nil {
				break operationActions
			}

			taskManager.deleteTaskByTitle(taskTitle)

		case "PRINT TASKS":
			fmt.Println()
			taskManager.printTasks()

		case "EXIT":
			exit = true
			fmt.Print("\nApplication closed!")

		default:
			fmt.Print("\nInvalid operation! Try again...\n")
		}
	}
}
