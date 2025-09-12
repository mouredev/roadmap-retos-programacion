package main

import (
	"log"
	"os"
	"sync"
	"time"
)

var (
	logger *log.Logger
	once   sync.Once
)

func GetLogger() *log.Logger {
	once.Do(func() {
		logger = log.New(os.Stdout, "", log.LstdFlags|log.Lshortfile)
	})
	return logger
}

type Tarea struct {
	Nombre      string
	Descripcion string
}

type GestorTareas struct {
	tareas []Tarea
}

func (g *GestorTareas) AñadirTarea(nombre, descripcion string) {
	l := GetLogger()
	inicio := time.Now()

	g.tareas = append(g.tareas, Tarea{Nombre: nombre, Descripcion: descripcion})

	l.Printf("Tarea añadida: %s - %s", nombre, descripcion)
	l.Printf("Tiempo de ejecución para añadir tarea: %v", time.Since(inicio))
}

func (g *GestorTareas) EliminarTarea(nombre string) {
	l := GetLogger()
	inicio := time.Now()

	for i, tarea := range g.tareas {
		if tarea.Nombre == nombre {
			g.tareas = append(g.tareas[:i], g.tareas[i+1:]...)
			l.Printf("Tarea eliminada: %s", nombre)
			l.Printf("Tiempo de ejecución para eliminar tarea: %v", time.Since(inicio))
			return
		}
	}

	l.Printf("No se encontró la tarea: %s", nombre)
	l.Printf("Tiempo de ejecución para buscar tarea: %v", time.Since(inicio))
}

func (g *GestorTareas) ListarTareas() {
	l := GetLogger()
	inicio := time.Now()

	l.Println("Lista de tareas:")
	for _, tarea := range g.tareas {
		l.Printf("- %s: %s", tarea.Nombre, tarea.Descripcion)
	}

	l.Printf("Tiempo de ejecución para listar tareas: %v", time.Since(inicio))
}

func main() {

	l := GetLogger()
	l.Println("Iniciando programa de gestión de tareas")

	gestor := &GestorTareas{}

	gestor.AñadirTarea("Comprar víveres", "Ir al supermercado y comprar alimentos para la semana")
	gestor.AñadirTarea("Hacer ejercicio", "Realizar 30 minutos de cardio")
	gestor.ListarTareas()
	gestor.EliminarTarea("Hacer ejercicio")
	gestor.ListarTareas()
	gestor.EliminarTarea("Tarea inexistente")

	l.Println("Finalizando programa de gestión de tareas")

}
