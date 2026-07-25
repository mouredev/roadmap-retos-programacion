/**
 * #06 RECURSIVIDAD
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    private static int num;
    private static int counter;

    private static void recursividadDesc(int inf, int sup) {
        if (inf <= sup) {
            System.out.printf("%d. %d%n", ++counter, sup--);
            recursividadDesc(inf, sup);
        }
    }

    private static void imprimirRecursividadDesc(int inf, int sup) {
        System.out.printf("Inicio de iteración recursividad de números del %d al %d:%n", inf, sup);
        recursividadDesc(inf, sup);
        System.out.printf("Fin de iteración recursividad de números del %d al %d!%n", inf, sup);
        counter = 0;
    }

    private static Long factorial(int num) {
        if (num == 0) return 1L;
        return num * factorial(--num);
    }

    private static void imprimirFactorial(int num) {
        if (num < 0) System.out.printf("El número %d es negativo. Debe ingresar números enteros positivos!%n", num);
        else System.out.printf("El factorial de %d es: %d%n", num, factorial(num));
    }

    private static Long fibonacci(int num) {
        if (num == 1) return 0L;
        else if (num == 2) return 1L;
        return fibonacci(--num) + fibonacci(--num);
    }

    private static void imprimirFibonacci(int num) {
        if (num <= 0) System.out.printf("El número %d debe ser entero positivo!%n", num);
        else System.out.printf("El valor del elemento %d° en la serie de Fibonacci es: %d%n", num, fibonacci(num));
    }

    private static int solveHanoi(int n, char source, char auxiliary, char destination) {
        if (n == 1) {
            System.out.println("Move disk 1 from " + source + " to " + destination);
            return ++counter;
        }
        solveHanoi(n - 1, source, destination, auxiliary);
        System.out.println("Move disk " + n + " from " + source + " to " + destination);
        solveHanoi(n - 1, auxiliary, source, destination);
        return ++counter;
    }

    public static void main(String[] args) {
        System.out.println("IMPRIMIR RECURSIVIDAD:");
        imprimirRecursividadDesc(-30, -20);
        imprimirRecursividadDesc(30, 60);
        /*
         * DIFICULTAD EXTRA
         */
        // Factorial
        System.out.println("CALCULAR FACTORIAL:");
        imprimirFactorial(-20);
        imprimirFactorial(0);
        imprimirFactorial(20);
        // Fibonacci
        System.out.println("CALCULAR FIBONACCI:");
        imprimirFibonacci(-5);
        imprimirFibonacci(0);
        imprimirFibonacci(5);
        imprimirFibonacci(10);
        System.out.printf("La cantidad de movimientos necesarios fue: %d%n",
                solveHanoi(5, 'A', 'B', 'C'));
    }
}
