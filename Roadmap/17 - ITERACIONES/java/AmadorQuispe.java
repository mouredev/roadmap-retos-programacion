
import java.util.ArrayList;
import java.util.BitSet;
import java.util.Iterator;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/* ╔══════════════════════════════════════╗
   ║ Autor:  Amador Q                     ║
   ║ Web  : https://amsoft.dev            ║
   ║ 2024                                 ║
   ╚══════════════════════════════════════╝
*/
public class Main {

    public static void main(String[] args) {
        iteration1();
        iteration2();
        iteration3();
        iteration4();
        iteration5();
        iteration6();
        System.out.println("Iteración utilizando recursividad");
        iterator7(1);
        iteration8();
    }

    public static void iteration1() {
        System.out.println("Iteración usando un bucle for");
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }
    }

    public static void iteration2() {
        int num = 1;
        System.out.println("Iteración usando un bucle while");
        while (num <= 10) {
            System.out.println(num);
            num++;
        }
    }

    public static void iteration3() {
        System.out.println("Iteración usando do while");
        int i = 1;
        do {
            System.out.println(i);
            i++;
        } while (i <= 10);
    }

    public static void iteration4() {
        System.out.println("Iteración utilizando un iterator");
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            list.add(i);
        }
        Iterator<Integer> iterator = list.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }

    public static void iteration5() {
        System.out.println("Iteración utilizando IntStream");
        IntStream numbers = IntStream.rangeClosed(1, 10);
        numbers.forEach(System.out::println);

    }

    public static void iteration6() {
        System.out.println("Iteración usando Api Stream (java 8)");
        Stream.iterate(1, n -> n + 1).limit(10)
                .forEach(System.out::println);
    }

    private static void iterator7(int i) {
        if (i <= 10) {
            System.out.println(i++);
            iterator7(i);
        }
    }

    public static void iteration8() {
        System.out.println("Iteración utilizando la clase BitSet");
        BitSet bitSet = new BitSet(10);
        bitSet.set(0, 10);
        for (int i = bitSet.nextSetBit(0); i >= 0; i = bitSet.nextSetBit(i + 1)) {
            System.out.println(i + 1);
        }
    }

}
