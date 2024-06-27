import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.function.Consumer;

public interface diegosilval {
    static void main(String... args) {
        System.out.println("** Usando una clase para todo **");
        var libraryUtil = new LibraryUtil();
        libraryUtil.addUser("01", "Alex", "alex@mail.com");
        libraryUtil.addUser("02", "Bob", "bob@mnail.com");
        libraryUtil.addUser("03", "Cark", "carl@mnail.com");

        libraryUtil.addBook("To Kill a Mockingbird", "Harper Lee", 2);
        libraryUtil.addBook("1984", "George Orwell", 1);
        libraryUtil.addBook("Pride and Prejudice", "Jane Austen", 0);

        libraryUtil.bookBorrow("1984", "01").ifPresentOrElse(showBorrowSuccess, showBorrowFail);
        libraryUtil.bookBorrow("To Kill a Mockingbird", "02").ifPresentOrElse(showBorrowSuccess, showBorrowFail);
        libraryUtil.bookBorrow("1984", "03").ifPresentOrElse(showBorrowSuccess, showBorrowFail);

        // Usando SRP
        System.out.println("** Usando una clase por cada responsabilidad");
        var usersRepository = new UsersRepository();
        var booksRepository = new BooksRepository();
        var srpLibraryUtil = new SrpLibraryUtil(usersRepository, booksRepository); // inyectando
        usersRepository.addUser("01", "Alex", "alex@mail.com");
        usersRepository.addUser("02", "Bob", "bob@mnail.com");
        usersRepository.addUser("03", "Cark", "carl@mnail.com");

        booksRepository.addBook("To Kill a Mockingbird", "Harper Lee", 2);
        booksRepository.addBook("1984", "George Orwell", 1);
        booksRepository.addBook("Pride and Prejudice", "Jane Austen", 0);

        srpLibraryUtil.bookBorrow("1984", "01").ifPresentOrElse(showBorrowSuccess, showBorrowFail);
        srpLibraryUtil.bookBorrow("To Kill a Mockingbird", "02").ifPresentOrElse(showBorrowSuccess, showBorrowFail);
        srpLibraryUtil.bookBorrow("1984", "03").ifPresentOrElse(showBorrowSuccess, showBorrowFail);

    }

    static Consumer<BookLoan> showBorrowSuccess = (bookLoan) -> {
        System.out.println(String.format("Se prestó correctamente %s a %s", bookLoan.getBook().getTitle(),
                bookLoan.getUser().getName()));
    };
    static Runnable showBorrowFail = () -> System.err.println(
            "El usuario no existe, el nombre del libro no existe, o no existen libros disponibles para prestar");

}

/**
 * Book Class
 */
class Book {
    private String title;
    private String author;
    private int available;

    public Book() {
    }

    public Book(String title, String author, int available) {
        this.title = title;
        this.author = author;
        this.available = available;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public int getAvailable() {
        return available;
    }

    public void setAvailable(int available) {
        this.available = available;
    }

    public void addAvailable(int delta) {
        this.available += delta;
    }

    public void removeAvailable(int delta) {
        this.available -= delta;
    }

}

/**
 * User Class
 */
class User {
    private String name;
    private String id;
    private String email;

    public User() {
    }

    public User(String name, String id, String email) {
        this.name = name;
        this.id = id;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

}

class BookLoan {
    private final Book book;
    private final User user;

    public BookLoan(Book book, User user) {
        this.book = book;
        this.user = user;
    }

    public Book getBook() {
        return book;
    }

    public User getUser() {
        return user;
    }

}

class LibraryUtil {
    private List<Book> books = new ArrayList<>();
    private List<User> users = new ArrayList<>();
    private List<BookLoan> bookLoans = new ArrayList<>();

    public void addBook(String title, String author, int available) {
        books.add(new Book(title, author, available));
    }

    public void addUser(String id, String name, String email) {
        users.add(new User(name, id, email));
    }

    public Optional<BookLoan> bookBorrow(String title, String userId) {
        var user = users.stream().filter(aUser -> aUser.getId().equals(userId)).findFirst();
        if (user.isEmpty())
            return Optional.empty();
        var book = books.stream().filter(aBook -> aBook.getTitle().equalsIgnoreCase(title)).findFirst();
        if (book.isEmpty() || book.get().getAvailable() == 0)
            return Optional.empty();
        book.get().removeAvailable(1);
        var bookLoan = new BookLoan(book.get(), user.get());
        bookLoans.add(bookLoan);
        return Optional.of(bookLoan);
    }
}

/**
 * Clase LibraryUtil aplicando SRP
 */
class SrpLibraryUtil {
    private final UsersRepository usersRepository;
    private final BooksRepository booksRepository;
    private List<BookLoan> bookLoans = new ArrayList<>();

    public SrpLibraryUtil(UsersRepository usersRepository, BooksRepository booksRepository) {
        this.usersRepository = usersRepository;
        this.booksRepository = booksRepository;
    }

    public Optional<BookLoan> bookBorrow(String title, String userId) {
        var user = usersRepository.findById(userId);
        var book = booksRepository.findByTitle(title);
        if (user.isEmpty() || book.isEmpty())
            return Optional.empty();
        book.get().removeAvailable(1);
        var bookLoan = new BookLoan(book.get(), user.get());
        bookLoans.add(bookLoan);
        return Optional.of(bookLoan);
    }

}

/**
 * Repositorio de usuarios
 */
class UsersRepository {
    private List<User> users = new ArrayList<>();

    public void addUser(String id, String name, String email) {
        users.add(new User(name, id, email));
    }

    public Optional<User> findById(String userId) {
        return users.stream().filter(aUser -> aUser.getId().equals(userId)).findFirst();
    }
}

class BooksRepository {
    private List<Book> books = new ArrayList<>();

    public void addBook(String title, String author, int available) {
        books.add(new Book(title, author, available));
    }

    public Optional<Book> findByTitle(String title) {
        return books.stream().filter(aBook -> aBook.getTitle().equalsIgnoreCase(title) && aBook.getAvailable() > 0)
                .findFirst();
    }
}