public class Main {

    public static void main(String[] args) {

        printNumber(100);

        System.out.println("Factorial de 5: " + factorial(5));

    }


    /**
     * Función recursiva que imprime los números desde n hasta 0
     * @param n
     */
    public static void printNumber(int n) {
        if (n >= 0) {
            System.out.println(n);
            printNumber(n - 1);
        }
    }

    /**
     * Función recursiva que calcula el factorial de un número
     * @param n número del que se quiere calcular el factorial
     * @return factorial de n
     */
    public static int factorial(int n) {
        if (n == 0) return 1;
        else return n * factorial(n - 1);
    }

    /**
     * Función recursiva que calcula el n-ésimo número de la serie de Fibonacci
     * @param n posición del número en la serie
     * @return n-ésimo número de la serie de Fibonacci
     */
    public static int fibonacci(int n) {
        if (n <= 1) return n;
        else return fibonacci(n - 1) + fibonacci(n - 2);
    }

}
