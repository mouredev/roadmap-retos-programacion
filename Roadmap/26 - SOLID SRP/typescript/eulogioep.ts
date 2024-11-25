/**
 * PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
 * 
 * El Principio de Responsabilidad Única es el primer principio de SOLID y establece que:
 * "Una clase debe tener una única razón para cambiar"
 * 
 * Esto significa que una clase debe tener una sola responsabilidad o tarea principal.
 * Los beneficios de aplicar SRP incluyen:
 * - Código más mantenible y fácil de entender
 * - Mejor testabilidad
 * - Menor acoplamiento
 * - Facilita la reutilización de código
 */

// ========== IMPLEMENTACIÓN INCORRECTA (Violando SRP) ==========

/**
 * Esta implementación viola el SRP porque la clase Library tiene múltiples responsabilidades:
 * 1. Gestionar libros
 * 2. Gestionar usuarios
 * 3. Gestionar préstamos
 */
class Library {
    private books: Book[] = [];
    private users: User[] = [];
    private loans: Loan[] = [];

    // Gestión de libros
    public addBook(title: string, author: string, copies: number): void {
        const book = new Book(title, author, copies);
        this.books.push(book);
    }

    public removeBook(bookId: string): void {
        this.books = this.books.filter(book => book.id !== bookId);
    }

    // Gestión de usuarios
    public registerUser(name: string, id: string, email: string): void {
        const user = new User(name, id, email);
        this.users.push(user);
    }

    public removeUser(userId: string): void {
        this.users = this.users.filter(user => user.id !== userId);
    }

    // Gestión de préstamos
    public loanBook(userId: string, bookId: string): void {
        const book = this.books.find(b => b.id === bookId);
        const user = this.users.find(u => u.id === userId);

        if (!book || !user) throw new Error("Libro o usuario no encontrado");
        if (book.availableCopies <= 0) throw new Error("No hay copias disponibles");

        book.availableCopies--;
        this.loans.push(new Loan(user.id, book.id, new Date()));
    }

    public returnBook(userId: string, bookId: string): void {
        const loan = this.loans.find(l => l.userId === userId && l.bookId === bookId);
        if (!loan) throw new Error("Préstamo no encontrado");

        const book = this.books.find(b => b.id === bookId);
        if (book) book.availableCopies++;

        this.loans = this.loans.filter(l => l !== loan);
    }
}

// ========== IMPLEMENTACIÓN CORRECTA (Siguiendo SRP) ==========

/**
 * BookManager: Responsable únicamente de la gestión de libros
 */
class BookManager {
    private books: Book[] = [];

    public addBook(title: string, author: string, copies: number): void {
        const book = new Book(title, author, copies);
        this.books.push(book);
    }

    public removeBook(bookId: string): void {
        this.books = this.books.filter(book => book.id !== bookId);
    }

    public getBook(bookId: string): Book | undefined {
        return this.books.find(book => book.id === bookId);
    }

    public updateBookCopies(bookId: string, change: number): void {
        const book = this.getBook(bookId);
        if (book) {
            book.availableCopies += change;
        }
    }
}

/**
 * UserManager: Responsable únicamente de la gestión de usuarios
 */
class UserManager {
    private users: User[] = [];

    public registerUser(name: string, id: string, email: string): void {
        const user = new User(name, id, email);
        this.users.push(user);
    }

    public removeUser(userId: string): void {
        this.users = this.users.filter(user => user.id !== userId);
    }

    public getUser(userId: string): User | undefined {
        return this.users.find(user => user.id === userId);
    }
}

/**
 * LoanManager: Responsable únicamente de la gestión de préstamos
 */
class LoanManager {
    private loans: Loan[] = [];

    constructor(
        private bookManager: BookManager,
        private userManager: UserManager
    ) {}

    public loanBook(userId: string, bookId: string): void {
        const book = this.bookManager.getBook(bookId);
        const user = this.userManager.getUser(userId);

        if (!book || !user) throw new Error("Libro o usuario no encontrado");
        if (book.availableCopies <= 0) throw new Error("No hay copias disponibles");

        this.bookManager.updateBookCopies(bookId, -1);
        this.loans.push(new Loan(user.id, book.id, new Date()));
    }

    public returnBook(userId: string, bookId: string): void {
        const loan = this.loans.find(l => l.userId === userId && l.bookId === bookId);
        if (!loan) throw new Error("Préstamo no encontrado");

        this.bookManager.updateBookCopies(bookId, 1);
        this.loans = this.loans.filter(l => l !== loan);
    }
}

// Clases de modelo
class Book {
    public id: string;
    constructor(
        public title: string,
        public author: string,
        public availableCopies: number
    ) {
        this.id = Math.random().toString(36).substr(2, 9);
    }
}

class User {
    constructor(
        public name: string,
        public id: string,
        public email: string
    ) {}
}

class Loan {
    constructor(
        public userId: string,
        public bookId: string,
        public loanDate: Date
    ) {}
}

// Ejemplo de uso del sistema refactorizado
const bookManager = new BookManager();
const userManager = new UserManager();
const loanManager = new LoanManager(bookManager, userManager);

// Registrar un libro
bookManager.addBook("El Quijote", "Miguel de Cervantes", 5);

// Registrar un usuario
userManager.registerUser("Juan Pérez", "USER001", "juan@email.com");

// Realizar un préstamo
loanManager.loanBook("USER001", "BOOK001");