package main

import (
	"log"
	"os"
	"time"
)

// -- exercise
func setupLogging() {
	logFile, err := os.OpenFile("log.txt", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		log.Fatal("Failed to open log file:", err)
	}

	log.SetOutput(logFile)
	log.SetFlags(log.Ldate | log.Ltime | log.Lmicroseconds)
}

// -- extra challenge
type Task struct {
	Name        string
	Description string
}

type TaskManager struct {
	Tasks []Task
}

func (tm *TaskManager) AddTask(name, description string) {
	start := time.Now()
	tm.Tasks = append(tm.Tasks, Task{Name: name, Description: description})
	elapsed := time.Since(start)
	log.Printf("Task '%s' added successfully. Elapsed time: %s", name, elapsed)
}

func (tm *TaskManager) DeleteTask(name string) {
	start := time.Now()
	for i, task := range tm.Tasks {
		if task.Name == name {
			tm.Tasks = append(tm.Tasks[:i], tm.Tasks[i+1:]...)
			elapsed := time.Since(start)
			log.Printf("Task '%s' deleted successfully. Elapsed time: %s", name, elapsed)
			return
		}
	}
	log.Printf("Task '%s' not found.", name)
}

func (tm *TaskManager) ListTasks() {
	start := time.Now()
	if len(tm.Tasks) == 0 {
		log.Println("No tasks found.")
		return
	}
	log.Println("Tasks:")
	for _, task := range tm.Tasks {
		log.Printf("Name: %s, Description: %s", task.Name, task.Description)
	}
	elapsed := time.Since(start)
	log.Printf("Listed all tasks. Elapsed time: %s", elapsed)
}

func main() {
	setupLogging()

	log.Println("This is a log message.")
	log.Printf("This is a log message with formatted output: %s", "Hello, World!")

	log.Println("This is an informational message.")

	log.Printf("This is an informational message with formatted output: %s", "Hello, World!")


	log.Println("This is a warning message.")

	log.Printf("This is a warning message with formatted output: %s", "Hello, World!")

	log.Println("This is an error message.")
	log.Printf("This is an error message with formatted output: %s", "Hello, World!")

	log.Println("This is a fatal message.")
	log.Printf("This is a fatal message with formatted output: %s", "Hello, World!")
	log.Fatal("Fatal error occurred.")

	taskManager := TaskManager{}

	taskManager.AddTask("Task 1", "Description 1")
	taskManager.AddTask("Task 2", "Description 2")
	taskManager.AddTask("Task 3", "Description 3")

	taskManager.ListTasks()

	taskManager.DeleteTask("Task 2")

	taskManager.ListTasks()
}
