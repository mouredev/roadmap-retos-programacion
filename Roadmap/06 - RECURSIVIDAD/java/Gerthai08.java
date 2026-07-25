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
public class Gerthai08 {
    public static void main(String[] args) {

        //Llamando al método "countdown"
        System.out.println("=====Countdown=====");
        countdown(100);

        //Llamando al método "factorial"
        System.out.println("\n<=====Factorial=====");
        System.out.println("El factorial de 5 es: " + factorial(5));

        //Llamado al método para "la sucesión de Fibonacci"
        System.out.println("\n<=====Fibonacci=====");
        int position = 7;
        System.out.println("Fibonacci en posición " + position + " es " + fibonacci(position));
    }

    //Método para la sucesión de Fibonacci
    private static int fibonacci(int n){
        if (n == 0) {
            return 0;
        }else if (n == 1){
            return 1;
        }else{
            return fibonacci(n-1) + fibonacci(n-2);
        }
    }

    //Método para calculo factorial
    private static int factorial(int n) {
        if(n > 1){
            return n * factorial(n - 1);
        }else{
            return 1;
        }
    }

    //Método que imprime números del 100 al 0
    static void countdown(int n){
        if(n >= 0){
            System.out.print(n + " ");
            //si el numero es múltiplo de 10 hace un salto de linea
            if (n % 10 == 0){
                System.out.println();
            }
            countdown(n - 1);
        }
    }
}
