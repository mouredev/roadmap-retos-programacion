import java.util.*;

public class frangarmez21 {

    public static void main(String[] args) {

        System.out.println("##Ejercicios de pilas y colas##");
        /*
         * EJERCICIO:
         * Implementa los mecanismos de introducción y recuperación de elementos propios de las
         * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
         * o lista (dependiendo de las posibilidades de tu lenguaje).
         */
        System.out.println("##Implementando los mecanismos de introducción y recuperación de elementos.##");
        System.out.println();
        System.out.println("##Las pilas (stacks - LIFO)##");
        ArrayList stack = new ArrayList();
        System.out.println("1-Añadimos elementos a la pila.");
        stack.add(1);
        stack.add(2);
        stack.add(3);
        System.out.println("2-Tenemos la siguiente pila: " + stack);
        System.out.println("3-Quitamos elementos de la pila.");
        while (!stack.isEmpty()) {
            stack.removeLast();
        }
        System.out.println("4-Resultado de desapilar: " + stack);
        System.out.println();

        System.out.println("##Las colas (queue - FIFO)##");
        ArrayList queue = new ArrayList();
        System.out.println("1-Añadimos elementos a la cola");
        queue.add(1);
        queue.add(2);
        queue.add(3);
        System.out.println("2-Tenemos la siguiente cola: " + queue);
        System.out.println("3-Quitamos elementos de la cola");
        while (!queue.isEmpty()) {
            queue.removeFirst();
        }
        System.out.println("4-Resultado de desencolar: " + queue);

        System.out.println();
        System.out.println("##Dificultad Extra##");
        System.out.println();

        /*
         * DIFICULTAD EXTRA (opcional):
         * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
         *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
         *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
         *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
         *   el nombre de una nueva web.
         *
         * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
         *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
         *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
         *   interpretan como nombres de documentos.
         */

        System.out.println("Simula el mecanismo adelante/atrás de un navegador web:");
        System.out.println();


        System.out.println();
        System.out.println("Simula el mecanismo de una impresora:");
        System.out.println();


    }
}
