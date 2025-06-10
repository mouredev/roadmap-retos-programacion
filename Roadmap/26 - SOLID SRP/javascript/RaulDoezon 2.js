// https://medium.com/@diego.coder/principios-solid-en-javascript-1c734e3554fd
// https://dev.to/ruben_alapont/solid-principles-series-understanding-the-single-responsibility-principle-srp-in-nodejs-with-typescript-57e8

/*
  EJERCICIO:
  Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
  Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
  de forma correcta e incorrecta.
*/

console.log("+++++++++ PRINCIPIO SOLID SRP IMPLEMENTADO DE FORMA INCORRECTA +++++++++");

class UserService {
  constructor(userName, password, user, subject, message) {
    this.userName = userName;
    this.password = password;
    this.user = user;
    this.subject = subject;
    this.message = message;
  }

  authenticateUser() {
    console.log(`Nombre de usuario: ${this.userName}. Contraseña: ${this.password}`);
  }

  sendEmail() {
    console.log(`- Usuario: ${this.user}.`);
    console.log(`- Asunto: ${this.subject}.`);
    console.log(`- Mensaje: ${this.message}`);
  }
}

let userService = new UserService("4rm4ndo", "12345678", "Armando", "SOLID SRP", "IMPLEMENTACIÓN INCORRECTA.");
userService.authenticateUser();
userService.sendEmail();

console.log("\n+++++++++ PRINCIPIO SOLID SRP IMPLEMENTADO DE FORMA CORRECTA +++++++++");

class AuthenticationService {
  authenticate(userName, password) {
    console.log(`- Nombre de usuario: ${userName}.\n- Contraseña: ${password}`);
  }
}

class EmailService {
  send(user, subject, message) {
    console.log(`- Usuario: ${user}.\n- Asunto: ${subject}.\n- Mensaje: ${message}`);
  }
}

let authentication = new AuthenticationService();
let email = new EmailService();

authentication.authenticate("RaulDoezon", "urue764h^<d");
email.send("Raúl", "Principio SOLID SRP", "El objetivo principal del SRP es promover la cohesión y la modularidad en el diseño de software. Al asignar una sola responsabilidad a cada clase, se facilita la comprensión, el mantenimiento y la evolución del código, ya que cada clase se enfoca en una tarea específica y limitada.");

/*
  DIFICULTAD EXTRA (opcional):
  Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
  manejar diferentes aspectos como el registro de libros, la gestión de usuarios
  y el procesamiento de préstamos de libros.
  Requisitos:
  1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
  información básica como título, autor y número de copias disponibles.
  2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
  información básica como nombre, número de identificación y correo electrónico.
  3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
  tomar prestados y devolver libros.
  Instrucciones:
  1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
  los tres aspectos mencionados anteriormente (registro de libros, registro de
  usuarios y procesamiento de préstamos).
  2. Refactoriza el código: Separa las responsabilidades en diferentes clases
  siguiendo el Principio de Responsabilidad Única.
*/

// https://www.youtube.com/watch?v=7NM8FK9G91M&list=PLv0dxH7HRDx_kQRNoldG7iPvydy8DyvE3&index=28

console.log("\nDIFICULTAD EXTRA +++++++++");

