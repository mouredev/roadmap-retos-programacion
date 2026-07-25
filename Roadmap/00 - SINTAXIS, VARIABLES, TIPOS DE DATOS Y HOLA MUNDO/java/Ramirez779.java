//#00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO;

/* EJERCICIO:

 * 1- Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * 2- Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * 3- Crea una variable (y una constante si el lenguaje lo soporta).
 * 4- Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * 5- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

//1. Sitio web del lenguaje escogido, en este caso Java => https://www.oracle.com/java/

//2. Sintaxis al momento de usar comentarios

// Comentario de una sola linea

/* Comentario 
   de más de 
   una linea */

public class Ramirez779 {
    public static void main(String[] args) {
        // 3. Variables y constantes

        // Variable:
        int Variable = 10;
        Variable = 15;

        // Constante:
        final int ONSTANTE = 100;

        // 4. Tipos de datos primitivos

        byte miByte = 127;
        short miShort = 32767;
        int miEntero = 2147483647; // Para números enteros sin decimales
        long miLong = 9223372036854775807L;
        float miFloat = 3.14f; // Para números decimales
        double miDouble = 3.141592653589793;
        boolean miBooleano = true; // Representa valores lógicos los cuales son true/false
        char miCaracter = 'A';
        // String
        String miCadena = "Hola, Java";

        // 5. Imprimir mensaje por terminal:
        System.out.println("¡Hola, Java!");
    }
}