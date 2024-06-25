 package main

 import (
	"fmt"
	"time"
	"sort"
)

// Nota: una funcion de orden superior (HOF) es una funcion que recibe como parametro 
// otra(s) funcion(es) o devuelve una funcion.

// Primero definimos una funcion de orden superior (recibe una funcion como parametro).
func applyOperation(x int, y int, operation func(int, int) int) int {
	return operation(x, y)
}

// Luego definimos dos funciones que seran pasadas como parametro a la funcion de orden superior anterior.
func add(x int, y int) int {
	return x + y
}

func subtract(x int, y int) int {
	return x - y
}

// Y una funcion que regresa una funcion (tambien es una funcion de orden superior)...
func makeMultiplier(factor int) func(int) int {
	return func(x int) int {
		return x * factor
	}
}

func main() {
	fmt.Println("Resultado de sumar 5 y 3:", applyOperation(5, 3, add))
	fmt.Println("Resultado de multiplicar 5 y 3:", applyOperation(5, 3, subtract))
	
	triple := makeMultiplier(3)
	fmt.Println("Resultado de multiplicar 8 por 3:", triple(8))

	//Extra
	analisisEstudiantes()
}

// Extra

// Definimos una estructura para los estudiantes
type Student struct {
	name string
	birthDate string
	grades []float64
}

// Definimos una funcion de orden superior que realiza el analisis de los estudiantes
func applyAnalysis(students []Student, analysisType func([]Student) []string) []string {
	return analysisType(students)
}

// Definimos las funciones para los tipos de analisis
func average (students []Student) []string {
	var result []string
	for _, student := range students {
		sum := 0.0
		for _, grade := range student.grades {
			sum += grade
		}
		average := sum / float64(len(student.grades))
		result = append(result, student.name + ": " + fmt.Sprintf("%.2f", average))
	}
	return result
}

func bestStudents (students []Student) []string {
	var result []string
	for _, student := range students {
		sum := 0.0
		for _, grade := range student.grades {
			sum += grade
		}
		average := sum / float64(len(student.grades))
		if average >= 9.0 {
			result = append(result, student.name)
		}
	}
	return result
}

func birthDateSort (students []Student) []string {
	var result []string
	sort.Slice(students, func(i, j int) bool {
		date1, _ := time.Parse("2006-01-02", students[i].birthDate)
		date2, _ := time.Parse("2006-01-02", students[j].birthDate)
		return date1.After(date2)
	})
	for _, student := range students {
		result = append(result, student.name)
	}
	return result
}

func highestGrade (students []Student) []string {
	var result []string
	highest := 0.0
	for _, student := range students {
		for _, grade := range student.grades {
			if grade > highest {
				highest = grade
			}
		}
	}
	for _, student := range students {
		for _, grade := range student.grades {
			if grade == highest {
				result = append(result, student.name + ": " + fmt.Sprintf("%.2f", grade))
			}
		}
	}
	return result
}

func analisisEstudiantes() {
	// Definimos una lista de estudiantes
	studentsList := []Student{
		{"Juan", "2000-01-01", []float64{8.5, 9.0, 7.5}},
		{"Maria", "2001-02-03", []float64{9.0, 9.5, 8.0}},
		{"Pedro", "1999-03-05", []float64{7.0, 8.0, 6.5}},
		{"Ana", "2000-04-07", []float64{9.5, 9.0, 8.5}},
		{"Luis", "1998-05-09", []float64{6.0, 7.0, 5.5}},
	}

	// Realizamos el analisis de los estudiantes
	fmt.Println("Promedio de calificaciones: ", applyAnalysis(studentsList, average))
	fmt.Println("Mejores estudiantes: ", applyAnalysis(studentsList, bestStudents))
	fmt.Println("Estudiantes ordenados empezando con los mas jovenes: ", applyAnalysis(studentsList, birthDateSort))
	fmt.Println("Calificacion(es) mas alta(s): ", applyAnalysis(studentsList, highestGrade))
}