/**
 * Solución del reto #00: Sintaxis, variables, tipos de  datos y hola mundo;
 * @author Alejosor
 */
public class alejosor {
    
    public static final int num_max = 100; // Constante entera
    
    public static final String mensaje_bienvenida = "¡Bienvenido a Java!"; // Constante de cadena

    public static void main(String[] args) {
        /*
         * EJERCICIO:
         * - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
         * - Representa las diferentes sintaxis que existen de crear comentario en el lenguaje (en una línea, varias...).
         * - Crea una variable (y una constante si el lenguaje lo soporta).
         * - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
         * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
         */

        // - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
        // URL del sitio web oficial de Java: https://www.java.com/es/


        // - Representa las diferentes sintaxis que existen de crear comentario en el lenguaje (en una línea, varias...).
            // <- Forma de comentar en una sola línea.

            /*
             *  <- Forma de comentar en varias líneas.
             */
        
        // - Crea una variable (y una constante si el lenguaje lo soporta).
        String variable = "Esto es una variable";  // Creación de una variable.

        final int num_mim = 1; //Constante dentro de un método

        // - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
        byte byt = 10; // Tipo de dato primitivo -> Byte

        short shrt = 12; // Tipo de dato primitivo -> Short

        int entero = 150; // Tipo de dato primitivo -> Int

        long lng = 14567l; // Tipo de dato primitivo -> Long

        float flat = 23.6f; // Tipo de dato primitivo -> Float

        double dbl = 23.54566; // Tipo de dato primitivo -> Double

        char chr = 'A'; // Tipo de dato primitivo -> Char

        boolean bool = true; // Tipo de dato primitivo -> Boolean

        // - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        System.out.println("¡Hola, Java!");

    }
}