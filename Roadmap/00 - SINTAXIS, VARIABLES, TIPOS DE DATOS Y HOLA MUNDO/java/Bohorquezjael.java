public class Bohorquezjael {
    /**
     * * EJERCICIO #00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO:
     * - Crea un comentario en el código y coloca la URL del sitio web oficial del
     *  lenguaje de programación que has seleccionado.
     * - Representa las diferentes sintaxis que existen de crear comentarios
     * en el lenguaje (en una línea, varias...).
     * - Crea una variable (y una constante si el lenguaje lo soporta).
     * - Crea variables representando todos los tipos de datos primitivos
     * del lenguaje (cadenas de texto, enteros, booleanos...).
     * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
     * 
     * @param void
     */

    public static void main(String[] args) {
        // https://www.java.com/es/

        // This is a single line comment
        /*
         * This is a multiline comment
         */

        String variable = "this is a variable";
        final String constant = "this is a constant";

        byte age = 123; // 8 bits
        short height = 12345; // 16 bits
        int quantity = 1234567890; // 32 bits
        long longNumber = 1234567890123456789L; // 64 bits

        float floating = 11.11f; // 32 bits
        double doubleNumber = 11.1; // 64 bits

        boolean isTrue = true;

        char letter = 'A'; // 16 bits

        System.out.println("¡Hola, Java!");
    }
}