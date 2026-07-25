/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */
import java.util.Stack;
import java.util.LinkedList;

public class RodrigoGit87 {
    private String nombre, genero;
    private int edad;
    private boolean esHumano;

    // Constructor
    public RodrigoGit87(String nombre, String genero, int edad, boolean esHumano) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.esHumano = esHumano;
    }

    // Getters y Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public boolean isEsHumano() {
        return esHumano;
    }

    public void setEsHumano(boolean esHumano) {
        this.esHumano = esHumano;
    }

    // metodo
    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Genero: " + genero);
        System.out.println("Edad: " + edad);
        System.out.println("Es Humano: " + esHumano);
    }

    public static void main(String[] args) {
        // Instanciar
        var usuario = new RodrigoGit87("RodrigoGit87", "hombre", 38, true);

        // llamada a metodo
        usuario.mostrarDatos();

        System.out.println("---------------");

        // Modificar atributos
        usuario.setNombre(" Rodrigo ");
        usuario.setGenero(" Gigachad ");

        // Ver valores modificados
        System.out.println("Cambiado genero a : " + usuario.getGenero());
        System.out.println("Cambiado nombre a : " + usuario.getNombre());

        //-- EXTRA --
        System.out.println("\n--- EXTRA - PILA ---");
        var pila = new Pila();
        pila.pushx10();
        pila.push(50);
        System.out.println(
                " \nHasta aqui se han añadido 10 numeros con el metodo pushx10() y 1 numero con el metodo push(). Hay "
                        + pila.size() + " elementos en total");
        pila.pop();
        System.out.println(
                " \nNotar como el metodo pop() elimina el ultimo elemento añadido pero de ambos metodos push (el del push normal y el pushx10)- habia 11 elementos, ahora: "
                        + pila.size());
        pila.mostrar();

        System.out.println("\n--- EXTRA - COLA ---");
        var cola = new Cola();
        cola.add("Hola");
        cola.add("Mundo");
        cola.add("soy");
        cola.add("RodrigoGit87");
        cola.add("!");
        System.out.println(" Elementos en la cola: " + cola.size() +" --> " + cola);
        System.out.println(" Elemento eliminado: " + cola.pop() + " <-- .pop() en una linkedlist elimina el primer elemento" );
        

    }

    // --- EXTRA ---
    // STACK (lifo)
    public static class Pila {
        private Stack<Integer> pila;

        public Pila() {
            this.pila = new Stack<>();
        };

        /*
         * Como he creado la clase Pila, aunque el constructor instancia un ' new Stack
         * ', al ser una clase aislada, no hereda los metodos de java.util.Stack (push,
         * pop, size ...)
         * - Para q la instancia use los metodos propios de la clase Stack, usamos un
         * wrapper de los metodos push, pop, .... Es decir, crear una función en esta
         * clase que 'conecte' con los
         * metodos propios de la clase Stack
         */

        // Metodos push
        public void push(int numero) {
            System.out.println("pusheado: " + numero);
            pila.push(numero);
        }

        public void pushx10() {

            for (int n = 1; n <= 10; n++) {
                pila.push(n);
            }
            System.out.println(" 10 numeros consecutivos añadidos a la lista");
        }

        // Metodo pop (tiene q retornar)
        public Integer pop() {
            if (pila.isEmpty()) {
                System.out.println("La pila está vacía.");
                return null;
            }
            System.out.println(" Elemento pop eliminado: " + pila.pop());
            return pila.pop();
        }

        // Metodo size
        public int size() {
            System.out.println(" Tamaño de la pila: " + pila.size());
            return pila.size();
        }

        // mostrar elementos
        public void mostrar() {
            System.out.println(" Elemntos en la pila: " + pila);
        }
    }

    // QUEUE (fifo)
    // Como he dicho antes, sin herencia, no hay metodos propios. para ahorrarse tener q wrappear, uso la herencia.
    public static class Cola extends LinkedList<String> {

        // Constructor
        public Cola() {
            super(); // Inicializa la propia lista heredada
        }
    }
    
    // La clase Cola ES una LinkedList, no necesita wrappear metodos, por q ya los hereda.
    // La clase Pila TIENE un Stack, pero no hereda sus metodos, por eso se crean metodos wrapeables

}