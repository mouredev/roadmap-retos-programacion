
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class simonguzman {
    public static void main(String[] args) {
        //incorrectSrp();
        //correctSrp();
        //additionalExerciseNoSrp();
        additionalExerciseSrp();
    }
    /****************************** Ejercicio adicional(Con srp) ******************************/
    public static void additionalExerciseSrp(){
        BookManager bookManager = new BookManager();
        UserManager userManager = new UserManager();
        LoanManager loanManager = new LoanManager();

        bookManager.registerBook("1984", "George Orwell", 3);
        userManager.registerUser("John Doe", "001", "johndoe@example.com");

        User user = userManager.findUserById("001");
        Book book = bookManager.findBookByTitle("1984");

        loanManager.borrowBook(user, book);
        loanManager.returnBook(user, book);
    }

    class BookSrp {
        private String title;
        private String author;
        private int copies;
    
        public BookSrp(){

        }

        public BookSrp(String title, String author, int copies) {
            this.title = title;
            this.author = author;
            this.copies = copies;
        }
    
        public String getTitle() {
            return title;
        }
    
        public int getCopies() {
            return copies;
        }
    
        public void setCopies(int copies) {
            this.copies = copies;
        }
    }
    
    class UserSrp {
        private String name;
        private String id;
        private String email;
    
        public UserSrp(){

        }

        public UserSrp(String name, String id, String email) {
            this.name = name;
            this.id = id;
            this.email = email;
        }
    
        public String getName() {
            return name;
        }
    
        public String getId() {
            return id;
        }
    }
    
    static class BookManager{
        private List<Book> books = new ArrayList<>();
        
        public void registerBook(String title, String author, int copies){
            books.add(new Book(title, author, copies));
            System.out.println("Libro registrado: " + title);
        }

        public Book findBookByTitle(String title){
            return books.stream().filter(b -> b.getTitle().equals(title)).findFirst().orElse(null);
        }
    }

    static class UserManager{
        private List<User> users = new ArrayList<>();

        public void registerUser(String name, String id, String email){
            users.add(new User(name, id, email));
            System.out.println("Usuario registrado: " + name);
        }

        public User findUserById(String id){
            return users.stream().filter(u -> u.getId().equals(id)).findFirst().orElse(null);
        }
    }

    static class LoanManager{
        private Map<User, List<Book>> borrowedBooks = new HashMap<>();

        public void borrowBook(User user, Book book) {
            if (book != null && book.getCopies() > 0) {
                borrowedBooks.computeIfAbsent(user, k -> new ArrayList<>()).add(book);
                book.setCopies(book.getCopies() - 1);
                System.out.println("Libro prestado: " + book.getTitle() + " a " + user.getName());
            } else {
                System.out.println("No se pudo procesar el préstamo.");
            }
        }

        public void returnBook(User user, Book book) {
            List<Book> borrowed = borrowedBooks.get(user);
            if (borrowed != null && borrowed.contains(book)) {
                borrowed.remove(book);
                book.setCopies(book.getCopies() + 1);
                System.out.println("Libro devuelto: " + book.getTitle());
            } else {
                System.out.println("No se pudo devolver el libro.");
            }
        }
    }

    /****************************** Ejercicio adicional(Sin srp) ******************************/
    public static void additionalExerciseNoSrp(){
        Library library = new Library();

        library.registerBook("1984", "George Orwell", 3);
        library.registerUser("John Doe", "001", "johndoe@example.com");

        library.borrowBook("001", "1984");
        library.returnBook("001", "1984");
    }

    static class Library{
        private List<Book> books = new ArrayList<>();
        private List<User> users = new ArrayList<>();
        private Map<User, List<Book>> borrowedBooks = new HashMap<>();

        public void registerBook(String title, String author, int copies){
            books.add(new Book(title, author, copies));
            System.out.println("Libro registrado: "+title);
        }

        public void registerUser(String name, String id, String email){
            users.add(new User(name, id, email));
            System.out.println("Usuario registrado: "+name);
        }

        public void borrowBook(String userId, String bookTitle){
            User user = users.stream().filter(u -> u.getId().equals(userId)).findFirst().orElse(null);
            Book book = books.stream().filter(b -> b.getTitle().equals(bookTitle)).findFirst().orElse(null);

            if(user != null && book != null && book.getCopies() > 0){
                borrowedBooks.computeIfAbsent(user, k -> new ArrayList<>()).add(book);
                book.setCopies(book.getCopies()-1);
                System.out.println("Libro prestado: " + bookTitle + " a " + user.getName());
            }else{
                System.out.println("No se pudo procesar el prestamo.");
            }
        }

        public void returnBook(String userId, String bookTitle){
            User user = users.stream().filter(u -> u.getId().equals(userId)).findFirst().orElse(null);
            List<Book> borrowed = borrowedBooks.get(user); 

            if(borrowed != null){
                Book book = borrowed.stream().filter(b -> b.getTitle().equals(bookTitle)).findFirst().orElse(null);
                if(book != null){
                    borrowed.remove(book);
                    book.setCopies(book.getCopies() + 1);
                    System.out.println("Libro devuelto: "+bookTitle);
                }
            }else{
                System.out.println("ERROR: No se pudo devolver el libro.");
            }
        }
    }

    static class Book{
        private String title;
        private String author;
        private int copies;

        public Book(){

        }

        public Book(String title, String author, int copies){
            this.title = title;
            this.author = author;
            this.copies = copies;
        }

        public String getTitle() {
            return title;
        }

        public int getCopies() {
            return copies;
        }

        public void setCopies(int copies) {
            this.copies = copies;
        }

    }

    static class User{
        private String name;
        private String id;
        private String email;

        public User(){

        }

        public User(String name, String id, String email){
            this.name = name;
            this.id = id;
            this.email = email;
        }

        public String getName() {
            return name;
        }

        public String getId() {
            return id;
        }

        public String getEmail() {
            return email;
        }
    }

    /****************************** ejemplo con srp(Correcto) ******************************/
    public static void correctSrp() {
        InvoiceSrp invoice = new InvoiceSrp("Laptop",2,1200.00);

        InvoicePrinter printer = new InvoicePrinter();
        printer.printInvoice(invoice);

        InvoiceSaver saver = new InvoiceSaver();
        saver.saveToFile(invoice);
    }
    static class InvoiceSrp{
        private String product;
        private int quantity;
        private double price;

        public InvoiceSrp(){
            
        }

        public InvoiceSrp(String product, int quantity, double price){
            this.product = product;
            this.quantity = quantity;
            this.price = price;
        }

        public double calculateTotal(){
            return quantity * price;
        }

        public String getProduct() {
            return product;
        }

        public int getQuantity() {
            return quantity;
        }

        public double getPrice() {
            return price;
        }
    }

    static class InvoicePrinter {
        public void printInvoice(InvoiceSrp invoice){
            System.out.println("Producto: "+invoice.getProduct());
            System.out.println("Cantidad: "+invoice.getQuantity());
            System.out.println("Precio: "+invoice.getPrice());
            System.out.println("Total: "+invoice.calculateTotal());
        }
    }

    static class InvoiceSaver{
        public void saveToFile(InvoiceSrp invoice){
            try (FileWriter writer = new FileWriter("invoice.txt")){
                writer.write("Producto: " + invoice.getProduct() + "\n");
                writer.write("Cantidad: " + invoice.getQuantity() + "\n");
                writer.write("Precio unitario: " + invoice.getPrice() + "\n");
                writer.write("Total: " + invoice.calculateTotal() + "\n");
            } catch (Exception e) {
                System.out.println("ERROR: no se pudo generar la factura..."+e.getMessage());
            }
        }
    }
    /****************************** ejemplo sin srp(Incorrecto) ******************************/
    public static void incorrectSrp(){
        Invoice invoice = new Invoice("Laptop",2,1200.00);
        invoice.printInvoice();
        invoice.saveToFile();
    }

    static class Invoice{
        private String product;
        private int quantity;
        private double price;

        public Invoice(){

        }

        public Invoice(String product, int quantity, double price){
            this.product = product;
            this.quantity = quantity;
            this.price = price;
        }

        public double calculateTotal(){
            return quantity * price;
        }

        public void printInvoice(){
            System.out.println("Producto: "+product);
            System.out.println("Cantidad: "+quantity);
            System.out.println("Precio: "+price);
            System.out.println("Total: "+calculateTotal());
        }
        
        public void saveToFile(){
            try (FileWriter writer = new FileWriter("invoice.txt")){
                writer.write("Producto: " + product + "\n");
                writer.write("Cantidad: " + quantity + "\n");
                writer.write("Precio Unitario: " + price + "\n");
                writer.write("Total: " + calculateTotal() + "\n");
            } catch (Exception e) {
                System.out.println("Error al guardar la factura: "+e.getMessage());
            }
        }
    }
}
