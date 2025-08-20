public class AnaLauDB {

    // Funcion recursiva que imprima todos los numeros del 1 al 100
    public static void NUmeros(int n) {
        if (n > 100) {
            return;
        }
        System.out.println(n);
        NUmeros(n + 1);
    }

    // Funcion recursiva para factorial
    public static int Facto(int x) {
        if (x == 0) {
            return 1;
        } else {
            return x * Facto(x - 1);
        }
    }

    // Funcion recursiva para Fibonacci
    public static int Fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }

    public static void main(String[] args) {
        NUmeros(1);

        int numero = 5;
        System.out.println("Factorial de " + numero + " es: " + Facto(numero));

        int fiboNumero = 10;
        System.out.println("Fibonacci de " + fiboNumero + " es: " + Fibonacci(fiboNumero));
    }
}
