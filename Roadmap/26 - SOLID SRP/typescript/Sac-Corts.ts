// Invalid way
class User {
    name: string;
    email: string;

    constructor(name: string, email: string) {
        this.name = name;
        this.email = email;
    }

    getUserInfo(): { name: string; email: string } {
        return {
            name: this.name,
            email: this.email
        };
    }

    formatUserInfo(): string {
        return `Name: ${this.name}, Email: ${this.email}`;
    }
}

const user = new User('Isaac Morales', 'isaac@gmail.com');
console.log(user.formatUserInfo());

// Correct way
class UserInfo {
    name: string;
    email: string;

    constructor(name: string, email: string) {
        this.name = name;
        this.email = email;
    }

    getUserInfo(): { name: string; email: string } {
        return {
            name: this.name,
            email: this.email
        };
    }
}

class FormatUser {
    static format(user: UserInfo): string {
        return `Name: ${user.name}, Email: ${user.email}`;
    }
}

const newUser = new UserInfo('Isaac Cortés', 'isaac@gmail.com');
console.log(FormatUser.format(newUser));

// ** Extra Exercise ** //
interface Book {
    title: string;
    author: string;
    copies: number;
}

class BookManager {
    private books: Book[];

    constructor() {
        this.books = [];
    }

    addBook(title: string, author: string, copies: number): void {
        this.books.push({ title, author, copies });
    }

    findBook(title: string): Book | undefined {
        return this.books.find(book => book.title === title);
    }
}

interface UserDetails {
    name: string;
    id: number;
    email: string;
}

class UserManager {
    private users: UserDetails[];

    constructor() {
        this.users = [];
    }

    addUser(name: string, id: number, email: string): void {
        this.users.push({ name, id, email });
    }

    findUser(id: number): UserDetails | undefined {
        return this.users.find(user => user.id === id);
    }
}

class LoanManager {
    private bookManager: BookManager;
    private userManager: UserManager;
    private loans: { userId: number; bookTitle: string }[];

    constructor(bookManager: BookManager, userManager: UserManager) {
        this.bookManager = bookManager;
        this.userManager = userManager;    
        this.loans = [];
    }

    borrowBook(userId: number, bookTitle: string): void {
        const user = this.userManager.findUser(userId);
        const book = this.bookManager.findBook(bookTitle);

        if (user && book && book.copies > 0) {
            book.copies--;
            this.loans.push({ userId, bookTitle });
            console.log(`${user.name} borrowed "${book.title}"`);
        } else {
            console.log(`Book is unavailable or user not found`);
        }
    }

    returnBook(userId: number, bookTitle: string): void {
        const loanIndex = this.loans.findIndex(
            loan => loan.userId === userId && loan.bookTitle === bookTitle
        );
        const book = this.bookManager.findBook(bookTitle);

        if (loanIndex !== -1 && book) {
            book.copies++;
            this.loans.splice(loanIndex, 1);
            console.log(`"${book.title}" has been returned`);
        } else {
            console.log('Loan not found or book not available');
        }
    }
}

const bookManager = new BookManager();
const userManager = new UserManager();
const loanManager = new LoanManager(bookManager, userManager);

bookManager.addBook('The Great Gatsby', 'F. Scott Fitzgerald', 5);
userManager.addUser('Isaac', 1, 'isaac@gmail.com');

loanManager.borrowBook(1, 'The Great Gatsby');
loanManager.returnBook(1, 'The Great Gatsby');
