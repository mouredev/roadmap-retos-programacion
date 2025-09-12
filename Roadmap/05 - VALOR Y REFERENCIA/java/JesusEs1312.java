/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

public class JesusEs1312 {
    public static void main(String[] args) {
        // Asignación de variables por valor
        int a = 5;
        int b = a;
        b = 10;
        System.out.println("a: " + a + ", b: " + b); // a: 5, b: 10

        // Asignación de variables por referencia
        int[] c = {5};
        int[] d = c;
        d[0] = 10;
        System.out.println("c[0]: " + c[0] + ", d[0]: " + d[0]); // c[0]: 10, d[0]: 10

        // Funciones con variables por valor
        int f = 20;
        porValor(f);
        System.out.println("f fuera de la función: " + f); // f: 20

        // Funciones con variables por referencia
        int[] g = {10};
        porReferencia(g);
        System.out.println("g[0] fuera de la función: " + g[0]); // g[0]: 10

        // Ejercicio Extra
        int i = 5;
        int j = 10;
        System.out.println("Variables originales - i: " + i + ", j: " + j); // i: 5, j: 10
        int[] h = intercambioPorValor(i, j);
        System.out.println("Variables retornadas - i: " + h[0] + ", j: " + h[1]); // h[0]: 10, h[1]: 5

        int[] k = {5};
        int[] l = {10};
        System.out.println("Variables originales - k[0]: " + k[0] + ", l[0]: " + l[0]); // k[0]: 5, l[0]: 10
        int[] m = intercambioPorReferencia(k, l);
        System.out.println("Variables retornadas - k[0]: " + m[0] + ", l[0]: " + m[1]); // m[0]: 10, m[1]: 5
    }
    
    // Funciones con variables por valor
    public static void porValor(int f) {
        f = 10;
        System.out.println("f dentro de la función: " + f); // f: 10
    }

    // Funciones con variables por referencia
    public static void porReferencia(int[] g) {
        int h[] = g;
        h[0] = 10;
        h[1] = 20;
        System.out.println("g[0] dentro la función: " + g[0]); // g[0]: 10
    }

    // Funciones de Ejercicio Extra
    public static int[] intercambioPorValor(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
        return new int[] {a, b};
    }

    public static int[] intercambioPorReferencia(int[] a, int[] b) {
        int temp = a[0];
        a[0] = b[0];
        b[0] = temp;
        return new int[] {a[0], b[0]};
    }
}
