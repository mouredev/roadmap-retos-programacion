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

import java.util.InputMismatchException;

public class RodrigoGit87 {
    public static void countdown(int number){
        if (number >= 0){
        System.out.println(number);
        countdown(number -1);
        }
    }

    //FACTOrial
    public static int factorial (int numero){

        if (numero < 0) {
            System.out.println(" Número establecido no válido, valor establecido a:  1 ");
            return 1;
        }else if( numero == 0 || numero == 1){
            return 1;
        } else return numero * factorial(numero -1);
    }

    // Fibbonacci
    public static int fibbo (int posicion){
        if (posicion <= 0) {
            System.out.println("La posicion debe ser mayor q 0");
            return 0;
        } else if( posicion == 1 || posicion == 2)
            return posicion -1;
        else return fibbo(posicion-1) + fibbo(posicion-2);
    }
    

    public static void main (String[] args){
        countdown(10);
        System.out.println("");

        int llamadaMetodo = factorial( 6) ;
        System.out.println(" REsultado de factorizar: " + llamadaMetodo + "\n");

        int llamadaFibbo = fibbo(8);
        System.out.println("Fibbo: " + llamadaFibbo);
    }
}
