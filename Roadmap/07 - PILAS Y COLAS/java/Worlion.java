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

    public void printStack() {
        System.out.println("Stack content:" + stack);
    }
}

class Queue<T> {
    private List<T> queue = new LinkedList<T>();

    public T get() {
        if(this.queue.isEmpty()) {
            //throw new Exception("Pila vacia!");
            System.err.println("Cola vacia!");
            return null;
        }
        T element = queue.getFirst();
        queue.remove(0);
        return element;
    }
    
    public void put(T element) {
        this.queue.add(element);
    }

    public void printQueue() {
        System.out.println("Queue content:" + queue);
    }
}

public class Worlion {

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run() {
        playWithStack();
        playWithQueue();
    }

    private void playWithStack(){
        System.out.println("Jugando con la pila...");
        Stack<Integer> stack = new Stack<Integer>();
        System.out.println("Añado 4 valores:");
        stack.push(3);
        stack.push(65);
        stack.push(1);
        stack.push(99);
        stack.printStack();

        System.out.println("elimino el primero: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();

        System.out.println("elimino otro: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();

        System.out.println("elimino otro: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();

        System.out.println("elimino otro: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();
        
        System.out.println("elimino otro: ");
        System.out.println("pop: {" + stack.pop() + "}");
        stack.printStack();

    }

    private void playWithQueue(){
        System.out.println("Jugando con la cola...");
        Queue<String> queue = new Queue<String>();

        System.out.println("Añado 4 valores");
        queue.put("a");
        queue.put("b");
        queue.put("c");
        queue.put("d");
                
        queue.printQueue();
        
        System.out.println("elimino el primero: ");
        System.out.println("get: {" + queue.get() + "}");
        queue.printQueue();
        System.out.println("elimino otro: ");
        System.out.println("get: {" + queue.get() + "}");
        queue.printQueue();
        System.out.println("get: {" + queue.get() + "}");
        queue.printQueue();
        System.out.println("get: {" + queue.get() + "}");
        queue.printQueue();
        System.out.println("get: {" + queue.get() + "}");
    }

}
