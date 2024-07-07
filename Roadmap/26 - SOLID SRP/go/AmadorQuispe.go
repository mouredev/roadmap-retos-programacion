package main

import (
	"fmt"
)

//APLICANDO SRP

type Employee struct {
	id    int
	name  string
	email string
}

func (e *Employee) GetId() int {
	return e.id
}

func (e *Employee) GetName() string {
	return e.name
}

func (e *Employee) GetEmail() string {
	return e.email
}

// Repository
type EmployeeRepository struct {
	// Database connection or other storage-related fields
}

func (repo *EmployeeRepository) Save(employee *Employee) error {
	// Save user to the database
	fmt.Println("saving data...", employee)
	return nil
}

// Service
type EmployeeService struct {
	//Repositories and other services
}

func (svc *EmployeeService) Notification(employee *Employee) error {
	fmt.Println("Sending notification", employee.GetEmail())
	return nil
}

//EXTRA
// APLICANDO SRP

type User struct {
	doi   string
	name  string
	email string
}

type UserRepository struct {
	users []User
}

func (userRepo *UserRepository) Register(user User) {
	userRepo.users = append(userRepo.users, user)
	fmt.Println("usuario registrado")
}

func (userRepo *UserRepository) FindByDoi(doi string) *User {
	for i, user := range userRepo.users {
		if user.doi == doi {
			return &userRepo.users[i]
		}
	}
	return nil
}

type Book struct {
	title  string
	author string
	copies int
}

type BookRepository struct {
	books []Book
}

func (bookRepo *BookRepository) Register(book Book) {
	bookRepo.books = append(bookRepo.books, book)
	fmt.Println("libro registrado")
}

func (bookRepo *BookRepository) FindByTitle(title string) *Book {
	for i, book := range bookRepo.books {
		if book.title == title {
			return &bookRepo.books[i]
		}
	}
	return nil
}

func (bookRepo *BookRepository) IncreaseCopies(title string, delta int) {
	book := bookRepo.FindByTitle(title)
	book.copies += delta
}

type LoanRepository struct {
	loanBooks map[string][]string
}

func (loanRepo *LoanRepository) LoanBook(userDoi, bookTitle string) {
	if v, ok := loanRepo.loanBooks[userDoi]; ok {
		v = append(v, bookTitle)
		loanRepo.loanBooks[userDoi] = v
	} else {
		loanRepo.loanBooks[userDoi] = []string{bookTitle}
	}
	fmt.Println("préstamo del libro registrado")
}

func (loanRepo *LoanRepository) ReturnBook(userDoi, bookTitle string) {
	for key, values := range loanRepo.loanBooks {
		if key == userDoi {
			var newList []string
			for _, v := range values {
				if v != bookTitle {
					newList = append(newList, v)
				}
			}
			loanRepo.loanBooks[userDoi] = newList
			fmt.Println("Libro devuelto correctamente")
			break
		}
	}
}

type Library struct {
	bookRepo BookRepository
	userRepo UserRepository
	loanRepo LoanRepository
}

func (lib *Library) CreateBook(book Book) {
	lib.bookRepo.Register(book)
}

func (lib *Library) CreateUser(user User) {
	lib.userRepo.Register(user)
}

func (lib *Library) RegisterLoanBook(userDoi, bookTitle string) {
	user := lib.userRepo.FindByDoi(userDoi)
	book := lib.bookRepo.FindByTitle(bookTitle)
	if user == nil && book == nil {
		fmt.Println("usuario o book no está registrado")
	}
	lib.loanRepo.LoanBook(userDoi, bookTitle)
	lib.bookRepo.IncreaseCopies(bookTitle, -1)
}

func (lib *Library) RegisterReturnBook(userDoi, bookTitle string) {
	user := lib.userRepo.FindByDoi(userDoi)
	book := lib.bookRepo.FindByTitle(bookTitle)
	if user == nil && book == nil {
		fmt.Println("usuario o book no está registrado")
	}
	lib.loanRepo.ReturnBook(userDoi, bookTitle)
	lib.bookRepo.IncreaseCopies(bookTitle, +1)

}

