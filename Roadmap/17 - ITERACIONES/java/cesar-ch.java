/*
 * #17 ITERACIONES
*/

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Arreglo de números
        int[] numeros = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        // Bucle for
        for (int i = 0; i < numeros.length; i++) {
            System.out.println(numeros[i]);
        }

        // Bucle for each
        for (int numero : numeros) {
            System.out.println(numero);
        }

        /*
         * DIFICULTAD EXTRA
        */
        // Bucle while
        int j = 0;
        while (j < numeros.length) {
            System.out.println(numeros[j]);
            j++;
        }

        // Bucle do while
        int k = 0;
        do {
            System.out.println(numeros[k]);
            k++;
        } while (k < numeros.length);

        // Usando un bucle for each
        Arrays.stream(numeros)
                .forEach(numero -> System.out.println(numero));

        // Usando un bucle map
        Arrays.stream(numeros)
                .map(numero -> numero * 2)
                .forEach(numero -> System.out.println(numero));

        // ....
    }
}
