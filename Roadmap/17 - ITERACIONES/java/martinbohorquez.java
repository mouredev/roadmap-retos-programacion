import java.util.*;

/**
 * #17 ITERACIONES
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    public static void main(String[] args) {
        // 1. for
        System.out.println("1. Iteración usando 'for':");
        for (int i = 1; i <= 10; i++) System.out.println(i);

        // 2. while
        System.out.println("2. Iteración usando 'while':");
        int i = 1;
        while (i <= 10) System.out.println(i++);

        // 3. recursividad
        System.out.println("3. Iteración usando 'función recursiva':");
        count10(1);

        /*
         * DIFICULTAD EXTRA
         */
        //4. Array y for
        System.out.println("4. Iteración usando 'array con fori'");
        int[] numbers = {6, 5, 4, 3, 2, 1};
        for (int number : numbers) System.out.println(number);

        //5. Stream y forEach
        System.out.println("5. Iteración usando 'stream con forEach'");
        Arrays.stream(numbers).forEach(System.out::println);

        // 6. Lista, reversed y forEach
        System.out.println("6. Iteración usando 'lista con forEach(reversed)'");
        Arrays.asList(1, 2, 3, 4).reversed().forEach(System.out::println);

        //7 String, split, stream y forEach
        System.out.println("7. Iteración para una 'string' (sorted) usando 'split, stream y forEach'");
        String word = "strawberry";
        Arrays.stream(word.split("")).sorted().forEach(System.out::println);

        // 8. Map, keySet, values, forEach
        System.out.println("8. Iteración para una 'map' por keys/values usando 'forEach'");
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "a");
        map.put(2, "b");
        map.put(3, "c");
        map.put(4, "d");
        map.put(5, "e");
        map.keySet().forEach(System.out::println);
        map.values().forEach(System.out::println);
        map.forEach((key, value) -> System.out.println(key + ": " + value));

        // 9. do-while
        System.out.println("9. Iteración usando 'do-while':");
        i = 10;
        do {
            System.out.println(i--);
        } while (i >= 1);

        // 10. set, iterator
        System.out.println("10. Iteración de un 'set' usando 'iterator':");
        Set<String> set = new HashSet<>(Arrays.asList("a", "b", "c", "d", "e"));
        Iterator<String> iterator = set.iterator();
        iterator.forEachRemaining(System.out::println);

    }

    private static void count10(int i) {
        if (i <= 10) {
            System.out.println(i);
            count10(++i);
        }
    }
}
