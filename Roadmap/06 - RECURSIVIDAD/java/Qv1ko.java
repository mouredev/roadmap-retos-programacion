public class Qv1ko {

    public static void main(String[] args) {
        
        func(0);

        System.out.println("---");

        System.out.println(fact(5));

        System.out.println("---");

        System.out.println(fib(5));

    }

    private static void func(int number) {

        System.out.println(number);

        number++;

        if (number <= 100) {
            func(number);
        }

    }

    private static int fact(int number) {
        if (number <= 0) {
            return 0;
        } else if (number == 1) {
            return 1;
        } else {
            return number * fact(number - 1);
        }
    }

    private static int fib(int pos) {
        if (pos <= 1) {
            return 0;
        } else if (pos == 2 || pos == 3) {
            return 1;
        } else {
            return fib(pos - 1) + fib(pos - 2);
        }
    }

}
