//#26 - Principio SOLID de Responsabilidad Única (Single Responsibility Principle, SRP)
//Bibliografy: The Web Development Glossary (Jens Oliver Meiert) (Z-Library)
//GPT
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


/*  Single Responsibility Principle
A computer programming principle that states that every module, class, or
function should have responsibility over a single part of the functionality
provided by the software, and that responsibility should be entirely
encapsulated by the module, class, or function. All its services should be
narrowly aligned with that responsibility.  */

//Not Following the Single Responsibility Principle (SRP)

let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #26.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #26. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #26'); 
});

class Library {
    constructor() {
        this.books = [];
        this.users = [];
        this.loans = [];
    }

    addBook(title, author, copies) {
        this.books.push({ title, author, copies });
    }

    registerUser(name, id, email) {
        this.users.push({ name, id, email });
    }

    loanBook(userId, bookTitle) {
        const user = this.users.find(u => u.id === userId);
        const book = this.books.find(b => b.title === bookTitle);

        if (user && book && book.copies > 0) {
            this.loans.push({ userId, bookTitle });
            book.copies--;
            log(`Book "${bookTitle}" loaned to ${user.name}`);
        } else {
            log("Loan failed: User or book not found, or no copies available.");
        }
    }
}


const library = new Library();
library.addBook("Learn Bash the Hard Way", "Ian Miell", 2);
library.addBook("MATLAB Notes for Professionals", "GoalKicker.com", 4);
library.registerUser("Royer Rabit", "006", "happyrabbit@proton.me");
library.loanBook("006", "MATLAB Notes for Professionals"); //Book "MATLAB Notes for Professionals" loaned to Royer Rabit


//Extra difiiculty Excercise
//Following the Single Responsibility Principle (SRP)

class Book {
    constructor(title, author, copies) {
        this.title = title;
        this.author = author;
        this.copies = copies;
    }
}

class User {
    constructor(name, id, email) {
        this.name = name;
        this.id = id;
        this.email = email;
    }
}

class BookManager {
    constructor() {
        this.books = [];
    }

    addBook(title, author, copies) {
        this.books.push(new Book(title, author, copies));
    }

    getBooks() {
        return this.books; 
    }

    findBook(title) {
        return this.books.find(b => b.title === title);
    }

    increaseCopies(bookTitle) {
        const book = this.findBook(bookTitle);
        if (book) {
            book.copies++;
        }
    }
}

function searchBooksByPartialTitle(books, searchTerm) {
    return books.filter(book => 
        book.title.toLowerCase().includes(searchTerm.toLowerCase())
    );
}

class UserManager {
    constructor() {
        this.users = [];
    }

    registerUser(name, id, email) {
        this.users.push(new User(name, id, email));
    }

    findUser(id) {
        return this.users.find(u => u.id === id);
    }
}

class LoanManager {
    constructor() {
        this.loans = [];
        this.nextLoanId = 1;
    }

    loanBook(user, book) {
        if (book.copies > 0) {
            const loanId = this.nextLoanId++;
            this.loans.push({loanId, userId: user.id, bookTitle: book.title });
            book.copies--;
            log(`Book "${book.title}" loaned to ${user.name} with Loan ID: ${loanId}`);
        } else {
            log("Loan failed: No copies available.");
        }
    }

    returnBook(loanId, bookManager) {
        const loanIndex = this.loans.findIndex(loan => loan.loanId === loanId);

        if (loanIndex !== -1) {
            const loan = this.loans[loanIndex];
            const book = bookManager.findBook(loan.bookTitle);
            if (book) {
                book.copies++;
            }

            // Remove the loan from the loans array
            this.loans.splice(loanIndex, 1);
            log(`Book "${loan.bookTitle}" returned with Loan ID: ${loanId}`);
        } else {
            log("Return failed: No loan record found for this Loan ID.");
        }
    }

    getLoansByPartialBookTitle(searchTerm, userId) {
        return this.loans.filter(loan => 
            loan.bookTitle.toLowerCase().includes(searchTerm.toLowerCase()) && loan.userId === userId
        );
    }
}


const bookManager = new BookManager();
const userManager = new UserManager();
const loanManager = new LoanManager();

bookManager.addBook("300 JavaScript Interview Mastery Questions Dive Deep into JavaScript Theory, Syntax, and APIs, and Interview with Confidence", "Middaugh, Jonathan", 3);
bookManager.addBook("Javascript Interview Questions and Answers", "Bandal, Pratik", 7);
bookManager.addBook("100 MOST ASKED JOB READY QUESTIONS ANSWERS IN THE TECH SPACE Here are the most asked questions in PYTHON, SQL, JAVASCRIPT...", "Aimee Mills", 2);
userManager.registerUser("Niko Zen", "008", "duendeintemporal@hotmail.com");

const searchTerm1 = "JavaScript";
const searchTerm2 = "Interview Questions";

const searchResults1 = searchBooksByPartialTitle(bookManager.getBooks(), searchTerm1);
const searchResults2 = searchBooksByPartialTitle(bookManager.getBooks(), searchTerm2);

log(searchResults1); 
/*
Book {title: '300 JavaScript Interview Mastery Questions Dive De…, Syntax, and APIs, and Interview with Confidence', author: 'Middaugh, Jonathan', copies: 3}
Book {title: 'Javascript Interview Questions and Answers', author: 'Bandal, Pratik', copies: 7} 
Book {title: '100 MOST ASKED JOB READY QUESTIONS ANSWERS IN THE …ost asked questions in PYTHON, SQL, JAVASCRIPT...', author: 'Aimee Mills', copies: 2}
  */
log(searchResults2); 
/* {author:"Bandal, Pratik", copies:7, title:"Javascript Interview Questions and Answers"} */

const user = userManager.findUser("008");
const bookTitle = searchResults1[2]?.title; 
const book = bookManager.findBook(bookTitle); 

if (book) {
    loanManager.loanBook(user, book); // Book "100 MOST ASKED JOB READY QUESTIONS ANSWERS IN THE TECH SPACE Here are the most asked questions in PYTHON, SQL, JAVASCRIPT..." loaned to Niko Zen with Loan ID: 1
    const loans = loanManager.getLoansByPartialBookTitle(book.title, user.id);
    loanManager.returnBook(loans[0].loanId, bookManager); // Book "100 MOST ASKED JOB READY QUESTIONS ANSWERS IN THE TECH SPACE Here are the most asked questions in PYTHON, SQL, JAVASCRIPT..." returned with Loan ID: 1
} else {
    log("Book not found for loan.");
}

