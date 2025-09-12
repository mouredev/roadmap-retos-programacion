import java.util.Stack;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class danhingar {

    public static void main(String[] args) {
        // Declarar una pila
        Stack<String> books = new Stack<>();

        // Añadir elementos
        books.addElement("Libro2");
        books.add("Libro3");
        books.addFirst("Libro1");
        books.push("Libro4");
        books.addLast("Libro5");

        System.out.println(books);

        // Recuperar último elemento introducido y lo elimina
        String lastBook = books.pop();

        System.out.println(lastBook);
        System.out.println(books);

        // Recuperar el último elemento sin eliminarlo
        String lastBook2 = books.peek();
        System.out.println(lastBook2);
        System.out.println(books);

        // Buscar elemento
        int index = books.search("Libro3");
        System.out.println(books.get(index));

        // Invertir orden
        System.out.println(books.reversed());
        System.out.println(books.reversed().getLast());
        System.out.println(books.reversed().getFirst());

        // Colas
        Queue<Integer> numbers = new ArrayDeque<>();

        // Añadir elementos
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);

        System.out.println(numbers);

        // Recupera el primer elemento añadido y lo elimina
        Integer number = numbers.poll();
        System.out.println(number);
        System.out.println(numbers);

        // Recupera el primer elemento añadido sin eliminarlo
        Integer number2 = numbers.peek();
        System.out.println(number2);
        System.out.println(numbers);

        // Igual que peek pero lanza una excepción si está vacía
        Integer number3 = numbers.element();
        System.out.println(number3);
        System.out.println(numbers);

        // browser();
        printer();
    }

    private static Stack<String> pages = new Stack<>();
    private static int pointer = -1;

    // EXTRA
    private static void browser() {
        while (Boolean.TRUE) {
            System.out.println("Añade una url o selecciona la opción adelantes/atras/salir");
            Scanner scanner = new Scanner(System.in);
            String input = scanner.nextLine();
            switch (input) {
                case "atras":
                    if (pages.size() > 1 && pointer > 0) {
                        System.out.println("Has navegado a la web: " + pages.get(pointer - 1));
                        pointer--;
                    } else {
                        System.out.println("Estás en la página de inicio");
                    }
                    break;
                case "adelante":
                    if (pages.size() > 1 && pointer < pages.size() - 1) {
                        System.out.println("Has navegado a la web: " + pages.get(pointer + 1));
                        pointer++;
                    } else {
                        System.out.println("No puedes avanzar más");
                    }
                    break;

                case "salir":
                    scanner.close();
                    System.exit(0);
                default:
                    pages.push(input);
                    pointer++;
                    System.out.println("Has navegado a la web: " + pages.peek());
                    break;
            }
        }

    }

    private static Queue<String> documents = new ArrayDeque<>();

    private static void printer() {
        while (Boolean.TRUE) {
            System.out.println("Añade un docmento o selecciona la opción imprimir/salir");
            Scanner scanner = new Scanner(System.in);
            String input = scanner.nextLine();

            switch (input) {
                case "imprimir":
                    if (documents.size()>0) {
                        System.out.println(documents.poll());
                    }
                    System.out.println("No hay documentos para imprimir");
                    break;
                case "salir":
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    documents.add(input);
                    break;
            }

            System.out.println("Cola de impresión: " + documents);
        }

    }
}
