import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class TofeDev {
    public static void main(String[] args) {
        Persona usuario1 = new Persona("Santiago Rodriguez", "Chile", 25);
        Persona usuario2 = new Persona();
        usuario2.setNombre("Marta Gonzales");
        usuario2.setPais("Argentina");
        usuario2.setEdad(28);

        System.out.println(usuario1.info());
        System.out.println(usuario2.info());

        // *EXTRA*
        // Pila
        Pila pila = new Pila();
        // Añadir elementos
        pila.agregarElementoPila("Cajas");
        pila.agregarElementoPila("Libros");
        pila.agregarElementoPila("Botellas");
        // Eliminar elemento
        pila.eleminarElementoPila();
        // Ver elementos
        pila.verElementosPila();
        // Ver tamaño
        pila.sizePila();
        System.out.println("");
        // Cola
        Cola cola = new Cola();
        // Agregar elementos
        cola.agregarElementoCola(1);
        cola.agregarElementoCola(2);
        cola.agregarElementoCola(3);
        // Elimianr elementos
        cola.eleminarElementoCola();
        // Ver elementos
        cola.verElementosCola();
        // Ver tamaño
        cola.sizeCola();
    }

    static class Persona {
        private String nombre;
        private String pais;
        private int edad;

        public Persona(String nombre, String pais, int edad) {
            this.nombre = nombre;
            this.pais = pais;
            this.edad = edad;
        }

        public Persona() {

        }

        //Getters
        public String getNombre() {
            return nombre;
        }
        public String getPais() {
            return pais;
        }
        public int getEdad() {
            return edad;
        }

        //Setters
        public void setNombre(String nombre) {
            this.nombre = nombre;
        }
        public void setPais(String pais) {
            this.pais = pais;
        }
        public void setEdad(int edad) {
            this.edad = edad;
        }

        public String info() {
            return "--Información del Usuario-- " + "\n" +
                    "Nombre: " + nombre + "\n" +
                    "Pais: " + pais + "\n" +
                    "Edad: " + edad + " años";
        }
    }

    /* DIFICULTAD EXTRA (opcional):
     * Implementa dos clases que representen las estructuras de Pila y Cola
     * (estudiadas en el ejercicio número 7 de la ruta de estudio)
     * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
     * retornar el número de elementos e imprimir todo su contenido.
     */

    static class Pila {
        private Stack<String> pila;

        public Pila(){
            this.pila = new Stack<>();
        }

        public void agregarElementoPila(String elemento){
            this.pila.push(elemento);
        }

        public void eleminarElementoPila(){
            this.pila.pop();
        }

        public void verElementosPila(){
            System.out.println("Elementos de la pila: ");
            for (String elemento : this.pila) {
                System.out.println(elemento);
            }
        }

        public void sizePila(){
            System.out.print("Tamaño de pila: " + pila.size());
        }

    }

    static class Cola {

        private Queue<Integer> cola;

        public Cola(){
            this.cola = new LinkedList<>();
        }


        public void agregarElementoCola(Integer elemento){
            this.cola.add(elemento);
        }

        public void eleminarElementoCola(){
            this.cola.poll();
        }

        public void verElementosCola(){
            System.out.println("Elementos de la cola");
            for (Integer elementos : cola) {
                System.out.println(elementos);
            }
        }

        public void sizeCola(){
            System.out.print("Tamaño de la cola: " + cola.size());
        }
        
    }

}
