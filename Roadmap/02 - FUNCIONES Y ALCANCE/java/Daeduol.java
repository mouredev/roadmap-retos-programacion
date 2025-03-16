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
public class FunsYalcance {
    static String variableGlobal = "soy una variable global";

    // funcion sin parametros ni retorno
    static void funSinParam() {
        System.out.println("funcion sin parametros ni retorno");
    }

    //funcion con parametros
    static void funConParam(int a, int b) {
        int resultado = a + b;
        System.out.println("La suma de " + a + " y " + b + " es: " + resultado);

    }

    // funcion con retorno
    public static int funConReto(int a, int b) {
        int respuesta = a - b;
        return respuesta;

    }

    //funcion dentro de funcion
    static void funEnfun() {
        System.out.println("En java no se permiten funciones anidadas");
    }
    static int caraCorona(String text1, String text2) {

        int contador = 0;

        for (int i = 1; i <= 100; i++) {

            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(text1 + text2);
            } else if (i % 3 == 0) {
                System.out.println(text1);
            } else if (i % 5 == 0) {
                System.out.println(text2);
            } else {
                System.out.println(i);

                contador++;
            }
        }
        return contador;

    }

    public static void main(String[] args) {
        String variableLocal = "soy una variable local";

        // Llamando a la función sin parámetros ni retorno
        funSinParam();
        // Llamando a la función con parámetros
        funConParam(2, 3);
        // Llamando a la función con retorno y almacenando el resultado en una variable
        int respuestaResta = funConReto(5, 3);
        System.out.println(respuestaResta);
        // Llamando a la función dentro de función
        funEnfun();
        // variables local y global
        System.out.println(variableLocal);
        System.out.println(variableGlobal);
        int numImpresiones = caraCorona("cara", "corona");
        System.out.println("Se imprimieron " + numImpresiones + " números.");

    }


}