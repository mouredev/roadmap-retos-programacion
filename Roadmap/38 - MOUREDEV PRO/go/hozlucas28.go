package main

import (
	"encoding/csv"
	"fmt"
	"math/rand"
	"os"
	"slices"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                 STRUCTURES                                 */
/* -------------------------------------------------------------------------- */

type User struct {
	Email  string
	ID     string
	Status string
	_      struct{}
}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

func createCSV(content *[][]string, path string) error {
	csvFile, err := os.Create(path)
	if err != nil {
		return err
	}
	defer csvFile.Close()

	writer := csv.NewWriter(csvFile)
	defer writer.Flush()

	err = writer.WriteAll(*content)
	if err != nil {
		return err
	}

	return nil
}

func getCSVData(path string) (*[][]string, error) {
	var csvData [][]string

	csvFileContent, err := os.ReadFile(path)
	if err != nil {
		return &csvData, err
	}

	reader := csv.NewReader(strings.NewReader(string(csvFileContent)))

	csvData, err = reader.ReadAll()
	if err != nil {
		return &csvData, err
	}

	return &csvData, nil
}

func getUniqueChoices(choices *[]User, nUniqueChoices int) *[]*User {
	var uniqueChoices []*User

	for len(uniqueChoices) < nUniqueChoices {
		var rndIndex int = rand.Intn(len(*choices))
		var rndChoice *User = &(*choices)[rndIndex]

		if !slices.Contains(uniqueChoices, rndChoice) {
			uniqueChoices = append(uniqueChoices, rndChoice)
		}
	}

	return &uniqueChoices
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var csvContent [][]string = [][]string{
		{"email", "id", "status"},
		{"test01@gmail.com", "1", "active"},
		{"test02@gmail.com", "2", "inactive"},
		{"test03@gmail.com", "3", "inactive"},
		{"test04@gmail.com", "4", "active"},
		{"test05@gmail.com", "5", "inactive"},
		{"test06@gmail.com", "6", "active"},
		{"test07@gmail.com", "7", "active"},
		{"test08@gmail.com", "8", "active"},
	}

	var err error = createCSV(&csvContent, "./users.csv")
	if err != nil {
		panic(err)
	}

	csvUsers, err := getCSVData("./users.csv")
	if err != nil {
		panic(err)
	}

	var users []User
	for _, csvUser := range (*csvUsers)[1:] {
		var user User = User{
			Email:  csvUser[0],
			ID:     csvUser[1],
			Status: csvUser[2],
		}

		users = append(users, user)
	}

	users = slices.DeleteFunc(users, func(user User) bool {
		return user.Status == "inactive"
	})

	var winners *[]*User = getUniqueChoices(&users, 3)

	fmt.Println(winners)

	fmt.Println("> The first winner is...")
	fmt.Printf("> Congratulations %s with id %s, you won a subscription!\n", (*winners)[0].Email, (*winners)[0].ID)

	fmt.Println("\n> The second winner is...")
	fmt.Printf("> Congratulations %s with id %s, you won a discount!\n", (*winners)[1].Email, (*winners)[1].ID)

	fmt.Println("\n> The third winner is...")
	fmt.Printf("> Congratulations %s with id %s, you won a book!", (*winners)[2].Email, (*winners)[2].ID)
}
