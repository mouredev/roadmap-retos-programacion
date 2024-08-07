package main

import "fmt"

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* --------------------------------- BadUser -------------------------------- */

type BadUser struct {
	Email     string
	FirstName string
	LastName  string
}

func (user *BadUser) Save() error {
	fmt.Println("User saved!")
	return nil
}

func (user *BadUser) SendEmail() error {
	fmt.Println("Email sent!")
	return nil
}

/* -------------------------------- GoodUser -------------------------------- */

type GoodUser struct {
	Email     string
	FirstName string
	LastName  string
}

/* ------------------------------ EmailService ------------------------------ */

type EmailService struct{}

func (emailService *EmailService) Send() error {
	fmt.Println("Email sent!")
	return nil
}

/* ----------------------------- DatabaseService ---------------------------- */

type DatabaseService struct{}

func (databaseService *DatabaseService) SaveUser() error {
	fmt.Println("User saved!")
	return nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Single Responsibility Principle (SRP)...
	*/

	fmt.Println("Single Responsibility Principle (SRP)...")

	fmt.Println(
		"\n```",
		"\ntype BadUser struct {\n  Email  string\n  FirstName  string\n  LastName  string\n}",
		"\n\nfunc (user *BadUser) Save() error {\n  fmt.Println(\"User saved!\")\n  return nil\n}",
		"\n\nfunc (user *BadUser) SendEmail() error {\n  fmt.Println(\"Email sent!\")\n  return nil\n}",
		"\n```",
	)

	fmt.Println("\nBad implementation of Single Responsibility Principle (SRP)...")

	fmt.Println(
		"\n```",
		"\ntype GoodUser struct {\n  Email  string\n  FirstName  string\n  LastName string\n}",
		"\n\ntype EmailService struct{}",
		"\n\nfunc (emailService *EmailService) Send() error {\n  fmt.Println(\"Email sent!\")\n  return nil\n}",
		"\n\ntype DatabaseService struct{}",
		"\n\nfunc (databaseService *DatabaseService) SaveUser() error {\n  fmt.Println(\"User saved!\")\n  return nil\n}",
		"\n```",
	)

	fmt.Println(
		"\nThis is a bad implementation of Single Responsibility Principle (SRP),",
		"\nbecause the class 'BadUser' has three responsibilities:",
		"\n\n1°) User creation.",
		"\n2°) Data persistence of the user.",
		"\n3°) User notification.",
	)

	fmt.Println("\nGood implementation of Single Responsibility Principle (SRP)...")

	fmt.Print(
		"\nThis is a good implementation of Single Responsibility Principle (SRP),",
		"\nbecause each class ('GoodUser', 'EmailService', and 'DatabaseService') has only",
		"\none responsability (user creation, notifications service, and data persistance).",
	)
}
