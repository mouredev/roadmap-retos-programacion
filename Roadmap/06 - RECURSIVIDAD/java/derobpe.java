
/**
 * derobpe.java
 * 
 * Descripción breve de la clase o el programa.
 * 
 * @autor derobpe
 * @version 1.0
 * @fecha 07/02/2024
 *
 *        EJERCICIO:
 *        Entiende el concepto de recursividad creando una función recursiva que
 *        imprima números del 100 al 0.
 *
 *        DIFICULTAD EXTRA (opcional):
 *        Utiliza el concepto de recursividad para:
 *        - Calcular el factorial de un número concreto (la función recibe ese
 *        número).
 *        - Calcular el valor de un elemento concreto (según su posición) en la
 *        sucesión de Fibonacci (la función recibe la posición).
 */

import java.util.Scanner;

public class derobpe {
    public static void main(String[] args) {
        // Ejercicio Imprimir Recursivamente
        imprimirRecursivamenteNNumeros(100);

        // Extra 1: Factorial
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce un número positivo para calcular su factorial: ");
        int num = scanner.nextInt();
        System.out.println("El factorial de " + num + "! es " + factorial(num));

        // Extra 2: Fibonacci
        System.out.println("Introduce un número positivo para calcular su Fibonacci: ");
        int pos = scanner.nextInt();
        System.out.println("El valor de la posición " + pos + " en la serie de fibonacci es " + fibonacci(pos));
        scanner.close();

    }

    public static void imprimirRecursivamenteNNumeros(int n) {
        // No utilizo for pues sería una aproximación iterativa.
        // Un método es recursivo cuando se llama a sí mismo para resolver una versión
        // más pequeña del problema original, hasta que alcanza un caso base que puede
        // resolver sin necesidad de más llamadas recursivas.

        if (n == 0) {
            return;
        } else {
            System.out.println(n);
            imprimirRecursivamenteNNumeros(n - 1);
        }
        for (int i = n; i >= 0; i--) {
            System.out.print(i + ",");
            if (i == 0) {
                System.out.println(i + ".");
            }
        }
    }

    public static int factorial(int n) {
        // El factorial de un número entero no negativo n, denotado como n!, es el
        // producto de todos los números enteros positivos desde n hasta 1.
        // - Para n = 0, el factorial es 1, es decir, 0! = 1.
        // - Para n > 0, el factorial de n es n! = n × (n-1) × (n-2) × ... × 2 × 1.

        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    public static int fibonacci(int n) {
        // La sucesión de Fibonacci es una secuencia de números en la que cada número es
        // la suma de los dos números precedentes, empezando por 0 y 1.
        // La definición formal de la sucesión es la siguiente:
        // - F(0) = 0
        // - F(1) = 1
        // - Para todo n > 1, se cumple que F(n) = F(n-1) + F(n-2)

        if (n <= 1) {
            return n;
        } else {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
}
