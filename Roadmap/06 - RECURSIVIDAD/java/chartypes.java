public class chartypes {
    public static void main(String[] args) {
        iterator(100, 0);
        System.out.println("\nExecrice:");
        System.out.println(factorial(6));
        System.out.println(getFromFibonacci(8));

    }

    static int iterator(int start, int stop) {
        System.out.print(start + " ");
        if (start == stop)
            return stop;
        return iterator(start - 1, stop);
    }

    static int factorial(int number) {
        if (number == 1)
            return 1;
        return number * factorial(number - 1);
    }

    static int getFromFibonacci(int position) {
        if (position <= 0 || position == 1)
            return 0;
        else if (position == 2)
            return 1;
        return getFromFibonacci(position - 1) + getFromFibonacci(position - 2);

    }

}