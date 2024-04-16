import java.security.PublicKey;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class GustavoGomez19 {
    /*
     * EJERCICIO:
     * Explora el concepto de clase y crea un ejemplo que implemente un
     * inicializador,
     * atributos y una función que los imprima (teniendo en cuenta las posibilidades
     * de tu lenguaje).
     * Una vez implementada, créala, establece sus parámetros, modifícalos e
     * imprímelos
     * utilizando su función.
     */

    public static void main(String[] args) {

        Animal perro = new Animal(2, "Roko", "Criollo");
        Animal gato = new Animal();
        gato.setEdad(3);
        gato.setNombre("Gael");
        gato.setRaza("Criollo");

        System.out.println(perro.verInfo());
        System.out.println();
        System.out.println(gato.verInfo());
        System.out.println("******************");

        // DIFICULTAD EXTRA
        // Pila
        Pila miPila = new Pila();
        // Añadir elementos
        miPila.agregarElemento("Gustavo");
        miPila.agregarElemento("Katerine");
        miPila.agregarElemento("María José");
        // Eliminar elemento
        miPila.eleminarElemento();
        // Ver elementos de la pila
        miPila.verElementos();
        // Tamaño de la pila
        miPila.conocerTamanoPila();
        System.out.println();
        System.out.println("************************");

        // Cola
        Cola miCola = new Cola();
        // Agregar elementos a la cola
        miCola.agregarElementoCola(1);
        miCola.agregarElementoCola(2);
        miCola.agregarElementoCola(3);
        // Elimianr elementos de la cola
        miCola.eleminarElementoCola();
        // Ver elementos de la cola
        miCola.verElementosCola();
        // Tamaño de la cola
        miCola.conocerTamanoCola();



    }

    static class Animal {
        private int edad;
        private String nombre;
        private String raza;

        // Contructor vacío
        public Animal() {
        };

        // Contructor con parámetros
        public Animal(int edad, String nombre, String raza) {
            this.edad = edad;
            this.nombre = nombre;
            this.raza = raza;
        }

        // Métodos accesores (Getters - Setters)
        public int getEdad() {
            return edad;
        }

        public void setEdad(int edad) {
            this.edad = edad;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public String getRaza() {
            return raza;
        }

        public void setRaza(String raza) {
            this.raza = raza;
        }

        // Método para impirmir la información
        public String verInfo() {
            return "*** INFORMACIÓN DE LA MASCOTA*** " + "\n" +
                    "Edad: " + edad + " años" + "\n" +
                    "Nombre: " + nombre + "\n" +
                    "Raza: " + raza;
        }
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Implementa dos clases que representen las estructuras de Pila y Cola
     * (estudiadas
     * en el ejercicio número 7 de la ruta de estudio)
     * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
     * retornar el número de elementos e imprimir todo su contenido.
     */

    static class Pila {
        // Creación de la pila
        private Stack<String> pila;

        public Pila(){
            this.pila = new Stack<>();
        }

        // Agregar elementos a la pila
        public void agregarElemento(String elemento){
            this.pila.push(elemento);
        }
        // Eliminar elemento de la pila
        public void eleminarElemento(){
            this.pila.pop();
        }
        // Mostrar los elemanto de la pila
        public void verElementos(){
            System.out.println("Elementos de la pila: ");
            for (String elemento : this.pila) {
                System.out.println(elemento);
            }
        }
        // Método para saber el tamaño de la pila
        public void conocerTamanoPila(){
            System.out.print("Tamaño de pila: " + pila.size());
        }

    }

    static class Cola {
        // Creación de cola
        private Queue<Integer> cola;

        public Cola(){
            this.cola = new LinkedList<>();
        }

        // Agregar elemanto a la cola
        public void agregarElementoCola(Integer elemento){
            this.cola.add(elemento);
        }
        // Eliminar elemento de la cola
        public void eleminarElementoCola(){
            this.cola.poll();
        }
        // Mostrar elementos de la cola
        public void verElementosCola(){
            System.out.println("Elementos de la cola");
            for (Integer elementos : cola) {
                System.out.println(elementos);
            }
        }
        // Conocer el tamaño de la cola
        public void conocerTamanoCola(){
            System.out.print("Tamaño de la cola: " + cola.size());
        }
        
    }

}
