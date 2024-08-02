import java.util.ArrayList;
import java.util.LinkedList;

/** #07 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        // PILAS
        System.out.println("PILAS - STACKS - LIFO");
        Stack stack = new Stack();
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Contenido de la Pila: " + stack);
        System.out.println("Elemento de parte superior de la Pila: " + stack.peek());
        System.out.println("Elemento eliminado de la Pila: " + stack.pop());
        System.out.println("Contenido de la Pila: " + stack);

        // COLAS
        System.out.println("COLAS - QUEUE - FIFO");
        Queue queue = new Queue();
        queue.enqueue(40);
        queue.enqueue(50);
        queue.enqueue(60);
        System.out.println("Contenido de la Cola: " + queue);
        System.out.println("Primer elemento de Cola: " + queue.peek());
        System.out.println("Elemento eliminado de la Cola: " + queue.dequeue());
        System.out.println("Contenido de la Cola: " + queue);
        //---EXTRA---
        
    }

    //---EJERCIÓ---
    // STACKS - LIFO
    static class Stack{
        private ArrayList<Integer> stack;

        public Stack(){
            stack = new ArrayList<>();
        }

        // Se añade un elemento a la pila
        public void push(int value){
            stack.add(value);
        }

        public int pop(){
            if (stack.isEmpty()) {
                throw new IllegalAccessError("La pila esta vacía");
            }
            return stack.remove(stack.size() - 1);
        }

        public int peek(){
            if (stack.isEmpty()) {
                throw new IllegalAccessError("La pila esta vacía");
            }
            return stack.get(stack.size() - 1);
        }

        @Override
        public String toString() {
            return stack.toString();
        }
    }


    // QUEUE - FIFO
    static class Queue{
        private LinkedList<Integer> queue;

        public Queue(){
            queue = new LinkedList<>();
        }

        // Se añade un elemento a la pila
        public void enqueue(int value){
            queue.addLast(value);
        }

        public int dequeue(){
            if (queue.isEmpty()) {
                throw new IllegalAccessError("La cola esta vacía");
            }
            return queue.removeFirst();
        }

        public int peek(){
            if (queue.isEmpty()) {
                throw new IllegalAccessError("La pila esta vacía");
            }
            return queue.getFirst();
        }

        @Override
        public String toString() {
            return queue.toString();
        }
    }



    /**-----DIFICULTAD EXTRA-----*/

    // Pendiente

    /**-----DIFICULTAD EXTRA-----*/
}