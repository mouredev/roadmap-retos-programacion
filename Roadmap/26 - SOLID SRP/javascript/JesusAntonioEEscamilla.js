/** #26 - JavaScript -> Jesus Antonio Escamilla */

/**
 * Los principios SOLID son un conjunto de cinco principios de diseño orientados a objetos que buscan hacer
    el software más comprensible, flexible y mantenible.
 * Principio de Responsabilidad Única (Single Responsibility Principle - SRP)
 * Una clase debe tener una, y solo una, razón para cambiar. En otras palabras, una clase debe tener una 
    única responsabilidad o propósito.
 */

//---EJERCIÓ---
// INCORRECTA
class User_Incorrecto{
    constructor(nombre, email){
        this.nombre = nombre,
        this.email = email
    };

    getUserData(){
        return{
            nombre: this.nombre,
            email: this.email
        };
    }

    saveToDatabase(){
        console.log(`Guardando el usuario ${this.nombre} en la base de datos`);
    }
}

// Uso del ejemplo Incorrecto
const user1 = new User_Incorrecto('Jesus', 'jesus_20@gmail.com');
console.log(user1.getUserData());
user1.saveToDatabase();

// CORRECTO
class User_Correcto{
    constructor(nombre, email){
        this.nombre = nombre;
        this.email = email;
    }

    getUserData(){
        return{
            nombre: this.nombre,
            email: this.email
        };
    }
}

class UserRepository{
    saveToDatabase(user){
        console.log(`Guardando el usuario ${user.nombre} en la base de datos`);
    }
}

// Uso de Ejemplo Correcto
const user = new User_Correcto('Antonio', 'antonio_25@hotmail.com');
console.log(user.getUserData());

const userRepository = new UserRepository();
userRepository.saveToDatabase(user);



/**-----DIFICULTAD EXTRA-----*/

//La Clase no cumple SRP de los principios SOLID de forma Incorrecta
class Library {
    constructor(){
        this.books = [];
        this.users = [];
        this.loans = [];
    }

    // Registro de Libro
    addBooks(title, author, copies){
        const book = {title, author, copies};
        this.books.push(book);
    }

    // Registro de Usuario
    addUsers(name, id_user, email){
        const user = {name, id_user, email};
        this.users.push(user);
    }

    // Registro de Préstamo de Libro
    loanBock(userId, bookTitle){
        const user = this.users.find(user => user.id_user === userId);
        const book = this.books.find(book => book.title === bookTitle);

        if(user && book && book.copies > 0){
            book.copies--;
            this.loans.push({userId, bookTitle, data: new Date()});
            console.log(`El libro "${bookTitle}" ha sido prestado a ${user.name}`);
        } else{
            console.log('No se proceso el préstamo');
        }
    }

    // Devolver el Libro
    returnBook(userId, bookTitle){
        const loanIndex = this.loans.findIndex(
            loan => loan.userId === userId && loan.bookTitle === bookTitle
        );

        if (loanIndex !== -1) {
            const book = this.books.find(book => book.title === bookTitle);
            book.copies++;
            this.loans.splice(loanIndex, 1);
            console.log(`El libro "${bookTitle}" ha sido devuelto`);
        } else {
            console.log('No se puede procesar la devolución');
        }
    }
}


// Uso de SRP de SOLID de forma Incorrecta
const library = new Library();
library.addBooks('Hábitos Atómicos', 'James Clear', 3);
library.addUsers('Jesus', '123', 'jesus@ejemplo.com');
library.loanBock('123', 'Hábitos Atómicos');
library.returnBook('123', 'Hábitos Atómicos');



// Agora con el Uso de SRP con los principios de SOLID de forma Correcta
// Gestión de Libros
class BookManager{
    constructor(){
        this.books = [];
    }

    // Registrar el Libro
    addBook(title, author, copies){
        const book = {title, author, copies};
        this.books.push(book);
        console.log(`El Libro "${title}" fue creado`);
    }

    // Obtener el Titulo del Libro
    getBook(title){
        return this.books.find(book => book.title === title);
    }
}

// Gestión de Usuarios
class UserManager{
    constructor(){
        this.users = [];
    }

    // Registrar Usuario
    addUser(name, id_user, email){
        const user = {name, id_user, email};
        this.users.push(user);
        console.log(`El Usuario "${name}" fue creado`);
    }

    // Obtener el Id del Usuario
    getUser(Id_user){
        return this.users.find(user => user.id_user === Id_user);
    }
}

// Gestión de Préstamo de Libro
class LoanManager{
    constructor(userManager,bookManager){
        this.loans = [];
        this.userManager = userManager;
        this.bookManager = bookManager;
    }

    // Registrar el Préstamo del Libro
    addLoan(userId, bookTitle){
        const book = this.bookManager.getBook(bookTitle);
        const user = this.userManager.getUser(userId);

        if (user && book && book.copies > 0) {
            book.copies--;
            this.loans.push({ userId, bookTitle, data: new Date() });
            console.log(`El libro "${bookTitle}" ha sido prestado a ${user.name}`);
        } else {
            console.log('No se proceso el préstamo');
        }
    }

    // Devuelve el Préstamo del Libro
    returnBook(userId, bookTitle){
        const loanIndex = this.loans.findIndex(
            loan => loan.userId === userId && loan.bookTitle === bookTitle
        );

        if (loanIndex !== -1) {
            const book = this.bookManager.getBook(bookTitle);
            book.copies++;
            this.loans.splice(loanIndex, 1);
            console.log(`El libro "${bookTitle}" ha sido devuelto`);
        } else {
            console.log('No se puede procesar la devolución');
        }
    }
}


// Uso de SRP de SOLID de forma Correcta
const bookManager = new BookManager();
const userManager = new UserManager();
const loanManager = new LoanManager(userManager, bookManager);

bookManager.addBook('Git & GitHub desde Cero', 'Brais Moure', 1);
bookManager.addBook('La teoría del todo', 'Stephen W. Hawking', 1);

userManager.addUser('Fatima', '01', 'faty@ejemplo.com');
userManager.addUser('Antonio', '02', 'toño@ejemplo.com');

loanManager.addLoan('02', 'Git & GitHub desde Cero');
loanManager.addLoan('01', 'La teoría del todo');
loanManager.returnBook('02', 'Git & GitHub desde Cero');
loanManager.returnBook('01', 'La teoría del todo');

/**-----DIFICULTAD EXTRA-----*/