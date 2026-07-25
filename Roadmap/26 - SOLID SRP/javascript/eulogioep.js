/**
 * PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
 * 
 * El Principio de Responsabilidad Única establece que:
 * "Una clase debe tener una única razón para cambiar"
 * 
 * Este principio nos ayuda a:
 * - Crear código más mantenible
 * - Facilitar las pruebas unitarias
 * - Reducir el acoplamiento
 * - Mejorar la cohesión del código
 * - Facilitar la reutilización
 */

// ========== IMPLEMENTACIÓN INCORRECTA (Violando SRP) ==========

/**
 * Esta implementación viola el SRP porque la clase Library maneja múltiples responsabilidades:
 * 1. Gestión de libros
 * 2. Gestión de usuarios
 * 3. Gestión de préstamos
 */
class Library {
    constructor() {
        this.books = [];
        this.users = [];
        this.loans = [];
    }

    // Gestión de libros
    addBook(title, author, copies) {
        const book = new Book(title, author, copies);
        this.books.push(book);
    }

    removeBook(bookId) {
        this.books = this.books.filter(book => book.id !== bookId);
    }

    // Gestión de usuarios
    registerUser(name, id, email) {
        const user = new User(name, id, email);
        this.users.push(user);
    }

    removeUser(userId) {
        this.users = this.users.filter(user => user.id !== userId);
    }

    // Gestión de préstamos
    loanBook(userId, bookId) {
        const book = this.books.find(b => b.id === bookId);
        const user = this.users.find(u => u.id === userId);

        if (!book || !user) {
            throw new Error("Libro o usuario no encontrado");
        }

        if (book.availableCopies <= 0) {
            throw new Error("No hay copias disponibles");
        }

        book.availableCopies--;
        this.loans.push(new Loan(userId, bookId, new Date()));
    }

    returnBook(userId, bookId) {
        const loan = this.loans.find(
            l => l.userId === userId && l.bookId === bookId
        );
        
        if (!loan) {
            throw new Error("Préstamo no encontrado");
        }

        const book = this.books.find(b => b.id === bookId);
        if (book) {
            book.availableCopies++;
        }

        this.loans = this.loans.filter(l => l !== loan);
    }
}

// ========== IMPLEMENTACIÓN CORRECTA (Siguiendo SRP) ==========

/**
 * BookManager: Responsable únicamente de la gestión de libros
 */
class BookManager {
    constructor() {
        this.books = [];
    }

    addBook(title, author, copies) {
        const book = new Book(title, author, copies);
        this.books.push(book);
        return book;
    }

    removeBook(bookId) {
        this.books = this.books.filter(book => book.id !== bookId);
    }

    findBook(bookId) {
        return this.books.find(book => book.id === bookId);
    }

    updateBookCopies(bookId, change) {
        const book = this.findBook(bookId);
        if (book) {
            book.availableCopies += change;
        }
    }

    getAllBooks() {
        return [...this.books];
    }
}

/**
 * UserManager: Responsable únicamente de la gestión de usuarios
 */
class UserManager {
    constructor() {
        this.users = [];
    }

    registerUser(name, id, email) {
        const user = new User(name, id, email);
        this.users.push(user);
        return user;
    }

    removeUser(userId) {
        this.users = this.users.filter(user => user.id !== userId);
    }

    findUser(userId) {
        return this.users.find(user => user.id === userId);
    }

    getAllUsers() {
        return [...this.users];
    }
}

/**
 * LoanManager: Responsable únicamente de la gestión de préstamos
 */
class LoanManager {
    constructor(bookManager, userManager) {
        this.loans = [];
        this.bookManager = bookManager;
        this.userManager = userManager;
    }

    loanBook(userId, bookId) {
        const book = this.bookManager.findBook(bookId);
        const user = this.userManager.findUser(userId);

        if (!book || !user) {
            throw new Error("Libro o usuario no encontrado");
        }

        if (book.availableCopies <= 0) {
            throw new Error("No hay copias disponibles");
        }

        this.bookManager.updateBookCopies(bookId, -1);
        const loan = new Loan(userId, bookId, new Date());
        this.loans.push(loan);
        return loan;
    }

    returnBook(userId, bookId) {
        const loan = this.findLoan(userId, bookId);
        
        if (!loan) {
            throw new Error("Préstamo no encontrado");
        }

        this.bookManager.updateBookCopies(bookId, 1);
        this.removeLoan(userId, bookId);
    }

    findLoan(userId, bookId) {
        return this.loans.find(
            loan => loan.userId === userId && loan.bookId === bookId
        );
    }

    removeLoan(userId, bookId) {
        this.loans = this.loans.filter(
            loan => !(loan.userId === userId && loan.bookId === bookId)
        );
    }

    getAllLoans() {
        return [...this.loans];
    }
}

// Clases de modelo
class Book {
    constructor(title, author, availableCopies) {
        this.id = Math.random().toString(36).substr(2, 9);
        this.title = title;
        this.author = author;
        this.availableCopies = availableCopies;
    }
}

class User {
    constructor(name, id, email) {
        this.name = name;
        this.id = id;
        this.email = email;
    }
}

class Loan {
    constructor(userId, bookId, loanDate) {
        this.userId = userId;
        this.bookId = bookId;
        this.loanDate = loanDate;
    }
}

// Ejemplo de uso del sistema
// Creación de los managers
const bookManager = new BookManager();
const userManager = new UserManager();
const loanManager = new LoanManager(bookManager, userManager);

// Ejemplo de uso
try {
    // Agregar un libro
    const book = bookManager.addBook("El Quijote", "Miguel de Cervantes", 5);
    console.log("Libro agregado:", book);

    // Registrar un usuario
    const user = userManager.registerUser("Juan Pérez", "USER001", "juan@email.com");
    console.log("Usuario registrado:", user);

    // Realizar un préstamo
    const loan = loanManager.loanBook(user.id, book.id);
    console.log("Préstamo realizado:", loan);

    // Devolver el libro
    loanManager.returnBook(user.id, book.id);
    console.log("Libro devuelto exitosamente");

    // Verificar el estado del libro
    const updatedBook = bookManager.findBook(book.id);
    console.log("Estado actual del libro:", updatedBook);
} catch (error) {
    console.error("Error:", error.message);
}