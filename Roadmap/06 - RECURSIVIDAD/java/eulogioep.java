public class eulogioep {

    public static void main(String[] args) {
        // Llamada a la función para imprimir números del 100 al 0
        System.out.println("Números del 100 al 0:");
        imprimirNumeros(100);
        
        // Prueba del cálculo de factorial
        int numeroFactorial = 5;
        System.out.println("\nFactorial de " + numeroFactorial + ": " + factorial(numeroFactorial));
        
        // Prueba de la sucesión de Fibonacci
        int posicionFibonacci = 7;
        System.out.println("Elemento en la posición " + posicionFibonacci + " de Fibonacci: " + fibonacci(posicionFibonacci));
    }
    
    /**
     * Función recursiva para imprimir números del 100 al 0.
     * @param numero El número actual a imprimir.
     */
    public static void imprimirNumeros(int numero) {
        // Caso base: si el número es menor que 0, terminamos la recursión
        if (numero < 0) {
            return;
        }
        
        // Imprimimos el número actual
        System.out.print(numero + " ");
        
        // Llamada recursiva con el número decrementado
        imprimirNumeros(numero - 1);
    }
    
    /**
     * Función recursiva para calcular el factorial de un número.
     * @param n El número del cual calcular el factorial.
     * @return El factorial del número.
     */
    public static int factorial(int n) {
        // Casos base: factorial de 0 y 1 es 1
        if (n == 0 || n == 1) {
            return 1;
        }
        
        // Llamada recursiva: n * factorial(n-1)
        return n * factorial(n - 1);
    }
    
    /**
     * Función recursiva para calcular el valor de un elemento en la sucesión de Fibonacci.
     * @param posicion La posición del elemento en la sucesión de Fibonacci.
     * @return El valor del elemento en la posición dada.
     */
    public static int fibonacci(int posicion) {
        // Casos base: posiciones 0 y 1 de Fibonacci son 0 y 1 respectivamente
        if (posicion == 0) {
            return 0;
        }
        if (posicion == 1) {
            return 1;
        }
        
        // Llamada recursiva: suma de los dos elementos anteriores
        return fibonacci(posicion - 1) + fibonacci(posicion - 2);
    }
}