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

interface IUser {
    name: string;
    id: number;
    email: string;
}

// ========== IMPLEMENTACIÓN INCORRECTA (Violando SRP) ==========

/*
 * Esta implementación viola el SRP porque la clase User tiene múltiples responsabilidades en la gestión de los usuarios.
 */

class UserWrong implements IUser {
    constructor(
        public name: string,
        public id: number,
        public email: string,
    ) {}

    save() {
        console.log(`User ${this.name} has been stored`);
    }

    sendEmail() {
        console.log(`Email has been sent to ${this.email}`);
    }
}

console.log(`IMPLEMENTACIÓN INCORRECTA (Violando SRP)`);

const userWrong = new UserWrong('Juan Perez', 1, 'jperez@gmail.com');
userWrong.save();
userWrong.sendEmail();

// ========== IMPLEMENTACIÓN CORRECTA (Siguiendo SRP) ==========

/*
 * Esta implementación respeta el SRP, ya que cada clase tiene una única razón para cambiar:
 * - User: solamente cambia si se modifica la estructura del usuario.
 * - UserRepository: solamente cambia si se modifica la forma de persistir datos.
 * - EmailService: solamente cambia si se modifica la forma de enviar emails.
 */

class User implements IUser {
    constructor(
        public name: string,
        public id: number,
        public email: string,
    ) {}
}

class UserRightRepository {
    save(user: IUser) {
        console.log(`User ${user.name} has been stored`);
    }
}

class EmailRightService {
    sendEmail(email: string) {
        console.log(`Email has been sent to ${email}`);
    }
}

console.log(`\nIMPLEMENTACIÓN CORRECTA (Siguiendo SRP)`);

const user = new User('Juan Perez', 1, 'jperez@gmail.com');
const userRightRepository = new UserRightRepository();
const emailRightService = new EmailRightService();

userRightRepository.save(user);
emailRightService.sendEmail(user.email);

/* EXTRAS */
interface IBook {
    title: string;
    author: string;
    copies: number;
}

interface IUser {
    name: string;
    id: number;
    email: string;
}

interface ILoan {
    loanId: number;
    userId: number;
    bookTitle: string;
}

// ========== IMPLEMENTACIÓN INCORRECTA (Violando SRP) ==========

/*
 * Esta implementación viola el SRP porque la clase Library tiene múltiples responsabilidades, por lo que tiene varias razones para cambiar:
 * - Gestión de libros.
 * - Gestión de usuarios.
 * - Gestión de préstamos.
 * - Envío de notificaciones.
 */

class LibraryWrong {
    constructor(
        private books: IBook[] = [],
        private users: IUser[] = [],
        private loans: ILoan[] = [],
    ) {}

    addBook(title: string, author: string, copies: number) {
        this.books.push({ title: title, author: author, copies: copies });
    }

    addUser(name: string, id: number, email: string): void {
        this.users.push({ name: name, id: id, email: email });
    }

    loanBook(userId: number, bookTitle: string): void {
        const user = this.users.find((u: IUser) => u.id === userId);
        const book = this.books.find((b: IBook) => b.title === bookTitle);

        if (!user) throw new Error('User not found');
        if (!book) throw new Error('Book not found');
        if (book.copies <= 0) throw new Error(`No copies available for "${book.title}"`);

        const loanId = this.loans.length + 1;
        this.loans.push({ loanId: loanId, userId: user.id, bookTitle: bookTitle });
        book.copies--;
        this.sendEmail(user.email, `Book "${book.title}" loaned to ${user.name}`);
    }

    sendEmail(email: string, message: string): void {
        console.log(`Email has been sent to ${email}, message: ${message}`);
    }

