/* EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
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


// Incorrect


class User1 {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    addUser() {
        // add user
    }

    sendEmail() {
        // send an email
    }
};


// Correct


class User2 {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
}


class UserService {
    addUser(user) {
        // add user to database
    }
}


class EmailService {
    sendEmail(email, message) {
        // send an email
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


// Incorrect


class LibraryWrong {
    constructor() {
        this.books = [];
        this.users = [];
        this.loans = [];
    }

    addBook(title, author, copies) {
        this.books.push({title, author, copies});
    }

    addUser(id, name, email) {
        this.users.push({id, name, email});
    }

    loanBook(userId, bookTitle) {
        for (const book of this.books) {
            if (book.title === bookTitle && book.copies > 0) {
                book.copies--;
                this.loans.push({userId, bookTitle});
                return true;
            }
        }

        return false;
    }

    returnBook(userId, bookTitle) {
        for (const loan of this.loans) {
            if (loan.userId === userId && loan.bookTitle === bookTitle) {
                const currentIndex = this.loans.indexOf(loan);
                this.loans.splice(currentIndex, 1);
                
                for (const book of this.books) {
                    if (book.title === bookTitle) {
                        book.copies++;
                        return true;
                    }
                }
            }
        }

        return false;
    }
}


// Correct


class User {
    constructor(id, name, email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }
}


class Book {
    constructor(title, author, copies) {
        this.title = title;
        this.author = author;
        this.copies = copies;
    }
}


class BookLending {
    constructor() {
        this.loans = [];
    }

    loanBook(user, book) {
        if (book.copies > 0) {
            book.copies--;
            this.loans.push({userId: user.id, bookTitle: book.title});
            return true;
        }

        return false;
    }

    returnBook(user, book) {
        for (const loan of this.loans) {
            if (loan.userId === user.id && loan.bookTitle === book.title) {
                const currentIndex = this.loans.indexOf(loan);
                this.loans.splice(currentIndex, 1);
                book.copies++;
                return true;
            }
        }

        return false;
    }
}


class Library {
    constructor() {
        this.books = [];
        this.users = [];
        this.loansService = new BookLending();
    }

    addBook(book) {
        this.books.push(book);
    }

    addUser(user) {
        this.users.push(user);
    }

    loanBook(userId, bookTitle) {
        const user = this.users.find(u => u.id === userId);
        const book = this.books.find(b => b.title === bookTitle);

        if (user && book) {
            return this.loansService.loanBook(user, book);
        }

        return false;
    }

    returnBook(userId, bookTitle) {
        const user = this.users.find(u => u.id === userId);
        const book = this.books.find(b => b.title === bookTitle);

        if (user && book) {
            return this.loansService.returnBook(user, book);
        }

        return false;
    }
}


const library = new Library();
library.addUser(new User(id='a11', name='Naia', email='naia@email.com'));
library.addBook(new Book(title='The Lord Of The Rings', author='J.R.R. Tolkien', copies=10));

console.log(library.loanBook('a11', 'The Lord Of The Rings'));  // true
console.log(library.loanBook('123', 'Not existing book'));  // false

console.log(library.returnBook('a11', 'The Lord Of The Rings'));  // true
console.log(library.returnBook('123', 'Not existing book'));  // false