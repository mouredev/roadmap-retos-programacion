public class ycanas {

    public static void myFunc(int n) {
        if (n < 0)
            return;

        System.out.println(n);
        myFunc(n - 1);
    }


    public static int Factorial(int n) {
        if (n <= 2)
            return n;

        return Factorial(n - 1) * n;
    }


    public static int Fibonacci(int n) {
        if (n <= 1)
            return n;

        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }

    public static void main(String[] args) {
        // Ejercicio
        System.out.println("Ejercicio:");
        myFunc(100);

        // Extra
        System.out.println("Factorial:");
        System.out.println(Factorial(5));

        System.out.println("Fibonacci:");
        System.out.println(Fibonacci(8));
    }
}
