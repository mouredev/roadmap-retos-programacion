package main

import (
	"bufio"
	"fmt"
	"math/rand/v2"
	"os"
	"regexp"
	"strings"
)

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* ---------------------------- PasswordGenerator --------------------------- */

type passwordGenerator struct {
	_hash        string
	failAttempts uint
	length       uint
	password     string
	_            struct{}
}

type PasswordGenerator interface {
	GetFailAttempts() uint
	GetMaximumLength() uint

	GetAdvice(password string) string
	IsThePassword(password string) bool
}

func NewPasswordGenerator(_hash string, length uint) PasswordGenerator {
	var passwordGenerator passwordGenerator = passwordGenerator{
		_hash:  _hash,
		length: length,
	}

	for len(passwordGenerator.password) < int(length) {
		var rndChar rune = (rune)(_hash[rand.IntN(len(_hash))])
		if !strings.ContainsRune(passwordGenerator.password, rndChar) {
			passwordGenerator.password += (string)(rndChar)
		}
	}

	return &passwordGenerator
}

func (generator *passwordGenerator) GetFailAttempts() uint {
	return generator.failAttempts
}

func (generator *passwordGenerator) GetMaximumLength() uint {
	return generator.length
}

func (generator *passwordGenerator) GetAdvice(password string) string {
	var advice []string

	for i, char := range password {
		var passwordChar rune = (rune)(generator.password[i])

		if char == passwordChar {
			advice = append(advice, fmt.Sprintf("  - \"%c\" is in the correct position.", char))
			continue
		}

		if strings.ContainsRune(generator.password, char) {
			advice = append(advice, fmt.Sprintf("  - \"%c\" exist but it's not in the %dth position.", char, i+1))
			continue
		}

		advice = append(advice, fmt.Sprintf("  - \"%c\" not exist in the password.", char))
	}

	return strings.Join(advice, "\n")
}

func (generator *passwordGenerator) IsThePassword(password string) bool {
	if generator.password == password {
		return true
	}

	generator.failAttempts++
	return false
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var _hash string = "ABC123"
	var length uint = 4

	var passwordGenerator PasswordGenerator = NewPasswordGenerator(
		_hash,
		length,
	)

	regex, err := regexp.Compile(fmt.Sprintf("^[%s]{%d}$", _hash, length))
	if err != nil {
		panic(err)
	}

	var reader *bufio.Reader = bufio.NewReader(os.Stdin)

	fmt.Printf("> Enter the password (maximum of 4 chars): ")
	userInput, err := reader.ReadString('\n')
	if err != nil {
		panic(err)
	}

	userInput = strings.TrimSpace(userInput)

	for !regex.MatchString(userInput) {
		fmt.Printf(
			"\n> Error! The password length must be 4 characters, "+
				"and it should contain any of these characters: \"%s\". Try again...",
			_hash,
		)

		fmt.Printf("\n\n> Enter the password (maximum of 4 chars): ")
		userInput, err = reader.ReadString('\n')
		if err != nil {
			panic(err)
		}

		userInput = strings.TrimSpace(userInput)
	}

	for !passwordGenerator.IsThePassword(userInput) && passwordGenerator.GetFailAttempts() < 10 {
		fmt.Printf("\n%s", passwordGenerator.GetAdvice(userInput))

		fmt.Println("\n\n> Invalid password! Try again...")

		fmt.Printf("\n> Enter the password (maximum of 4 chars): ")
		userInput, err = reader.ReadString('\n')
		if err != nil {
			panic(err)
		}

		userInput = strings.TrimSpace(userInput)

		for !regex.MatchString(userInput) {
			fmt.Printf(
				"\n> Error! The password length must be 4 characters, "+
					"and it should contain any of these characters: \"%s\". Try again...",
				_hash,
			)

			fmt.Printf("\n\n> Enter the password (maximum of 4 chars): ")
			userInput, err = reader.ReadString('\n')
			if err != nil {
				panic(err)
			}

			userInput = strings.TrimSpace(userInput)
		}
	}

	if passwordGenerator.GetFailAttempts() < 10 {
		fmt.Printf("\n> Santa won! The password is \"%s\".", userInput)
	} else {
		fmt.Println("\n> Santa lost! Storage will be closed forever.")
	}
}
