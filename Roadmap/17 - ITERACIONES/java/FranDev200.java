import java.util.ArrayList;
import java.util.Iterator;
import java.util.ListIterator;
import java.util.Spliterator;
import java.util.stream.Stream;

public class FranDev200 {


    static void main() {

        /*

        EJERCICIO:
         * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
         * números del 1 al 10 mediante iteración.

         */

        // Mecanismo 1
        for(int i = 1; i <= 10; i++){
            System.out.print(i + ", ");
        }

        System.out.println();

        // Mecanismo 2
        int contador = 1;
        while(contador <= 10){

            System.out.print(contador + ", ");
            contador++;

        }

        System.out.println();

        // Mecanismo 3

        contador = 1;
        do{

            System.out.print(contador + ", ");
            contador++;

        }while(contador <= 10);

        /*

        DIFICULTAD EXTRA (opcional):
         * Escribe el mayor número de mecanismos que posea tu lenguaje
         * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?


         */

        System.out.println("\nEJERCICIO EXTRA");
        System.out.println("===============");

        System.out.println("- - - - - - ");
        System.out.println("Iteracion 1");
        System.out.println("- - - - - - ");
        iteracion1();

        System.out.println("\n- - - - - - ");
        System.out.println("Iteracion 2");
        System.out.println("- - - - - - ");
        iteracion2();

        System.out.println("\n- - - - - - ");
        System.out.println("Iteracion 3");
        System.out.println("- - - - - - ");
        iteracion3();

        System.out.println("\n- - - - - - ");
        System.out.println("Iteracion 4");
        System.out.println("- - - - - - ");
        iteracion4(1);

        System.out.println("\n- - - - - - ");
        System.out.println("Iteracion 5");
        System.out.println("- - - - - - ");
        iteracion5();

        System.out.println("\n- - - - - - ");
        System.out.println("Iteracion 6");
        System.out.println("- - - - - - ");
        iteracion6();

        System.out.println("\n- - - - - - ");
        System.out.println("Iteracion 7");
        System.out.println("- - - - - - ");
        iteracion7();

        System.out.println("\n- - - - - - ");
        System.out.println("Iteracion 8");
        System.out.println("- - - - - - ");
        iteracion8();

        System.out.println("\n- - - - - - ");
        System.out.println("Iteracion 9");
        System.out.println("- - - - - - ");
        iteracion9();

        System.out.println("\n- - - - - - ");
        System.out.println("Iteracion 10");
        System.out.println("- - - - - - ");
        iteracion10();

    }

    // Bucle for
    static public void iteracion1(){

        for(int i = 1; i <= 10; i++){
            System.out.print(i + ", ");
        }

    }

    // Bucle while
    static public void iteracion2(){

        int contador = 1;
        while(contador <= 10){

            System.out.print(contador + ", ");
            contador++;

        }

    }

    // Bucle do-while
    static public void iteracion3(){

        int contador = 1;
        do{

            System.out.print(contador + ", ");
            contador++;

        }while(contador <= 10);

    }

    // Recursividad
    static public void iteracion4(int contador){

        System.out.print(contador + ", ");
        contador ++;

        if(contador <= 10){

            iteracion4(contador);

        }

    }

    // Iterador
    static public void iteracion5(){

        ArrayList<Integer> lista = new ArrayList<>();
        for(int i = 1; i <= 10; i++){
            lista.add(i);
        }

        Iterator<Integer> iterator = lista.iterator();
        while(iterator.hasNext()){
            System.out.print(iterator.next() + ", ");
        }

    }

    // Stream, forEach (lambda)
    static public void iteracion6(){

        ArrayList<Integer> lista = new ArrayList<>();
        for(int i = 1; i <= 10; i++){
            lista.add(i);
        }

        Stream<Integer> stream = lista.stream();

        stream.forEach(n -> System.out.print(n + ", "));

    }

    // Iterador y Stream
    static public void iteracion7(){

        ArrayList<Integer> lista = new ArrayList<>();
        for(int i = 1; i <= 10; i++){
            lista.add(i);
        }

        Stream<Integer> stream = lista.stream();
        Iterator<Integer> iterator = stream.iterator();
        while(iterator.hasNext()){
            System.out.print(iterator.next() + ", ");
        }

    }

    // Iterador con lambda
    static public void iteracion8(){

        ArrayList<Integer> lista = new ArrayList<>();
        for(int i = 1; i <= 10; i++){
            lista.add(i);
        }

        Iterator<Integer> iterator = lista.iterator();

        iterator.forEachRemaining(s-> System.out.print(s+", "));

    }

    // Spliterator
    static public void iteracion9(){

        ArrayList<Integer> lista = new ArrayList<>();

        for(int i = 1; i <= 10; i++){
            lista.add(i);
        }

        Spliterator<Integer> spliterator = lista.spliterator();

        spliterator.forEachRemaining(s-> System.out.print(s+", "));

    }

    // ListIterator
    static public void iteracion10(){

        ArrayList<Integer> lista = new ArrayList<>();
        for(int i = 1; i <= 10; i++){
            lista.add(i);
        }

        ListIterator<Integer> listIterator =  lista.listIterator();

        listIterator.forEachRemaining(n -> System.out.print(n + ", "));


    }

}
