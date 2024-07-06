/**
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 * 
 * @version v1.0
 * 
 * @since 05/07/2024
 * 
 * @author GlossyPath
 * 
 */

public class GlossyPath {
    /*
     * Descripción: método para calcular el valor de un elemento.
     */
    public static int Fibonacci(int num){

        if (num <= 1) {
            return num; 
        } else {
            return Fibonacci(num - 1) + Fibonacci(num - 2);
        }
    }
    /*
     * Descripción: método para obtener el factorial de un número.
     */
    public static int factorial(int num){

        int total;

        if(num>0){
            return total = num * factorial(num-1);
        } else {
            return 1;
        }
    }
    /*
     * Descripción: método para imprimir recursivamente numeros de mayor a menor.
     */
    public static void impresionRecursiva(int num){

        if(num>=0){

            System.out.println(num);
            impresionRecursiva(num-1);
        }
    }

    public static void main(String[] args) {
        
        impresionRecursiva(100);

        int total = factorial(0);
        System.out.println(total);

        int totalFibo = Fibonacci(5);
        System.out.println(totalFibo);
    }
}
