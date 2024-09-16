// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

"use strict";

/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA:
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
*/

const readline = require('readline');

class Book {
    constructor(title, author, copies) {
        this.title = title;
        this.author = author;
        this.copies = copies;
    }
}

class BookManager {
    constructor() {
        this.books = [];
    }

    addBook(rl, callback) {
        console.clear();
        rl.question('Ingrese el título del libro: ', (title) => {
            rl.question('Ingrese el autor del libro: ', (author) => {
                rl.question('Ingrese el número de copias: ', (copies) => {
                    this.books.push(new Book(title, author, parseInt(copies)));
                    console.log('Libro agregado exitosamente.');
                    callback();
                });
            });
        });
    }

    listBooks() {
        console.clear();
        if (this.books.length === 0) {
            console.log('No hay libros disponibles.');
            return;
        }
        this.books.forEach(book => {
            console.log(`Título: ${book.title}, Autor: ${book.author}, Copias: ${book.copies}`);
        });
    }
}

class User {
    constructor(name, id, email) {
        this.name = name;
        this.id = id;
        this.email = email;
    }
}

class UserManager {
    constructor() {
        this.users = [];
    }

    addUser(rl, callback) {
        console.clear();
        rl.question('Ingrese el nombre del usuario: ', (name) => {
            rl.question('Ingrese el ID del usuario: ', (id) => {
                rl.question('Ingrese el correo electrónico del usuario: ', (email) => {
                    this.users.push(new User(name, parseInt(id), email));
                    console.log('Usuario agregado exitosamente.');
                    callback();
                });
            });
        });
    }

    listUsers() {
        console.clear();
        if (this.users.length === 0) {
            console.log('No hay usuarios registrados.');
            return;
        }
        this.users.forEach(user => {
            console.log(`Nombre: ${user.name}, ID: ${user.id}, Correo: ${user.email}`);
        });
    }
}

class LoanManager {
    lendBook(rl, userManager, bookManager, callback) {
        console.clear();
        rl.question('Ingrese el ID del usuario: ', (userId) => {
            rl.question('Ingrese el título del libro a prestar: ', (bookTitle) => {
                // Lógica de préstamo
                console.log(`Libro '${bookTitle}' prestado al usuario ID ${userId}.`);
                callback();
            });
        });
    }

    returnBook(rl, userManager, bookManager, callback) {
        console.clear();
        rl.question('Ingrese el ID del usuario: ', (userId) => {
            rl.question('Ingrese el título del libro a devolver: ', (bookTitle) => {
                // Lógica de devolución
                console.log(`Libro '${bookTitle}' devuelto por el usuario ID ${userId}.`);
                callback();
            });
        });
    }
}

function displayMenu() {
    console.clear();
    console.log('******** Menú de la Biblioteca ********');
    console.log('[1] - Agregar un libro');
    console.log('[2] - Listar libros');
    console.log('[3] - Agregar un usuario');
    console.log('[4] - Listar usuarios');
    console.log('[5] - Prestar un libro');
    console.log('[6] - Devolver un libro');
    console.log('[7] - Salir');
    console.log('Seleccione una opción: ');
}

function main() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const bookManager = new BookManager();
    const userManager = new UserManager();
    const loanManager = new LoanManager();

    function menu() {
        displayMenu();
        rl.question('', (option) => {
            switch (parseInt(option)) {
                case 1:
                    bookManager.addBook(rl, menu);
                    break;
                case 2:
                    bookManager.listBooks();
                    pause(menu);
                    break;
                case 3:
                    userManager.addUser(rl, menu);
                    break;
                case 4:
                    userManager.listUsers();
                    pause(menu);
                    break;
                case 5:
                    loanManager.lendBook(rl, userManager, bookManager, menu);
                    break;
                case 6:
                    loanManager.returnBook(rl, userManager, bookManager, menu);
                    break;
                case 7:
                    console.log('Saliendo del sistema...');
                    rl.close();
                    break;
                default:
                    console.log('Opción no válida. Intente de nuevo.');
                    pause(menu);
            }
        });
    }

    function pause(callback) {
        rl.question('Presione Enter para continuar...', () => {
            callback();
        });
    }

    menu();
}

main();
