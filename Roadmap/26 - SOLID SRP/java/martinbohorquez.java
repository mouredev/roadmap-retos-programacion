import java.util.*;

/**
 * #26 SOLID: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    static List<User> users = new ArrayList<>();
    static List<Usuario> usuarios = new ArrayList<>();

    public static void main(String[] args) {
        incorrectSrp();
        correctSrp();
        /*
         * DIFICULTAD EXTRA
         */
        addExerciseNoSrp();

    }

    private static void addExerciseNoSrp() {
        Library library = new Library();
        library.addBook("Libro 1", "Autor 1", 2);
        library.addBook("Libro 2", "Autor 2", 1);
        System.out.printf("La lista de libros es: %s%n", library.books);
        library.addUser("User 1", 1, "user1@gmail.com");
        library.addUser("User 2", 2, "user2@gmail.com");
        library.addUser("User 3", 3, "user3@gmail.com");
        System.out.printf("La lista de usuarios es: %s%n", library.users);
        library.loanBook(2, "Libro 1");
        library.loanBook(3, "Libro 2");
        library.loanBook(1, "Libro 2");
        library.loanBook(1, "Libro 1");
        System.out.printf("La lista de prestámos es: %s%n", library.loans);
        library.returnBook(2, "Libro 2");
        library.returnBook(2, "Libro 1");
        System.out.printf("La lista de prestámos es: %s%n", library.loans);
    }

    private static void addExerciseSrp() {
        Biblioteca biblioteca = new Biblioteca();
        Book book1 = new Book("Libro 1", "Autor 1", 2);
        Book book2 = new Book("Libro 2", "Autor 2", 1);
        biblioteca.addBook(book1);
        biblioteca.addBook(book2);
        System.out.printf("La lista de libros es: %s%n", biblioteca.books);
        Usero user1 = new Usero("User 1", 1, "user1@gmail.com");
        Usero user2 = new Usero("User 2", 2, "user2@gmail.com");
        Usero user3 = new Usero("User 3", 3, "user3@gmail.com");
        biblioteca.addUser(user1);
        biblioteca.addUser(user2);
        biblioteca.addUser(user3);
        System.out.printf("La lista de usuarios es: %s%n", biblioteca.users);
        biblioteca.loanBook(2, "Libro 1");
        biblioteca.loanBook(3, "Libro 2");
        biblioteca.loanBook(1, "Libro 2");
        biblioteca.loanBook(1, "Libro 1");
        System.out.printf("La lista de prestámos es: %s%n", biblioteca.loans);
        biblioteca.returnBook(2, "Libro 2");
        biblioteca.returnBook(2, "Libro 1");
        System.out.printf("La lista de prestámos es: %s%n", biblioteca.loans);
    }

    private static void incorrectSrp() {
        User user1 = new User("Jose", "josesc3@gmail.com");
        User user2 = new User("Luis", "luisc5@gmail.com");
        user1.saveDatabase();
        user2.saveDatabase();
        user1.sendEmail("Mensaje enviado desde la una instancia que no aplica el principio de SRP!");
        user2.sendEmail("Mensaje 2 enviado desde la una instancia que no aplica el principio de SRP!");
    }

    private static void correctSrp() {
        Usuario usuario1 = new Usuario("Jose", "josesc3@gmail.com");
        Usuario usuario2 = new Usuario("Luis", "luisc5@gmail.com");
        UsuarioService usuarioService = new UsuarioService();
        usuarioService.saveDatabase(usuario1)
                .saveDatabase(usuario2);
        EmailService emailService = new EmailService();
        emailService.sendEmail(usuario1,
                "Mensaje enviado desde la una instancia que aplica el principio de SRP!");
        emailService.sendEmail(usuario2,
                "Mensaje 2 enviado desde la una instancia que aplica el principio de SRP!");
    }

    static class User {
        private final String name;
        private final String email;

        User(String name, String email) {
            this.name = name;
            this.email = email;
        }

        protected void saveDatabase() {
            users.add(this);
            System.out.printf("Se ha creado el usuario con nombre %s%n", name);
        }

        protected void sendEmail(String message) {
            System.out.printf("Se envía correo desde '%s':%n%s%n", email, message);
        }
    }

    static class Usuario {
        private final String name;
        private final String email;

        Usuario(String name, String email) {
            this.name = name;
            this.email = email;
        }
    }

    static class UsuarioService {
        protected UsuarioService saveDatabase(Usuario usuario) {
            usuarios.add(usuario);
            System.out.printf("Se ha creado el usuario con nombre %s (usando SRP)%n", usuario.name);
            return this;
        }
    }

    static class EmailService {
        protected void sendEmail(Usuario usuario, String message) {
            System.out.printf("Se envía correo desde '%s':%n%s%n", usuario.email, message);
        }
    }

    static class Library {
        private List<Map<String, Object>> books;
        private List<Map<String, Object>> users;
        private List<Map<String, Object>> loans;

        public Library() {
            this.books = new ArrayList<>();
            this.users = new ArrayList<>();
            this.loans = new ArrayList<>();
        }

        private void addBook(String title, String author, Integer copies) {
            Map<String, Object> book = new HashMap<>();
            book.put("title", title);
            book.put("author", author);
            book.put("copies", copies);
            books.add(book);
        }

        private void addUser(String name, Integer id, String email) {
            Map<String, Object> user = new HashMap<>();
            user.put("name", name);
            user.put("id", id);
            user.put("email", email);
            users.add(user);
        }

        private void loanBook(Integer userId, String bookTitle) {
            books.stream()
                    .filter(b -> b.get("title").equals(bookTitle) && (Integer) b.get("copies") > 0)
                    .findFirst()
                    .ifPresent(b -> {
                        b.put("copies", (Integer) b.get("copies") - 1);
                        Map<String, Object> loan = new HashMap<>();
                        loan.put("userId", userId);
                        loan.put("bookTitle", bookTitle);
                        loans.add(loan);
                    });
        }

        private void returnBook(Integer userId, String bookTitle) {
            loans.stream()
                    .filter(l -> l.get("userId").equals(userId) && l.get("bookTitle").equals(bookTitle))
                    .findFirst()
                    .ifPresent(l -> {
                        loans.remove(l);
                        books.stream()
                                .filter(b -> b.get("title").equals(bookTitle))
                                .findFirst()
                                .ifPresent(b -> b.put("copies", (Integer) b.get("copies") + 1));
                    });
        }
    }

    static class Biblioteca {
        private List<Book> books;
        private List<Usero> users;
        private Loan loans;

        public Biblioteca() {
            this.books = new ArrayList<>();
            this.users = new ArrayList<>();
            this.loans = new Loan();
        }

        private void addBook(Book book) {
            books.add(book);
        }

        private void addUser(Usero user) {
            users.add(user);
        }

        private void loanBook(Integer userId, String bookTitle) {
            Optional<Usero> user = users.stream().filter(u -> u.id.equals(userId)).findAny();
            Optional<Book> book = books.stream().filter(b -> b.title.equals(bookTitle)).findAny();
            if (user.isPresent() && book.isPresent()) loans.loanBook(user.get(), book.get());

        }

        private void returnBook(Integer userId, String bookTitle) {
            Optional<Usero> user = users.stream().filter(u -> u.id.equals(userId)).findAny();
            Optional<Book> book = books.stream().filter(b -> b.title.equals(bookTitle)).findAny();
            if (user.isPresent() && book.isPresent()) loans.returnBook(user.get(), book.get());
        }
    }

    static class Book {
        private String title;
        private String author;
        private Integer copies;

        public Book(String title, String author, Integer copies) {
            this.title = title;
            this.author = author;
            this.copies = copies;
        }
    }

    static class Usero {
        private String name;
        private Integer id;
        private String email;

        public Usero(String name, Integer id, String email) {
            this.name = name;
            this.id = id;
            this.email = email;
        }
    }

    static class Loan {
        private List<Map<String, Object>> loans;

        public Loan() {
            List<Loan> loans = new ArrayList<>();
        }

        private void loanBook(Usero user, Book book) {
            if (book.copies > 0) {
                book.copies--;
                Map<String, Object> loan = new HashMap<>();
                loan.put("userId", user.id);
                loan.put("bookTitle", book.title);
                loans.add(loan);
            }
        }

        private void returnBook(Usero user, Book book) {
            loans.stream()
                    .filter(loan -> loan.get("userId").equals(user.id) && loan.get("bookTitle").equals(book.title))
                    .findFirst()
                    .ifPresent(loan -> {
                        loans.remove(loan);
                        book.copies++;
                    });
        }
    }

}
