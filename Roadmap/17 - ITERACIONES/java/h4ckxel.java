import java.util.Arrays;
import java.util.List;

public class h4ckxel{

    public static void main(String[] args) {
        // exercise
        System.out.println();
        System.out.println(1);
        for (int i = 1; i < 11; i++)
            System.out.print(i);

        System.out.println();
        System.out.println(2);
        int iterator = 1;
        while (iterator <= 10) {
            System.out.print(iterator);
            iterator++;
        }

        System.out.println();
        System.out.println(3);
        iterator = 1;
        do {
            System.out.print(iterator);
            iterator++;

        } while (iterator <= 10);

        // extra
        System.out.println();
        System.out.println(4);
        int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        for (int i : numbers)
            System.out.print(i);

        System.out.println();
        System.out.println(5);
        List<Integer> numbersList = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        numbersList.stream().forEach(System.out::print);

        System.out.println();
        System.out.println(6);
        recursiveIterator(1);

    }

    private static void recursiveIterator(int number) {
        if (number > 10) {
            return;
        }
        System.out.print(number);
        number++;
        recursiveIterator(number);
    }

}