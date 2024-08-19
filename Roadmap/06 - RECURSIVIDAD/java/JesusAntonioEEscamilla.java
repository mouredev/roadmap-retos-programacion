

/** #06 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        System.out.println("Recursividad");
        imprimirNúmeros(100);
    //---EXTRA---
        System.out.println("Factorial");
        System.out.println(factorial(5));
        System.out.println("Fibonacci");
        System.out.println(fibonacci(10));
    }

    //---EJERCIÓ---
    // Definiendo la función
    public static void imprimirNúmeros(int n) {
        if (n < 0) {
            return;
        }
        System.out.println(n);
        // Aquí es donde se realizar la Recursividad
        imprimirNúmeros(n - 1);
    }

    /**-----DIFICULTAD EXTRA-----*/

    // Factorial
    public static int factorial(int n){
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    // Fibonacci
    public static int fibonacci(int n){
        if (n == 0) {
            return 0;
        } else if(n == 1) {
            return 1;
        }
        return fibonacci(n - 1) + fibonacci(n -2);
    }

    /**-----DIFICULTAD EXTRA-----*/
}