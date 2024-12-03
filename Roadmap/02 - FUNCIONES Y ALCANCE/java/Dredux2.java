/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje: Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */
package org.example;
import java.util.Random;
class Dredux {
    public static void main(String[] args) {
        Random rm = new Random();
        funcionSimple();
        funcionParametros();
        System.out.println("El resultado de la funcion de retorno es: " + funcionRetorno());
        funcionJava(rm);
        funcionLocal(rm);
        funcionGlobal();
        System.out.println("\nNumeros totales: " + funcionExtra("Multiplo de 3", "Multiplo de 5"));
    }

    // 1)
    // Funcion simple sin parametros ni retorno
    public static void funcionSimple() {
        System.out.println("Hola, soy una funcion simple");
    }

    // Funcion con un parametro
    public static void funcionParametros() {
        String nombre = "Juan";
        int edad = 25;
        System.out.println("Hola, soy una funcion, mi nombre es " + nombre + " y tengo " + edad + " años");
    }

    // Funcion con retorno
    public static int funcionRetorno() {
        return 5;
    }

    // 2)
    public static void funcionJava(Random rm) {
        int a = rm.nextInt(51);
        int b = rm.nextInt(51);
        int mayor = Math.max(a, b);
        System.out.println("El valor máximo entre " + a + " y " + b + " es: " + mayor);
    }

    // 3)
    // Variable local
    public static void funcionLocal(Random rm) {
        int x = rm.nextInt(11);
        System.out.println("Variable local: " + x);
    }

    // Variable global
    static int y = 20;
    public static void funcionGlobal() {
        System.out.println("Variable global: " + y);
        System.out.println();
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
     * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
     *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
     *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
     *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
     */

    public static int funcionExtra(String a, String b) {
        int count = 0;
        for (int num = 1; num <= 100; num++) {
            if (num % 3 == 0 && num % 5 == 0) {
                System.out.println(num + " es " + a + " y " + b);
            } else if (num % 3 == 0) {
                System.out.println(num + " es " + a);
            } else if (num % 5 == 0) {
                System.out.println(num + " es " + b);
            } else {
                System.out.println(num);
                count++;
            }
        }
        return count;
    }
}
