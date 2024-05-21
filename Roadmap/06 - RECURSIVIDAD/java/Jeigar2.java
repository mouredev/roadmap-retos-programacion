import java.util.stream.IntStream;
import java.util.stream.LongStream;

public class Jeigar2 {
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
    public static final int TOTAL = 100;
    public static void main(String[] args) {
        System.out.println("Los número del 0 al 100");
        impresionRecursiva(TOTAL);
        System.out.println("");

        System.out.println("\nLos 10 primeros factoriales");
        IntStream.rangeClosed(0,10).forEach(fac -> System.out.println(String.format(" - %d! = %d", fac, factorial(fac))));
        System.out.println("\nPosicione Fibonacci de la 10 a la 12");
        IntStream.rangeClosed(10,12).forEach(fibo -> System.out.println(String.format(" - F(%d) = %d", fibo, (new Fibonacci(fibo)).getValor())));
    }

    public static void impresionRecursiva(int total){
        if(total>=0) {
            if(total%10==0) {
                System.out.println("");
                System.out.print(TOTAL - total);
            }else {
                System.out.print((((total < TOTAL) ? ", " : "") + (TOTAL - total)));
            }
            impresionRecursiva(total-1);
        }
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Utiliza el concepto de recursividad para:
     * - Calcular el factorial de un número concreto (la función recibe ese número).
     * - Calcular el valor de un elemento concreto (según su posición) en la
     *   sucesión de Fibonacci (la función recibe la posición).
     */
    public static long factorial(int total){
        long resultado = 0;
        if(total == 0 && resultado == 0)
            resultado = 1;
        if(total > 0)
            resultado = total * factorial(total-1);
        return resultado;
    }

    static class Fibonacci {
        private long a = 0;
        private long b = 1;
        private long valor = 0;

        Fibonacci(int n){
            if (n == 0)
                valor = a;
            if (n == 1)
                valor = b;
            if (n >= 2)
                valor = secuencia(n);
        }
        private long secuencia(int n){
            long suma = 1;
            long aux = 0;
            if(n>2) {
                aux = this.a;
                this.a = this.b;
                this.b = aux + this.b;
                suma = a + secuencia(n - 1);
            }
            return suma;
        }

        public long getValor() {
            return valor;
        }
    }
}
