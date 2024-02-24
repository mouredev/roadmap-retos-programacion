import java.util.LinkedList;

public class Main {

    /**
     * Una clase es una plantilla que permite crear objetos de un tipo determinado.
     * Un objeto representa una entidad del mundo real.
     * Por lo que, una clase posee atributos (propiedades) y métodos (funciones).
     * Para utilizar una clase es necesario crear una instancia de la misma.
     */

    public static void main(String[] args) {

        // Crear una instancia de la clase Persona
        Persona persona = new Persona("Pedrito", 20);

        // Acceder a los atributos de la clase Persona
        System.out.println("Nombre: " + persona.getNombre());
        System.out.println("Edad: " + persona.getEdad());

        // Modificar los atributos de la clase Persona
        persona.setNombre("Juanito");
        persona.setEdad(25);

        // Ejecutar métodos de la clase Persona
        persona.caminar();
        persona.hablar();

        // Imprimir el objeto
        System.out.println(persona);


        Cola<String> cola = new Cola<>();
        cola.agregar("Elemento 1");
        cola.agregar("Elemento 2");
        cola.agregar("Elemento 3");

        cola.imprimir();

        Pila<Integer> pila = new Pila<>();
        pila.agregar(1);
        pila.agregar(2);
        pila.agregar(3);

        pila.imprimir();

    }

    // Clase Persona
    static class Persona {

        // Atributos
        String nombre;
        int edad;

        // Constructor
        public Persona(String nombre, int edad) {
            this.nombre = nombre;
            this.edad = edad;
        }

        // Getters y Setters
        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public int getEdad() {
            return edad;
        }

        public void setEdad(int edad) {
            this.edad = edad;
        }

        // Métodos
        public void caminar() {
            System.out.println(nombre + " está caminando");
        }

        public void hablar() {
            System.out.println(nombre + " está hablando");
        }

        @Override
        public String toString() {
            return "Persona{" +
                    "nombre='" + nombre + '\'' +
                    ", edad=" + edad +
                    '}';
        }
    }

    /**
     * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
     * en el ejercicio número 7 de la ruta de estudio)
     * Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
     * retornar el número de elementos e imprimir todo su contenido.
     */
    static class Cola<T> {
        private LinkedList<T> elementos;

        public Cola() {
            this.elementos = new LinkedList<>();
        }

        public void agregar(T elemento) {
            elementos.addLast(elemento);
        }

        public T eliminar() {
            if (elementos.isEmpty()) {
                return null;
            }
            return elementos.removeFirst();
        }

        public int tamaño() {
            return elementos.size();
        }

        public void imprimir() {
            System.out.println(elementos);
        }
    }

    static class Pila<T> {
        private LinkedList<T> elementos;

        public Pila() {
            this.elementos = new LinkedList<>();
        }

        public void agregar(T elemento) {
            elementos.addLast(elemento);
        }

        public T eliminar() {
            if (elementos.isEmpty()) {
                return null;
            }
            return elementos.removeLast();
        }

        public int tamaño() {
            return elementos.size();
        }

        public void imprimir() {
            System.out.println(elementos);
        }
    }

}
