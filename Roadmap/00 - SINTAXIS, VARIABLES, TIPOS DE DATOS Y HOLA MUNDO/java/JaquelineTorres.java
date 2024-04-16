/**
 * Este es un programa de ejemplo en Java que cubre varios aspectos básicos del lenguaje.
 * Puedes encontrar más información sobre Java en el sitio web oficial:
 * https://www.oracle.com/java/
 */

public class JaquelineTorres {
    public static void main(String[] args) {
        // Comentarios de una línea

        /*
         * Comentarios
         * de varias
         * líneas o bloque
         */

        // Declaración de una variable
        char variableA = 'a';

        // Declaración de una constante usando la palabra clave 'final'
        final double PI = 3.1416;

        System.out.println("variableA: " + variableA);
        System.out.println("PI: " + PI);

        // Variables representando todos los tipos de datos primitivos del lenguaje

        // Numéricos enteros
        byte primitivoByte = 123;
        short primitivoShort = 456;
        int primitivoInt = 14;
        long primitivoLong = 45435345;

        System.out.println("byte: " + primitivoByte + ", short: " + primitivoShort + ", int: " + primitivoInt + ", long: " + primitivoLong);

        // Numéricos en punto flotante
        float primitivoFloat = 1.122F;
        double primitivoDouble = 122.21212121D;

        System.out.println("float: " + primitivoFloat + ", double: " + primitivoDouble);

        // Caracteres
        char primitivoChar = 'g';
        System.out.println("char: " + primitivoChar);

        // Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        System.out.println("¡Hola, Java!");
    }
}
