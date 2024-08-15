import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

/** #07 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        // PILAS
        System.out.println("PILAS - STACKS - LIFO");
        Stack__ stack = new Stack__();
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Contenido de la Pila: " + stack);
        System.out.println("Elemento de parte superior de la Pila: " + stack.peek());
        System.out.println("Elemento eliminado de la Pila: " + stack.pop());
        System.out.println("Contenido de la Pila: " + stack);

        // COLAS
        System.out.println("COLAS - QUEUE - FIFO");
        Queue__ queue = new Queue__();
        queue.enqueue(40);
        queue.enqueue(50);
        queue.enqueue(60);
        System.out.println("Contenido de la Cola: " + queue);
        System.out.println("Primer elemento de Cola: " + queue.peek());
        System.out.println("Elemento eliminado de la Cola: " + queue.dequeue());
        System.out.println("Contenido de la Cola: " + queue);
        //---EXTRA---
        System.out.println("EXTRA - PILAS");
        SitioWeb();
        System.out.println("EXTRA - COLAS");
        Impresora();
    }

    //---EJERCIÓ---
    // STACKS - LIFO
    static class Stack__{
        private ArrayList<Integer> stack;

        public Stack__(){
            stack = new ArrayList<>();
        }

        // Se añade un elemento a la pila
        public void push(int value){
            stack.add(value);
        }

        public int pop(){
            if (stack.isEmpty()) {
                throw new IllegalAccessError("La pila esta vacía");
            }
            return stack.remove(stack.size() - 1);
        }

        public int peek(){
            if (stack.isEmpty()) {
                throw new IllegalAccessError("La pila esta vacía");
            }
            return stack.get(stack.size() - 1);
        }

        @Override
        public String toString() {
            return stack.toString();
        }
    }


    // QUEUE - FIFO
    static class Queue__{
        private LinkedList<Integer> queue;

        public Queue__(){
            queue = new LinkedList<>();
        }

        // Se añade un elemento a la pila
        public void enqueue(int value){
            queue.addLast(value);
        }

        public int dequeue(){
            if (queue.isEmpty()) {
                throw new IllegalAccessError("La cola esta vacía");
            }
            return queue.removeFirst();
        }

        public int peek(){
            if (queue.isEmpty()) {
                throw new IllegalAccessError("La pila esta vacía");
            }
            return queue.getFirst();
        }

        @Override
        public String toString() {
            return queue.toString();
        }
    }



    /**-----DIFICULTAD EXTRA-----*/

    // PILAS
    // Programa - Sitio Web
    public static void SitioWeb(){
        Browser browser = new Browser();
        Scanner scanner = new Scanner(System.in);
        String input;
        
        System.out.println("Simulación de Navegación web. Ingresa nombre de paginas web, adelante o atrás");
        while(true){
            System.out.print("Ingrese un comando:\n");
            input = scanner.nextLine();

            if (input.equalsIgnoreCase("adelante")){
                browser.forward();
            } else if (input.equalsIgnoreCase("atras")){
                browser.back();
            } else if (input.equalsIgnoreCase("salir")){
                break;
            } else {
                browser.visit(input);
            }

            System.out.println("Pagina actual: " + browser.current());
        }
        scanner.close();
    }

    static class Browser{
        private Stack history;
        private Stack forwardStack;
        private String currentPage;

        public Browser(){
            history = new Stack();
            forwardStack = new Stack();
            currentPage = "home";
        }

        public void visit(String url){
            if(currentPage != null){
                history.push(currentPage);
            }
            currentPage = url;
            forwardStack = new Stack();
        }

        public void back(){
            if (!history.isEmpty()){
                forwardStack.push(currentPage);
                currentPage = history.pop();
            } else {
                System.out.println("No hay paginas anteriores");
            }
        }

        public void forward(){
            if (!forwardStack.isEmpty()){
                history.push(currentPage);
                currentPage = forwardStack.pop();
            } else {
                System.out.println("No hay paginas siguientes");
            }
        }

        public String current(){
            return currentPage;
        }
    }

    static class Stack{
        private ArrayList<String> stack;

        public Stack() {
            stack = new ArrayList<>();
        }

        public void push(String value) {
            stack.add(value);
        }

        public String pop() {
            if (isEmpty()) {
                throw new IllegalStateException("La pila está vacía");
            }
            return stack.remove(stack.size() - 1);
        }

        public boolean isEmpty() {
            return stack.isEmpty();
        }

        @Override
        public String toString() {
            return stack.toString();
        }
    }


    // COLAS
    // Programa - Impresora
    public static void Impresora(){
        Printer printer = new Printer();
        Scanner scanner = new Scanner(System.in);
        String input;
        
        System.out.println("Simulación Compartida. Ingrese nombres de documentos o imprimir para imprimir");
        while(true){
            System.out.print("Ingrese un comando:\n");
            input = scanner.nextLine();

            if (input.equalsIgnoreCase("imprimir")){
                printer.print();
            } else if (input.equalsIgnoreCase("salir")){
                break;
            } else {
                printer.addDocument(input);
            }
        }
        scanner.close();
    }

    static class Printer{
        private Queue printerQueue;

        public Printer() {
            printerQueue = new Queue();
        }

        public void addDocument(String document){
            printerQueue.enqueue(document);
            System.out.println("Documento agregado a la cola: " + document);
        }

        public void print(){
            if(printerQueue.isEmpty()){
                System.out.println("No hay documentos para imprimir");
            } else {
                String document = printerQueue.dequeue();
                System.out.println("Imprimiendo documento: " + document);
            }
        }
    }

    static class Queue {
        private LinkedList<String> queue;

        public Queue() {
            queue = new LinkedList<>();
        }

        public void enqueue(String value) {
            queue.addLast(value);
        }

        public String dequeue() {
            if (isEmpty()) {
                throw new IllegalStateException("La cola está vacía");
            }
            return queue.removeFirst();
        }

        public boolean isEmpty() {
            return queue.isEmpty();
        }

        @Override
        public String toString() {
            return queue.toString();
        }
    }

    /**-----DIFICULTAD EXTRA-----*/
}