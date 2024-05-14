import java.util.LinkedList;
import java.util.List;

/*
 * EJERCICIO: Colas y Pilas
 */

class Stack<T> {
    private List<T> stack = new LinkedList<T>();

    public T pop() {
        if(this.stack.isEmpty()) {
            //throw new Exception("Pila vacia!");
            System.err.println("Pila vacia!");
            return null;
        }
        T element = stack.getLast();
        stack.removeLast();
        return element;
    }

    public void push(T element) {
        this.stack.add(element);
    }

}

class Queue<T> {
    private List<T> queue = new LinkedList<T>();

    public T get() {
        if(this.queue.isEmpty()) {
            //throw new Exception("Pila vacia!");
            System.err.println("Pila vacia!");
            return null;
        }
        T element = queue.getFirst();
        queue.remove(0);
        return element;
    }
    
    public void add(T element) {
        this.queue.add(element);
    }
}

public class Worlion {

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run() {
        
    }
}
