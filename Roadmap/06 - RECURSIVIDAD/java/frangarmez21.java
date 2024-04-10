public class frangarmez21 {

    public static void main(String[] args) {

        System.out.println("##Ejercicio de recursividad##");
        /*
         * EJERCICIO:
         * Entiende el concepto de recursividad creando una función recursiva que imprima
         * números del 100 al 0.
         */
        System.out.println("##Creando función recursiva que imprime números del 100 al 0.##");
        System.out.println();

        int initialNumber = 100;
        System.out.println("Llamamos al método recursivo:");
        recursiveCounting(initialNumber);
        System.out.println("Salimos del método recursivo.");

        System.out.println();
        System.out.println("##Dificultad Extra##");
        System.out.println();

        /* * DIFICULTAD EXTRA (opcional):
         * Utiliza el concepto de recursividad para:
         * - Calcular el factorial de un número concreto (la función recibe ese número).
         * - Calcular el valor de un elemento concreto (según su posición) en la
         *   sucesión de Fibonacci (la función recibe la posición).
         */

        System.out.println("Calcular el factorial de un número concreto:");
        System.out.println();

        int number = 10;
        System.out.println("Llamamos al método calcular factorial con el número: " + number);
        System.out.println();
        int factorial = factorialCalculation(number, number);
        if ((factorial >= 0)) {
            System.out.println("El resultado es: " + factorial);
        } else {
            System.out.println("No se ha podido calcular, debe ser un numero natural");
        }

        System.out.println();
        System.out.println("Calcular el valor de un elemento concreto en la sucesión de Fibonacci:");
        System.out.println();

        int position = 6;
        int initNumber = 1;
        int prevNumber = 0;
        System.out.println("Llamamos al método obtener valor en Fibonacci en la posición: " + position);
        System.out.println();
        int fibonacciResult = getFibonacciValue(position - 1, initNumber, prevNumber);
        System.out.println("El valor en la posición " + position + " de la sucesión de Fibonacci es: " + fibonacciResult);
    }

    private static int getFibonacciValue(int position, int initNumber, int prevNumber) {
        int result = initNumber + prevNumber;
        position--;
        if (position > 0) {
            result = getFibonacciValue(position, result, initNumber);
        }
        return result;
    }

    private static int factorialCalculation(int number, int initMultiplier) {
        int multiplier = initMultiplier - 1;
        int result = number * multiplier;

        if (multiplier == 0) {
            result = 1;
            return result;
        } else if (multiplier == 1) {
            return result;
        } else if (multiplier > 1) {
            return factorialCalculation(result, multiplier);
        } else {
            result = -1;
            return result;
        }
    }

    private static void recursiveCounting(int initialNumber) {
        System.out.println(initialNumber);
        if (initialNumber > 0) {
            recursiveCounting(initialNumber - 1);
        }
    }
}
