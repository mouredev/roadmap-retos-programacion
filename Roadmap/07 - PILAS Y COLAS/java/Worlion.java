import java.util.Scanner;
import java.util.LinkedList;
import java.util.List;

/*
 * EJERCICIO: Colas y Pilas
 */

class Stack<T> {
    private List<T> stack = new LinkedList<T>();

    public T pop() {
        if(this.stack.isEmpty()) {
            //throw new Exception("Pila vacia!");
            System.err.println("Pila vacia!");
            return null;
        }
        T element = stack.getLast();
        stack.removeLast();
        return element;
    }

    public void push(T element) {
        this.stack.add(element);
    }

    public void printStack() {
        System.out.println("Stack content:" + stack);
    }

    public int size() {
        return stack.size();
    }

    public boolean isEmpty() {
        return stack.isEmpty();
    }

    public T top(){
        return stack.getLast();
    }

    public void clear() {
        stack.clear();
    }
}

class Queue<T> {
    private List<T> queue = new LinkedList<T>();

    public T get() {
        if(this.queue.isEmpty()) {
            //throw new Exception("Pila vacia!");
            System.err.println("Cola vacia!");
            return null;
        }
        T element = queue.getFirst();
        queue.remove(0);
        return element;
    }
    
    public void put(T element) {
        this.queue.add(element);
    }

    public void printQueue() {
        System.out.println("Queue content:" + queue);
    }
}

public class Worlion {

    private static final String GREEN = "\u001B[32m";
    private static final String RED = "\u001B[31m";
    private static final String RED_BACKGROUND = "\u001B[41m";
    private static final String ANSI_RESET = "\u001B[0m";
    
    public static void clearScreen() {
        System.out.print("\033\143");
    }

    Scanner scanner = new Scanner(System.in);

    Stack<String> history;
    Stack<String> backHistory;

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run() {
        playWithStack();
        playWithQueue();

        extra();
    }

    private void playWithStack(){
        System.out.println("\nJugando con la pila...");
        Stack<Integer> stack = new Stack<Integer>();
        System.out.println("Añado 4 valores:");
        stack.push(3);
        stack.push(65);
        stack.push(1);
        stack.push(99);
        stack.printStack();

        System.out.println("elimino el primero: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();

        System.out.println("elimino otro: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();

        System.out.println("elimino otro: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();

        System.out.println("elimino otro: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();
        
        System.out.println("elimino otro: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();

    }

    private void playWithQueue(){
        System.out.println("\nJugando con la cola...");
        Queue<String> queue = new Queue<String>();

        System.out.println("Añado 4 valores");
        queue.put("a");
        queue.put("b");
        queue.put("c");
        queue.put("d");
                
        queue.printQueue();
        
        System.out.println("elimino el primero: ");
        System.out.println("get: {" + queue.get() + "}");
        queue.printQueue();
        System.out.println("elimino otro: ");
        System.out.println("get: {" + queue.get() + "}");
        queue.printQueue();
        System.out.println("get: {" + queue.get() + "}");
        queue.printQueue();
        System.out.println("get: {" + queue.get() + "}");
        queue.printQueue();
        System.out.println("get: {" + queue.get() + "}");
    }


    private void extra() {
        /*
        * DIFICULTAD EXTRA (opcional):
        * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
        *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
        *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
        *   interpretan como nombres de documentos.
        */

        System.out.println(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");

        history = new Stack<String>();
        backHistory = new Stack<String>();
        
        history.push("Home Page");
        
        String option = null;
        do{
            option = showMenu();
            processOption(option.toLowerCase());

        } while (!"0".equals(option));
    }

    private String showMenu() {

        System.out.println("\n\n WEB BROWSER\n");
        System.out.println("\n - curren page: "+GREEN+history.top()+ANSI_RESET);
        System.out.println("\n Select an option or type the url you want to navigate to: \n");

        System.out.println("\t 1.- "+option1());
        System.out.println("\t 2.- "+option2());
        System.out.println("\t 3.- Show history");
        System.out.println(RED_BACKGROUND+"\t 0.- Exit"+ANSI_RESET);
        System.out.print("\n Choose an option (or type url):");

        return scanner.nextLine();
    }

    private void processOption(String option){
        clearScreen();
        switch (option) {
            case "1":
            case "back":
            case "go back":
                if(history.size()==1) {
                    System.out.println("\n"+RED+"Invalid option:"+ ANSI_RESET+" the history is empty (you are in the home page)");
                }
                else {
                    System.out.println("going back...");
                    backHistory.push(history.pop());
                }
                
                break;

            case "2":
            case "ahead":
            case "go ahead":
                if(backHistory.isEmpty()) {
                    System.out.println("\n"+RED+"Invalid option:"+ ANSI_RESET+" the forward history is empty");
                }
                else {
                    System.out.println("going forward...");
                    history.push(backHistory.pop());
                }
                break;

            case "3":
            case "show":
            case "history":
            case "show history":
                System.out.println("\nShowing history:");
                System.out.print(" - Back history: ");
                history.printStack();
                System.out.print(" - Forward history: ");
                backHistory.printStack();
                break;

            case "0":
            case "exit":
                System.out.println("\nSee you soon...");
                break;

            default:
                System.out.println("Browsing to '" + option + "'...");
                history.push(option);
                backHistory.clear();
                break;
        }
    }

    private String option1(){
        String msg = "Go back";
        if(history.size()==1){
            return RED + msg + ANSI_RESET;
        }
        return GREEN + msg + ANSI_RESET;
    }

    private String option2(){
        String msg = "Go ahead";
        if(backHistory.size()==0){
            return RED + msg + ANSI_RESET;
        }
        return GREEN + msg + ANSI_RESET;
    }

    
}
