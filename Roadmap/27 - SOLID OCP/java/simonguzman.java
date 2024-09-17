
import java.util.ArrayList;
import java.util.List;

public class simonguzman {
    public static void main(String[] args) {
        libraryViolationOcp();
    }

    /*************************** Ejemplo sin ocp(Incorrecto) ***************************/
    static void libraryViolationOcp(){
        Library library = new Library();
        library.registerBook("El quijote");
        library.registerUser("Juan Perez");
        library.loanBook("El quijote", "Juan Perez");
        library.returnBook("El quijote", "Juan Perez");
    }

    static class Library{
        private List<String> books = new ArrayList<>();
        private List<String> users = new ArrayList<>();

        public void registerBook(String book){
            books.add(book);
            System.out.println("Libro registrado: " + book);
        }

        public void registerUser(String user){
            users.add(user);
            System.out.println("Usuario registrado: "+user);
        }

        public void loanBook(String book, String user){
            if(books.contains(book)){
                System.out.println("Libro: " + book + " prestado a " + user);
            }else{
                System.out.println("El libro no esta disponible");
            }
        }

        public void returnBook(String book, String user){
            System.out.println("Libro: " + book + " devuelto por " + user);
        }
    }
}
