import java.util.Stack;
import java.util.Queue;
import java.util.*;

public class simonguzman {
    public static void main(String[] args) {
        //Pilas
        Stack<String> books = new Stack<>();
        //Agregando elementos a la piila
        books.push("Cien años de soledad");
        books.push("El amor en los tiempos del colera");
        books.push("El pianista del gueto de varsovia");
        //Monstrando la pila
        System.out.println(books);
        //Mostrar el ultimo elemento de la pila, el ultimo que entro en esta
        System.out.println("Ultimo elemento de la pila: "+ books.peek());
        //Eliminar el ultimo elemento de la pila, el ultimo que entro
        books.pop();
        //Mostrar la pila actualizada
        System.out.println(books);
        //Buscar la posicion del elemento en la pila
        System.out.println("Posicion del libro: "+books.search("Cien años de soledad"));

        //Colas
        Queue<String> cola = new LinkedList<>();
        //Añadir elementos a la cola
        cola.add("Simon");
        cola.add("Julian");
        cola.add("Camilo");
        //Mostrar la cola
        System.out.println(cola);
        //Remover elemento
        cola.remove();
        System.out.println(cola);
        //Alternativa a remover elemento
        cola.poll();
        System.out.println(cola);
        //Consultar el primer elemento de la cola
        System.out.println(cola.element());
        System.out.println(cola.peek());
        //Tamaño de la cola
        System.out.println(cola.size());
    }

    public static boolean validarColaVacia(Queue<String> cola){
        return !cola.isEmpty();
    }


}
