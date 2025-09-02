/**
 * # 00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
 *
 * @author JavierIncio
 * @version 1.0
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 *
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

public class JavierIncio {
    public static void main(String[] args) {
        // Sitio web oficial Java: https://www.oracle.com/java/

        // Comentario de una línea

        /*
        Comentario
        en
        bloque
         */

        /**
         * Comentario de
         * documentación
         */

        final String CONSTANTE = "Valor fijo";
        String variable = "Valor fijo";

        byte varByte = 127;
        short varShort = 32767;
        int varInt = 2147483647;
        long varLong = 9223372036854775807L;
        float varFloat = 23.67F;
        double varDouble = 145678.9785754D;
        char varChar = 'a';
        boolean varBoolean = true;
        // Las cadenas de texto no son un tipo de dato primitivo en Java
        String texto = "¡Hola, Java!";

        System.out.println(texto);
    }
}