    returnBook(userId: number, bookTitle: string): void {
        const user = this.users.find((u: IUser) => u.id === userId);
        const book = this.books.find((b: IBook) => b.title === bookTitle);

        if (!user) throw new Error('User not found');
        if (!book) throw new Error('Book not found');

        const loan = this.loans.find((l: ILoan) => l.userId === user.id && l.bookTitle === book.title);

        if (!loan) throw new Error('Loan not found');

        this.loans = this.loans.filter((l: ILoan) => l !== loan);
        book.copies++;
        console.log(`Book "${book.title}" returned by ${user.name}`);
    }
}

console.log(`\nIMPLEMENTACIÓN INCORRECTA - EXTRA (Violando SRP)`);

const libraryWrong = new LibraryWrong();

libraryWrong.addBook('El hombre mediocre', 'Jose Ingenieros', 5);
libraryWrong.addBook('Matar a un ruiseñor', 'Harper Lee', 2);
libraryWrong.addUser('Juan Pérez', 1, 'juan@email.com');
libraryWrong.addUser('John Doe', 2, 'jdoe@email.com');
libraryWrong.loanBook(1, 'El hombre mediocre');
libraryWrong.returnBook(1, 'El hombre mediocre');

// ========== IMPLEMENTACIÓN CORRECTA (Siguiendo SRP) ==========

/*
 * Esta implementación respeta el SRP, ya que cada clase tiene una única razón para cambiar.
 * De esta forma se reduce el acoplamiento y permite que los cambios en una parte del sistema no afecten a las demás:
 * - Entities: representan el modelo del dominio y sus reglas internas.
 *   Cambian si se modifican las reglas propias del dominio (por ejemplo, cómo se gestionan las copias de un libro).
 *
 * - Repositories: se encargan de la persistencia de datos.
 *   Cambian si se modifica la forma de almacenamiento (memoria, base de datos, API, etc.).
 *
 * - Services: contienen la lógica de negocio y los casos de uso.
 *   Cambian si se modifican las reglas del negocio (por ejemplo, cómo se realiza un préstamo).
 *
 * - EmailService: maneja el envío de notificaciones.
 *   Cambia si se modifica la forma de enviar emails o el proveedor utilizado.
 *
 * - Library: actúa como orquestador del sistema.
 *   Cambia si se modifica el flujo de la aplicación o la coordinación entre servicios.
 */

interface IBookRepository {
    save(book: IBook): Book;
    findByTitle(title: string): Book | undefined;
}

interface IBookService {
    save(title: string, author: string, copies: number): Book;
    findByTitle(title: string): Book | undefined;
}

interface IUserRepository {
    save(user: IUser): User;
    findById(userId: number): User | undefined;
}

interface IUserService {
    save(name: string, id: number, email: string): User;
    findById(userId: number): User | undefined;
}

interface ILoanRepository {
    save(loan: Loan): void;
    find(userId: number, bookTitle: string): Loan | undefined;
    delete(loan: Loan): void;
    getNewId(): number;
}

interface ILoanService {
    loanBook(user: User, book: Book): Loan;
    returnBook(user: User, book: Book): void;
}

interface IEmailService {
    sendEmail(email: string, message: string): void;
}

class Book implements IBook {
    constructor(
        public title: string,
        public author: string,
        public copies: number,
    ) {}

    decreaseCopies(): void {
        if (this.copies <= 0) throw new Error('No copies available');
        this.copies--;
    }

    increaseCopies(): void {
        this.copies++;
    }
}

class BookRepository implements IBookRepository {
    private books: Book[] = [];

    save(book: IBook): Book {
        const newBook = new Book(book.title, book.author, book.copies);
        this.books.push(newBook);
        return newBook;
    }

    findByTitle(title: string): Book | undefined {
        return this.books.find((b: Book) => b.title === title);
    }
}

class BookService implements IBookService {
    constructor(private bookRepository: IBookRepository) {}

    save(title: string, author: string, copies: number): Book {
        return this.bookRepository.save({ title, author, copies });
    }

    findByTitle(title: string): Book | undefined {
        return this.bookRepository.findByTitle(title);
    }
}

class UserRepository implements IUserRepository {
    private users: User[] = [];

