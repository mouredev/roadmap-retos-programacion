// Archivo: eulogioep.java

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

 import java.util.ArrayList;
 import java.util.Date;
 import java.util.List;
 import java.util.UUID;
 import java.util.stream.Collectors;
 
 public class eulogioep {
     public static void main(String[] args) {
         // Ejemplo de uso del sistema
         try {
             // Creación de los managers
             BookManager bookManager = new BookManager();
             UserManager userManager = new UserManager();
             LoanManager loanManager = new LoanManager(bookManager, userManager);
 
             // Agregar un libro
             Book book = bookManager.addBook("El Quijote", "Miguel de Cervantes", 5);
             System.out.println("Libro agregado: " + book);
 
             // Registrar un usuario
             User user = userManager.registerUser("Juan Pérez", "USER001", "juan@email.com");
             System.out.println("Usuario registrado: " + user);
 
             // Realizar un préstamo
             Loan loan = loanManager.loanBook(user.getId(), book.getId());
             System.out.println("Préstamo realizado: " + loan);
 
             // Devolver el libro
             loanManager.returnBook(user.getId(), book.getId());
             System.out.println("Libro devuelto exitosamente");
 
             // Verificar el estado del libro
             Book updatedBook = bookManager.findBook(book.getId());
             System.out.println("Estado actual del libro: " + updatedBook);
 
         } catch (Exception e) {
             System.err.println("Error: " + e.getMessage());
         }
     }
 }
 
 // ========== IMPLEMENTACIÓN INCORRECTA (Violando SRP) ==========
 
 /**
  * Esta implementación viola el SRP porque la clase Library maneja múltiples responsabilidades:
  * 1. Gestión de libros
  * 2. Gestión de usuarios
  * 3. Gestión de préstamos
  */
 class Library {
     private List<Book> books;
     private List<User> users;
     private List<Loan> loans;
 
     public Library() {
         this.books = new ArrayList<>();
         this.users = new ArrayList<>();
         this.loans = new ArrayList<>();
     }
 
     // Gestión de libros
     public void addBook(String title, String author, int copies) {
         Book book = new Book(title, author, copies);
         books.add(book);
     }
 
     public void removeBook(String bookId) {
         books.removeIf(book -> book.getId().equals(bookId));
     }
 
     // Gestión de usuarios
     public void registerUser(String name, String id, String email) {
         User user = new User(name, id, email);
         users.add(user);
     }
 
     public void removeUser(String userId) {
         users.removeIf(user -> user.getId().equals(userId));
     }
 
     // Gestión de préstamos
     public void loanBook(String userId, String bookId) throws Exception {
         Book book = books.stream()
                         .filter(b -> b.getId().equals(bookId))
                         .findFirst()
                         .orElseThrow(() -> new Exception("Libro no encontrado"));
 
         User user = users.stream()
                         .filter(u -> u.getId().equals(userId))
                         .findFirst()
                         .orElseThrow(() -> new Exception("Usuario no encontrado"));
 
         if (book.getAvailableCopies() <= 0) {
             throw new Exception("No hay copias disponibles");
         }
 
         book.decrementCopies();
         loans.add(new Loan(userId, bookId, new Date()));
     }
 
     public void returnBook(String userId, String bookId) throws Exception {
         Loan loan = findLoan(userId, bookId);
         if (loan == null) {
             throw new Exception("Préstamo no encontrado");
         }
 
         Book book = books.stream()
                         .filter(b -> b.getId().equals(bookId))
                         .findFirst()
                         .orElse(null);
 
         if (book != null) {
             book.incrementCopies();
         }
 
         loans.removeIf(l -> l.getUserId().equals(userId) && l.getBookId().equals(bookId));
     }
 
     private Loan findLoan(String userId, String bookId) {
         return loans.stream()
                    .filter(l -> l.getUserId().equals(userId) && l.getBookId().equals(bookId))
                    .findFirst()
                    .orElse(null);
     }
 }
 
 // ========== IMPLEMENTACIÓN CORRECTA (Siguiendo SRP) ==========
 
 /**
  * BookManager: Responsable únicamente de la gestión de libros
  */
 class BookManager {
     private List<Book> books;
 
     public BookManager() {
         this.books = new ArrayList<>();
     }
 
     public Book addBook(String title, String author, int copies) {
         Book book = new Book(title, author, copies);
         books.add(book);
         return book;
     }
 
     public void removeBook(String bookId) {
         books.removeIf(book -> book.getId().equals(bookId));
     }
 
     public Book findBook(String bookId) {
         return books.stream()
                    .filter(book -> book.getId().equals(bookId))
                    .findFirst()
                    .orElse(null);
     }
 
     public void updateBookCopies(String bookId, int change) {
         Book book = findBook(bookId);
         if (book != null) {
             if (change > 0) {
                 book.incrementCopies();
             } else {
                 book.decrementCopies();
             }
         }
     }
 
     public List<Book> getAllBooks() {
         return new ArrayList<>(books);
     }
 }
 
 /**
  * UserManager: Responsable únicamente de la gestión de usuarios
  */
 class UserManager {
     private List<User> users;
 
     public UserManager() {
         this.users = new ArrayList<>();
     }
 
     public User registerUser(String name, String id, String email) {
         User user = new User(name, id, email);
         users.add(user);
         return user;
     }
 
     public void removeUser(String userId) {
         users.removeIf(user -> user.getId().equals(userId));
     }
 
     public User findUser(String userId) {
         return users.stream()
                    .filter(user -> user.getId().equals(userId))
                    .findFirst()
                    .orElse(null);
     }
 
     public List<User> getAllUsers() {
         return new ArrayList<>(users);
     }
 }
 
 /**
  * LoanManager: Responsable únicamente de la gestión de préstamos
  */
 class LoanManager {
     private List<Loan> loans;
     private final BookManager bookManager;
     private final UserManager userManager;
 
     public LoanManager(BookManager bookManager, UserManager userManager) {
         this.loans = new ArrayList<>();
         this.bookManager = bookManager;
         this.userManager = userManager;
     }
 
     public Loan loanBook(String userId, String bookId) throws Exception {
         Book book = bookManager.findBook(bookId);
         User user = userManager.findUser(userId);
 
         if (book == null || user == null) {
             throw new Exception("Libro o usuario no encontrado");
         }
 
         if (book.getAvailableCopies() <= 0) {
             throw new Exception("No hay copias disponibles");
         }
 
         bookManager.updateBookCopies(bookId, -1);
         Loan loan = new Loan(userId, bookId, new Date());
         loans.add(loan);
         return loan;
     }
 
     public void returnBook(String userId, String bookId) throws Exception {
         Loan loan = findLoan(userId, bookId);
         if (loan == null) {
             throw new Exception("Préstamo no encontrado");
         }
 
         bookManager.updateBookCopies(bookId, 1);
         loans.removeIf(l -> l.getUserId().equals(userId) && l.getBookId().equals(bookId));
     }
 
     private Loan findLoan(String userId, String bookId) {
         return loans.stream()
                    .filter(loan -> loan.getUserId().equals(userId) && loan.getBookId().equals(bookId))
                    .findFirst()
                    .orElse(null);
     }
 
     public List<Loan> getAllLoans() {
         return new ArrayList<>(loans);
     }
 }
 
 // Clases de modelo
 class Book {
     private final String id;
     private final String title;
     private final String author;
     private int availableCopies;
 
     public Book(String title, String author, int availableCopies) {
         this.id = UUID.randomUUID().toString();
         this.title = title;
         this.author = author;
         this.availableCopies = availableCopies;
     }
 
     public String getId() {
         return id;
     }
 
     public String getTitle() {
         return title;
     }
 
     public String getAuthor() {
         return author;
     }
 
     public int getAvailableCopies() {
         return availableCopies;
     }
 
     public void incrementCopies() {
         this.availableCopies++;
     }
 
     public void decrementCopies() {
         this.availableCopies--;
     }
 
     @Override
     public String toString() {
         return "Book{" +
                "id='" + id + '\'' +
                ", title='" + title + '\'' +
                ", author='" + author + '\'' +
                ", availableCopies=" + availableCopies +
                '}';
     }
 }
 
 class User {
     private final String id;
     private final String name;
     private final String email;
 
     public User(String name, String id, String email) {
         this.name = name;
         this.id = id;
         this.email = email;
     }
 
     public String getId() {
         return id;
     }
 
     public String getName() {
         return name;
     }
 
     public String getEmail() {
         return email;
     }
 
     @Override
     public String toString() {
         return "User{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                '}';
     }
 }
 
 class Loan {
     private final String userId;
     private final String bookId;
     private final Date loanDate;
 
     public Loan(String userId, String bookId, Date loanDate) {
         this.userId = userId;
         this.bookId = bookId;
         this.loanDate = loanDate;
     }
 
     public String getUserId() {
         return userId;
     }
 
     public String getBookId() {
         return bookId;
     }
 
     public Date getLoanDate() {
         return loanDate;
     }
 
     @Override
     public String toString() {
         return "Loan{" +
                "userId='" + userId + '\'' +
                ", bookId='" + bookId + '\'' +
                ", loanDate=" + loanDate +
                '}';
     }
 }