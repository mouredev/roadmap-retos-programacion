import java.util.*;

public class Main {

    public static void main(String[] args) {

        ejemploNavegadorPila();
        ejemploImpresoraCola();

    }

    /**
     * Tanto Stack como Deque (cuando se utiliza como pila) siguen siendo estructuras LIFO.
     * Es decir, independientemente de cómo se impriman,
     * el último elemento que se insertó será el primero en ser eliminado.
     */
    static void estructurasLIFO() {

        // Estructura LIFO (Last In First Out)
        Stack<Integer> pila = new Stack<>();

        // Agregar elementos
        pila.push(1);
        pila.push(2);
        pila.push(3);

        // Remover el último elemento
        pila.pop();

        System.out.println("Contenido de la pila: " + pila);
        System.out.println("El último elemento es: " + pila.peek());
        System.out.println("El elemento 2 está en la posición: " + pila.search(2));
        System.out.println("La pila está vacía: " + pila.isEmpty());

        // Una estructura LIFO más completa y consistente es la clase Deque
        Deque<Integer> pila2 = new ArrayDeque<>();

        // Agregar elementos
        pila2.push(1);
        pila2.push(2);
        pila2.push(3);

        // Remover el último elemento
        pila2.pop();

        System.out.println("Contenido de la pila2 (se muestra en orden inverso): " + pila2);
        System.out.println("El último elemento es: " + pila2.peek());
        System.out.println("La pila contiene el elemento 2: " + pila2.contains(2));
        System.out.println("La pila2 está vacía: " + pila2.isEmpty());
        System.out.println("Obtener pero no remover el primer elemento: " + pila2.peekFirst());
        System.out.println("Obtener pero no remover el último elemento: " + pila2.peekLast());

    }

    static void estructurasFIFO() {

        // Estructuras FIFO (First In First Out)
        Queue<Integer> cola = new LinkedList<>();

        // Agregar elementos
        cola.add(1);
        cola.add(2);
        cola.add(3);

        // Remover el primer elemento agregado
        int primero = cola.remove();

        System.out.println("El primer elemento removido es: " + primero);
        System.out.println("Contenido de la cola después de remover: " + cola);

        /**
         * Deque (Double Ended Queue)
         * en Java también puede funcionar como una estructura FIFO (First In First Out).
         * Esto se debe a que permite la inserción y eliminación de elementos desde ambos extremos.
         * Cuando se utilizan los métodos addLast (o offer) para agregar elementos
         * y removeFirst (o poll) para eliminarlos, actúa como una cola FIFO.
         */

        Deque<Integer> dequeCola = new ArrayDeque<>();

        // Agregar elementos
        dequeCola.addLast(1);
        dequeCola.addLast(2);
        dequeCola.addLast(3);

        // Remover el primer elemento agregado
        int primerElemento = dequeCola.removeFirst();

        System.out.println("El primer elemento removido es: " + primerElemento);
        System.out.println("Contenido de la cola después de remover: " + dequeCola);

    }

    /**
     * LinkedList en Java puede ser utilizado tanto como una estructura FIFO (First In First Out) como LIFO (Last In First Out).
     * Para usarlo como una estructura FIFO (como una cola),
     * puedes usar los métodos addLast() para agregar elementos al final de la lista y removeFirst() para eliminar el primer elemento de la lista.
     * Para usarlo como una estructura LIFO (como una pila),
     * puedes usar los métodos addLast() o push() para agregar elementos al final de la lista y removeLast() o pop() para eliminar el último elemento de la lista.
     */
    static void estructuraLifoFifo() {
        LinkedList<Integer> fifoList = new LinkedList<>();

        // Agregar elementos
        fifoList.addLast(1);
        fifoList.addLast(2);
        fifoList.addLast(3);

        // Remover el primer elemento agregado
        int primero = fifoList.removeFirst();

        System.out.println("El primer elemento removido es: " + primero);
        System.out.println("Contenido de la lista después de remover: " + fifoList);

        LinkedList<Integer> lifoList = new LinkedList<>();

        // Agregar elementos
        lifoList.addLast(1);
        lifoList.addLast(2);
        lifoList.addLast(3);

        // Remover el último elemento agregado
        int ultimo = lifoList.removeLast();

        System.out.println("El último elemento removido es: " + ultimo);
        System.out.println("Contenido de la lista después de remover: " + lifoList);
    }

    /**
     * Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web.
     * Crea un programa en el que puedas navegar a una página o indicarle
     * que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
     * Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
     * el nombre de una nueva web.
     */

    static void ejemploNavegadorPila() {

        Deque<String> historial = new ArrayDeque<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Introduce el nombre de la web o 'adelante'/'atras' o salir: ");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("salir")) break;

            if (input.equals("adelante")) {
                if (historial.isEmpty()) System.out.println("No hay páginas para avanzar");
                else {
                    String pagina = historial.pollLast();
                    System.out.println("Avanzando a la página: " + pagina);
                }
            } else if (input.equals("atras")) {
                if (historial.isEmpty()) System.out.println("No hay páginas para retroceder");
                else {
                    String pagina = historial.pollFirst();
                    System.out.println("Retrocediendo a la página: " + pagina);
                }
            } else {
                historial.addFirst(input);
                System.out.println("Navegando a la página: " + input);
            }
        }

    }

    /**
     * Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
     * impresora compartida que recibe documentos y los imprime cuando así se le indica.
     * La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
     * interpretan como nombres de documentos.
     */

    static void ejemploImpresoraCola() {

        Deque<String> colaImpresion = new ArrayDeque<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Introduce el nombre del documento o 'imprimir' o salir: ");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("salir")) break;

            if (input.equals("imprimir")) {
                if (colaImpresion.isEmpty()) System.out.println("No hay documentos para imprimir");
                else {
                    String documento = colaImpresion.poll();
                    System.out.println("Imprimiendo el documento: " + documento);
                }
            } else {
                colaImpresion.addLast(input);
                System.out.println("Añadiendo el documento: " + input);
            }
        }
    }

}
