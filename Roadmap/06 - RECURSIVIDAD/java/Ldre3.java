public class Ldre3 {
    public static void main(String[] args) {
        /*
         * EJERCICIO:
         * Entiende el concepto de recursividad creando una función recursiva que imprima
         * números del 100 al 0.
         */
         printRecursive(100);
         /* DIFICULTAD EXTRA (opcional):
         * Utiliza el concepto de recursividad para:
         * - Calcular el factorial de un número concreto (la función recibe ese número).
         * - Calcular el valor de un elemento concreto (según su posición) en la
         *   sucesión de Fibonacci (la función recibe la posición).
         */
        System.out.println(factorial(7));
        for(int i = 1; i < 50; i++) {
            System.out.println(nNumeroFibo(i));
        }

    }
    public static void printRecursive(int n){
        if (n<0)return;
        System.out.println(n);
        printRecursive(n-1);
    }
    public static int factorial(int n){
        return n==1?1:n*factorial(n-1);
    }

    public static int nNumeroFibo (int n){
        return n==1?0:n==2?1:nNumeroFibo(n-2)+nNumeroFibo(n-1);
    }
}