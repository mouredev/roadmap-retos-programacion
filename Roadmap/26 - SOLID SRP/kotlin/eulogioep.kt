/*
 * Principio de Responsabilidad Única (SRP)
 * 
 * El Principio de Responsabilidad Única es el primer principio de SOLID y establece que una clase
 * debe tener una, y solo una, razón para cambiar. En otras palabras, una clase debe tener una
 * única responsabilidad bien definida.
 *
 * Este principio promueve la modularidad, facilita el mantenimiento y mejora la legibilidad del código.
 * Cuando una clase tiene múltiples responsabilidades, se vuelve más difícil de entender, modificar y probar.
 */

// Definiciones de datos comunes
data class Book(val title: String, val author: String, var availableCopies: Int)
data class User(val name: String, val id: String, val email: String)
data class Loan(val user: User, val book: Book)

// Versión que no cumple con SRP
class LibraryWithoutSRP {
    private val books = mutableListOf<Book>()
    private val users = mutableListOf<User>()
    private val loans = mutableListOf<Loan>()

    fun addBook(title: String, author: String, copies: Int) {
        books.add(Book(title, author, copies))
    }

    fun registerUser(name: String, id: String, email: String) {
        users.add(User(name, id, email))
    }

    fun loanBook(userId: String, bookTitle: String) {
        val user = users.find { it.id == userId }
        val book = books.find { it.title == bookTitle }
        if (user != null && book != null && book.availableCopies > 0) {
            loans.add(Loan(user, book))
            book.availableCopies--
        }
    }

    fun returnBook(userId: String, bookTitle: String) {
        val loan = loans.find { it.user.id == userId && it.book.title == bookTitle }
        if (loan != null) {
            loans.remove(loan)
            loan.book.availableCopies++
        }
    }
}

// Versión refactorizada que cumple con SRP
class BookManager {
    private val books = mutableListOf<Book>()

    fun addBook(title: String, author: String, copies: Int) {
        books.add(Book(title, author, copies))
    }

    fun findBook(title: String): Book? = books.find { it.title == title }
}

class UserManager {
    private val users = mutableListOf<User>()

    fun registerUser(name: String, id: String, email: String) {
        users.add(User(name, id, email))
    }

    fun findUser(id: String): User? = users.find { it.id == id }
}

class LoanManager {
    private val loans = mutableListOf<Loan>()

    fun loanBook(user: User, book: Book) {
        if (book.availableCopies > 0) {
            loans.add(Loan(user, book))
            book.availableCopies--
        }
    }

    fun returnBook(user: User, book: Book) {
        val loan = loans.find { it.user == user && it.book == book }
        if (loan != null) {
            loans.remove(loan)
            book.availableCopies++
        }
    }
}

class Library(
    private val bookManager: BookManager,
    private val userManager: UserManager,
    private val loanManager: LoanManager
) {
    fun addBook(title: String, author: String, copies: Int) {
        bookManager.addBook(title, author, copies)
    }

    fun registerUser(name: String, id: String, email: String) {
        userManager.registerUser(name, id, email)
    }

    fun loanBook(userId: String, bookTitle: String) {
        val user = userManager.findUser(userId)
        val book = bookManager.findBook(bookTitle)
        if (user != null && book != null) {
            loanManager.loanBook(user, book)
        }
    }

    fun returnBook(userId: String, bookTitle: String) {
        val user = userManager.findUser(userId)
        val book = bookManager.findBook(bookTitle)
        if (user != null && book != null) {
            loanManager.returnBook(user, book)
        }
    }
}

// Uso del sistema refactorizado
fun main() {
    val bookManager = BookManager()
    val userManager = UserManager()
    val loanManager = LoanManager()
    val library = Library(bookManager, userManager, loanManager)

    library.addBook("1984", "George Orwell", 5)
    library.registerUser("EulogioEP", "001", "eulogioep@email.com")
    library.loanBook("001", "1984")
    library.returnBook("001", "1984")
}