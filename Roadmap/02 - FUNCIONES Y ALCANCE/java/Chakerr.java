
import java.util.Scanner;

/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
public class Chakerr {

    //Variable global
    static int global = 20;

    public static void main(String[] args) {

        sinParametros();
        conParametros(3);
        conRetorno();

        //Funciones ya creadas en el lenguaje
        int max = Math.max(10, 20);
        System.out.println("numero maximo entre 10 y 20 : " + max);
        int min = Math.min(10, 20);
        System.out.println("numero minimo entre 10 y 20 : " + min);

        //Variable local y global
        int local = 3;
        System.out.println("variable local : " + local);
        System.out.println("Variable global : " + global);

        //Dificultad extra
        reto();
    }

    //Funcion sin parámetros ni retorno
    static void sinParametros() {
        System.out.println("Funcion sin parámetros ni retornos");
    }

    //Funcion con uno o varios parámetros
    public static void conParametros(int a) {
        System.out.println("suma de variables a + variable global  = " + (a + global));
    }

    public static String conRetorno() {
        return "Retorno";
    }

    public static int reto() {

        int contadorNumeros = 0;
        String cadena1 = "Multiplo de 3";
        String cadena2 = "Multiplo de 5";

        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(i + " : " + cadena1 + "y" + cadena2);

            } else if (i % 3 == 0) {
                System.out.println(i + " : " + cadena1);

            } else if (i % 5 == 0) {
                System.out.println(i + " : " + cadena2);
            } else {
                System.out.println(i);
                contadorNumeros++;
            }
        }

        return contadorNumeros;
    }
}
