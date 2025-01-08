import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/** #07 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        System.out.println("CLASES");
        Persona persona = new Persona("Jesus Antonio", 24, "Programador");
        persona.imprimirDetalles();
    //---EXTRA---
        // Ejemplo con Pila
        System.out.println("\nSTACK");
        Pila<Integer> pila = new Pila<>();
        pila.apilar(1);
        pila.apilar(2);
        pila.apilar(3);
        pila.imprimir();  // Contenido de la Pila: [1, 2, 3]
        pila.desapilar();
        pila.imprimir();  // Contenido de la Pila: [1, 2]

        // Ejemplo con Cola
        System.out.println("\nQUEUE");
        Cola<String> cola = new Cola<>();
        cola.encolar("A");
        cola.encolar("B");
        cola.encolar("C");
        cola.imprimir();  // Contenido de la Cola: [A, B, C]
        cola.desencolar();
        cola.imprimir();  // Contenido de la Cola: [B, C]
    }

    //---EJERCIÓ---
    // Definición de la clase Persona
    static class Persona {
        // Atributos de la clase
        private String nombre;
        private int edad;
        private String ocupacion;

        // Constructor de la clase Persona
        public Persona(String nombre, int edad, String ocupacion) {
            this.nombre = nombre;       // Inicializa el atributo nombre
            this.edad = edad;           // Inicializa el atributo edad
            this.ocupacion = ocupacion; // Inicializa el atributo ocupacion
        }

        // Método para imprimir los atributos de la clase
        public void imprimirDetalles() {
            System.out.println("Nombre: " + nombre);
            System.out.println("Edad: " + edad);
            System.out.println("Profesión: " + ocupacion);
        }
    }



    /**-----DIFICULTAD EXTRA-----*/

    // Clase Pila (Stack)
    public static class Pila<T> {
        private ArrayList<T> elementos;

        public Pila() {
            elementos = new ArrayList<>();
        }

        // Agregar un elemento a la pila
        public void apilar(T elemento) {
            elementos.add(elemento);
        }

        // Eliminar el último elemento agregado (pop)
        public T desapilar() {
            if (!estaVacia()) {
                return elementos.remove(elementos.size() - 1);
            }
            return null;  // Devuelve null si la pila está vacía
        }

        // Retornar el número de elementos en la pila
        public int tamano() {
            return elementos.size();
        }

        // Verificar si la pila está vacía
        public boolean estaVacia() {
            return elementos.isEmpty();
        }

        // Imprimir el contenido de la pila
        public void imprimir() {
            System.out.println("Contenido de la Pila: " + elementos);
        }
    }

    // Clase Cola (Queue)
    public static class Cola<T> {
        private Queue<T> elementos;

        public Cola() {
            elementos = new LinkedList<>();
        }

        // Agregar un elemento a la cola
        public void encolar(T elemento) {
            elementos.add(elemento);
        }

        // Eliminar el primer elemento (dequeue)
        public T desencolar() {
            if (!estaVacia()) {
                return elementos.poll();  // poll elimina y retorna el primer elemento
            }
            return null;  // Devuelve null si la cola está vacía
        }

        // Retornar el número de elementos en la cola
        public int tamano() {
            return elementos.size();
        }

        // Verificar si la cola está vacía
        public boolean estaVacia() {
            return elementos.isEmpty();
        }

        // Imprimir el contenido de la cola
        public void imprimir() {
            System.out.println("Contenido de la Cola: " + elementos);
        }
    }

    /**-----DIFICULTAD EXTRA-----*/
}