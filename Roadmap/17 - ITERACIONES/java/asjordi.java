import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) {
        printNumbers();
        iterate();
    }

    /**
     * EJERCICIO:
     * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
     * números del 1 al 10 mediante iteración.
     */
    static void printNumbers() {
        // Forma 1: Usando un for
        for (int i = 1; i <= 10 ; i++) System.out.println(i);

        // Forma 2: Iterando un List con forEach
        for (int i : Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) System.out.println(i);

        // Forma 3: Iterando un IntStream
        IntStream.rangeClosed(1, 10).forEach(System.out::println);
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Escribe el mayor número de mecanismos que posea tu lenguaje
     * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
     */

    static void iterate() {
        List<Integer> nums = List.of(1, 2, 3, 4, 5);

        for (int i = 0; i < nums.size(); i++) System.out.println(nums.get(i));

        for (Integer num : nums) System.out.println(num);

        nums.forEach(System.out::println);

        nums.stream().forEach(n -> System.out.println(n));

        int i = 0;
        while (i < nums.size()) {
            System.out.println(nums.get(i));
            i++;
        }

        Iterator<Integer> iterator = nums.iterator();
        while (iterator.hasNext()) System.out.println(iterator.next());

        Iterator<Integer> it = nums.iterator();
        it.forEachRemaining(num -> System.out.println(num));

        ListIterator<Integer> listIterator = nums.listIterator();
        while (listIterator.hasNext()) System.out.println(listIterator.next());

        nums.spliterator().forEachRemaining(System.out::println);

        Arrays.stream(nums.toArray()).forEach(n -> System.out.println(n));

        Stream.of(nums).forEach(System.out::println);

    }
}
