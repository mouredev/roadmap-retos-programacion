


import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class reto_7 {

    private static Scanner input = new Scanner(System.in);
    private static Stack<String> historial = new Stack<>();
    private static Stack<String> adelante = new Stack<>();
    private static Queue<String> palabra = new Queue<>();

    public static void main(String[] args) {
        // Prueba de la pila
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println("Pila después de insertar 1, 2, 3: " + stack);
        System.out.println("Elemento retirado de la pila: " + stack.pop());
        System.out.println("Pila después de retirar un elemento: " + stack);

        // Prueba de la cola
        Queue<Integer> queue = new Queue<>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        System.out.println("Cola después de insertar 1, 2, 3: " + queue);
        System.out.println("Elemento retirado de la cola: " + queue.dequeue());
        System.out.println("Cola después de retirar un elemento: " + queue + " \n");

        // Problema 1: Navegación de páginas
        historial.push("www.pagina1.com");
        historial.push("www.pagina2.com");
        historial.push("www.pagina3.com");

        while (true) {
            System.out.println("Ingresa a donde te quieres dirigir en la pagina");
            System.out.println("Escribe: adelante, para ir a otra pagina");
            System.out.println("Escribe: atras, para ir a la pagina anterior");
            System.out.println("Escribe: impresora, para ingresar al reto de la impresora");
            System.out.println("Escribe: salir, para salir");
            String valor = input.nextLine().toLowerCase();

            switch (valor) {
                case "adelante":
                    navegarAdelante();
                    break;
                case "atras":
                    navegarAtras();
                    break;
                case "impresora":
                while (true) {
                    
                    // problema 2: impresora
                    System.out.println("Ingresa la palabra 'imprimir' para imprimir el elemento en la consulo ");
                    System.out.println("Ingresa una parabra diferento y se guardara como un archivo para inprimir");
                    String palabras = input.nextLine().toLowerCase();

                    imprimir(palabras);
                }
                case "salir":
                    System.out.println("Saliendo del navegador.");
                    input.close();
                    return;
                default:
                    navegarNuevaPagina(valor);
                    break;
            }

        }

    }

    private static void imprimir(String palabras) {
        String calve = "imprimir".toLowerCase();

        if (palabras.equals(calve) ) {
        
            System.out.println("Imprimir: " + palabra.dequeue());

        } else {
            palabra.enqueue(palabras);
            System.out.println("Palabra agregada con exito: " + palabra);
        }
    }

    public static void navegarAdelante() {
        if (adelante.isEmpty()) {
            System.out.println("No hay página siguiente para mostrar.");
        } else {
            String pagina = adelante.pop();
            historial.push(pagina);
            System.out.println("Navegando adelante a: " + pagina);
        }
    }

    public static void navegarAtras() {
        if (historial.size() < 2) {
            System.out.println("No hay página anterior para mostrar.");
        } else {
            String paginaActual = historial.pop();
            adelante.push(paginaActual);
            String paginaAnterior = historial.peek();
            System.out.println("Navegando atrás a: " + paginaAnterior);
        }
    }

    public static void navegarNuevaPagina(String pagina) {
        historial.push(pagina);
        System.out.println("Navegando a nueva página: " + pagina);
        // Limpiamos la pila de adelante porque se considera una nueva navegación
        adelante = new Stack<>();
    }

    // Implementación de la pila (stack)
    static class Stack<T> {
        private List<T> elements = new ArrayList<>();

        public void push(T element) {
            elements.add(element);
        }

        public T pop() {
            if (elements.isEmpty()) {
                throw new RuntimeException("La pila está vacía");
            }
            return elements.remove(elements.size() - 1);
        }

        public T peek() {
            if (elements.isEmpty()) {
                throw new RuntimeException("La pila está vacía");
            }
            return elements.get(elements.size() - 1);
        }

        public int size() {
            return elements.size();
        }

        public boolean isEmpty() {
            return elements.isEmpty();
        }

        @Override
        public String toString() {
            return elements.toString();
        }
    }
}

// Implementación de la cola (queue) genérica
class Queue<T> {
    private List<T> elements = new LinkedList<>();

    public void enqueue(T element) {
        elements.add(element);
    }

    public T dequeue() {
        if (elements.isEmpty()) {
            throw new RuntimeException("La cola está vacía");
        }
        return elements.remove(0);
    }

    @Override
    public String toString() {
        return elements.toString();
    }
}
