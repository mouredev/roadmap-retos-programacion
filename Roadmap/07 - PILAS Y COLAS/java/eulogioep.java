import java.util.Scanner;

// Implementación de la Pila (Stack - LIFO)
class Stack {
    private String[] array;
    private int top;
    private int capacity;

    // Constructor
    public Stack(int size) {
        array = new String[size];
        capacity = size;
        top = -1;
    }

    // Método para añadir un elemento a la pila
    public void push(String x) {
        if (isFull()) {
            System.out.println("Error: Pila llena");
            return;
        }
        array[++top] = x;
    }

    // Método para quitar un elemento de la pila
    public String pop() {
        if (isEmpty()) {
            System.out.println("Error: Pila vacía");
            return null;
        }
        return array[top--];
    }

    // Método para verificar si la pila está vacía
    public boolean isEmpty() {
        return top == -1;
    }

    // Método para verificar si la pila está llena
    public boolean isFull() {
        return top == capacity - 1;
    }

    // Método para obtener el elemento en la cima de la pila sin quitarlo
    public String peek() {
        if (isEmpty()) {
            System.out.println("Error: Pila vacía");
            return null;
        }
        return array[top];
    }
}

// Implementación de la Cola (Queue - FIFO)
class Queue {
    private String[] array;
    private int front;
    private int rear;
    private int capacity;
    private int count;

    // Constructor
    public Queue(int size) {
        array = new String[size];
        capacity = size;
        front = 0;
        rear = -1;
        count = 0;
    }

    // Método para añadir un elemento a la cola
    public void enqueue(String x) {
        if (isFull()) {
            System.out.println("Error: Cola llena");
            return;
        }
        rear = (rear + 1) % capacity;
        array[rear] = x;
        count++;
    }

    // Método para quitar un elemento de la cola
    public String dequeue() {
        if (isEmpty()) {
            System.out.println("Error: Cola vacía");
            return null;
        }
        String x = array[front];
        front = (front + 1) % capacity;
        count--;
        return x;
    }

    // Método para verificar si la cola está vacía
    public boolean isEmpty() {
        return count == 0;
    }

    // Método para verificar si la cola está llena
    public boolean isFull() {
        return count == capacity;
    }

    // Método para obtener el primer elemento de la cola sin quitarlo
    public String peek() {
        if (isEmpty()) {
            System.out.println("Error: Cola vacía");
            return null;
        }
        return array[front];
    }
}

// Clase principal que contiene los programas de navegador web e impresora
public class eulogioep {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Programa de navegador web
        Stack backStack = new Stack(100);
        Stack forwardStack = new Stack(100);
        String currentPage = "";

        System.out.println("Simulador de navegador web (escribe 'salir' para terminar):");
        while (true) {
            System.out.print("Ingresa una acción o nombre de página web: ");
            String input = scanner.nextLine().trim().toLowerCase();
            
            if (input.equals("salir")) {
                break;
            } else if (input.equals("atrás")) {
                if (!backStack.isEmpty()) {
                    forwardStack.push(currentPage);
                    currentPage = backStack.pop();
                    System.out.println("Página actual: " + currentPage);
                } else {
                    System.out.println("No hay páginas anteriores");
                }
            } else if (input.equals("adelante")) {
                if (!forwardStack.isEmpty()) {
                    backStack.push(currentPage);
                    currentPage = forwardStack.pop();
                    System.out.println("Página actual: " + currentPage);
                } else {
                    System.out.println("No hay páginas siguientes");
                }
            } else {
                if (!currentPage.isEmpty()) {
                    backStack.push(currentPage);
                }
                forwardStack = new Stack(100);  // Limpia la pila de adelante
                currentPage = input;
                System.out.println("Página actual: " + currentPage);
            }
        }

        // Programa de impresora compartida
        Queue printQueue = new Queue(100);

        System.out.println("\nSimulador de impresora compartida (escribe 'salir' para terminar):");
        while (true) {
            System.out.print("Ingresa un nombre de documento o 'imprimir': ");
            String input = scanner.nextLine().trim().toLowerCase();
            
            if (input.equals("salir")) {
                break;
            } else if (input.equals("imprimir")) {
                String document = printQueue.dequeue();
                if (document != null) {
                    System.out.println("Imprimiendo: " + document);
                }
            } else {
                printQueue.enqueue(input);
                System.out.println("Documento añadido a la cola: " + input);
            }
        }

        scanner.close();
    }
}