/*
  * EJERCICIO:
  * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
  * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
  * de forma correcta e incorrecta.
*/

// Correcto
class User {
  constructor(name, age, email) {
    this.name = name
    this.age = age
    this.email = email
  }
}

class SaveUser {
  save(user) {
    return
  }
}

class GetUsers {
  getUsers() {
    return
  }
}

// Incorrecto
class User_2 {
  constructor(name, age, email) {
    this.name = name
    this.age = age
    this.email = email
  }

  save(user) {
    return
  }

  getUsers() {
    return
  }
}

/*
  * DIFICULTAD EXTRA (opcional):
  * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
  * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
  * y el procesamiento de préstamos de libros.
  * Requisitos:
  * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
  * información básica como título, autor y número de copias disponibles.
  * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
  * información básica como nombre, número de identificación y correo electrónico.
  * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
  * tomar prestados y devolver libros.
  * Instrucciones:
  * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
  * los tres aspectos mencionados anteriormente (registro de libros, registro de
  * usuarios y procesamiento de préstamos).
  * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
  * siguiendo el Principio de Responsabilidad Única.
*/

class Library {
  constructor() {
    this.books = []
    this.users = []
    this.loans = []
  }

  booksRegister(title, author, availableCopies) {
    if (availableCopies > 0) {
      this.books.push({ title, author, availableCopies })
    } else {
      console.log('Cantidad de copias debe ser mayor a 0')
    }
  }

  usersRegister(name, id, email) {
    this.users.push({ name, id, email })
  }

  booksLoan(state, quantity, bookTitle, userId) {
    if (state === 'prestar') {
      let bookFound = false

      this.books.forEach(book => {
        if (book.title === bookTitle) {
          bookFound = true
          if (quantity > 0 && book.availableCopies >= quantity) {
            console.log('Libro prestado')
            book.availableCopies -= quantity
            this.loans.push({ bookTitle, userId, quantity })
          } else {
            console.log('No hay suficientes copias disponibles para prestar')
          }
        }
      })

      if (!bookFound) {
        console.log('Libro no encontrado')
      }

    } else if (state === 'devolver') {
      let loanFound = false

      this.loans = this.loans.filter(item => {
        if (item.bookTitle === bookTitle && item.userId === userId) {
          loanFound = true
          this.books.forEach(book => {
            if (book.title === bookTitle) {
              console.log('Libro devuelto')
              book.availableCopies += item.quantity
            }
          })
          return false
        }
        return true
      })

      if (!loanFound) {
        console.log('No se encontró un préstamo correspondiente para devolver')
      }

    } else {
      console.log('Opción no válida')
    }
  }
}

const library = new Library()
library.booksRegister('Harry Potter', 'J.K. Rowling', 12)
library.booksRegister('Harry Potter 2', 'J.K. Rowling', 7)
library.booksRegister('Harry Potter 3', 'J.K. Rowling', 6)
library.usersRegister('Victor', 123, 'victor@gmail.com')
library.usersRegister('Juan', 124, 'juan@gmail.com')
library.booksLoan('prestar', 2, 'Harry Potter', 123)
library.booksLoan('prestar', 1, 'Harry Potter', 124)
library.booksLoan('devolver', 2, 'Harry Potter', 123)
console.log(library)

// Refactor SRP

class LibraryContent {
  constructor(books = [], users = [], loans = []) {
    this.books = books
    this.users = users
    this.loans = loans
  }
}

class BooksRegister {
  constructor() {
    this.books = []
  }

  booksRegister(title, author, availableCopies) {
    if (availableCopies > 0) {
      this.books.push({ title, author, availableCopies })
    } else {
      console.log('Cantidad de copias debe ser mayor a 0')
    }
  }
}

class UsersRegister {
  constructor() {
    this.users = []
  }

  usersRegister(name, id, email) {
    this.users.push({ name, id, email })
  }
}

class BooksLoans {
  constructor(library) {
    this.library = library
  }

  booksLoan(state, quantity, bookTitle, userId) {
    if (state === 'prestar') {
      const book = this.library.books.find(book => book.title === bookTitle)
      const user = this.library.users.find(user => user.id === userId)

      if (book && user) {
        if (quantity > 0 && book.availableCopies >= quantity) {
          console.log('Libro prestado')
          book.availableCopies -= quantity
          this.library.loans.push({ bookTitle, userId, quantity })
        } else {
          console.log('No hay suficientes copias disponibles para prestar')
        }
      } else {
        console.log(book ? 'Usuario no encontrado' : 'Libro no encontrado')
      }

    } else if (state === 'devolver') {
      const loanIndex = this.library.loans.findIndex(
        loan => loan.bookTitle === bookTitle && loan.userId === userId
      )

      if (loanIndex !== -1) {
        const loan = this.library.loans[loanIndex]
        const book = this.library.books.find(book => book.title === bookTitle)

        if (book) {
          console.log('Libro devuelto')
          book.availableCopies += loan.quantity
          this.library.loans.splice(loanIndex, 1)
        }
      } else {
        console.log('No se encontró un préstamo correspondiente para devolver')
      }

    } else {
      console.log('Opción no válida')
    }
  }
}


let bookRegister = new BooksRegister()
bookRegister.booksRegister('Harry Potter', 'J.K. Rowling', 12)
bookRegister.booksRegister('Harry Potter 2', 'J.K. Rowling', 22)
bookRegister.booksRegister('Harry Potter 3', 'J.K. Rowling', 2)

let userRegister = new UsersRegister()
userRegister.usersRegister('Victor', 1231, 'victor@gmail.com')
userRegister.usersRegister('Juan', 1232, 'juan@gmail.com')
userRegister.usersRegister('John', 1233, 'john@gmail.com')
userRegister.usersRegister('Alfred', 1234, 'alfred@gmail.com')


let myLibrary = new LibraryContent(bookRegister.books, userRegister.users)


let loansSystem = new BooksLoans(myLibrary)
loansSystem.booksLoan('prestar', 2, 'Harry Potter', 1231)
loansSystem.booksLoan('prestar', 1, 'Harry Potter', 1232)
loansSystem.booksLoan('devolver', 2, 'Harry Potter', 1231)

console.log(myLibrary.books)
console.log(myLibrary.users)
console.log(myLibrary.loans)