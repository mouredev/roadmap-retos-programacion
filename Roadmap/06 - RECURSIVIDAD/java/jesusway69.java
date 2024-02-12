package ejercicio06;

import java.util.Scanner;

/**
 * EJERCICIO: Entiende el concepto de recursividad creando una función recursiva
 * que imprima números del 100 al 0.
 */
public class JesusWay69 {

    private static void countdown(int num) {//Definimos la función y le pasamos el número 100 en la primera ejecución
        
        if (num >= 0) { //Establecemos la condición de parada en 0
            System.out.print(num + " "); //Imprimimos cada número horizontalmente y separado en cada ejecución de la función
            
            if (num % 10 == 0 && num != 100) { //Establecemos un salto de línea cada 10 números para hacerlo más visual (opcional)
                System.out.println(" "); //Salto de línea
            }
            num--; // Al terminar las condiciones para seguir iterando e imprimir le restamos 1 al valor del parámetro de la función...
            countdown(num); //...y hacemos la llamada recursiva enviando el nuevo valor del parámetro a la función
        }

    }

 /*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
    public static int fibonacci(int n) {
        n--;
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fibonacci(n) + fibonacci(n - 1);
        }
    }

    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    public static void main(String[] args) {
        countdown(100);
        Scanner sc = new Scanner(System.in);
        System.out.print("""
                           \n1- Calcular factorial
                           2- Calcular posici\u00f3n en la secuencia Fibonacci
                           3- Salir
                           Elija una opci\u00f3n: """);
        String choose = sc.next();

        if (choose.matches("[1-3]")) {
            int option = Integer.parseInt(choose);
            if (option == 1) {
                System.out.println("\nIntroduzca un número para calcular su factorial: ");
                String num = sc.next();
                if (num.matches("[1-9]+") == true) {
                    int number = Integer.parseInt(num);
                    System.out.println("El factorial de " + number + " es: " + factorial(number));
                } else {
                    System.out.println("Sólo se pueden introducir números enteros");
                }

            } else if (option == 2) {
                System.out.println("\nIntroduzca un número para calcular su posición en la secuencia Fibonacci:");
                String num = sc.next();
                if (num.matches("[1-9]+")) {
                    int number = Integer.parseInt(num);
                    System.out.println("La posición " + number + " de la secuencia Fibonacci tiene el valor " + fibonacci(number));
                } else {
                    System.out.println("Sólo se pueden introducir números enteros");
                }

            } else if (option == 3) {
                System.out.println("Fin del programa");

            }

        } else {
            System.out.println("Sólo se pueden introducir números enteros del 1 al 3");

        }

    }

}
