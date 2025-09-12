public class fredylopez01 {

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

    public static void main(String[] args) {
        //Sitio de JAVA
        //https://www.java.com/es/

        //Diferentes sintaxis de comentarios JAVA
        //Unica línea
        /*
         * Varias lineas
         */

        String miVariable;       //variable
        final int constante = 2; //constante

        //Datos Primitivos
        int numeroEntero = 1;
        double decimal = 0.3;
        byte bite = 4;
        short corto = 32000;
        long extenso = 4444444;
        char caracter = 'a';

        //String es una clase que puede almacenar cadenas de caracteres
        String saludo = "¡Hola, ";

        //Impresión de información
        System.out.println(saludo + "JAVA!");
    }
}
