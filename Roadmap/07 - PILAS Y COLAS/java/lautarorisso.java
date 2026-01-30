import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class LogicaJava07 {
    
    public static void main(String[] args) {
        
        // 1.
        
        // Queue
        Queue<String> cola = new LinkedList<>();

        cola.add("Cliente 1");
        cola.add("Cliente 2");

        cola.poll(); // elimina el primero

        System.out.println(cola);

        // Stack
        Stack<Integer> pila = new Stack<>();

        pila.push(10);
        pila.push(20);

        pila.pop(); // elimina el último

        System.out.println(pila);
        
    }
}
