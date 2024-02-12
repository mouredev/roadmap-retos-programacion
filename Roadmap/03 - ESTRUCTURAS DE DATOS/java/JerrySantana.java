/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Stack;

class JerrySantana {
    public static void main(String[] args) {
        System.out.println("Estructuras de datos.");
        arrays();
        pilas();
        colas();
    }
    // Arreglos
    private static void arrays() {
        System.out.println("- Arreglos.");
        System.out.println("\tUtilizando la declaracion de arrays: tipoDato nombreVariable[] = {elementos};.");
        System.out.println("\t\tAl inicializar un arreglo automaticamente se define el tamano que tendra, por lo que no se puede agregar ni eliminar valores.");
        System.out.println("\t\tCada elemento dentro del arreglo cuenta con un indice que define la posicion que ocupa dentro del arreglo, este indice comienza en '0'.");
        int arreglo[] = {1, 2, 3, 4, 5};
        System.out.print("\t\tarreglo original: {");
        for (int i : arreglo) {
            System.out.printf(i + " ");
        }
        System.out.println('}');
        System.out.println("\t\tLas operaciones que podemos realizar sobre arreglos son: obtener longitud, acceder a sus valores y modificar los valores de sus elementos.");
        System.out.println("\t\t\tTamano de arreglo: " + arreglo.length);
        System.out.println("\t\tModificando el valor '5', en la posición [4]; por el valor '6'");
        arreglo[4] = 6;
        System.out.print("\t\tarreglo modificado: {");
        for (int i : arreglo) {
            System.out.printf(i + " ");
        }
        System.out.println('}');
        System.out.println("\tUtilizando la clase ArrayList de la biblioteca java.util.");
        System.out.println("\t\tEsta clase nos permite realizar más cosas que con la definición anterior de arreglos. Mediante ArrayList podemos realizar diferentes acciones:");
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (Integer integer : arreglo) {
            arrayList.add(integer);
        }
        System.out.println("\t\tarrayList: " + arrayList.toString());
        arrayList.add(2, 9);
        System.out.println("\t\tAñadir elementos.");
        System.out.println("\t\t\tAñadiendo un valor en la posición '2' del arreglo: " + arrayList.toString());
        arrayList.remove(0);
        System.out.println("\t\tEliminar elementos.");
        System.out.println("\t\t\tEliminando el valor en la posición '0' del arreglo: " + arrayList.toString());
        arrayList.set(2, 25);
        System.out.println("\t\tModificar elementos.");
        System.out.println("\t\t\tModificado el valor '3', en la posición '2'; por el valor '25': " + arrayList.toString());
        arrayList.sort(null);
        System.out.println("\t\tOrdenar elementos.");
        System.out.println("\t\t\tOrdenando el arreglo mediante la función sort de la clase: " + arrayList.toString());
        System.out.println("\tTambién podemos utilizar la definición inicial de arrays para crear arreglos bidimensionales o también llamados matrices.");
    }
    // Pilas
    private static void pilas() {
        System.out.println("- Arreglos.");
        System.out.println("\tUtilizamos la clase Stack de la biblioteca java.utils, para implementar pilas.");
        System.out.println("\tLas pilas utilizan el principio LIFO 'Last In First Out' (Ultimo en entrar, primero en salir).");
        System.out.println("\tUtilizamos la clase Stack de la biblioteca java.utils, para implementar pilas.");
        System.out.println("\tMediante esta clase podemos realizar las siguientes acciones:");
        Stack<Integer> pila = new Stack<>();
        System.out.println("\t\tAñadir elementos al final de la pila mediante el comando push.");
        for(int i = 0; i < 5; i++) {
            System.out.println("\t\t\tAñadiendo valor: " + i + ", a la pila: " + pila.toString());
            pila.push(i);
        }
        System.out.println("\t\t\tpila resultante: " + pila.toString());
        System.out.println("\t\tAñadir elementos en un lugar específico mediante el comando add.");
        pila.add(2, 8);
        System.out.println("\t\t\tAñadido el valor '8', en la posición 2.");
        System.out.println("\t\t\tpila resultante: " + pila.toString());
        System.out.println("\t\tBorrar elementos mediante el comando pop.");
        pila.pop();
        System.out.println("\t\t\tEliminado el último elemento de la pila.");
        System.out.println("\t\t\tpila resultante: " + pila.toString());
        System.out.println("\t\tModificar elementos mediante el comando set.");
        pila.set(3, 6);
        System.out.println("\t\t\tModificado el valor '3', en la posición 3; con el valor '6'.");
        System.out.println("\t\t\tpila resultante: " + pila.toString());
        System.out.println("\t\tOrdenar elementos mediante el comando sort.");
        pila.sort(null);
        System.out.println("\t\t\tpila resultante: " + pila.toString());
    }
    // Colas
    private static void colas() {
        System.out.println("- Colas.");
        System.out.println("\tSon estructuras que siguen el principio FIFO 'First In First Out' (Primero en entrar primero en salir).");
        System.out.println("\tPueden ser implementadas mediante la clase PriorityQueue o Linkedlist de la biblioteca java.util.");
        System.out.println("\tUtilizando la clase PriorityQueue, podemos realizar las siguientes operaciones:");
        PriorityQueue<Integer> colaPrioridad = new PriorityQueue<>();
        System.out.println("\t\tAñadir elementos a la cola de prioridad mediante el comando add.");
        for(int i = 11; i < 21; i++) {
            System.out.println("\t\t\tAñadiendo valor: " + i + ", a la cola de prioridad: " + colaPrioridad.toString());
            colaPrioridad.add(i);
        }
        System.out.println("\t\t\tCola de prioridad resultante: " + colaPrioridad.toString());
        System.out.println("\t\tEliminar el elemento en la cabeza de la cola de prioridad mediante el comando poll.");
        System.out.println("\t\t\tEliminando el elemento al frente de la cola de prioridad...: " + colaPrioridad.poll());
        System.out.println("\t\t\tCola de prioridad resultante: " + colaPrioridad.toString());
        System.out.println("\tUtilizando la clase Queue y LinkedList, podemos realizar las siguientes operaciones:");
        Queue<Integer> queue = new LinkedList<Integer>();
        for(int i = 21; i < 31; i++) {
            System.out.println("\t\t\tAñadiendo valor: " + i + ", a la cola: " + queue.toString());
            queue.offer(i);
        }
        System.out.println("\t\t\tCola resultante: " + queue.toString());
        System.out.println("\t\tEliminar el elemento en la cabeza de la cola mediante el comando poll.");
        System.out.println("\t\t\tEliminando el elemento al frente de la cola...: " + queue.poll());
        System.out.println("\t\t\tCola resultante: " + queue.toString());
        System.out.println("\t\t");
        System.out.println("\t\t\t");
    }
}