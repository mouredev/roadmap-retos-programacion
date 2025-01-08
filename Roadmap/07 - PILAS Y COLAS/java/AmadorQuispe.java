import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class AmadorQuispe {
    public static void main(String[] args) {
        example();
        stackNavigation();
        queuePrint();
    }

    public static void stackNavigation() {
        Stack<String> history = new Stack<>();
        Scanner sc = new Scanner(System.in);
        int pointerIndex = 1;
        while (true) {
            if (!history.isEmpty()) {
                System.out.println("-".repeat(15));
                history.forEach(h -> System.out.printf("%s | ", h));
                System.out.println("\n" + "-".repeat(16));
                System.out.print(
                        "Digite la 'pagina' o  'forward' para ir adelante, 'backward' para ir atras o 'exit' para cerrar :");
            } else {
                System.out.println("Digita la pagina a visitar");
            }
            String command = sc.next();
            switch (command) {
                case "forward":
                    if (pointerIndex == 1) {
                        System.out.println("No hay mas historial hacia adelante\n\n");
                        break;
                    }
                    pointerIndex--;
                    String pageName = history.get(history.size() - pointerIndex);
                    System.out.printf("Visualizando la pagina %s \n\n\n\n", pageName + pointerIndex);
                    break;
                case "backward":
                    if (pointerIndex == history.size()) {
                        System.out.println("No hay mas historial hacia atras \n\n");
                        break;
                    }
                    pointerIndex++;
                    pageName = history.get(history.size() - pointerIndex);
                    System.out.printf("Visualizando la pagina %s \n\n\n\n", pageName + pointerIndex);
                    break;
                case "exit":
                    System.out.println("Saliendo del navegador");
                    sc.close();
                    System.exit(0);
                default:
                    pointerIndex = 1;
                    System.out.printf("Visualizando la pagina %s \n\n\n\n", command);
                    history.push(command);
                    break;
            }

        }
    }

    public static void queuePrint() {
        Queue<String> jobPrints = new LinkedList<>();
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingresa el comando 'enqueue' para agregar archivo a cola de impresión");
        System.out.println("Ingresa el comando 'print' para empezar a imprimir un documento de la cola");
        System.out.println(
                "Ingresa el comando 'print-all' para empezar a imprimir todos los documentos de la cola");
        System.out.println("Ingresa el comando 'show' para mostrar todos los documentos de la cola");
        System.out.println("*".repeat(20));
        while (true) {
            System.out.print("Ingresa tu comando :");
            String command = sc.next();
            switch (command) {
                case "show":
                    System.out.println("-".repeat(30));
                    System.out.println(String.format("Documentos en cola (%d)", jobPrints.size()));
                    for (String string : jobPrints) {
                        System.out.println("-> " + string);
                    }
                    break;
                case "enqueue":
                    System.out.println("-".repeat(30));
                    System.out.print("Ingresa el nombre del documento a encolar :");
                    String docs = sc.next();
                    jobPrints.add(docs);
                    break;
                case "print":
                    System.out.println("-".repeat(30));
                    if (jobPrints.isEmpty()) {
                        System.out.println("No hay nada para imprimir");
                        break;
                    }
                    System.out.println("Imprimiendo -> " + jobPrints.poll());
                    try {
                        Thread.sleep(3000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    break;
                case "print-all":
                    System.out.println("-".repeat(30));
                    System.out.println("imprimiendo todo los de la cola");
                    while (!jobPrints.isEmpty()) {
                        System.out.println("Imprimiendo -> " + jobPrints.poll());
                        try {
                            Thread.sleep(3000);
                        } catch (InterruptedException e) {
                            e.printStackTrace(System.out);
                        }
                    }
                    break;
                case "exit":
                    System.out.println("Apagando impresora");
                    System.exit(0);
                    sc.close();
                    break;
                default:
                    System.out.println("!".repeat(30));
                    System.out.println("comando no reconocido");
                    break;
            }
        }

    }

    public static void example() {
        // Pilas con la clase Stack
        // Crear una pila de libros
        Stack<String> books = new Stack<>();
        // Agregando elementos a la pila
        books.push("Book 1");
        books.push("Book 2");
        books.push("Book 3");
        // Mostrando la pila
        System.out.println(books);
        // Ver el ultimo elemento
        System.out.println("ultimo elemento: " + books.peek());
        // Eliminar el ultimo elemento
        System.out.println("ultimo elemento eliminado: " + books.pop());
        // ver luego de eliminar
        System.out.println(books);
        // buscar elemento
        System.out.println("ubicación de Book 1 respecto a la parte superior: " + books.search("Book 1"));

        // Colas con la clase Dequeue
        Queue<String> colas = new ArrayDeque<>();
        colas.add("Amador");
        colas.add("Alex");
        colas.add("Pedro");

        System.out.println(colas);
        // Eliminar el primer elimento
        System.out.println(colas.poll());

        System.out.println(colas);
    }
}
