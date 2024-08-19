package main

import (
	"fmt"
	"reflect"
	"testing"
)

type BasicCalculator struct{}

func (bc BasicCalculator) Sum(a, b int) int {
	return a + b
}

type Profile struct {
	Name                 string
	Age                  int
	BirthDate            string
	ProgrammingLanguages []string
}

func CreateProfile() Profile {
	return Profile{
		Name:                 "Isaias Ramos López",
		Age:                  21,
		BirthDate:            "2002-11-09",
		ProgrammingLanguages: []string{"Go", "Java", "Python"},
	}
}

func main() {
	calculator := BasicCalculator{}
	result := calculator.Sum(3, 4)
	fmt.Println("Sum: ", result)

	profile := CreateProfile()
	fmt.Println("Profile Name: ", profile.Name)
	fmt.Println("Profile Age: ", profile.Age)
	fmt.Println("Profile BirthDate: ", profile.BirthDate)
	fmt.Println("Profile ProgrammingLanguages: ", profile.ProgrammingLanguages)
}

/* - Create a new file named qwik-zgheib_test.go for the test */
/* - import this packages: "reflect", "testing" */

// test for exercise:
func TestBasicCalculator_Sum(t *testing.T) {
	calculator := BasicCalculator{}

	tests := []struct {
		name string
		a, b int
		want int
	}{
		{"Sum of 1 and 1", 1, 1, 2},
		{"Sum of -1 and 1", -1, 1, 0},
		{"Sum of 0 and 0", 0, 0, 0},
		{"Sum of 100 and 200", 100, 200, 300},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := calculator.Sum(tt.a, tt.b); got != tt.want {
				t.Errorf("Sum(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.want)
			}
		})
	}
}

// text for extra i
func TestProfileFieldsExist(t *testing.T) {
	profile := CreateProfile()

	if profile.Name == "" {
		t.Error("Expected field 'Name' to be present")
	}
	if profile.Age == 0 {
		t.Error("Expected field 'Age' to be present")
	}
	if profile.BirthDate == "" {
		t.Error("Expected field 'BirthDate' to be present")
	}
	if len(profile.ProgrammingLanguages) == 0 {
		t.Error("Expected field 'ProgrammingLanguages' to be present")
	}
}

// test for extra ii
func TestProfileDataCorrectness(t *testing.T) {
	expectedProfile := Profile{
		Name:                 "Isaias Ramos López",
		Age:                  21,
		BirthDate:            "2002-11-09",
		ProgrammingLanguages: []string{"Go", "Java", "Python"},
	}

	profile := CreateProfile()

	if profile.Name != expectedProfile.Name {
		t.Errorf("Expected Name to be %v, got %v", expectedProfile.Name, profile.Name)
	}
	if profile.Age != expectedProfile.Age {
		t.Errorf("Expected Age to be %v, got %v", expectedProfile.Age, profile.Age)
	}
	if profile.BirthDate != expectedProfile.BirthDate {
		t.Errorf("Expected BirthDate to be %v, got %v", expectedProfile.BirthDate, profile.BirthDate)
	}
	if !reflect.DeepEqual(profile.ProgrammingLanguages, expectedProfile.ProgrammingLanguages) {
		t.Errorf("Expected ProgrammingLanguages to be %v, got %v", expectedProfile.ProgrammingLanguages, profile.ProgrammingLanguages)
	}
}

/* run all test with go test -v*/
