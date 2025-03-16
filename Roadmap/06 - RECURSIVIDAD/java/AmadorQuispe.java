public class AmadorQuispe {
    public static void main(String[] args) {
        // Una función recursiva es una función que llama a sí misma para resolver un
        // problema, para evitar loop infinito debe tener una condición base donde ya
        // no sea necesario llamarse a la función.
        int number = 7;
        // Ejercicio 01, imprimir cuenta regresiva dado un número hasta llegar a cero.
        countDown(100); // sin recursividad
        countDownRecursive(100); // con recursividad

        // Ejercicio 02, Calcular el factorial de un número concreto
        System.out.println("El factorial del número " + number + " es :" + factorial(number));// sin recursividad.
        System.out.println("El factorial del número " + number + " es :" + factorialRecursive(number));// con
                                                                                                       // recursividad.

        // Ejercicio 03, Calcular el valor de un elemento concreto (según su posición)
        System.out.println("El término " + number + " de la secuencia de Fibonacci es: " + fibonacci(number)); // sin
                                                                                                               // recursividad.
        System.out.println("El término " + number + " de la secuencia de Fibonacci es: " + fibonacciRecursive(number));// con
                                                                                                                       // recursividad.

    }

    public static void countDown(int n) {
        for (int i = n; i >= 0; i--) {
            System.out.println(i);
        }
        System.out.println("termino la cuenta regresiva");
    }

    public static void countDownRecursive(int n) {
        if (n < 0) {
            System.out.println("termino la cuenta regresiva");
            return;
        }
        System.out.println("cuenta " + n);
        countDownRecursive(--n);
    }

    public static int factorial(int n) {
        int result = n;
        for (int i = n; i >= 2; i--) {
            result *= i - 1;
        }
        return result;
    }

    public static int factorialRecursive(int n) {
        if (n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }

        int prev1 = 0;
        int prev2 = 1;
        int fib = 0;

        for (int i = 2; i <= n; i++) {
            fib = prev1 + prev2;
            prev1 = prev2;
            prev2 = fib;
        }

        return fib;
    }

    public static int fibonacciRecursive(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
