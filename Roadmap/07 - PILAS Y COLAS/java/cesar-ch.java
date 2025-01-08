import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        // pila
        List<Integer> pila = new ArrayList<>();

        // push
        pila.add(1);
        pila.add(2);
        pila.add(3);

        // pop
        pila.remove(pila.size() - 1);
        System.out.println(pila);

        // cola
        List<Integer> cola = new ArrayList<>();

        // enqueue
        cola.add(1);
        cola.add(2);
        cola.add(3);

        // dequeue
        cola.remove(0);
        System.out.println(cola);

        // DIFICULTAD EXTRA
        webNavigation();
        sharedPrinted();
    }

    public static void webNavigation() {
        List<String> stack = new ArrayList<>();

        while (true) {
            System.out.print("Añade una url o interactúa con palabras adelante/atras/salir: ");
            String action = scanner.nextLine();

            if (action.equals("salir")) {
                System.out.println("Saliendo del navegador web.");
                break;
            } else if (action.equals("adelante")) {
                continue;
            } else if (action.equals("atras")) {
                if (stack.size() > 0) {
                    stack.remove(stack.size() - 1);
                }
            } else {
                stack.add(action);
            }

            if (!stack.isEmpty()) {
                System.out.println("Has navegado a la web: " + stack.get(stack.size() - 1));
            } else {
                System.out.println("Estás en la página de inicio.");
            }
        }
    }

    public static void sharedPrinted() {
        List<String> queue = new ArrayList<>();

        while (true) {
            System.out.print("Añade un documento o selecciona imprimir/salir: ");
            String action = scanner.nextLine();

            if (action.equals("salir")) {
                break;
            } else if (action.equals("imprimir")) {
                if (!queue.isEmpty()) {
                    System.out.println("Imprimiendo: " + queue.remove(0));
                }
            } else {
                queue.add(action);
            }
            System.out.println("Cola de impresión: " + queue);
        }
    }
}
