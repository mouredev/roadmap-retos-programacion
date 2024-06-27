package main

import (
	"bufio"
	"fmt"
	"log/slog"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	//logging 'slog' estándar de go (desde la versión 1.21)
	slog.SetLogLoggerLevel(slog.LevelDebug)
	slog.Debug("log debug")
	slog.Info("log info")
	slog.Warn("log warn")
	slog.Error("log error")
	taskManager()
}

func taskManager() {

	logger := slog.Default()
	tasks := make(map[string]string)
	logger.Info("administrador de tareas iniciado.")
	reader := bufio.NewReader(os.Stdin)
	var option string
	for option != "4" {
		printMenu()
		fmt.Print("Ingrese la opción :")
		option, _ = reader.ReadString('\n')
		option = strings.TrimSpace(option)
		switch option {
		case "1":
			fmt.Println("Tareas registradas")
			timeStart := time.Now()
			if len(tasks) == 0 {
				fmt.Println("No hay tareas registradas")
			}
			for k, v := range tasks {
				fmt.Println(k, "-", v)
			}
			timeEnd := time.Now()
			timeDuration := timeEnd.Compare(timeStart)
			logger.Info("Tiempo de ejecución en listado " + strconv.Itoa(timeDuration) + "ms")
		case "2":
			fmt.Println("Agregar una tarea")
			timeStart := time.Now()
			fmt.Print("Ingrese nombre de la tarea:")
			name, _ := reader.ReadString('\n')
			name = strings.TrimSpace(name)
			fmt.Print("Ingrese descripción de la tarea:")
			description, _ := reader.ReadString('\n')
			description = strings.TrimSpace(description)
			tasks[name] = description
			timeEnd := time.Now()
			timeDuration := timeEnd.Compare(timeStart)
			logger.Info("Tarea creada " + name + " Tiempo de ejecución " + strconv.Itoa(timeDuration) + "ms")
		case "3":
			fmt.Println("Eliminar una tarea")
			timeStart := time.Now()
			fmt.Print("Ingrese nombre de la tarea a eliminar:")
			nameToDelete, _ := reader.ReadString('\n')
			nameToDelete = strings.TrimSpace(nameToDelete)
			if _, ok := tasks[nameToDelete]; ok {
				delete(tasks, nameToDelete)
				timeEnd := time.Now()
				timeDuration := timeEnd.Compare(timeStart)
				logger.Info("Tarea eliminada " + nameToDelete + " ,tiempo de ejecución " + strconv.Itoa(timeDuration) + "ms")
			} else {
				timeEnd := time.Now()
				timeDuration := timeEnd.Compare(timeStart)
				logger.Info("Tarea no registrada " + nameToDelete + " ,tiempo de ejecución " + strconv.Itoa(timeDuration) + "ms")
			}
		case "4":
			logger.Info("saliendo del sistema, gracias por usar")
		default:
			logger.Warn("opción no valida")
		}
	}
}

func printMenu() {
	fmt.Println(strings.Repeat("-", 29))
	fmt.Println("|| ADMINISTRADOR DE TAREAS ||")
	fmt.Println(strings.Repeat("-", 29))
	fmt.Println("Opciones disponibles")
	fmt.Println("[1] Mostrar tareas")
	fmt.Println("[2] Agregar una tarea")
	fmt.Println("[3] Eliminar una tarea")
	fmt.Println("[4] Salir")
}
