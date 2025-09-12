import java.util.Scanner;

public class TofeDev {
    /* EJERCICIO:
    * Entiende el concepto de recursividad creando una función recursiva que imprima
    * números del 100 al 0.
    *
    * DIFICULTAD EXTRA (opcional):
    * Utiliza el concepto de recursividad para:
    * - Calcular el factorial de un número concreto (la función recibe ese número).
    * - Calcular el valor de un elemento concreto (según su posición) en la 
    *   sucesión de Fibonacci (la función recibe la posición).
    */
    public static void main(String[] args) {
        //Sacar números del 100 al 0
        for (int i = 100; i >= 0; i--) {
            System.out.println(i);
        }

        //Sacar factorial de un número concreto
        Scanner scanner = new Scanner(System.in);
        int num1 = scanner.nextInt();
        factorial(num1);

        //Sucesión de Fibonacci
        int num2 = scanner.nextInt();
        fibonacci(num2);

        scanner.close();
    }

    public static void factorial(int numero) {
        int resultado;
        int temp = numero;
        numero--;
        resultado = temp * numero;
        System.out.println(numero);
        System.out.println(resultado);
        for (int i = numero; i > 1; i--) {
            temp = i;
            temp--;
            System.out.println(temp);
            resultado *= temp;
            System.out.println(resultado);
        }
    }  

    public static void fibonacci(int numero) {
        int a = 0;
        int b = 1;
        int temp;
        for (int i = numero; i > 0; i--) {
            temp = a + b;
            b = a;
            a = temp;
            System.out.println(temp);
        }
    }
}

