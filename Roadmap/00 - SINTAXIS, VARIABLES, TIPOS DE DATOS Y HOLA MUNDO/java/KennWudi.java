/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

public class KennWudi {
    public static void main(String[] args) {
        /*
         * - Crea un comentario en el código y coloca la URL del sitio web oficial del
         * lenguaje de programación que has seleccionado.
         */

        // https://docs.oracle.com/en/java/

        /*
         * - Representa las diferentes sintaxis que existen de crear comentarios
         * en el lenguaje (en una línea, varias...).
         */

        // Comentario en una línea

        /*
         * Comentario
         * en
         * varias
         * líneas
         */
        // - Crea una variable (y una constante si el lenguaje lo soporta).
        String myString1 = "myString";
        final String MY_CONSTANT = "MY_CONSTANT";

        /*
         * - Crea variables representando todos los tipos de datos primitivos
         * del lenguaje (cadenas de texto, enteros, booleanos...).
         */
        int myInt = 1;
        double myDouble = 2.2;
        float myFloat = 2.2f;
        String myString = "myString";
        char myChar = 'K';
        Boolean myBoolean = true;

        // - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        System.out.println("Hola, Java");

        // * Uso de variables
        System.out.println(myString1);
        System.out.println(MY_CONSTANT);
        System.out.println(myInt);
        System.out.println(myDouble);
        System.out.println(myFloat);
        System.out.println(myString);
        System.out.println(myChar);
        System.out.println(myBoolean);
    }

}
