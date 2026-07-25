
import java.util.ArrayList;
import java.util.List;

public class simonguzman {
    public static void main(String[] args) {
        libraryViolationOcp();
        libraryFollowOCP();
        calculatorTest();
        calculatorOCPTest();
    }
    /*************************** Ejercicio adicional con ocp(Correcto) ***************************/
    static void calculatorOCPTest(){
        CalculatorOCP calculator = new CalculatorOCP();

        double resultAdd = calculator.Calculate(new Addition(), 10, 5);
        System.out.println("Suma: " + resultAdd);

        double resultSub = calculator.Calculate(new Subtraction(), 10, 5);
        System.out.println("Resta: " + resultSub);

        double resultMul = calculator.Calculate(new Multiplication(), 10, 5);
        System.out.println("Multiplicación: " + resultMul);

        double resultDiv = calculator.Calculate(new Division(), 10, 5);
        System.out.println("División: " + resultDiv);

        double resultPow = calculator.Calculate(new Power(), 2, 3);
        System.out.println("Potencia: " + resultPow);
    }
    interface Operation{
        double function(double num1, double num2);
    }

    static class Addition implements Operation{
        @Override
        public double function(double num1, double num2) {
            return num1 + num2; 
        }
    }

    static class Subtraction implements Operation{
        @Override
        public double function(double num1, double num2) {
            return num1 - num2;
        }  
    }

    static class Multiplication implements Operation{
        @Override
        public double function(double num1, double num2) {
            return num1 * num2;
        }  
    }

    static class Division implements Operation{
        @Override
        public double function(double num1, double num2) {
            return num1 /  num2;
        }      
    }

    static class Power implements Operation{
        @Override
        public double function(double num1, double num2) {
            return Math.pow(num1, num2);
        }
    }

    static class CalculatorOCP{
        public double Calculate(Operation operation, double num1, double num2){
            return operation.function(num1, num2);
        }
    }


    /*************************** Ejercicio adicional sin ocp(Incorrecto) ***************************/
    static void calculatorTest(){
        Calculator calculator = new Calculator();

        double resultAdd = calculator.calculate("sum", 10, 5);
        System.out.println("Suma: " + resultAdd);

        double resultSub = calculator.calculate("substract", 10, 5);
        System.out.println("Resta: " + resultSub);

        double resultMul = calculator.calculate("multiply", 10, 5);
        System.out.println("Multiplicación: " + resultMul);

        double resultDiv = calculator.calculate("divide", 10, 5);
        System.out.println("División: " + resultDiv);

        try {
            double resultPow = calculator.calculate("power", 2, 3);
            System.out.println("Potencia: " + resultPow);
        } catch (UnsupportedOperationException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    static class Calculator{
        public double calculate(String operation, double num1, double num2){
            switch (operation) {
                case "sum": return  num1 + num2; 
                case "substract": return  num1 - num2; 
                case "multiply": return  num1 * num2; 
                case "divide": return  num1 / num2; 
                default:
                    throw new UnsupportedOperationException("Operacion no soportada");
            }
        }
    }

    /*************************** Ejemplo con ocp(Correcto) ***************************/
    static void libraryFollowOCP(){
        List<String> books = new ArrayList<>();
        List<String> users = new ArrayList<>();
        LibraryOcp library = new LibraryOcp();

        LibraryOperation registerBook = new RegisterBookOperation("El Quijote", books);
        library.performOperation(registerBook);

        LibraryOperation registerUser = new RegisterUserOperation("Juan Perez", users);
        library.performOperation(registerUser);

        LibraryOperation loanBook = new LoanBookOperation("El Quijote", "Juan Perez", books);
        library.performOperation(loanBook);

        LibraryOperation renewLoan = new RenewLoanOperation("El Quijote", "Juan Perez");
        library.performOperation(renewLoan);
    }

    interface LibraryOperation{
        void execute();
    }

    static class RegisterBookOperation implements LibraryOperation{
        private String book;
        private List<String> books;

        public RegisterBookOperation(){
            
        }

        public RegisterBookOperation(String book, List<String> books){
            this.book = book;
            this.books = books;
        }

        @Override
        public void execute() {
            books.add(book);
            System.out.println("Libro registrado: " + book);
        }
    }

    static class RegisterUserOperation implements LibraryOperation{
        private String user;
        private List<String> users;

        public RegisterUserOperation(){

        }

        public RegisterUserOperation(String user, List<String> users){
            this.user = user;
            this.users = users;
        }
        @Override
        public void execute() {
            users.add(user);
            System.out.println("Usuario registrado: "+user);
        }
    }

    static class LoanBookOperation implements LibraryOperation{
        private String book;
        private String user;
        private List<String> books;

        public LoanBookOperation(){

        }

        public LoanBookOperation(String book, String user, List<String> books){
            this.book = book;
            this.user = user;
            this.books = books;
        }

        @Override
        public void execute() {
            if(books.contains(book)){
                System.out.println("Libro: " + book + " usuario " + user);
            }else{
                System.out.println("El libro no esta disponible.");
            }
        }
        
    }

    static class RenewLoanOperation implements LibraryOperation{
        private String book;
        private String user;

        public RenewLoanOperation(){

        }

        public RenewLoanOperation(String book, String user){
            this.book = book;
            this.user = user;
        }

        @Override
        public void execute() {
            System.out.println("El prestamo del libro " + book + " a sido renovado por " + user);
        }
    }

    static class LibraryOcp{
        public void performOperation(LibraryOperation operation){
            operation.execute();
        }
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
