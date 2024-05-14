import java.util.Scanner;
import java.util.LinkedList;
import java.util.List;

/*
 * EJERCICIO: Colas y Pilas
 */

class Stack<T> {
    private List<T> stack = new LinkedList<T>();

    public T pop() {
        if(stack.isEmpty()) {
            //throw new Exception("Pila vacia!");
            System.err.println("Pila vacia!");
            return null;
        }
        T element = stack.getLast();
        stack.removeLast();
        return element;
    }

    public void push(T element) {
        stack.add(element);
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
        if(queue.isEmpty()) {
            //throw new Exception("Pila vacia!");
            System.err.println("Cola vacia!");
            return null;
        }
        T element = queue.getFirst();
        queue.remove(0);
        return element;
    }
    
    public void put(T element) {
        queue.add(element);
    }

    public void printQueue() {
        System.out.println("Queue content:" + queue);
    }

    public int size(){
        return queue.size();
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }
}

class WebBrowser {

    private Stack<String> history = new Stack<String>();
    private Stack<String> backHistory = new Stack<String>();

    public void run() {

        history.push("Home Page");
        
        String option = null;
        do{
            option = showMenu();
            processOption(option.toLowerCase());

        } while (!"0".equals(option));
    }

    private String showMenu() {

        System.out.println("\n\n WEB BROWSER\n");
        System.out.println("\n - curren page: "+ Worlion.GREEN+history.top()+ Worlion.ANSI_RESET);
        System.out.println("\n Select an option or type the url you want to navigate to: \n");

        System.out.println("\t 1.- "+option1());
        System.out.println("\t 2.- "+option2());
        System.out.println("\t 3.- Show history");
        System.out.println(Worlion.RED_BACKGROUND+"\t 0.- Exit"+ Worlion.ANSI_RESET);
        System.out.print("\n Choose an option (or type url):");

        return Worlion.scanner.nextLine();
    }

    private void processOption(String option){
        Worlion.clearScreen();
        switch (option) {
            case "1":
            case "back":
            case "go back":
                if(history.size()==1) {
                    System.out.println("\n"+Worlion.RED+"Invalid option:"+ Worlion.ANSI_RESET+" the history is empty (you are in the home page)");
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
                    System.out.println("\n"+Worlion.RED+"Invalid option:"+ Worlion.ANSI_RESET+" the forward history is empty");
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
            return Worlion.RED + msg + Worlion.ANSI_RESET;
        }
        return Worlion.GREEN + msg + Worlion.ANSI_RESET;
    }

    private String option2(){
        String msg = "Go ahead";
        if(backHistory.size()==0){
            return Worlion.RED + msg + Worlion.ANSI_RESET;
        }
        return Worlion.GREEN + msg + Worlion.ANSI_RESET;
    }

    
}

class Printer {

    private Queue<String> impresora = new Queue<String>();

    public void run() {
            /* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
        *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
        *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
        *   interpretan como nombres de documentos.
        */
        String option  ="";
        do {
            option = showMenu();
        } while(! "0".equals(processOption(option)) );

    }

    private String showMenu(){

        System.out.println("  --- COLA DE IMPRESIÓN --- ");
        impresora.printQueue();
        
        System.out.println("\nOpciones: ");
        System.out.println(Worlion.GREEN + "\t - Escriba el nombre del documento" + Worlion.ANSI_RESET);
        String msg = "\t - Escriba 'Imprimir' o '1' para comenzar la impresión'";
        if(impresora.size() == 0) {
            System.out.println( Worlion.RED+ msg + Worlion.ANSI_RESET );
        } else {
            System.out.println( Worlion.GREEN+ msg + Worlion.ANSI_RESET );
        }
        System.out.println( Worlion.RED + "\t - Escriba 'Salir' o '0' para salir de la aplicación'"+ Worlion.ANSI_RESET);

        System.out.print("\n\t > ");
        return Worlion.scanner.nextLine();
    }

    private String processOption(String option) {
        if ("0".equals(option) || "salir".equalsIgnoreCase(option)){
            return "0";
        }
        if ("1".equals(option) || "imprimir".equalsIgnoreCase(option)) {
            print();
        } else{
            impresora.put(option);
        }
        return "1";
    }

    private void print() {
        if(impresora.isEmpty()){
            System.out.println(Worlion.RED + "WARNING: "+Worlion.ANSI_RESET + "Cola de impresión vacía, nada que imprimir");
        }
        else {
            System.out.println("Imprimiendo '"+impresora.get()+"'...");
        }
    }
}

public class Worlion {

    public static final String GREEN = "\u001B[32m";
    public static final String RED = "\u001B[31m";
    public static final String RED_BACKGROUND = "\u001B[41m";
    public static final String ANSI_RESET = "\u001B[0m";
    
    public static void clearScreen() {
        System.out.print("\033\143");
    }

    public static Scanner scanner = new Scanner(System.in);



    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run() {
        playWithStack();
        playWithQueue();
        /*
        * DIFICULTAD EXTRA (opcional):
        */
        System.out.println(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");

        new WebBrowser().run();

        new Printer().run();
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


}
