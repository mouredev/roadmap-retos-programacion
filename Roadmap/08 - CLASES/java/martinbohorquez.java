import java.util.Queue;
import java.util.Stack;
import java.util.*;

public class martinbohorquez {

    private static Queue<Integer> cola = new LinkedList<>(); //Cola

    public static void main(String[] args) {
        Programador programador = new Programador("MartinDev", 29,
                Arrays.asList("Java", "Python", "Typescript"));
        programador.setSurname("Bohorquez");
        programador.imprimir();
        programador.languages.add("Kotlin");
        programador.imprimir();

        /*
         * DIFICULTAD EXTRA
         */
        //stack
        System.out.println("[------- STACK ---------]");
        Pila pila = new Pila(Arrays.asList(10, 20, 30, 40));
        pila.push(50);
        pila.count();
        pila.pop();
        pila.count();
        pila.push(60);
        pila.count();
        pila.print();
        //queue
        System.out.println("[------- QUEUE ---------]");
        Cola cola = new Cola(Arrays.asList(100, 200, 300, 400));
        cola.offer(500);
        cola.count();
        cola.poll();
        cola.count();
        cola.offer(600);
        cola.count();
        cola.print();

    }

    private static class Pila {
        private Stack<Integer> pila = new Stack<>();

        private Pila(List<Integer> pila) {
            this.pila.addAll(pila);
        }

        private void push(Integer num) {
            printStack();
            System.out.printf("Se añade el elemento %d a la pila: %n", pila.push(num));
            printStack();
        }

        private void pop() {
            printStack();
            if (!pila.isEmpty()) {
                System.out.printf("Se extrae un elemento %d a la pila: %n", pila.pop());
                printStack();
            }
        }

        private void count() {
            System.out.printf("La pila cuenta con %d elementos.%n", pila.size());
        }

        private void printStack() {
            System.out.printf("La pila contiene los siguientes elementos: %s%n", pila.toString());
        }

        private void print() {
            System.out.println("La pila contiene los siguientes elementos:");
            pila.forEach(System.out::println);
        }
    }

    private static class Cola {
        private Queue<Integer> cola;

        private Cola(List<Integer> cola) {
            this.cola = new LinkedList<>(cola);
        }

        private void offer(Integer num) {
            printQueue();
            cola.offer(num);
            System.out.printf("Se añade el elemento %d a la cola: %n", num);
            printQueue();
        }

        private void poll() {
            printQueue();
            if (!cola.isEmpty()) {
                System.out.printf("Se extrae un elemento %d a la pila: %n", cola.poll());
                printQueue();
            }
        }

        private void count() {
            System.out.printf("La pila cuenta con %d elementos.%n", cola.size());
        }

        private void printQueue() {
            System.out.printf("La cola contiene los siguientes elementos: %s%n", cola.toString());
        }

        private void print() {
            System.out.println("La pila contiene los siguientes elementos:");
            cola.forEach(System.out::println);
        }
    }

    private static class Programador {
        private String name;
        private String surname;
        private int age;
        private List<String> languages;

        private Programador(String name, int age, List<String> lenguajes) {
            this.name = name;
            this.age = age;
            this.languages = new ArrayList<>(lenguajes);
        }

        private void setSurname(String surname) {
            this.surname = surname;
        }

        private void imprimir() {
            System.out.printf("Nombre: %s | Apellido: %s | Edad: %d | Lenguajes: %s%n",
                    name, surname, age, languages.toString());
        }
    }
}
