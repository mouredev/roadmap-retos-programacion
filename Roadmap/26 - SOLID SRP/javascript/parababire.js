// Forma incorrecta

class Person_Incorrect {
  constructor(name, mail) {
    this.name = name,
    this.mail = mail
  }
  show_name() {
    console.log(this.name)
  }
  show_mail() {
    console.log(this.mail)
  }
}

let user = new Person_Incorrect('Ángel', 'angelenarvaez@gmail.com')
user.show_name()
user.show_mail()

// Forma correcta

class Person {
  constructor(name, mail) {
    this.name = name,
    this.mail = mail
  }
}
class Person_Name {
  saludo(person) {
    return `Hola mi nombre es ${person.name}`
  }
}
class Send_Mail {
  send(person, message) {
    return `${person.mail} ${message}`
  }
}

let person1 = new Person('Ángel', 'angelenarvaez@gmail.com')

let message = new Send_Mail()
console.log(message.send(person1, 'Bienvenido a nuestra plataforma'))

let bienvenida = new Person_Name()
console.log(bienvenida.saludo(person1))

// Extra

// Forma incorrecta

class Library_Incorrect {
  constructor() {
    this.books = []
    this.users = []
    this.loans = []
  }
  add_book (bookName, author, copies) {
    return this.books.push({
      Title: bookName,
      Author: author,
      Copies: copies
    })
  }
  add_user (userName, id, mail) {
    return this.users.push({
      User: userName,
      Id_Number: id,
      Mail: mail
    })
  }
  loan_book (user_id, book_title) {
    for (const book of this.books) {
      if (book.Title == book_title && book.Copies > 0) {
        book.Copies -= 1
        this.loans.push({
          User_Id: user_id,
          Book_Title: book_title
        })
        return true
      }
      return false
    }
  }
  return_book (user_id, book_title) {
    for (const loan of this.loans) {
      if (loan.User_Id == user_id && loan.Book_Title == book_title) {
        this.loans = this.loans.filter(function (el) {
          return el.User_Id != user_id
        })
        for (const book of this.books) {
          if (book.Title == book_title) {
            book.Copies += 1
          }
        }
        return true
      }
      return false
    }
  }
}

// Forma correcta

class Book {
  constructor(title, author, copies) {
    this.title = title,
    this.author = author,
    this.copies = copies
  }
}

class User {
  constructor(name, id, mail) {
    this.name = name,
    this.id = id,
    this.mail = mail
  }
}
// Gestión de prestamos
class Loans {
  constructor() {
    this.loans = []
  }
  loan_book (user, book) {
      if (book.copies > 0) {
        book.copies -= 1
        this.loans.push({
          User_Id: user.id,
          Book_Title: book.title
        })
        return true
      }
      return false
  }
  return_book (user, book) {
    for (const loan of this.loans) {
      if (loan.User_Id == user.id && loan.Book_Title == book.title) {
        this.loans = this.loans.filter(function (el) {
          return el.User_Id != user_id
        })
        book.copies += 1
        return true
      }
      return false
    }
  }
}

class Library {
  constructor() {
    this.books = []
    this.users = []
    this.loans_service = new Loans()
  }
  add_book (book) {
    return this.books.push(book)
  }
  add_user (user) {
    return this.users.push(user)
  }
  loan_book (user_id, book_title) {
    let user = this.users.find((user) => user.id == user_id)
    let book = this.books.find((book) => book.title == book_title)
    if (user && book) {
      return this.loans_service.loan_book(user, book)
    }
    return false
  }

  return_book (user_id, book_title) {
    let user = this.users.find((user) => user.id == user_id)
    let book = this.books.find((book) => book.title == book_title)
    if (user && book) {
      return this.loans_service.return_book(user, book)
    }
    return false
  }
}

let someBook = new Book('100 Años de Soledad', 'Gabo', 10)
let principalLibrary = new Library()
principalLibrary.add_book(someBook)

let someUser = new User('Ángel', 15154142, 'anarvamon@gmail.com')
principalLibrary.add_user(someUser)

principalLibrary.loan_book(15154142, '100 Años de Soledad')
console.log(principalLibrary)
console.log(principalLibrary.loans_service)