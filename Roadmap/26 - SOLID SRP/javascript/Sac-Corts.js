// Invalid way
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    getUserInfo() {
        return {
            name: this.name,
            email: this.email
        };
    }

    formatUserInfo() {
        return `Name: ${this.name}, Email: ${this.email}`;
    }
}

const user = new User('Isaac Morales', 'isaac@gmail.com');
console.log(user.formatUserInfo());

// Correct way
class UserInfo {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    getUserInfo() {
        return {
            name: this.name,
            email: this.email
        };
    }
}

class FormatUser {
    static format(user) {
        return `Name: ${user.name}, Email: ${user.email}`;
    }
}

const newUser = new UserInfo('Isaac Cortés', 'isaac@gmail.com');
console.log(FormatUser.format(newUser));

// Extra Exercise //
class BookManager {
    constructor() {
        this.books = [];
    }

    addBook(title, author, copies) {
        this.books.push({ title, author, copies });
    }

    findBook(title) {
        return this.books.find(book => book.title === title);
    }
}

class UserManager {
    constructor() {
        this.users = [];
    }

    addUser(name, id, email) {
        this.users.push({ name, id, email });
    }

    findUser(id) {
        return this.users.find(user => user.id === id); 
    }
}

class LoanManager {
    constructor(bookManager, userManager) {
        this.bookManager = bookManager;
        this.userManager = userManager;    
        this.loans = [];
    }

    borrowBook(userId, bookTitle) {
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

    returnBook(userId, bookTitle) {
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
