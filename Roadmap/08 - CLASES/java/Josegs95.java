import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class Josegs95 {
    public static void main(String[] args) {
        //Clases
        Persona p1 = new Persona("Jose", 29); //Crea un objeto 'p1' de la clase persona
        Persona p2 = new Persona("María", 27);
        Persona p3 = new Persona("Alberto", 41);

        System.out.println("p1: " + p1); //Out: 'p1: Nombre: Jose, edad: 29 años.'
        System.out.println("p2: " + p2); //Out: 'p2: Nombre: María, edad: 27 años.'
        System.out.println("p3: " + p3); //Out: 'p3: Nombre: Alberto, edad: 41 años.'

        p3.setName("Juan Alberto");

        System.out.println("p3: " + p3); //Out: 'p3: Nombre: Juan Alberto, edad: 41 años.'

        //Reto
        System.out.println("\n");
        retoFinal();
    }

    public static void retoFinal(){
        //Pila
        My_Stack<String> stack = new My_Stack<>();
        System.out.println(stack); //Out: 'Stack: []'

        stack.push("Element 1");
        stack.push("Element 2");
        stack.push("Element 3");
        stack.print(); //Out: '[Element 3] [Element 2] [Element 1]'
        System.out.println(stack); //Out: 'Stack: [Element 1, Element 2, Element 3]'

        System.out.println(stack.pop()); //Out: 'Element 3'
        stack.print(); //Out: '[Element 2] [Element 1]'
        System.out.println(stack); //Out: 'Stack: [Element 1, Element 2]'

        System.out.println("\n\n");
        //Cola
        My_Queue<String> queue = new My_Queue<>();
        System.out.println(queue); //Out: 'Queue: []'

        queue.add("Element 1");
        queue.add("Element 2");
        queue.add("Element 3");
        queue.print(); //Out: '[Element 1] [Element 2] [Element 3]'
        System.out.println(queue); //Out: 'Queue: [Element 1, Element 2, Element 3]'

        System.out.println(queue.poll()); //Out: 'Element 1'
        queue.print(); //Out: '[Element 2] [Element 3]'
        System.out.println(queue); //Out: 'Queue: [Element 2, Element 3]'
    }

    public static class Persona{
        private String name;
        private int age;

        Persona(String name, int age){
            this.name = name;
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        @Override
        public String toString(){
            return "Nombre: " + name + ", edad: " + age + " años.";
        }
    }

    //Reto
    public static class My_Stack<E>{
        List<E> elements;

        public  My_Stack(Collection<E> collection){
            if (collection == null)
                elements = new ArrayList<>();
            else
                elements = new ArrayList<>(collection);
        }
        public My_Stack(){
            this(null);
        }

        public E push(E element){
            elements.add(element);
            return element;
        }

        public E pop(){
            if (size() == 0)
                return null;

            return elements.remove(size() - 1);
        }

        public int size(){
            return elements.size();
        }

        public void print(){
            List<E> cloneList = new ArrayList<>(elements);
            Collections.reverse(cloneList);
            for (E element : cloneList)
                System.out.print("[" + element + "] ");
            System.out.println();
        }

        @Override
        public String toString() {
            return "Stack: " + elements.toString();
        }
    }

    public static class My_Queue<E>{
        List<E> elements;

        public  My_Queue(Collection<E> collection){
            if (collection == null)
                elements = new ArrayList<>();
            else
                elements = new ArrayList<>(collection);
        }
        public My_Queue(){
            this(null);
        }

        public E add(E element){
            elements.add(element);
            return element;
        }

        public E poll(){
            if (size() == 0)
                return null;

            return elements.remove(0);
        }

        public int size(){
            return elements.size();
        }

        public void print(){
            for (E element : elements)
                System.out.print("[" + element + "] ");
            System.out.println();
        }

        @Override
        public String toString() {
            return "Queue: " + elements.toString();
        }
    }
}
