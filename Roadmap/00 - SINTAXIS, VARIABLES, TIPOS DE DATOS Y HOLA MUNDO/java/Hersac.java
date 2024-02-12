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

//https://www.java.com/es/
/*Reto de programacion 00 j de Mouredev*/

public class reto00 {
    public reto00() {

        var laVariable = "variable";
        final String laConstante = "constante";

        String texto = "Cadena de texto";
        int numero = 12;
        double decimales = 12.2;
        float flotantes = 1.5f;
        boolean buleano = true;
        char caracter = 'c';
        long largos = 1234567890;
        short cortos = 12345;
        byte muyPequeño = 22;

        String java = "Java";
        System.out.println("¡Hola " + java + "!");
    }

    public static void main(String args[]) {
        reto00 newReto = new reto00();
    }
}
