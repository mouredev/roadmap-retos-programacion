import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

public class Worlion {


/*
 * EJERCICIO: Clases en JAVA
 */
    class Developer {
        private String name ="";
        private int age = 0;
        private List<String> languages = new ArrayList<>();

        public Developer(String name, int age, Collection<String> languages){
            this.name = name;
            this.age = age;
            this.languages.addAll(languages);
        }

        public void addLanguage(String newLanguage) {
            if(!this.languages.contains(newLanguage)) {
                this.languages.add(newLanguage);
            }
        }

        public String toString() {
            StringBuilder s = new StringBuilder("\"Developer\": {");

            s.append("\n\t\"this.name\": \"" + this.name + "\",");
            s.append("\n\t\"this.age\": \"" + this.age + "\",");
            s.append("\n\t\"this.languages\": " + this.languages );
            s.append("\n}");

            return s.toString();
        }
    }

/*
 * DIFICULTAD EXTRA (opcional):
 */


class Stack<T> {
    private List<T> stack = new LinkedList<T>();

    public T pop() {
        if(stack.isEmpty()) {
            //throw new Exception("Pila vacia!");
            System.err.println("Pila vacia!");
            return null;
        }
        T element = stack.getLast();
        stack.removeLast();
        return element;
    }

    public void push(T element) {
        stack.add(element);
    }

    public void printStack() {
        System.out.println("Stack content:" + stack);
    }

    public int size() {
        return stack.size();
    }

    public boolean isEmpty() {
        return stack.isEmpty();
    }

    public T top(){
        return stack.getLast();
    }

    public void clear() {
        stack.clear();
    }

    public String toString() {
        return stack.toString();
    }
}

class Queue<T> {
    private List<T> queue = new LinkedList<T>();

    public T get() {
        if(queue.isEmpty()) {
            //throw new Exception("Pila vacia!");
            System.err.println("Cola vacia!");
            return null;
        }
        T element = queue.getFirst();
        queue.remove(0);
        return element;
    }
    
    public void put(T element) {
        queue.add(element);
    }

    public void printQueue() {
        System.out.println("Queue content:" + queue);
    }

    public int size(){
        return queue.size();
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }

    public String toString() {
        return queue.toString();
    }
}

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run() {
    
        Developer me = new Developer("Worlion", 40, List.of("Java", "Python"));
        System.out.println(me);

        testQueueAndStack();
    }

    private void testQueueAndStack() {

        System.out.println(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");
        
        String[] values = {"A", "B", "C", "D"};

        Queue<String> queue = new Queue<>();
        Stack<String> stack = new Stack<>();

        for(String s: values) {
            queue.put(s);
            stack.push(s);
        }
        System.out.println("Contenido de la cola: "+queue);
        System.out.println("Contenido de la pila: "+stack);

        int i = 0;
        int errorCount = 0;

        while(!queue.isEmpty()) {
            if(!values[i++].equals(queue.get())) {
                System.out.println("Este no coincide ("+i+") en la cola!");
                errorCount++;
            }
        }
        
        if(errorCount == 0) {
            System.out.println("Cola sin errores");
        }

        i = values.length-1;
        errorCount = 0;
        while (!stack.isEmpty()) {
            if(!values[i--].equals(stack.pop())) {
                System.out.println("Este no coincide ("+i+") en la pila!");
                errorCount++;
            }
        }
                
        if(errorCount == 0) {
            System.out.println("Pila sin errores");
        }
    }
}
