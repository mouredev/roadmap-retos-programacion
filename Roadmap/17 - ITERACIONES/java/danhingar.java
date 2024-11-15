import java.util.Iterator;
import java.util.List;
import java.util.stream.IntStream;

public class danhingar {

    public static void main(String[] args) {

        for (int i = 1; i < 11; i++) {
            System.out.println(i);
        }

        int j = 1;
        while (j < 11) {
            System.out.println(j);
            j++;
        }

        int x = 1;
        do {
            System.out.println(x);
            x++;
        } while (x < 11);

        List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Extra 1

        IntStream.range(1, 10).forEach(i -> System.out.println(i));

        // Extra 2

        for (Integer number : numbers) {
            System.out.println(number);
        }

        // Extra 3
        numbers.forEach(i -> System.out.println(i));

        //Extra 4
        Iterator<Integer> i = numbers.iterator();
        while(i.hasNext()){
            System.out.println(i.next());
        }

    }

}