func main() {
	/*library := Library{
		books:     []Book{},
		users:     []User{},
		loanBooks: make(map[string][]string),
	}
	library.AddUser(&User{doi: "44557855", name: "Amador", email: "aquispe@gmail.com"})
	library.AddBook(&Book{title: "clean code", author: "Robert C. Martin", copies: 4})
	library.LoanBook("clean code", "44557855")
	fmt.Println(library.books)
	library.ReturnBook("clean code", "44557855")
	fmt.Println(library.books)*/
	bookRepo := BookRepository{
		books: []Book{},
	}

	userRepo := UserRepository{
		users: []User{},
	}

	loanRepo := LoanRepository{
		loanBooks: make(map[string][]string),
	}

	library := Library{
		bookRepo: bookRepo,
		userRepo: userRepo,
		loanRepo: loanRepo,
	}

	library.CreateBook(Book{title: "clean code", author: "Robert C. Martin", copies: 4})
	library.CreateBook(Book{title: "clean architecture", author: "Robert C. Martin", copies: 4})

	library.CreateUser(User{doi: "44557855", name: "Amador", email: "aquispe@gmail.com"})
	library.CreateUser(User{doi: "44775588", name: "Alex", email: "alex@gmail.com"})

	library.RegisterLoanBook("44557855", "clean code")
	fmt.Println(library.bookRepo.books)

	library.RegisterReturnBook("44557855", "clean code")
	fmt.Println(library.bookRepo.books)

}

//Viola SRP
/*type Employee struct {
	id    int
	name  string
	email string
}

func (e *Employee) GetName() string {
	return e.name
}

func (e *Employee) GetEmail() string {
	return e.email
}

func (e *Employee) SaveToDatabase() {
	fmt.Println("saving data in database!! ", e)
}

func (e *Employee) SendNotification() {
	fmt.Println("sending notification ", e.email)
}*/

//EXTRA
//Viola SRP
/*
type Book struct {
	title  string
	author string
	copies uint
}

type User struct {
	doi   string
	name  string
	email string
}

type Library struct {
	books     []Book
	users     []User
	loanBooks map[string][]string
}

func (l *Library) AddUser(user *User) {
	l.users = append(l.users, *user)
}

func (l *Library) AddBook(book *Book) {
	l.books = append(l.books, *book)
}

func (l *Library) LoanBook(bookTitle, userDoi string) {
	var userFound *User
	var bookFound *Book
	for i, user := range l.users {
		if user.doi == userDoi {
			userFound = &l.users[i]
			break
		}
	}

	for i, book := range l.books {
		if book.title == bookTitle {
			bookFound = &l.books[i]
			break
		}
	}

	if userFound == nil || bookFound == nil {
		fmt.Println("usuario o libro no está registrada")
		return
	}

	if bookFound.copies <= 0 {
		fmt.Println("no copias disponibles")
		return
	}

	if v, ok := l.loanBooks[userDoi]; ok {
		v = append(v, bookTitle)
		l.loanBooks[userDoi] = v
	} else {
		l.loanBooks[userDoi] = []string{bookTitle}
	}
	bookFound.copies--
	fmt.Println("préstamo del libro ", bookTitle, " al usuario ", userDoi, "fué registrado.")
}

func (l *Library) ReturnBook(bookTitle, userDoi string) {
	var bookFound *Book
	for i, book := range l.books {
		if book.title == bookTitle {
			bookFound = &l.books[i]
			break
		}
	}
	for key, values := range l.loanBooks {
		if key == userDoi {
			var newList []string
			for _, v := range values {
				if v != bookTitle {
					newList = append(newList, v)
				}
			}
			bookFound.copies++
			l.loanBooks[userDoi] = newList
			fmt.Println("Libro devuelto correctamente")
			break
		}
	}
}
*/
