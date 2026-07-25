
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class simonguzman {
    public static void main(String[] args) {
        //libraryManagementSystemLiskovViolation();
        //libraryLSP();
        //LiskovIncorrectTest();
        LiskovCorrectTest();
    }
    /****************************** ejercicio adicional con lsp (Correcto) ******************************/
    public static void LiskovCorrectTest() {
        VehiculoLsp coche = new Coche();
        VehiculoLsp bicicleta = new Bicicleta();
        VehiculoLsp motocicleta = new Motocicleta();

        // Probar comportamiento de los vehículos
        acelerarYFrenarLsp(coche);
        acelerarYFrenarLsp(bicicleta);
        acelerarYFrenarLsp(motocicleta);
    }

    public static void acelerarYFrenarLsp(VehiculoLsp vehiculo) {
        vehiculo.acelerar();
        vehiculo.frenar();
    }

    static class VehiculoLsp {
        public void acelerar() {
            System.out.println("El vehículo está acelerando.");
        }

        public void frenar() {
            System.out.println("El vehículo está frenando.");
        }
    }

    static class Coche extends VehiculoLsp {
        @Override
        public void acelerar() {
            System.out.println("El coche está acelerando rápidamente.");
        }

        @Override
        public void frenar() {
            System.out.println("El coche está frenando suavemente.");
        }
    }

    static class Bicicleta extends VehiculoLsp {
        @Override
        public void acelerar() {
            System.out.println("La bicicleta está acelerando lentamente.");
        }

        @Override
        public void frenar() {
            System.out.println("La bicicleta está frenando manualmente.");
        }
    }
    static class Motocicleta extends VehiculoLsp {
        @Override
        public void acelerar() {
            System.out.println("La motocicleta está acelerando con potencia.");
        }

        @Override
        public void frenar() {
            System.out.println("La motocicleta está frenando rápidamente.");
        }
    }
    /****************************** ejercicio adicional sin lsp (Incorrecto) ******************************/
    public static void LiskovIncorrectTest() {
        Vehiculo cocheElectrico = new CocheElectrico();
        acelerarYFrenar(cocheElectrico);

        ((CocheElectrico) cocheElectrico).recargarBateria();
    }

    public static void acelerarYFrenar(Vehiculo vehiculo) {
        vehiculo.acelerar();
        vehiculo.frenar();
    }

    static class Vehiculo {
        public void acelerar() {
            System.out.println("El vehículo está acelerando.");
        }

        public void frenar() {
            System.out.println("El vehículo está frenando.");
        }
    }

// Subclase CocheEléctrico que viola LSP
    static class CocheElectrico extends Vehiculo {
        @Override
        public void acelerar() {
            System.out.println("El coche eléctrico está acelerando silenciosamente.");
        }

        @Override
        public void frenar() {
            System.out.println("El coche eléctrico está frenando regenerativamente.");
        }

        // Método adicional que viola el LSP
        public void recargarBateria() {
            System.out.println("Recargando la batería del coche eléctrico.");
        }
    }
    /****************************** ejemplo con lsp (Correcto) ******************************/
    static void libraryLSP(){
        LibraryManager libraryManager = new LibraryManager();
        UserManager userManager = new UserManager();
        LoanManagerLsp loanManager = new LoanManagerLsp();

        libraryManager.registerBook(new PhysicalBook("1984", "George Orwell", 3));
        libraryManager.registerBook(new EBookLsp("Clean Code", "Robert Martin"));

        userManager.registerUser("John Doe", "001", "johndoe@example.com");

        User user = userManager.findUserById("001");
        BookLsp book1 = libraryManager.findBookByTitle("1984");
        BookLsp book2 = libraryManager.findBookByTitle("Clean Code");

        loanManager.borrowBook(user, book1);
        loanManager.borrowBook(user, book2);

        loanManager.returnBook(user, book1);
        loanManager.returnBook(user, book2);
    }

    static abstract class BookLsp{
        protected String title;
        protected String author;

        public BookLsp(){

        }

        public BookLsp(String title, String author){
            this.title = title;
            this.author = author;
        }

        public String getTitle() {
            return title;
        }

        public abstract boolean isAvailable();
        public abstract void borrow();
        public abstract void returnBook(); 
    }

    static class PhysicalBook extends BookLsp{
        private int copies;

        public PhysicalBook(){

        }

        public PhysicalBook(String title, String author, int copies){
            super(title, author);
            this.copies = copies;
        }

        @Override
        public boolean isAvailable(){
            return copies > 0;
        }

        @Override
        public void borrow(){
            if(copies > 0){
                copies--;
            }
        }

        @Override
        public void returnBook(){
            copies++;
        }
    }

    static class EBookLsp extends BookLsp {

        public EBookLsp(String title, String author) {
            super(title, author);
        }

        @Override
        public boolean isAvailable() {
            return true; // Siempre disponible
        }

        @Override
        public void borrow() {
            System.out.println("Descargando eBook...");
        }

        @Override
        public void returnBook() {
            System.out.println("El eBook ha sido devuelto.");
        }
    }
    static class LibraryManager{
        private List<BookLsp> books = new ArrayList<>();

        public void registerBook(BookLsp book){
            books.add(book);
            System.out.println("Libro registrado: " + book.getTitle());
        }

        public BookLsp findBookByTitle(String title){
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

    static class LoanManagerLsp{
        private Map<User, List<BookLsp>> borrowedBooks = new HashMap<>();

        public void borrowBook(User user, BookLsp book){
            if(book.isAvailable()){
                borrowedBooks.computeIfAbsent(user, k -> new ArrayList<>()).add(book);
                book.borrow();
                System.out.println("Libro prestado: " + book.getTitle() + " a " + user.getName());
            } else {
                System.out.println("El libro no está disponible para préstamo.");
            }
        }

        public void returnBook(User user, BookLsp book) {
            List<BookLsp> borrowed = borrowedBooks.get(user);
            if (borrowed != null && borrowed.contains(book)) {
                borrowed.remove(book);
                book.returnBook();
                System.out.println("Libro devuelto: " + book.getTitle());
            } else {
                System.out.println("No se pudo devolver el libro.");
            }
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
    }

    /****************************** ejemplo sin lsp (Incorrecto) ******************************/
    public static void libraryManagementSystemLiskovViolation(){
        Book physicalBook = new Book("1984", "George Orwell", 3);
        EBook ebook = new EBook("Digital Fortress", "Dan Brown", "www.download.com");

        LoanManager loanManager = new LoanManager();

        loanManager.borrowBook(physicalBook);
        
        loanManager.borrowBook(ebook);
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

        public void borrow(){
            if (copies > 0){
                copies--;
                System.out.println("Libro prestado: " + title);
            } else {
                System.out.println("No hay copias disponibles de: " + title);
            }
        }        
    }

    static class EBook extends Book {
        private String downloadLink;

        public EBook(String title, String author,String downloadLink) {
            super(title, author, 1);
            this.downloadLink = downloadLink;
        }

        @Override
        public void borrow(){
            System.out.println("No se puede prestar el eBook, pero puedes descargarlo aquí: " + downloadLink);
        }
    }

    static class LoanManager{
        public void borrowBook(Book book){
            book.borrow();
        }
    }
}