    save(user: IUser): User {
        const newUser = new User(user.name, user.id, user.email);
        this.users.push(newUser);
        return newUser;
    }

    findById(id: number): User | undefined {
        return this.users.find((u: User) => u.id === id);
    }
}

class UserService implements IUserService {
    constructor(private userRepository: IUserRepository) {}

    save(name: string, id: number, email: string): User {
        return this.userRepository.save({ name, id, email });
    }

    findById(id: number): User | undefined {
        return this.userRepository.findById(id);
    }
}

class Loan implements ILoan {
    constructor(
        public loanId: number,
        public userId: number,
        public bookTitle: string,
    ) {}
}

class LoanRepository implements ILoanRepository {
    private loans: Loan[] = [];
    private currentId = 0;

    save(loan: Loan): void {
        this.loans.push(loan);
    }

    find(userId: number, bookTitle: string): Loan | undefined {
        return this.loans.find((l: Loan) => l.userId === userId && l.bookTitle === bookTitle);
    }

    delete(loan: Loan): void {
        this.loans = this.loans.filter((l: Loan) => l !== loan);
    }

    getNewId(): number {
        this.currentId++;
        return this.currentId;
    }
}

class LoanService implements ILoanService {
    constructor(private loanRepository: ILoanRepository) {}

    loanBook(user: User, book: Book): Loan {
        book.decreaseCopies();

        const newLoan = new Loan(this.loanRepository.getNewId(), user.id, book.title);

        this.loanRepository.save(newLoan);

        return newLoan;
    }

    returnBook(user: User, book: Book): void {
        const loan = this.loanRepository.find(user.id, book.title);

        if (!loan) throw new Error('Loan not found');

        this.loanRepository.delete(loan);
        book.increaseCopies();
    }
}

class EmailService implements IEmailService {
    sendEmail(email: string, message: string): void {
        return;
    }
}

class Library {
    constructor(
        private bookService: IBookService,
        private userService: IUserService,
        private loanService: ILoanService,
        private emailService: IEmailService,
    ) {}

    loanBook(userId: number, bookTitle: string): void {
        const book = this.bookService.findByTitle(bookTitle);
        const user = this.userService.findById(userId);

        if (!book) throw new Error('Book not found');
        if (!user) throw new Error('User not found');

        this.loanService.loanBook(user, book);
        console.log(`Book "${book.title}" loaned to ${user.name}`);

        this.emailService.sendEmail(user.email, `Book "${book.title}" loaned to ${user.name}`);
        console.log(`Email has been sent to ${user.email}`);
    }

    returnBook(userId: number, bookTitle: string): void {
        const book = this.bookService.findByTitle(bookTitle);
        const user = this.userService.findById(userId);

        if (!book) throw new Error('Book not found');
        if (!user) throw new Error('User not found');

        this.loanService.returnBook(user, book);
        console.log(`Book "${book.title}" returned by ${user.name}`);

        this.emailService.sendEmail(user.email, `Book "${book.title}" returned by ${user.name}`);
        console.log(`Email has been sent to ${user.email}`);
    }
}

console.log(`\nIMPLEMENTACIÓN CORRECTA - EXTRA (Siguiendo SRP)`);

const bookRepository = new BookRepository();
const userRepository = new UserRepository();
const loanRepository = new LoanRepository();

const bookService = new BookService(bookRepository);
const userService = new UserService(userRepository);
const loanService = new LoanService(loanRepository);
const emailService = new EmailService();

const library = new Library(bookService, userService, loanService, emailService);

bookService.save('El hombre mediocre', 'Jose Ingenieros', 5);
bookService.save('Matar a un ruiseñor', 'Harper Lee', 2);

const user1 = userService.save('Juan Pérez', 1, 'juan@email.com');
const user2 = userService.save('John Doe', 2, 'jdoe@email.com');

library.loanBook(user1.id, 'El hombre mediocre');
library.returnBook(user1.id, 'El hombre mediocre');
