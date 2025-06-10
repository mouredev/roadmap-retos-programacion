/*                                                                                                                
 * EJERCICIO:                                                                                                     
 * Entiende el concepto de recursividad creando una función recursiva que imprima                                 
 * números del 100 al 0.                                                                                          
 *                                                                                                                
 * DIFICULTAD EXTRA (opcional):                                                                                   
 * Utiliza el concepto de recursividad para:                                                                      
 * - Calcular el factorial de un número concreto (la función recibe ese número).                                  
 * - Calcular el valor de un elemento concreto (según su posición) en la                                          
 *   sucesión de Fibonacci (la función recibe la posición).                                                       
 */
public class Alextc35 {
    public static void main(String[] args) {
        // Ejercicio
        System.out.println("----- Recursividad -----");
        recursividad(100);
        System.out.println("------------------------\n");

        // Opcional
        // Factorial
        System.out.println("----- Factorial -----");
        int fact = 4;
        System.out.println(" El factorial de " + fact
                + "! es " + factorial(fact));
        System.out.println("------------------------\n");

        // Fibonacci
        System.out.println("----- Fibonacci -----");
        int fib1 = 0;
        int fib2 = 1;
        int fib3 = 3;
        int fib4 = 5;
        System.out.println("En la posición " + fib1
                + " el valor de la sucesión de fibonacci es: "
                + fibonacci(fib1)); // 1
        System.out.println("\nEn la posición " + fib2
                + " el valor de la sucesión de fibonacci es: "
                + fibonacci(fib2)); // 1
        System.out.println("\nEn la posición " + fib3
                + " el valor de la sucesión de fibonacci es: "
                + fibonacci(fib3)); // 5
        System.out.println("\nEn la posición " + fib4
                + " el valor de la sucesión de fibonacci es: "
                + fibonacci(fib4)); // 8
        System.out.println("------------------------");
    }

    // Ejercicio
    public static void recursividad(int n) {
        if (n < 0) {
            return;
        }
        System.out.println(n);
        recursividad(n - 1);
    }

    // Opcional

    // Factorial
    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    // Fibonacci
    public static int fibonacci(int pos) {
        if (pos == 0) {
            return 0;
        } else if (pos == 1) {
            return 1;
        } else {
            return fibonacci(pos - 1) + fibonacci(pos - 2);
        }
    }
}