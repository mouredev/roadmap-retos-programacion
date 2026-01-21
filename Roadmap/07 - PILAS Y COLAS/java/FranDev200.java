import java.util.ArrayList;

public class FranDev200 {

    static ArrayList<Integer> arrayStack = new ArrayList<>();
    static ArrayList<Integer> arrayQueue = new ArrayList<>();

    static void main() {

        /*
            Implementa los mecanismos de introducción y recuperación de elementos propios de las
            pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
            o lista (dependiendo de las posibilidades de tu lenguaje).
         */

        // Añadimos elementos al Stack
        for(int i = 0; i < 5; i++){
            push(i);
        }

        // Añadimos elementos al Queue
        for(int i = 0; i < 5; i++){
            offer(i);
        }

        System.out.println("STACK");
        System.out.println(arrayStack);
        System.out.println("--------------");
        System.out.println("- Eliminamos y mostramos el primer elemento: " + pop());
        System.out.println("==============================================");
        System.out.println("STACK");
        System.out.println(arrayStack);
        System.out.println("--------------");
        System.out.println("- Eliminamos y mostramos el primer elemento: " + pop());
        System.out.println("==============================================");
        System.out.println("STACK");
        System.out.println(arrayStack);
        System.out.println("--------------");
        System.out.println("- Mostramos el primer elemento: " + peek());
        System.out.println("==============================================");
        System.out.println("STACK");
        System.out.println(arrayStack);
        System.out.println("--------------");
        System.out.println("- Esta vacio el stack: " + empty());
        System.out.println("- Numero de la posicion 3: " + search(3));
        System.out.println("- Numero de la posicion 5: " + search(5));
        System.out.println("=============================================\n\n");
        System.out.println("QUEUE");
        System.out.println(arrayQueue);
        System.out.println("--------------");
        System.out.println("- Eliminamos y mostramos el primer elemento: " + poll());
        System.out.println("==============================================");
        System.out.println("QUEUE");
        System.out.println(arrayQueue);
        System.out.println("--------------");
        System.out.println("- Eliminamos y mostramos el primer elemento: " + poll());
        System.out.println("==============================================");
        System.out.println("QUEUE");
        System.out.println(arrayQueue);
        System.out.println("--------------");
        System.out.println("- Mostramos el primer elemento: " + element());
        System.out.println("==============================================");
        System.out.println("QUEUE");
        System.out.println(arrayQueue);
        System.out.println("--------------");
    }

    // METODOS PARA EL STACK
    public static void push(int i){

        arrayStack.addFirst(i);

    }

    public static int pop(){

        int result =  arrayStack.getFirst();

        if(!empty()){
            arrayStack.removeFirst();
            return result;

        }else{
            System.out.println("El stack esta vacio.");
            return 0;
        }

    }

    public static Integer peek(){

        if(!empty()){
            return arrayStack.getFirst();
        }else{
            System.out.println("El array esta vacio.");
            return null;
        }

    }

    public static boolean empty(){

        return arrayStack.isEmpty();

    }

    public static int search(int position){

        if(position > arrayStack.size()){
            System.out.println("Esa posición excede el tamaño del stack.");
            return 0;
        }

        return arrayStack.get(position - 1);

    }

    // METODOS PARA LA QUEUE
    public static boolean offer(int i){

        arrayQueue.addLast(i);
        return true;

    }

    public static Integer poll(){

        int result =  arrayQueue.getFirst();

        if(!empty()){
            arrayQueue.removeFirst();
            return result;

        }else{
            System.out.println("La cola esta vacio.");
            return null;
        }

    }

    public static Integer element(){

        if(!empty()){
            return arrayStack.getFirst();
        }else{
            System.out.println("El array esta vacio.");
            return null;
        }

    }

}
