package main

import "fmt"

/* -- Exercise */

type User struct {
	Name  string
	Email string
}

/* -- exercise -- incorrect */

func (u *User) Save() {
	fmt.Printf("Saving user %s to the database\n", u.Name)
}

func (u *User) SendEmail() {
	fmt.Printf("Sending email to %s\n", u.Email)
}

/* -- exercise -- correct */

type UserRepository struct{}

func (repo *UserRepository) Save(user User) {
	fmt.Printf("Saving user %s to the database\n", user.Name)
}

type EmailService struct{}

func (service *EmailService) SendEmail(user User) {
	fmt.Printf("Sending email to %s\n", user.Email)
}

/* -- Extra Challenge */

type Book struct {
	Title  string
	Author string
	Copies int
}

type UserT struct {
	Name  string
	ID    string
	Email string
}

/* -- extra challenge - incorrect */

type Library struct {
	Books []Book
	Users []UserT
	Loans map[string]string // map[userID]bookTitle
}

func (lib *Library) AddBook(book Book) {
	lib.Books = append(lib.Books, book)
	fmt.Printf("Book '%s' by '%s' added to the library.\n", book.Title, book.Author)
}

func (lib *Library) AddUser(user UserT) {
	lib.Users = append(lib.Users, user)
	fmt.Printf("User '%s' added to the library.\n", user.Name)
}

func (lib *Library) LoanBook(userID, bookTitle string) {
	lib.Loans[userID] = bookTitle
	fmt.Printf("User '%s' loaned book '%s'.\n", userID, bookTitle)
}

/* -- extra challenge - correct */

type BookRepositoryC struct {
	Books []Book
}

func (repo *BookRepositoryC) AddBook(book Book) {
	repo.Books = append(repo.Books, book)
	fmt.Printf("Book '%s' by '%s' added to the library.\n", book.Title, book.Author)
}

type UserRepositoryC struct {
	Users []UserT
}

func (repo *UserRepositoryC) AddUserC(user UserT) {
	repo.Users = append(repo.Users, user)
	fmt.Printf("User '%s' added to the library.\n", user.Name)
}

type LoanService struct {
	Loans map[string]string // map[userID]bookTitle
}

func (service *LoanService) LoanBook(userID, bookTitle string) {
	service.Loans[userID] = bookTitle
	fmt.Printf("User '%s' loaned book '%s'.\n", userID, bookTitle)
}

func main() {
	/* Exercise */
	user := User{Name: "Legion Commander", Email: "legioncommander@gmail.com"}
	/* -- incorrect use */
	user.Save()
	user.SendEmail()

	/* -- correct use */
	userRepo := UserRepository{}
	userRepo.Save(user)

	emailService := EmailService{}
	emailService.SendEmail(user)

	/* Extra Challenge */
	/* -- incorrect use */
	library := &Library{
		Books: []Book{},
		Users: []UserT{},
		Loans: make(map[string]string),
	}

	library.AddBook(Book{Title: "1984", Author: "George Orwell", Copies: 3})
	library.AddUser(UserT{Name: "Legion Commander", ID: "xyz-123", Email: "legioncommander@gmail.com"})
	library.LoanBook("xyz-123", "1984")

	/* -- correct use */
	bookRepoC := &BookRepositoryC{Books: []Book{}}
	userRepoC := &UserRepositoryC{Users: []UserT{}}
	loanService := &LoanService{Loans: make(map[string]string)}

	bookRepoC.AddBook(Book{Title: "1984", Author: "George Orwell", Copies: 3})
	userRepoC.AddUserC(UserT{Name: "Legion Commander", ID: "xyz-123", Email: "legioncommander@gmail.com"})
	loanService.LoanBook("123", "1984")
}
