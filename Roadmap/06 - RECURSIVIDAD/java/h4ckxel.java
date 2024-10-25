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

 public class h4ckxel {
    public static void main(String[] args) {
        // Llamada a la función que imprime números del 100 al 0
        imprimirNumeros(100);

        // Llamada a la función que calcula el factorial de un número concreto
        System.out.println(factorial(5));

        // Llamada a la función que calcula el valor de un elemento concreto en la sucesión de Fibonacci
        System.out.println(fibonacci(10));
    }

    public static void imprimirNumeros(int numero) {
        if (numero >= 0) {
            System.out.println(numero);
            imprimirNumeros(numero - 1);
        }
    }

    // Calcula el factorial de un número concreto
    public static int factorial(int numero){
        if (numero == 0) {
            return 1;
        } else {
            return numero * factorial(numero - 1);
        }
    }

    // Calcula el valor de un elemento concreto en la sucesión de Fibonacci
    public static int fibonacci(int posicion){
        if (posicion == 0 || posicion == 1) {
            return posicion;
        } else {
            return fibonacci(posicion - 1) + fibonacci(posicion - 2);
        }
    }
 }