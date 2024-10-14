package main

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

/*
#  * EJERCICIO:
#  * Explora el concepto de funciones de orden superior en tu lenguaje
#  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
#  * lista de calificaciones), utiliza funciones de orden superior para
#  * realizar las siguientes operaciones de procesamiento y análisis:
#  * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#  *   y promedio de sus calificaciones.
#  * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#  *   que tienen calificaciones con un 9 o más de promedio.
#  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
#  * - Mayor calificación: Obtiene la calificación más alta de entre todas las
#  *   de los alumnos.
#  * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
#  */

//  Pasar una función como argumento a otra función.

// Interface
func Func_root(x interface{}, y interface{}, f func(interface{}, interface{}) interface{}) interface{} {
	return f(x, y)
}

func sum_number(n1 interface{}, n2 interface{}) interface{} {
	return n1.(int) + n2.(int)
}

func sum_string(s1 interface{}, s2 interface{}) interface{} {
	return fmt.Sprintf("%v %v\n", s1.(string), s2.(string))
}

// Genereic
func Func_rootG[Gen any](x, y Gen, f func(Gen, Gen) Gen) Gen {
	return f(x, y)
}

func sum_numberG(n1 int, n2 int) int {
	return n1 + n2
}

func sum_stringG(s1 string, s2 string) string {
	return fmt.Sprintf("%v %v\n", s1, s2)
}

// Devolver funciones

func Return_Func(x int) func(int) int {
	return func(number int) int {
		return number * x
	}

}

// implementacion de map, filter  porque en go no existe nativamente
// map
func mapF[T any](f func(T) T, slice []T) []T {
	result := []T{}
	for _, i := range slice {
		result = append(result, f(i))
	}
	return result

}

func Qua2(x int) int {
	return x * x
}

// filter

func filterF[T any](slice1 []T, f func(T) bool) []T {

	result := []T{}
	for _, i := range slice1 {

		if f(i) {
			result = append(result, i)
		}

	}
	return result
}

func even_number(x int) bool {
	return x%2 == 0
}

func odd_number(x int) bool {
	return x%2 != 0
}

// reduce

func reduceF[T any](slice1 []T, f func(x, y T) T) T {
	var result T
	for _, i := range slice1 {
		result = f(result, i)

	}
	return result
}

// Extra

type kv struct {
	key   string
	value float64
}

type Student struct {
	name        string
	dateBorn    time.Time
	note        map[string]float64
	averageNote float64
	bestMateria kv
}

// promedio de calidicaciones, usare reduceF

func (s *Student) AverageNote() { // point when variable is a map
	noteValue := []float64{}
	for _, v := range s.note {
		noteValue = append(noteValue, v)
	}

	sumNote := reduceF(noteValue, func(acc, n float64) float64 {
		return acc + n
	})
	s.averageNote = sumNote / float64(len(noteValue))

}

func (s *Student) OrderNote() {
	KV := []kv{}
	for k, v := range s.note {
		KV = append(KV, kv{k, v})
	}
	sort.Slice(KV, func(x, y int) bool {
		return KV[x].value > (KV[y].value)
	})

	for _, v := range KV {
		fmt.Printf("Materia: %v, Note: %v\n", v.key, v.value)
	}
	s.bestMateria = KV[0]

}

type Students []Student

func BestStudient(student Student) bool {
	return student.averageNote >= 9.0 // aqui paso como argumento el elemnto que paso en el slice de filterF
	// no puedo pasar la nota, porque el slice esta compuesto de Student y eso es lo que paso
}

func (s Students) SortByDateBorn() {
	sort.Slice(s, func(i, j int) bool {
		return s[i].dateBorn.Before(s[j].dateBorn) // Ordena en orden ascendente
	})
}

func (s Students) Display() {
	for _, i := range s {
		fmt.Printf("\tName: %v, Ano: %v, Mes : %v, Dia : %v\n", i.name, i.dateBorn.Year(), i.dateBorn.Month(), i.dateBorn.Day())
		fmt.Printf("Promedio: %.2f,mejor asignatura: %v,  Notas: %v\n", i.averageNote, i.bestMateria, i.note)
	}
}

func main() {
	f1 := Func_root(21, 21, sum_number)
	fmt.Println(f1)
	f1 = Func_root("Resba", "loso", sum_string)
	fmt.Println(f1)

	f1 = Func_rootG(210, 210, sum_numberG)
	fmt.Println(f1)
	f1 = Func_rootG("Resbaloso", "tiburcio", sum_stringG)
	fmt.Println(f1)

	f2 := Return_Func(100) //return_func retorna una funcion
	fmt.Println(f2(2))     // f2 es una funcion retornada que recibe parametro

	// map
	list1 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	Q_list := mapF(Qua2, list1)
	fmt.Println(Q_list)

	list2 := []string{"mama", "loka"}
	Q_list2 := mapF(func(n string) string {
		return strings.ToUpper(n)

	}, list2)
	fmt.Println(Q_list2)

	// filter
	Q_list3 := filterF(list1, even_number)
	Q_list4 := filterF(list1, odd_number)
	fmt.Printf("Even Number: %v\n Odd NUmber : %v\n", Q_list3, Q_list4)

	// reduce
	list4 := []string{"r", "e", "s", "b", "a"}
	Q_list5 := reduceF(list1, func(x, y int) int {
		return x + y
	})

	Q_list6 := reduceF(list4, func(x, y string) string {
		return x + y
	})

	fmt.Println(Q_list5)
	fmt.Println(Q_list6)

	// Extra

	student := Students{
		Student{
			"perico 3",
			time.Date(2001, 1, 1, 0, 0, 0, 0, time.UTC),
			map[string]float64{
				"ma": 9.0,
				"l":  5.6,
				"EF": 9.9,
			},
			0,
			kv{"", 0.0},
		},
		Student{
			"perico 2",
			time.Date(2000, 10, 10, 0, 0, 0, 0, time.UTC),
			map[string]float64{
				"ma": 9.2,
				"l":  9.5,
				"EF": 8.7,
			},
			0,
			kv{"", 0.0},
		},
		Student{
			"perico 1",
			time.Date(2011, 12, 12, 0, 0, 0, 0, time.UTC),
			map[string]float64{
				"ma": 9.0,
				"l":  9.3,
				"EF": 8.0,
			},
			0,
			kv{"", 0.0},
		}}

	fmt.Println(" EXTRA ")
	fmt.Println()
	fmt.Println("Promedio de Calificaciones")
	for i, _ := range student {
		student[i].AverageNote()
		fmt.Printf("\tName: %v, Average: %v\n", student[i].name, student[i].averageNote)
	}

	fmt.Println()
	fmt.Println("Mejores estudiantes")

	best := filterF(student, BestStudient) //uso la misma funcion filterF generica con T any y lo que paso es el elemento del slice a la funcion que paso como argumento
	for _, i := range best {
		fmt.Printf("\tName: %v, Average: %v\n", i.name, i.averageNote)
	}

	fmt.Println()
	fmt.Println("Sin Ordenar")
	student.Display()
	fmt.Println()
	fmt.Println("Ordenados por fecha de Nacimiento")
	student.SortByDateBorn()
	student.Display()

	fmt.Println()
	fmt.Println("Calificacion mas alta por alumno")
	for i, _ := range student {
		student[i].OrderNote()

	}
	student.Display()
}
