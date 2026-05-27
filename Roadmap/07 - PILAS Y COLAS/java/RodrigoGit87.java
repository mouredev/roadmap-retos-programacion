/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

import java.util.InputMismatchException;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class RodrigoGit87 {
    public static void main (String[] args){
    // PILAS / STACK (LIFO, Last In First Out)
        System.out.println("Stack");

        Stack<Integer> pila = new Stack<Integer>();
        for (int i=0; i <=10; i++) pila.push(i);
        System.out.println(pila);

        int pop = pila.pop(); //Devuelve el ultimo push y lo elimina
        System.out.println(pila + "\nElemento .pop() eliminado: " + pop);


    // COLAS  / Queue (FIFO, First In First Out) Se recomienda LinkedList o ArrayDeque
        System.out.println("Queue");
        LinkedList<Integer> numeros = new LinkedList<>();
        numeros.add(11);
        numeros.add(22);
        numeros.add(33);
        numeros.add(44);
        System.out.println(numeros);

        int n = numeros.pop(); // Devuelve el primer elemento y lo elimina
        System.out.println(numeros + "\nElemento .pop() eliminado: " + n);


        // ---------- EXTRA ------------
        System.out.println(" --- EXTRA  --- ");
        Stack<Accion> pilaAcciones = new Stack<>();
        Scanner sc =  new Scanner(System.in);

            //Añadir opciones
            pilaAcciones.push(new Accion("adelante"));
            pilaAcciones.push(new Accion("atras"));
            pilaAcciones.push(new Accion("salir"));

            //Mostrar opciones
        System.out.println(" Elige una acción ");
        for (int i =0 ; i < pilaAcciones.size(); i++){
            System.out.println(i + " -> " + pilaAcciones.get(i));
        }
            //Elegir una accion
        try {
            int eleccion = sc.nextInt();
            if (eleccion >= 0 && eleccion < pilaAcciones.size()) {
                Accion seleccionado = pilaAcciones.get(eleccion);
                System.out.println(" Acción realizada: " + seleccionado);
            }
        } catch (InputMismatchException e) {
            System.err.println(" ERROR " + e);
        }
    }

    //Clase para el EXTRA ->  Creo la clase Accion para crear una pila basada en Objetos
public static class Accion {
        protected String nombre;


        public Accion(String nombre) {
            this.nombre = nombre;
        }

        @Override
        public String toString() {
            return "'" + nombre + "'";
        }
    }
}

