import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

public class danhingar {

    // Incorrecto
    public class User {

        private String name;
        private String email;

        public User(String name, String email) {
            this.email = email;
            this.name = name;
        }

        public void save(User user) {

        }

        public void sendEmail(User user) {

        }

    }

    // Correcto
    public class User1 {

        private String name;
        private String email;

        public User1(String name, String email) {
            this.name = name;
            this.email = email;
        }

    }

    public class UserService {

        public void save(User1 user1) {

        }

    }

    public class EmailService {

        public void sendEmail(String email, String message) {

        }
    }

    public static void main(String[] args) {
        // WITHOUT SRP
        Library library = new Library();
        library.addUser(1, "Daniel", "example@gmail.com");
        library.addUser(2, "Pepe", "example@gmail.com");
        System.out.println(library.toString());
        library.addBook("Libro 1", "Autor 1", 5);
        library.addBook("Libro 2", "Autor 2", 3);
        System.out.println(library.toString());
        library.loanBook(1, "Libro 1");
        library.loanBook(2, "Libro 1");
        System.out.println(library.toString());
        library.returnBook(2, "Libro 1");
        System.out.println(library.toString());

        // WITH SRP
        Library2 library2 = new Library2();
        library2.addUser(new User2(1, "Daniel", "example@gmail.com"));
        library2.addUser(new User2(2, "Pepe", "example@gmail.com"));
        System.out.println(library2.toString());
        library2.addBook(new Book("Libro 1", "Autor 1", 5));
        library2.addBook(new Book("Libro 2", "Autor 2", 3));
        System.out.println(library2.toString());
        library2.loanBook(1, "Libro 1");
        library2.loanBook(2, "Libro 1");
        System.out.println(library2.toString());
        library2.returnBook(2, "Libro 1");
        System.out.println(library2.toString());
    }

}

// Extra

// Incorrecto

class Library {
    private List<Map<String, Object>> users;
    private List<Map<String, Object>> books;
    private Map<Integer, List<String>> loans;

    public Library() {
        this.users = new ArrayList<>();
        this.books = new ArrayList<>();
        this.loans = new HashMap<>();
    }

    public void addBook(String title, String author, Integer copies) {
        Map<String, Object> book = new HashMap<>();
        book.put("title", title);
        book.put("author", author);
        book.put("copies", copies);
        books.add(book);
    }

    public void addUser(Integer id, String name, String email) {
        Map<String, Object> user = new HashMap<>();
        user.put("id", id);
        user.put("name", name);
        user.put("email", email);
        users.add(user);
    }

    public void loanBook(Integer userId, String bookTitle) {
        for (Map<String, Object> book : books) {
            if (book.get("title").equals(bookTitle) && (Integer) book.get("copies") > 0) {
                book.put("copies", (Integer) book.get("copies") - 1);
                List<String> booksUser = loans.get(userId) != null ? loans.get(userId) : new ArrayList<>();
                booksUser.add(bookTitle);
                loans.put(userId, booksUser);
            }
        }
    }

    public void returnBook(Integer userId, String bookTitle) {
        boolean exist = this.loans.get(userId).stream().anyMatch(b -> b.equals(bookTitle));
        if (exist) {
            this.books.stream().filter(b -> b.get("title").equals(bookTitle))
                    .forEach(b -> b.put("copies", (Integer) b.get("copies") + 1));
            this.loans.get(userId).remove(bookTitle);
        }
    }

    @Override
    public String toString() {
        return "Library [users=" + users.toString() + ", books=" + books.toString() + ", loans=" + loans.toString() + "]";
    }
}

// Correcto

class Library2 {

    private List<User2> users;
    private List<Book> books;
    private Loan loans;

    public Library2() {
        users = new ArrayList<>();
        books = new ArrayList<>();
        loans = new Loan();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void addUser(User2 user) {
        users.add(user);
    }

    public void loanBook(Integer userId, String bookTitle) {
        Optional<User2> user = users.stream().filter(u -> u.getId().equals(userId)).findFirst();
        Optional<Book> book = books.stream().filter(b -> b.getTitle().equals(bookTitle)).findFirst();
        if (user.isPresent() && book.isPresent()) {
            loans.loanBook(user.get(), book.get());
        }

    }

    public void returnBook(Integer userId, String bookTitle) {
        Optional<User2> user = users.stream().filter(u -> u.getId().equals(userId)).findFirst();
        Optional<Book> book = books.stream().filter(b -> b.getTitle().equals(bookTitle)).findFirst();
        if (user.isPresent() && book.isPresent()) {
            loans.returnBook(user.get(), book.get());
        }
    }

    @Override
    public String toString() {
        return "Library [users=" + users + ", books=" + books.toString() + ", loans=" + loans + "]";
    }

}

class Book {

    private String author;
    private String title;
    private Integer copies;

    public Book(String title, String author, Integer copies) {
        this.title = title;
        this.author = author;
        this.copies = copies;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Integer getCopies() {
        return copies;
    }

    public void setCopies(Integer copies) {
        this.copies = copies;
    }

    @Override
    public String toString() {
        return "Book [author=" + author + ", title=" + title + ", copies=" + copies + "]";
    }

}

class User2 {
    private String name;
    private Integer id;
    private String email;

    public User2(Integer id, String name, String email) {
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

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

}

class Loan {

    private Map<Integer, List<String>> loans;

    public Loan() {
        this.loans = new HashMap<>();
    }

    public void loanBook(User2 user, Book book) {
        if (book.getCopies() > 0) {
            book.setCopies(book.getCopies() - 1);
            List<String> booksUser = loans.get(user.getId()) != null ? loans.get(user.getId()) : new ArrayList<>();
            booksUser.add(book.getTitle());
            loans.put(user.getId(), booksUser);
        }

    }

    public void returnBook(User2 user, Book book) {
        boolean exist = this.loans.get(user.getId()).stream().anyMatch(b -> b.equals(book.getTitle()));
        if (exist) {
            book.setCopies(book.getCopies() + 1);
            this.loans.get(user.getId()).remove(book.getTitle());
        }
    }

    public Map<Integer, List<String>> getLoans() {
        return loans;
    }

    @Override
    public String toString() {
        return "Loan [loans=" + loans.toString() + "]";
    }

    

}