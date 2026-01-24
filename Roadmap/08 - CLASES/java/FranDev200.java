import java.util.ArrayList;

public class FranDev200 {

    static void main() {

        /*

            EJERCICIO:
            * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
            * atributos y una función que los imprima (teniendo en cuenta las posibilidades de tu lenguaje).
            * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos utilizando su función.

         */

        Person person1 = new Person("Francisco", 20, "Futuro desarrollador de Software", 1.78, false);
        viewContent(person1);

        person1.setAge(21);
        person1.setCouple(true);
        viewContent(person1);


        /*

         * DIFICULTAD EXTRA (opcional):
         * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas en el ejercicio número 7 de la ruta de estudio)

         */

        // CLASE STACK / PILA
        StackFran<Object> stackMascotas = new StackFran<>();
        stackMascotas.push("Perro");
        stackMascotas.push("Gato");
        stackMascotas.push("Loro");
        stackMascotas.push("Hamster");

        System.out.println("¿Esta vacio?: " + stackMascotas.isEmpty());
        System.out.println("Elemento más arriba: " + stackMascotas.peek());
        System.out.println("Elemento más arriba: " + stackMascotas.pop());
        System.out.println("Elemento más arriba: " + stackMascotas.peek());
        System.out.println("Tamaño del stack: " + stackMascotas.size());
        System.out.print("Elementos del stack: ");
        stackMascotas.viewAll();
        stackMascotas.clear();
        System.out.print("Elementos del stack: ");
        stackMascotas.viewAll();

        // CLASE QUEUE / COLA
        QueueFran<Object> queueComida = new QueueFran<>();
        queueComida.offer("Tomates");
        queueComida.offer("Pollo");
        queueComida.offer("Lechuga");
        queueComida.offer("huevos");

        System.out.println("¿Esta vacio?: " + queueComida.isEmpty());
        System.out.println("Elemento más arriba: " + queueComida.peek());
        System.out.println("Elemento más arriba: " + queueComida.poll());
        System.out.println("Elemento más arriba: " + queueComida.peek());
        System.out.println("Numero de elementos del queue: " + queueComida.size());
        System.out.print("Elementos del queue: ");
        queueComida.viewAll();
        queueComida.clear();
        System.out.print("Elementos del queue: ");
        queueComida.viewAll();

    }

    private static void viewContent(Person person1) {
        System.out.println("\n" + person1.getName() + " (" + person1.getAge() + " años)");
        System.out.println("=".repeat(person1.getName().length() + 10));
        System.out.println("Trabajo: " + person1.getJob());
        System.out.println("Estatura: " + person1.getHeight());
        System.out.println("Pareja: " + person1.isCouple());
        System.out.println("=".repeat(person1.getName().length() + 10));
    }


}

class Person{

    private String name;
    private int age;
    private String job;
    private double height;
    private boolean couple;

    public Person(){
    }

    public Person(String name, int age, String job, double height, boolean couple){
        setName(name);
        setAge(age);
        setJob(job);
        setHeight(height);
        setCouple(couple);
    }

    public String getName() { return name; }

    public void setName(String name) { this.name = name; }

    public int getAge() { return age; }

    public void setAge(int age) { this.age = age; }

    public String getJob() { return job; }

    public void setJob(String job) { this.job = job; }

    public double getHeight() { return height; }

    public void setHeight(double height) { this.height = height; }

    public boolean isCouple() { return couple; }

    public void setCouple(boolean couple) { this.couple = couple; }
}

class StackFran<T>{

    private ArrayList<T> stack;

    public StackFran(){

        this.stack = new ArrayList<>();

    }

    // Añade elemento
    public void push(T i){

        stack.addFirst(i);

    }

    // Muestra y elimina el primer elemento
    public T pop(){

        T result = stack.getFirst();
        stack.remove(result);

        if(stack.isEmpty()){
            return null;
        }else{
            return result;
        }

    }

    // Muestra el primer elemento
    public T peek(){

        if(!isEmpty()){
            return stack.getFirst();
        }else{
            System.out.println("El array esta vacio.");
            return null;
        }

    }

    // Comprueba si esta vacio el stack
    public boolean isEmpty(){

        return stack.isEmpty();

    }

    // Numero de elementos del stack
    public int size(){

        return stack.size();

    }

    // Ver todos los elementos del stack
    public void viewAll(){

        System.out.print("[");
        for (T element: stack){
            if(!element.equals(stack.getLast())){
                System.out.print(element + ", ");
            }else{
                System.out.print(element);
            }

        }
        System.out.println("]");
    }

    // Limpiar el stack
    public void clear(){
        System.out.println("Elementos borrados.");
        stack.clear();
    }
}

class QueueFran<T>{

    private ArrayList<T> queue;

    public QueueFran(){

        this.queue = new ArrayList<>();

    }

    // Añado un elemento al final del queue
    public void offer(T i){
        queue.add(i);
    }

    // Muestro y elimino el primer elemento del queue
    public T poll(){
        T result = queue.getFirst();
        queue.remove(result);

        if(queue.isEmpty()){
            return null;
        }else{
            return result;
        }
    }

    // Muestro el primer elemento del queue
    public T peek(){

        if(!isEmpty()){
            return queue.getFirst();
        }else{
            System.out.println("La cola está vacía.");
            return null;
        }
    }

    // Compruebo si está vacía el queue
    public boolean isEmpty(){

        return queue.isEmpty();

    }

    // Devuelvo el tamaño del queue
    public int size(){

        return queue.size();

    }

    // Muestro todos los elementos del queue
    public void viewAll(){

        System.out.print("[");
        for (T element: queue){
            if(!element.equals(queue.getLast())){
                System.out.print(element + ", ");
            }else{
                System.out.print(element);
            }

        }
        System.out.println("]");
    }

    // Limpiar el queue
    public void clear(){
        System.out.println("Elementos borrados.");
        queue.clear();
    }

}
