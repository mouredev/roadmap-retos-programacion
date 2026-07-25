import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        //Forma incorrecta
        IncorrectStudent student1 = new IncorrectStudent(678, "Pepe");
        student1.addScore(8);

        //Forma correcta
        CorrectStudent student2 = new CorrectStudent(551, "Rocío");
        Exam exam1 = new Exam();
        exam1.addScore(student2, 8.25);

        //Si por ejemplo hay algún problema con un exámen y hay que subir la nota a una
        //o varios estudiantes, es mucho mas claro y fácil de la forma correcta que la incorrecta
    }

    public static class IncorrectStudent{
        private int id;
        private String name;
        private List<Double> scoreList;

        public IncorrectStudent(int id, String name) {
            this.id = id;
            this.name = name;
            scoreList = new ArrayList<>();
        }

        public void addScore(double newScore){
            scoreList.add(newScore);
        }
    }

    public static class CorrectStudent{
        private int id;
        private String name;

        public CorrectStudent(int id, String name) {
            this.id = id;
            this.name = name;
        }
    }

    public static class Exam{
        private Map<CorrectStudent, Double> scores;

        public Exam(){
            scores = new HashMap<>();
        }

        public void addScore(CorrectStudent student, Double score){
            scores.put(student, score);
        }
    }

    //Reto
    //Si queremos guardar varios datos datos de libros y usuario, debemos crear una
    //clase para ambos, aunque queramos hacerlo mal aposta.

    public static class IncorrectLibrary {

        private List<Book> bookList;
        private List<User> userList;
        private List<Loan> loanList;

        public IncorrectLibrary(){
            bookList = new ArrayList<>();
            userList = new ArrayList<>();
            loanList = new ArrayList<>();
        }

        public void registerBook(String title, String author, int nCopies){
            //Código para registrar un libro
        }

        public void registerUser(Integer id, String name, String email){
            //Código para registrar un usuario
        }

        public void lendBook(Integer idUser, String bookName, boolean returnBook){
            //Código para prestar un libro a un usuario
        }

        public static void returnBook(Integer idUser, String bookName){
            //Código para prestar un libro a un usuario
        }
    }

    public static class CorrectLibrary{
        private List<Book> bookList;
        private List<User> userList;
        private List<Loan> loanList;

        public CorrectLibrary() {
            bookList = new ArrayList<>();
            userList = new ArrayList<>();
            loanList = new ArrayList<>();
        }

        public void lendBook(Integer idUser, String bookName){
            //Código para prestar un libro a un usuario
        }

        public void returnBook(Integer idUser, String bookName){
            //Código para que un usuario devuelva un libro
        }

        public boolean registerUser(Integer id, String name, String email){
            return userList.add(Register.registerUser(id, name, email));
        }

        public boolean registerBook(String title, String author, int nCopies){
            return bookList.add(Register.registerBook(title, author, nCopies));
        }
    }

    public static class Register{

        public static Book registerBook(String title, String author, int nCopies){
            //Código para registrar un libro
            return null;
        }

        public static User registerUser(Integer id, String name, String email){
            //Código para registrar un usuario
            return null;
        }
    }

    public static class Book{
        private String title;
        private String author;
        private Integer nCopies;

        public Book(String title, String author, Integer nCopies) {
            this.title = title;
            this.author = author;
            this.nCopies = nCopies;
        }

        public String getTitle() {
            return title;
        }

        public String getAuthor() {
            return author;
        }

        public Integer getnCopies() {
            return nCopies;
        }
    }

    public static class User{
        private int id;
        private String name;
        private String email;

        public User(int id, String name, String email) {
            this.id = id;
            this.name = name;
            this.email = email;
        }

        public int getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public String getEmail() {
            return email;
        }
    }

    public static class Loan{
        private User user;
        private Book book;

        public Loan(User user, Book book) {
            this.user = user;
            this.book = book;
        }

        public User getUser() {
            return user;
        }

        public Book getBook() {
            return book;
        }
    }
}