// INCORRECTO
/*
class Library {
  constructor() {
    this.books = [];
    this.users = [];
    this.loans = [];
  }

  bookRegister(title, author, numberCopies) {
    this.books.push({title, author, numberCopies});

    console.log(`- Libro: ${title}. Autor: ${author}. Número de copias: ${numberCopies}`);
  }

  userRegister(name, idNumber, email) {
    this.users.push({name, idNumber, email});

    console.log(`- Usuario: ${name}. ID: ${idNumber}. Correo electrónico: ${email}`);
  }

  lendBook(loanBook, userID) {
    const checkBook = this.books.find((book) => book.title === loanBook && book.numberCopies > 0);
    const checkUser = this.users.find((user) => user.idNumber === userID);

    if (checkBook && checkUser) {
      this.loans.push({title: checkBook.title, userId: checkUser.idNumber});
      checkBook.numberCopies -= 1;

      console.log(`El libro ${checkBook.title} ha sido prestado al usuario ${checkUser.name} con ID: ${checkUser.idNumber}`);
    } else {
      console.log(`Lo sentimos ${checkUser.name}, el libro ${loanBook} no está disponible.`);
    }
  }

  returnBook(returnbook, userID) {
    const checkBorrowedBook = this.loans.findIndex((book) => book.title === returnbook && book.userId === userID);

    if (checkBorrowedBook > -1) {
      this.loans.splice(checkBorrowedBook, 1);
      this.books.find((book) => book.numberCopies += 1);

      console.log(`El libro ${returnbook} ha sido devuelto.`);
    } else {
      console.log(`El libro ${returnbook} o el ID de usuario ${userID} no corresponden al préstamo.`);
    }
  }
}

let library = new Library();
library.bookRegister("Corre Nicky Corre", "Nicky Cruz", 1);
library.bookRegister("La Cruz y el Puñal", "David Wilkerson", 4);
library.userRegister("Raúl", 112233, "raul@email.com");
library.userRegister("Armando", 445566, "armando@email.com");
library.lendBook("Corre Nicky Corre", 112233);
library.lendBook("Corre Nicky Corre", 445566);
library.returnBook("Corre Nicky Corre", 112233);

console.log(library.books);
console.log(library.users);
console.log(library.loans);
*/

// CORRECTO
class Library {
  constructor() {
    this.books = [];
    this.users = [];
  }

  bookRegister(book) {
    this.books.push(book);

    console.log(`- Libro: ${book.title}. Autor: ${book.author}. Número de copias: ${book.numberCopies}`);
  }

  userRegister(user) {
    this.users.push(user);

    console.log(`- Usuario: ${user.name}. ID: ${user.idNumber}. Correo electrónico: ${user.email}`);
  }

  findBook(bookTitle) {
    return this.books.find((book) => book.title === bookTitle && book.numberCopies > 0);
  }

  findUser(userID) {
    return this.users.find((user) => user.idNumber === userID);
  }
}

class Books {
  constructor(title, author, numberCopies) {
    this.title = title;
    this.author = author;
    this.numberCopies = numberCopies;
  }
}

class Users {
  constructor(name, idNumber, email) {
    this.name = name;
    this.idNumber = idNumber;
    this.email = email;
  }
}

class Loans {
  constructor() {
    this.loans = [];
  }

  lendBook(booksInformation, bookName, userID) {
    const checkBook = booksInformation.findBook(bookName);
    const checkUser = booksInformation.findUser(userID);

    if (checkBook && checkUser) {
      this.loans.push({title: checkBook.title, userId: checkUser.idNumber});
      checkBook.numberCopies -= 1;

      console.log(`El libro ${checkBook.title} ha sido prestado al usuario ${checkUser.name} con ID: ${checkUser.idNumber}`);
    } else {
      console.log(`Lo sentimos ${checkUser.name}, el libro ${bookName} no está disponible.`);
    }
  }

  returnBook(booksInformation, returnbook, userID) {
    const checkBorrowedBook = this.loans.findIndex((book) => book.title === returnbook && book.userId === userID);

    if (checkBorrowedBook > -1) {
      this.loans.splice(checkBorrowedBook, 1);
      booksInformation.books.find((book) => book.numberCopies += 1);

      console.log(`El libro ${returnbook} ha sido devuelto.`);
    } else {
      console.log(`El libro ${returnbook} o el ID de usuario ${userID} no corresponden al préstamo.`);
    }
  }
}

const library = new Library();
const book1 = new Books("Las Crónicas de Narnia: El Sobrino del Mago", "C. S. Lewis", 1);
const book2 = new Books("Cartas del diablo a su sobrino", "C. S. Lewis", 4);
const user1 = new Users("Raúl", 112233, "raul@email.com");
const user2 = new Users("Armando", 445566, "armando@email.com");
const loan = new Loans();

library.bookRegister(book1);
library.bookRegister(book2);
library.userRegister(user1);
library.userRegister(user2);
loan.lendBook(library, "Las Crónicas de Narnia: El Sobrino del Mago", 112233);
loan.lendBook(library, "Las Crónicas de Narnia: El Sobrino del Mago", 445566);
loan.returnBook(library, "Las Crónicas de Narnia: El Sobrino del Mago", 112233);

console.log(library.books);
console.log(library.users);
console.log(loan.loans);
