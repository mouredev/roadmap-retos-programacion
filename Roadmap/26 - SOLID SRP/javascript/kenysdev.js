/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
___________________________________________________
#26 SOLID: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
---------------------------------------------------
* EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesit
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
// ________________________________________________________
// SIN APLICAR SRP
// ---------------
class Program {
    constructor() {
      this.customers = [];
      this.suppliers = [];
    }
  
    addCustomer(name) {
      this.customers.push(name);
    }
  
    removeCustomer(name) {
      this.customers = this.customers.filter((customer) => customer !== name);
    }
  
    addSupplier(name) {
      this.suppliers.push(name);
    }
  
    removeSupplier(name) {
      this.suppliers = this.suppliers.filter((supplier) => supplier !== name);
    }
  
    printData() {
      console.log("Clientes:", this.customers);
      console.log("Proveedores:", this.suppliers);
    }
  }

// ________________________________________________________
// APLICANDO SRP
// ---------------

class Customers {
    constructor() {
      this.customers = [];
    }
  
    add(name) {
      this.customers.push(name);
    }
  
    remove(name) {
      this.customers = this.customers.filter((customer) => customer !== name);
    }
  
    print() {
      console.log("Clientes:", this.customers);
    }
  }
  
  class Suppliers {
    constructor() {
      this.suppliers = [];
    }
  
    add(name) {
      this.suppliers.push(name);
    }
  
    remove(name) {
      this.suppliers = this.suppliers.filter((supplier) => supplier !== name);
    }
  
    print() {
      console.log("Proveedores:", this.suppliers);
    }
  }
  
  const customers = new Customers();
  const suppliers = new Suppliers();
  
  customers.add("Cliente A");
  customers.add("Cliente B");
  suppliers.add("Proveedor X");
  
  customers.print();
  suppliers.print();
  
  customers.remove("Cliente A");
  suppliers.remove("Proveedor X");
  
  customers.print();
  suppliers.print();
  

// ________________________________________________________
// DIFICULTAD EXTRA
// ---------------
// SIN APLICAR SRP
// ---------------
class Library {
    constructor() {
        this.books = {};
        this.users = {};
        this.borrowed = {};
    }

    addBook(id, title, author, stock) {
        if (this.books[id]) {
            this.books[id].stock += stock;
            this.books[id].available += stock;
            console.log("El libro ya existe, se actualizó el inventario.");
        } else {
            this.books[id] = { title, author, stock, available: stock };
            console.log(`Libro '${title}' agregado.`);
        }
    }

    addUser(id, name, email) {
        if (this.users[id]) {
            console.log("El usuario ya existe.");
        } else {
            this.users[id] = { name, email };
            console.log(`Usuario '${name}' agregado.`);
        }
    }

    lendBook(borrowId, userId, bookId) {
        if (!this.books[bookId]) return console.log("El libro no existe.");
        if (!this.users[userId]) return console.log("El usuario no existe.");
        if (this.books[bookId].available <= 0)
            return console.log("El libro no está disponible.");

        this.borrowed[borrowId] = { userId, bookId };
        this.books[bookId].available -= 1;
        console.log(`Libro '${bookId}' prestado.`);
    }

    returnBook(borrowId) {
        if (!this.borrowed[borrowId]) return console.log("No existe el préstamo.");

        const { bookId } = this.borrowed[borrowId];
        this.books[bookId].available += 1;
        delete this.borrowed[borrowId];
        console.log(`Libro '${bookId}' devuelto.`);
    }
}

// ________________________________________________________
// Aplicando SRP:
// ---------------

// Singleton
class LibraryData {
    constructor() {
        if (!LibraryData.instance) {
            this.books = {};
            this.users = {};
            this.borrowed = {};
            LibraryData.instance = this;
        }
        return LibraryData.instance;
    }
}

const data = new LibraryData();

class Books {
    add(id, title, author, stock) {
        if (data.books[id]) {
            data.books[id].stock += stock;
            data.books[id].available += stock;
            console.log("El libro ya existe, se actualizó el inventario.");
        } else {
            data.books[id] = { title, author, stock, available: stock };
            console.log(`Libro '${title}' agregado.`);
        }
    }

    print() {
        console.log("Libros:", data.books);
    }
}

class Users {
    add(id, name, email) {
        if (data.users[id]) {
            console.log("El usuario ya existe.");
        } else {
            data.users[id] = { name, email };
            console.log(`Usuario '${name}' agregado.`);
        }
    }

    print() {
        console.log("Usuarios:", data.users);
    }
}

class BorrowedBooks {
    lend(borrowId, userId, bookId) {
        if (!data.books[bookId]) return console.log("El libro no existe.");
        if (!data.users[userId]) return console.log("El usuario no existe.");
        if (data.books[bookId].available <= 0)
            return console.log("El libro no está disponible.");

        data.borrowed[borrowId] = { userId, bookId };
        data.books[bookId].available -= 1;
        console.log(`Libro '${bookId}' prestado.`);
    }

    returnBook(borrowId) {
        if (!data.borrowed[borrowId]) return console.log("No existe el préstamo.");

        const { bookId } = data.borrowed[borrowId];
        data.books[bookId].available += 1;
        delete data.borrowed[borrowId];
        console.log(`Libro '${bookId}' devuelto.`);
    }

    print() {
        console.log("Préstamos:", data.borrowed);
    }
}

// ---------------
const books = new Books();
const users = new Users();
const borrowed = new BorrowedBooks();
console.log("\nDIFICULTAD EXTRA\n")
books.add(1, "Libro A", "Autor A", 2);
books.add(2, "Libro B", "Autor B", 3);

users.add(101, "Usuario 1", "user1@example.com");
users.add(102, "Usuario 2", "user2@example.com");

borrowed.lend(201, 101, 1);
borrowed.lend(202, 102, 2);

books.print();
users.print();
borrowed.print();

borrowed.returnBook(201);
books.print();
borrowed.print();
