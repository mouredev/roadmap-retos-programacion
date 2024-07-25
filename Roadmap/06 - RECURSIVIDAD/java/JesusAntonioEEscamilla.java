

/** #06 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        imprimirNúmeros(100);
    //---EXTRA---
        
    }

    //---EJERCIÓ---
    // Definiendo la función
    public static void imprimirNúmeros(int n) {
        if (n < 0) {
            return;
        }
        System.out.println(n);
        // Aquí es donde se realizar la Recursividad
        imprimirNúmeros(n - 1);
    }

    /**-----DIFICULTAD EXTRA-----*/

    // Pendiente

    /**-----DIFICULTAD EXTRA-----*/
}