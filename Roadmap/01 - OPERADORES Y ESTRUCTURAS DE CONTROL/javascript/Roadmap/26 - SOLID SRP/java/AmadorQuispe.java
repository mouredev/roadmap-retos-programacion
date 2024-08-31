package com.amsoft.roadmap.example26;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Example26 {
    public static void main(String[] args) {
        Employee employee = new Employee(100, "Amador Quispe", "correo@gmail.com");
        EmployeeRepository userRepository = new EmployeeRepository();
        userRepository.save(employee);
        EmployeeService userService = new EmployeeService();
        userService.sendMail(employee);

        /*Library library = new Library();
        library.registerUser(new User("47229145", "Amador Quispe", "aquispe@gmail.com"));
        library.registerBook(new Book("Clean Code", "Robert C. Martin", 4));
        library.registerBook(new Book("Clean Architecture", "Robert C. Martin", 5));
        library.registerBook(new Book("Clean Agile", "Robert C. Martin", 8));
        library.loanBook("Clean Code", "47229145");
        library.books.forEach(s -> System.out.println(s.getCopiesAvailable()));
        library.returnLoanBook("Clean Code", "47229145");
        library.books.forEach(s -> System.out.println(s.getCopiesAvailable()));*/
        SRPLibrary srpLibrary = new SRPLibrary();
        srpLibrary.run();
    }

}

//Viola SRP
/*class User {
    private Integer id;
    private String names;
    private String email;

    public User(Integer id, String names, String email) {
        this.id = id;
        this.names = names;
        this.email = email;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", names='" + names + '\'' +
                ", email='" + email + '\'' +
                '}';
    }

    public void saveInDB(){
        System.out.println("Guardando en la base de datos : " + this);
    }
    public void sendNotification(){
        System.out.println("Enviando notificación al correo: " + email);
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}*/
class Employee {
    private Integer id;
    private String names;
    private String email;

    public Employee(Integer id, String names, String email) {
        this.id = id;
        this.names = names;
        this.email = email;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", names='" + names + '\'' +
                ", email='" + email + '\'' +
                '}';
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}

class EmployeeRepository {
    public void save(Employee employee) {
        System.out.println("Guardando user en base de datos : " + employee.toString());
    }
}

class EmployeeService {
    public void sendMail(Employee employee) {
        System.out.println("Enviando mensaje de notificación al correo :" + employee.getEmail());
    }
}

//Viola SRP
/*class Library {
    private final Map<String, List<String>> loanBooks;
    public List<Book> books;
    public List<User> users;

    Library() {
        this.books = new ArrayList<>();
        this.users = new ArrayList<>();
        this.loanBooks = new HashMap<>();
    }

    public void registerBook(Book book) {
        books.add(book);
    }

    public void registerUser(User user) {
        users.add(user);
    }

    public void loanBook(String bookTitle, String userDoi) {
        User user = users.stream().filter(u -> u.getDoi().equals(userDoi)).findFirst().orElse(null);
        Book book = books.stream().filter(b -> b.getTitle().equalsIgnoreCase(bookTitle)).findFirst().orElse(null);
        if (user == null || book == null) {
            System.out.println("Usuario o Libro no está registrado");
            return;
        }

        if (book.getCopiesAvailable() == 0) {
            System.out.println("No hay copias disponibles");
        } else {
            var loanUsers = loanBooks.get(userDoi);
            if (loanUsers == null) {
                loanUsers = new ArrayList<>();
            }
            loanUsers.add(bookTitle);
            loanBooks.put(userDoi, loanUsers);
            book.setCopiesAvailable(book.getCopiesAvailable() - 1);
        }
    }

    public void returnLoanBook(String bookTitle, String userDoi) {
        User user = users.stream().filter(u -> u.getDoi().equals(userDoi)).findFirst().orElse(null);
        Book book = books.stream().filter(b -> b.getTitle().equalsIgnoreCase(bookTitle)).findFirst().orElse(null);
        if (user == null || book == null) {
            System.out.println("Usuario o Libro no está registrado");
            return;
        }
        var loanUsers = loanBooks.get(userDoi);
        if (loanUsers == null) {
            System.out.println("El préstamo no está registrada");
        } else {
            loanBooks.put(userDoi, loanUsers.stream().filter(lu -> !lu.equalsIgnoreCase(bookTitle)).toList());
            book.setCopiesAvailable(book.getCopiesAvailable() + 1);
        }
    }
}
*/
class Book {
    private String title;
    private String author;
    private int copiesAvailable;

    public Book() {
    }

    public Book(String title, String author, int copiesAvailable) {
        this.title = title;
        this.author = author;
        this.copiesAvailable = copiesAvailable;
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

    public int getCopiesAvailable() {
        return copiesAvailable;
    }

    public void setCopiesAvailable(int copiesAvailable) {
        this.copiesAvailable = copiesAvailable;
    }
}

class User {
    private String doi;
    private String name;
    private String email;

    public User() {
    }

