
import java.util.ArrayList;
import java.util.List;

public class reto_8 {
    private String nombre;
    private int edad;
    private String direccion;

    public reto_8(String nombre, int edad, String direccion) {
        this.nombre = nombre;
        this.edad = edad;
        this.direccion = direccion;
    }

    public void imprimir() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Dirección: " + direccion);
    }

    // Implementación de la pila (stack)
    class Stack<T> {
        private List<T> elementos = new ArrayList<>();

        // Agregar elementos
        public void agregar(T elemento) {
            elementos.add(elemento);
        }

        public void eliminar() {
            if (elementos.isEmpty()) {
                throw new RuntimeException("La pila está vacía");
            } else {
                elementos.remove(elementos.size() - 1);
            }
        }

        public int numeroElementos() {
            return elementos.size();
        }

        public void mostrarElementos() {
            System.out.println("Mostrar elementos de la pila: " + elementos);
        }

        @Override
        public String toString() {
            return elementos.toString();
        }
    }

    // Implementación de la cola (queue) genérica
    class Queue<T> {
        private List<T> elementos = new ArrayList<>();

        public void agregar(T elemento) {
            elementos.add(elemento);
        }

        public void eliminar() {
            if (elementos.isEmpty()) {
                throw new RuntimeException("La cola está vacía");
            } else {
                elementos.remove(0);
            }
        }

        public int numeroElementos() {
            return elementos.size();
        }

        public void mostrarElementos() {
            System.out.println("Mostrando elementos: " + elementos);
        }

        @Override
        public String toString() {
            return elementos.toString();
        }
    }
}

class Prueba {
    public static void main(String[] args) {
        reto_8 prueba = new reto_8("Julian", 19, "Carrera 101a");
        prueba.imprimir();

        System.out.println("\n****** Pila ******\n");

        reto_8.Stack<String> pila = prueba.new Stack<>();
        pila.agregar("Elemento 1");
        pila.agregar("Elemento 2");
        pila.agregar("Elemento 3");
        System.out.println("Agregar elemento: " + pila);

        pila.eliminar();
        System.out.println("Eliminar elemento: " + pila);

        int num = pila.numeroElementos();
        System.out.println("Número de elementos en la pila: " + num);

        pila.mostrarElementos();

        System.out.println("\n****** Cola ******\n");

        reto_8.Queue<String> cola = prueba.new Queue<>();
        cola.agregar("Elemento 1");
        cola.agregar("Elemento 2");
        cola.agregar("Elemento 3");
        System.out.println("Agregar elemento: " + cola);

        cola.eliminar();
        System.out.println("Eliminar elemento: " + cola);

        int numCola = cola.numeroElementos();
        System.out.println("Número de elementos en la cola: " + numCola);

        cola.mostrarElementos();
    }
}
