public class kleyner098 {
    /*
     * EJERCICIO:
     * Entiende el concepto de recursividad creando una función recursiva que
     * imprima números del 100 al 0.
     *
     * DIFICULTAD EXTRA (opcional):
     * Utiliza el concepto de recursividad para:
     * - Calcular el factorial de un número concreto (la función recibe ese número).
     * - Calcular el valor de un elemento concreto (según su posición) en la
     * sucesión de Fibonacci (la función recibe la posición).
     */

    public static void main(String[] args) {
        recursividad(0);

        int num = 5;
        System.out.printf("\n%1$d! = %2$d", num, factorial(num));
        int posicion = 7;
        System.out.printf("\nEl elemento en la posición %1$d es %2$d", posicion, fibonacci(posicion));
    }

    // Método recursivo que impreme los valores de 100 hasta n
    public static void recursividad(int num) {
        // caso base
        if (num >= 100) {
            System.out.print(num);
        } else {
            // Llamada recursiva
            recursividad(num + 1);
            System.out.print(" " + num);
        }
    }

    // Método que calcula el factorial
    public static int factorial(int num) {
        if (num == 0) {
            return 1;
        } else {
            return factorial(num - 1) * num;
        }
    }

    // Método que devuelve el elemento en la posición n de Fibonacci
    public static int fibonacci(int posicion) {
        if (posicion <= 1) {
            return 0;
        } else if (posicion == 2) {
            return 1;
        } else {
            return fibonacci(posicion - 1) + fibonacci(posicion - 2);
        }
    }
}