    public User(String doi, String name, String email) {
        this.name = name;
        this.doi = doi;
        this.email = email;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}

class SRPLibrary{
    private final LoanService loanService;
    private final UserService userService;
    private final BookService bookService;
    public SRPLibrary(){
        UserRepository userRepository = new UserRepository();
        BookRepository bookRepository =  new BookRepository();
        LoanBookRepository loanBookRepository =  new LoanBookRepository();
        this.loanService = new LoanService(userRepository,bookRepository,loanBookRepository);
        this.userService = new UserService(userRepository);
        this.bookService = new BookService(bookRepository);
    }
    public void run(){
        userService.register(new User("44445555","Amador Quispe","amador@gmail.com"));
        userService.register(new User("44446666","Alex","alex@gmail.com"));
        bookService.register(new Book("Clean Code", "Robert C. Martin", 4));
        bookService.register(new Book("Clean Architecture", "Robert C. Martin", 5));
        bookService.register(new Book("Clean Agile", "Robert C. Martin", 8));

        loanService.registerLoan("Clean Code","44445555");
        loanService.registerLoan("Clean Architecture","44446666");
        System.out.println("PRESTAMOS");
        loanService.findAll().forEach((k,v)-> System.out.println(k + " tiene en préstamo los libros: "+v));
    }
}
//SERVICIOS, LÓGICA DE NEGOCIO
class UserService {
    private final UserRepository userRepository;
    public UserService(UserRepository userRepository){
        this.userRepository = userRepository;
    }
    public void register(User user){
        userRepository.register(user);
    }
    public void findByDoi( String doi ){
        userRepository.findByDoi(doi);
    }
}
class BookService {
    private final BookRepository bookRepository;
    public BookService(BookRepository bookRepository){
        this.bookRepository = bookRepository;
    }
    public void register(Book book){
        bookRepository.register(book);
    }
    public void findByDoi( String doi ){
        bookRepository.findByTitle(doi);
    }
}
class LoanService {
    private final UserRepository userRepository;
    private final BookRepository bookRepository;
    private final LoanBookRepository loanBookRepository;

    public LoanService(UserRepository userRepository, BookRepository bookRepository, LoanBookRepository loanBookRepository) {
        this.userRepository = userRepository;
        this.bookRepository = bookRepository;
        this.loanBookRepository = loanBookRepository;
    }

    public void registerLoan(String bookTitle, String userDoi) {
        User user = userRepository.findByDoi(userDoi);
        Book book = bookRepository.findByTitle(bookTitle);
        System.out.println(user);
        System.out.println(book);
        if (user == null || book == null) {
            System.out.println("Usuario o Libro no está registrado");
            return;
        }
        if (book.getCopiesAvailable() == 0) {
            System.out.println("No hay copias disponibles");
        } else {
            loanBookRepository.registerLoan(bookTitle,userDoi);
            book.setCopiesAvailable(book.getCopiesAvailable() - 1);
        }
    }
    public void registerReturn(String bookTitle, String userDoi) {
        User user = userRepository.findByDoi(userDoi);
        Book book = bookRepository.findByTitle(bookTitle);
        if (user == null || book == null) {
            System.out.println("Usuario o Libro no está registrado");
            return;
        }
        loanBookRepository.registerReturn(bookTitle,userDoi);
        book.setCopiesAvailable(book.getCopiesAvailable() + 1);
    }
    public Map<String, List<String>> findAll(){
        return loanBookRepository.findAll();
    }
}
//REPOSITORIOS, ENCARGADOS DE GUARDAR
class UserRepository {
    private final List<User> userList = new ArrayList<>();

    public void register(User user) {
        userList.add(user);
    }

    public User findByDoi(String doi) {
        return userList.stream().filter(u -> u.getDoi().equals(doi)).findFirst().orElse(null);
    }
}
class BookRepository {
    private final List<Book> bookList = new ArrayList<>();

    public void register(Book book) {
        bookList.add(book);
    }

    public Book findByTitle(String title) {
        return bookList.stream().filter(b -> b.getTitle().equalsIgnoreCase(title))
                .findFirst().orElse(null);
    }
}
class LoanBookRepository {
    private final Map<String, List<String>> loanBooks;

    public LoanBookRepository() {
        this.loanBooks = new HashMap<>();
    }

    public void registerLoan(String bookTitle, String userDoi) {
        List<String> loanUsers = loanBooks.get(userDoi);
        if (loanUsers == null) {
            loanUsers = new ArrayList<>();
        }
        loanUsers.add(bookTitle);
        loanBooks.put(userDoi, loanUsers);
    }
    public void registerReturn(String bookTitle, String userDoi){
        List<String> loanUsers = loanBooks.get(userDoi);
        if (loanUsers == null) {
            System.out.println("El préstamo no está registrada");
        } else {
            loanBooks.put(userDoi, loanUsers.stream().filter(lu -> !lu.equalsIgnoreCase(bookTitle)).toList());
        }
    }
    public Map<String, List<String>> findAll(){
        return loanBooks;
    }
}

