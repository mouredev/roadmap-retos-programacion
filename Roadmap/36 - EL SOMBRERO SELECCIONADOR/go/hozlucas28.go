package main

import (
	"bufio"
	"fmt"
	"maps"
	rand "math/rand/v2"
	"os"
	"slices"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                   STRUCTS                                  */
/* -------------------------------------------------------------------------- */

type Question struct {
	CorrectAnswer string
	Options       []string
	Points        float32
	Question      string
	_             struct{}
}

type QuestionsPerHouse struct {
	Backend  [2]Question
	Data     [2]Question
	Frontend [2]Question
	Mobile   [2]Question
	_        struct{}
}

/* -------------------------------------------------------------------------- */
/*                                    UTILS                                   */
/* -------------------------------------------------------------------------- */

func toLongDisjunction[T string](slice []T) string {
	var arrayLength int = len(slice)

	if arrayLength == 0 {
		panic("slice empty")
	}

	var rtn string = string(slice[0])

	if arrayLength == 1 {
		return rtn
	}

	for _, element := range slice[1 : arrayLength-1] {
		rtn += fmt.Sprintf(", %s", element)
	}

	rtn += fmt.Sprintf(", and %s", slice[arrayLength-1])

	return rtn
}

func rndChoice[T string](choices []T) T {
	var choicesLength int = len(choices)

	if choicesLength == 0 {
		panic("slice of choices empty")
	}

	if choicesLength == 1 {
		return choices[0]
	}

	var rndIndex int = rand.IntN(choicesLength - 1)

	return choices[rndIndex]
}

func makeQuestion[T string](question *Question) float32 {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)

	var questionMsg string = fmt.Sprintf("> %s (%s): ", question.Question, toLongDisjunction(question.Options))

	fmt.Print(questionMsg)
	userAnswer, err := reader.ReadString('\n')
	if err == nil {
		userAnswer = strings.ToUpper(strings.TrimSpace(userAnswer))
	}

	var exit bool = slices.ContainsFunc(question.Options, func(opt string) bool {
		return strings.Compare(userAnswer, strings.ToUpper(opt)) == 0
	})

	for !exit {
		fmt.Printf("\n> Invalid option! Try again...\n\n")

		fmt.Print(questionMsg)
		userAnswer, err := reader.ReadString('\n')
		if err == nil {
			userAnswer = strings.ToUpper(strings.TrimSpace(userAnswer))
		}

		exit = slices.ContainsFunc(question.Options, func(opt string) bool {
			return strings.Compare(userAnswer, strings.ToUpper(opt)) == 0
		})
	}

	if strings.Compare(userAnswer, strings.ToUpper(question.CorrectAnswer)) == 0 {
		return question.Points
	} else {
		return 0
	}

}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)

	var questionsPerHouse QuestionsPerHouse = QuestionsPerHouse{
		Backend: [2]Question{
			{
				CorrectAnswer: "JavaScript",
				Options:       []string{"Java", "JavaScript", "Python", "Ruby"},
				Question:      "What is the primary language used in backend development?",
				Points:        5,
			},
			{
				CorrectAnswer: "PostgreSQL",
				Options:       []string{"MySQL", "MongoDB", "PostgreSQL", "SQLite"},
				Points:        5,
				Question:      "Which database is commonly used for storing data in backend applications?",
			},
		},
		Data: [2]Question{
			{
				CorrectAnswer: "Data analysis",
				Options:       []string{"Data analysis", "Data visualization", "Data mining", "Data modeling"},
				Points:        5,
				Question:      "What is the process of analyzing and interpreting data called?",
			},
			{
				CorrectAnswer: "Julia",
				Options:       []string{"Python", "R", "SQL", "Julia"},
				Points:        5,
				Question:      "Which programming language is commonly used for data analysis?",
			},
		},
		Frontend: [2]Question{
			{
				CorrectAnswer: "JavaScript",
				Options:       []string{"HTML", "CSS", "JavaScript", "Python"},
				Points:        5,
				Question:      "What is the primary language used in frontend development?",
			},
			{
				CorrectAnswer: "Angular",
				Options:       []string{"React", "Angular", "Vue", "Ember"},
				Points:        5,
				Question:      "Which framework is commonly used for building user interfaces?",
			},
		},
		Mobile: [2]Question{
			{
				CorrectAnswer: "Flutter",
				Options:       []string{"iOS", "Android", "React Native", "Flutter"},
				Points:        5,
				Question:      "Which platform is commonly used for developing mobile applications?",
			},
			{
				CorrectAnswer: "Objective-C",
				Options:       []string{"Swift", "Kotlin", "Java", "Objective-C"},
				Points:        5,
				Question:      "What is the primary language used in mobile app development?",
			},
		},
	}

	fmt.Print("> Enter your name: ")
	userName, err := reader.ReadString('\n')
	if err != nil {
		panic(err)
	}
	userName = strings.TrimSpace(userName)

	var pointsPerHouse map[string]float32 = map[string]float32{
		"backend":  0,
		"data":     0,
		"frontend": 0,
		"mobile":   0,
	}

	fmt.Println()
	pointsPerHouse["backend"] += makeQuestion(&questionsPerHouse.Backend[0])

	fmt.Println()
	pointsPerHouse["backend"] += makeQuestion(&questionsPerHouse.Backend[1])

	fmt.Println()
	pointsPerHouse["data"] += makeQuestion(&questionsPerHouse.Data[0])

	fmt.Println()
	pointsPerHouse["data"] += makeQuestion(&questionsPerHouse.Data[1])

	fmt.Println()
	pointsPerHouse["frontend"] += makeQuestion(&questionsPerHouse.Frontend[0])

	fmt.Println()
	pointsPerHouse["frontend"] += makeQuestion(&questionsPerHouse.Frontend[1])

	fmt.Println()
	pointsPerHouse["mobile"] += makeQuestion(&questionsPerHouse.Mobile[0])

	fmt.Println()
	pointsPerHouse["mobile"] += makeQuestion(&questionsPerHouse.Mobile[1])

	var maxPoint float32 = max(
		pointsPerHouse["backend"],
		pointsPerHouse["data"],
		pointsPerHouse["frontend"],
		pointsPerHouse["mobile"],
	)

	var maxPoints map[string]float32 = map[string]float32{
		"backend":  pointsPerHouse["backend"],
		"data":     pointsPerHouse["data"],
		"frontend": pointsPerHouse["frontend"],
		"mobile":   pointsPerHouse["mobile"],
	}

	maps.DeleteFunc(maxPoints, func(key string, value float32) bool {
		return value != maxPoint
	})

	if len(maxPoints) == 1 {
		for house := range maxPoints {
			fmt.Printf("\n> %s will be part of the %s house!", userName, house)
			break
		}
		return
	}

	var houses []string
	for house := range maxPoints {
		houses = append(houses, house)
	}

	var rndHouse string = rndChoice(houses)

	fmt.Printf("\n> The decision has been complicated, but %s will be part of the %s house!", userName, rndHouse)
}
