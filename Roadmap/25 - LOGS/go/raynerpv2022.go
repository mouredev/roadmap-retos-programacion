package main

/*
#  * EJERCICIO:
#  * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
#  * un ejemplo con cada nivel de "severidad" disponible.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
#  * y listar dichas tareas.
#  * - Añadir: recibe nombre y descripción.
#  * - Eliminar: por nombre de la tarea.
#  * Implementa diferentes mensajes de log que muestren información según la
#  * tarea ejecutada (a tu elección).
#  * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
#  */

import (
	"fmt"
	"log"
	"math/rand"
	"os"
	"time"
)

const (
	DEBUG = iota
	INFO
	WARN
	ERROR
	CRITICAL
)

var loglevel = DEBUG

func getLoggingMessage(level int, message string) {
	if level >= loglevel {
		switch level {
		case DEBUG:
			log.Println("DEBUG: ", message)
		case INFO:
			log.Println("INFO: ", message)
		case WARN:
			log.Println("WARN: ", message)
		case ERROR:
			log.Println("ERROR: ", message)
		case CRITICAL:
			log.Println("CRITICAL: ", message)

		}
	}

}

type TaskManager struct {
	tasks map[string]string
}

func (t *TaskManager) Create(name, desc string) {
	_, exist := t.tasks[name]
	if exist {
		getLoggingMessage(ERROR, fmt.Sprintf(" Task %v already created\n", name))
	} else {
		t.tasks[name] = desc
		getLoggingMessage(INFO, fmt.Sprintf(" Task %v  created succesfully\n", name))
	}

}

func (t *TaskManager) Delete(name string) {
	_, exist := t.tasks[name]
	if !exist {
		getLoggingMessage(ERROR, fmt.Sprintf(" Task %v Not Found\n", name))
	} else {
		delete(t.tasks, name)
		getLoggingMessage(INFO, fmt.Sprintf(" Task %v delete succesfully\n", name))
	}

}

func (t *TaskManager) Display() {

	getLoggingMessage(INFO, fmt.Sprintf(" Task %v  \n", t.tasks))
}

func (t *TaskManager) Execute(name string) {
	_, exist := t.tasks[name]
	if exist {
		getLoggingMessage(INFO, fmt.Sprintf(" Task %v EXECUTING ... \n", name))
		start := time.Now().Second()
		getLoggingMessage(DEBUG, fmt.Sprintf(" Task %v START TIME %v ... \n", name, start))
		random_sleep := rand.Intn(10)
		time.Sleep((time.Second * time.Duration(random_sleep)))
		end := time.Now().Second()
		getLoggingMessage(DEBUG, fmt.Sprintf(" Task %v END TIME %v ... \n", name, end))
		getLoggingMessage(DEBUG, fmt.Sprintf(" Task %v  DURATION TIME %v ... \n", name, random_sleep))
		getLoggingMessage(INFO, fmt.Sprintf(" Task %v DEAD ... \n", name))
	} else {
		getLoggingMessage(CRITICAL, fmt.Sprintf(" Task %v NOT EXECUTED, CRITICAL PARAMETER, NUCLEAR WAR is comming... \n", name))
	}

}

func main() {
	// log.Println("Error Normalito")

	// log.Panic("Error Panic")
	// log.Fatalln("Error Fatal")
	fmt.Println("Loggin in  File (F) or Display (D)")
	var op string
	_, e := fmt.Scan(&op)
	if e != nil {
		log.Fatal(e)
	}
	if op == "F" {

		f, e := os.OpenFile("app.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
		if e != nil {
			getLoggingMessage(ERROR, "Message ERROR, opening log file")
		}
		defer f.Close()
		log.SetOutput(f)
		log.SetFlags(log.Ldate | log.Ltime)
	}

	getLoggingMessage(INFO, "Message INFO")
	getLoggingMessage(DEBUG, "Message DEBUG")
	getLoggingMessage(WARN, "Message WARNING")
	getLoggingMessage(ERROR, "Message ERROR")
	getLoggingMessage(CRITICAL, "Message CRITICAL")
	log.Println("Errores")

	// ?Extra
	task_task := TaskManager{map[string]string{}}
	task_task.Create("t1", "ggggg")
	task_task.Create("t1", "ggggg")
	task_task.Create("t2", "ggggg")
	task_task.Create("t3", "ggggg")
	task_task.Delete("tqq1")
	task_task.Delete("t1")
	task_task.Display()
	task_task.Execute("t1")
	task_task.Execute("t3")
	task_task.Execute("t4")
	task_task.Display()

}
