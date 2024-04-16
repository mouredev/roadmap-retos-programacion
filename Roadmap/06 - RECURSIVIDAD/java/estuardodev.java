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


private class Estuardodev{
    public static void main(String[] args){
        numeros(100);
        System.out.println(factorial(5));
        System.out.println(fibonacci(5));
    }

    static void numeros(int numero){
        if (numero >= 0){
            System.out.println(numero);
            numeros(numeros((numero - 1)));
        }
    }

    static int factorial(int numero){
        if (numero < 0){
            return 1;
        } else if (numero == 0){
            return 1;
        } else{
            return numero * factorial(numero - 1);
        }
    }

    static int fibonacci(int posicion){
        if (posicion <= 0){
            return 0;
        } else if (posicion == 1){
            return 0;
        } else if (posicion == 2){
            return 1;
        } else{
            return fibonacci(posicion - 1) + fibonacci(posicion - 2);
        }
    }
}