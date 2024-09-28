package main

import (
	"fmt"
	"sort"
	"time"
)

/* -- i -- Pass functions as arguments */

func applyToEach(f func(int) int, list []int) []int {
	result := make([]int, len(list))
	for i, v := range list {
		result[i] = f(v)
	}
	return result
}

func square(n int) int {
	return n * n
}

func increment(n int) int {
	return n + 1
}

/* -- ii -- Return functions as results */
func makeMultiplier(multiplier int) func(int) int {
	return func(n int) int {
		return n * multiplier
	}
}

/* -- iii -- Anonymous functions and closures */
func filter(list []int, predicate func(int) bool) []int {
	var result []int
	for _, v := range list {
		if predicate(v) {
			result = append(result, v)
		}
	}
	return result
}

/* -- extra challenge */

type Student struct {
	Name      string
	BirthDate time.Time
	Grades    []float64
}

// StudentProcessor -> Higher-order functions for student operations
type StudentProcessor struct{}

func NewStudentProcessor() *StudentProcessor {
	return &StudentProcessor{}
}

func (sp *StudentProcessor) AverageGrades(students []Student) map[string]float64 {
	averages := make(map[string]float64)
	for _, student := range students {
		sum := 0.0
		for _, grade := range student.Grades {
			sum += grade
		}
		averages[student.Name] = sum / float64(len(student.Grades))
	}
	return averages
}

func (sp *StudentProcessor) BestStudents(students []Student) []string {
	var bestStudents []string //bestStudents := []string{}
	for _, student := range students {
		average := sp.AverageGrades([]Student{student})[student.Name]
		if average >= 9 {
			bestStudents = append(bestStudents, student.Name)
		}
	}
	return bestStudents
}

func (sp *StudentProcessor) SortByBirthDate(students []Student) []Student {
	sortedStudents := make([]Student, len(students))
	copy(sortedStudents, students)
	sort.Slice(sortedStudents, func(i, j int) bool {
		return sortedStudents[i].BirthDate.After(sortedStudents[j].BirthDate)
	})
	return sortedStudents
}

func (sp *StudentProcessor) HighestGrade(students []Student) float64 {
	highest := 0.0
	for _, student := range students {
		for _, grade := range student.Grades {
			if grade > highest {
				highest = grade
			}
		}
	}
	return highest
}

func main() {
	/* -- i */
	list := []int{1, 2, 3, 4, 5}

	squaredList := applyToEach(square, list)
	fmt.Println("Squared List:", squaredList)

	incrementedList := applyToEach(increment, list)
	fmt.Println("Incremented List:", incrementedList)

	/* -- ii */
	multiplyByTwo := makeMultiplier(2)
	fmt.Println("3 * 2 =", multiplyByTwo(3))

	multiplyByFive := makeMultiplier(5)
	fmt.Println("3 * 5 =", multiplyByFive(3))

	/* -- iii */
	list = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	evenNumbers := filter(list, func(n int) bool {
		return n%2 == 0
	})
	fmt.Println("Even Numbers:", evenNumbers)

	threshold := 5
	greaterThanThreshold := filter(list, func(n int) bool {
		return n > threshold
	})
	fmt.Println("Numbers greater than threshold:", greaterThanThreshold)

	/* -- extra challenge */
	students := []Student{
		{"Alice", time.Date(2000, 5, 14, 0, 0, 0, 0, time.UTC), []float64{8.5, 9.0, 9.5}},
		{"Bob", time.Date(1999, 3, 21, 0, 0, 0, 0, time.UTC), []float64{7.0, 6.5, 8.0}},
		{"Charlie", time.Date(2001, 7, 30, 0, 0, 0, 0, time.UTC), []float64{9.0, 9.5, 9.8}},
	}

	processor := NewStudentProcessor()

	averages := processor.AverageGrades(students)
	fmt.Println("Average Grades:")
	for name, avg := range averages {
		fmt.Printf("%s: %.2f\n", name, avg)
	}

	bestStudents := processor.BestStudents(students)
	fmt.Println("\nBest Students:")
	for _, name := range bestStudents {
		fmt.Println(name)
	}

	sortedStudents := processor.SortByBirthDate(students)
	fmt.Println("\nStudents sorted by birth date (youngest first):")
	for _, student := range sortedStudents {
		fmt.Printf("%s: %s\n", student.Name, student.BirthDate.Format("2006-01-02"))
	}

	highestGrade := processor.HighestGrade(students)
	fmt.Printf("\nHighest Grade: %.2f\n", highestGrade)
}
