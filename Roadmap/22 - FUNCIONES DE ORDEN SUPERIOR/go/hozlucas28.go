package main

import (
	"fmt"
	"slices"
	"sort"
	"strings"
	"time"
)

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

/* --------------------------------- Student -------------------------------- */

type Student struct {
	bornDate       time.Time
	name           string
	qualifications []float32
}

type Students []Student

func (students Students) Print() {
	for _, student := range students {
		var studentBornDate string = fmt.Sprintf(
			"%02d-%02d-%4d",
			student.bornDate.Month(),
			student.bornDate.Day(),
			student.bornDate.Year(),
		)

		fmt.Printf("\n%s / %s / %.2f", student.name, studentBornDate, student.qualifications)
	}
}

type SortByYoungestBornDate Students

func (students SortByYoungestBornDate) Len() int { return len(students) }
func (students SortByYoungestBornDate) Swap(i, j int) {
	students[i], students[j] = students[j], students[i]
}
func (students SortByYoungestBornDate) Less(i, j int) bool {
	return students[i].bornDate.After(students[j].bornDate)
}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

func Average(numbers ...float32) float32 {
	var total float32

	for _, number := range numbers {
		total += number
	}

	return total / float32(len(numbers))
}

func ToFiltered[T any](slice []T, filterFn func(element T) bool) []T {
	var filteredSlice []T

	for _, element := range slice {
		if filterFn(element) {
			filteredSlice = append(filteredSlice, element)
		}
	}

	return filteredSlice
}

func ToMap[T any](array []T, callback func(element T, index int) T) []T {
	var arrayCopy []T

	for index, element := range array {
		var mappedElement T = callback(element, index)
		arrayCopy = append(arrayCopy, mappedElement)
	}

	return arrayCopy
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Higher order functions (HOF)...
	*/

	fmt.Println("Higher order functions (HOF)...")

	var names []string = []string{
		"john",
		"mary",
		"david",
		"sarah",
		"james",
	}
	fmt.Printf("\nnames=%#v\n", names)

	var capitalizedNames []string = ToMap(names, func(name string, index int) string {
		name = strings.TrimSpace(name)
		return strings.ToUpper(string(name[0])) + name[1:]
	})
	fmt.Printf("\ncapitalizedNames=%#v\n", capitalizedNames)

	var uppercasedNames []string = ToMap(names, func(name string, index int) string {
		name = strings.TrimSpace(name)
		return strings.ToUpper(name)
	})

	fmt.Printf("\nuppercasedNames=%#v\n", uppercasedNames)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	var students Students = []Student{
		{
			bornDate:       time.Date(2000, time.January, 1, 0, 0, 0, 0, time.UTC),
			name:           "Alice",
			qualifications: []float32{8.5, 9.0, 7.8},
		},
		{
			bornDate:       time.Date(1999, time.February, 15, 0, 0, 0, 0, time.UTC),
			name:           "Bob",
			qualifications: []float32{7.2, 6.8, 8.0},
		},
		{
			bornDate:       time.Date(2001, time.January, 10, 0, 0, 0, 0, time.UTC),
			name:           "Charlie",
			qualifications: []float32{9.5, 8.7, 9.2},
		},
		{
			bornDate:       time.Date(2002, time.February, 5, 0, 0, 0, 0, time.UTC),
			name:           "David",
			qualifications: []float32{6.5, 7.0, 7.8},
		},
		{
			bornDate:       time.Date(2000, time.May, 20, 0, 0, 0, 0, time.UTC),
			name:           "Eve",
			qualifications: []float32{8.0, 8.5, 7.2},
		},
		{
			bornDate:       time.Date(1999, time.June, 25, 0, 0, 0, 0, time.UTC),
			name:           "Frank",
			qualifications: []float32{7.8, 7.5, 8.2},
		},
		{
			bornDate:       time.Date(2001, time.February, 15, 0, 0, 0, 0, time.UTC),
			name:           "Grace",
			qualifications: []float32{9.0, 9.2, 8.7},
		},
		{
			bornDate:       time.Date(2002, time.December, 10, 0, 0, 0, 0, time.UTC),
			name:           "Henry",
			qualifications: []float32{9.4, 7.87, 10.00},
		},
	}

	fmt.Println("\nStudents...")
	students.Print()

	fmt.Println("\n\nStudents with name and average qualification...")
	for _, student := range students {
		var averageQualification float32 = Average(student.qualifications...)
		fmt.Printf("\n%s / %.2f", student.name, averageQualification)
	}

	var studentsWithAverageQualificationMoreThanNine Students = ToFiltered(students, func(student Student) bool {
		return Average(student.qualifications...) >= 9
	})

	fmt.Println("\n\nStudents with an average qualification more than nine...")
	studentsWithAverageQualificationMoreThanNine.Print()

	var sortedStudentsByBornDate Students = slices.Clone(students)
	sort.Sort(SortByYoungestBornDate(sortedStudentsByBornDate))

	fmt.Println("\n\nSorted students by born date (youngest to oldest)...")
	sortedStudentsByBornDate.Print()

	fmt.Println("\n\nStudents with name and best qualification...")
	for _, student := range students {
		var bestQualification float32 = slices.Max(student.qualifications)
		fmt.Printf("\n%s / %.2f", student.name, bestQualification)
	}
}
