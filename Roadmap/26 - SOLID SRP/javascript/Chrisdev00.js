/*
* EJERCICIO:
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

// Ejemplo de Forma incorrecta 

class Order {
  constructor(items, taxRate){
    this.items = items;
    this.taxRate = taxRate;
  }

  calculateTotal() {
    let total = this.items.reduce((sum, item) => sum + item[1], 0);
    const discount = 5
    let tax = (total - discount) * this.taxRate
    return total - discount + tax;
  }

  generateInvoice(){
    const total = this.calculateTotal()
    let invoice = "Factura:\n";
    this.items.forEach(([item, price]) => {
      invoice += `${item}: $${price}\n`;
    });
    invoice += `Total (incluyendo impuestos): $${total.toFixed(2)}\n`;
    return invoice;
  }

  sendConfirmationEmail(email){
    const invoice = this.generateInvoice();
    console.log(`Enviando email a ${email} con la siguiente Factura:\n${invoice}`);

  }
}

const order1 = new Order([['item1', 10], ['item2', 20]], 0.1);
console.log(order1.generateInvoice());
order1.sendConfirmationEmail('example@example.com');


// Manera Correcta cumpliendo el Principio de Responsabilidad Única (SRP)

class Order {
  constructor(items){
    this.items = items;
  }

  getTotal() {
    return this.items.reduce((sum, item) => sum + item[1], 0);
  }
}

class TaxCalculator {
  constructor(taxRate, discount = 5) {
    this.taxRate = taxRate;
    this.discount = discount;
  }

  calculateTax(total) {
    return (total - this.discount) * this.taxRate;
  }

  calculateFinalTotal(total) {
    const tax = this.calculateTax(total);
    return total - this.discount + tax;
  }
}

class InvoiceGenerator {
  generateInvoice(order, finalTotal) {
    let invoice = "Factura:\n";
    order.items.forEach(([item, price]) => {
      invoice += `${item}: $${price}\n`;
    });
    invoice += `Total (incluyendo impuestos): $${finalTotal.toFixed(2)}\n`;
    return invoice;
  }
}

class EmailSender {
  sendConfirmationEmail(email, invoice) {
    console.log(`Enviando email a ${email} con la siguiente Factura:\n${invoice}`);
  }
}

// Uso del código
const order = new Order([['item1', 10], ['item2', 20]]);
const taxCalculator = new TaxCalculator(0.1);
const invoiceGenerator = new InvoiceGenerator();
const emailSender = new EmailSender();

const total = order.getTotal();
const finalTotal = taxCalculator.calculateFinalTotal(total);
const invoice = invoiceGenerator.generateInvoice(order, finalTotal);

console.log(invoice);
emailSender.sendConfirmationEmail('example@example.com', invoice);



/////////////-------------------------- EXTRA --------------------------- ////////////////////////////////


// Manera Incorrecta del ejercicio

class LibraryOne{

  constructor(){
    this.books = []
    this.users = []
    this.loans = []
  }

  addBook(title, author, copies){
    let book = {"title": title, "author": author, "copies": copies};
    this.books.push(book)
  }

  addUser(name, userId, email){
    let user = {"name": name, "userId": userId, "email": email};
    this.users.push(user)
  }

  borrowBook(userId, title){
    for (let book of this.books){
      if (book.title === title && book.copies > 0){
        book.copies -= 1;
        const loan = {"userId": userId, "title": title};
        this.loans.push(loan);
        return `El usuario '${userId}' se presto el libro '${title}'.`;
      }
    }
    return `Libro '${title}' no esta disponible.`
  }

  returnBook(userId, title){
    for (let loan of this.loans){
      if(loan.userId === userId && loan.title === title){
        this.loans = this.loans.filter(1 >= 1 !== loan);
        for (let book of this.books){
          if(book.title === title){
            book.copies += 1;
          }
        }
        return `Libro '${title}' retornado por el usuario '${userId}'.`;
      }
    }
    return `No hay registro de que el usuario '${userId}' se haya prestado el libro '${title}'.`;
  }
}

const library1 = new LibraryOne();

library1.addBook("Lord of the Rings", "JRR Tolkien", 4);
library1.addBook("Harry Potter", "JK Rowling", 2);

library1.addUser("Alice", "1", "alice@example.com");
library1.addUser("Matias", "2", "matias@example.com");

console.log(library1.borrowBook("1", "Lord of the Rings"));
console.log(library1.borrowBook("2", "Harry Potter"));
console.log(library1.borrowBook("1", "Lord of the Rings"));
console.log(library1.returnBook("2", "The Great Gatsby"));


// Manera Correcta cumpliendo el Principio de Responsabilidad Única (SRP)


class Library{
    constructor(){
      this.books = [];
      this.users = [];
    }
  
    addBook(book){
      this.books.push(book)
    }
  
    addUser(user){
      this.users.push(user);
    }
  
    findBook(title){
      return this.books.find(book => book.title === title) || null;
    }
  
    findUser(userId){
      return this.users.find(user => user.userId === userId) || null;
    }
  
    totalBooks(){
      return this.books.reduce((sum, book) => sum + book.copies, 0);
    }
  
    getLibraryInfo(){
      const totalBooks = this.totalBooks();
      const booksInfo = this.books.map(book => book.showInfo());
      return {totalBooks, booksInfo};
    }
  
}
  
class Book{
    constructor(title, author, copies){
      this.title = title;
      this.author = author;
      this.copies = copies;
    }
  
    showInfo(){
      return `'${this.title}' por '${this.author}', numero de copias '${this.copies}'`;
    }
}
  
class User{
    constructor(name, userId, email){
      this.name = name
      this.userId = userId
      this.email = email
      this.loans = []
    }
}
  
class LoanProcess{
    borrowBook(library, userId, title){
      let user = library.findUser(userId);
      let book = library.findBook(title);
      if(book && user){
        if(book.copies >0){
          user.loans.push(book)
          book.copies -= 1
          console.log(`Libro '${book.title}' prestado a '${user.name}'`)
        }else{
          console.log("Este libro no esta disponible para prestamo")
        }
      }else{
        console.log("Usuario o libro no encontrado")
      }
    }
  
    returnBook(library, userId, title){
      let user = library.findUser(userId);
      let book = library.findBook(title);
      if (book && user){
        const loanIndex = user.loans.indexOf(book);
        if(loanIndex !== -1){
          user.loans.splice(loanIndex, 1);
          book.copies += 1
          console.log(`Libro '${book.title}' devuelto por '${user.name}'.`)
        }else{
          console.log(`No hay registro de que el libro '${book.title}' haya sido prestado a '${user.name}'`)
        }
      }else{
        console.log("Usuario o libro no encontrado")
      }
    }
}
  
  
const library = new Library();
const book1 = new Book("Lord of the Rings", "JRR Tolkien", 4);
const book2 = new Book("1984", "George Orwell", 5);
const user = new User("Alice", "1", "alice@example.com");

library.addBook(book1);
library.addBook(book2);
library.addUser(user);

const loanProcessor = new LoanProcess();
loanProcessor.borrowBook(library, "1", "Lord of the Rings");
loanProcessor.returnBook(library, "1", "Lord of the Rings");

// Total de libros en la biblioteca
const { totalBooks, booksInfo } = library.getLibraryInfo();
console.log(`Total de libros en la biblioteca: ${totalBooks}`);
console.log("Información de la biblioteca:");
booksInfo.forEach(info => console.log(info));
