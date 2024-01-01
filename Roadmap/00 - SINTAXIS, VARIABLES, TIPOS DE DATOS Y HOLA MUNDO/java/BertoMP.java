public class BertoMP {
    public static void main(String[] args) {
        // WEB OFICIAL
        // Para encontrar información sobre Java dirígite a su web oficial: https://www.java.com/

        // COMENTARIOS
        // En Java tenemos 3 tipos de comentarios:

        // - Comentarios de una única línea (// Comentario):
        // Sirven por ejemplo para explicar una variable.

        // - Comentarios de varias líneas (/* Comentario */):
        /* Este tipo de comentarios sirven
         * para explicar por ejemplo un pequeño
         * proceso que ocurre dentro de una
         * de nuestras funciones. */

        // - Comentarios de documentación (/** Comentario */):
        /**
         * Este tipo de comentarios se utilizan para generar documentación
         * sobre el código que en el caso de Java se denomina JavaDoc.
         * Por ejemplo, los podremos ver explicando de forma detallada cómo
         * funciona una de las funciones que hayan sido implementadas.
         * Suelen ir acompañadas de etiquetas que ayudan a entender mejor
         * el código o aportan información extra:
         *  - @param: Determina el tipo de parámetro que recibe la función.
         *  - @return: Determina el tipo de resultado/retorno que produce
         *             la función al final de su ejecución.
         *  - @version: Versión del método o la clase.
         *  - Etc.
         */

        // VARIABLES Y CONSTANTES
        /* Para declarar una variable en Java debemos indicar su tipo y el
         * nombre de la variable. Puede estar inicializada o no, en el caso
         * de que no lo esté tendrá un valor por defecto u otro.
         * Por convención, el nombre de las variables debe seguir la nomenclatura
         * camelCase. */
        int miVariableInicializada = 33;
        int miVariableNoInicializada;

        /* Para declarar una constante en Java debemos hacer algo similar
         * pero utilizando la palabra reservada 'final'. Además, todas
         * las constantes deben ser inicializadas en su declaración y,
         * por convención, es recomendable que su nombre sea en mayúsculas. */
        final int MI_CONSTANTE = 40;

        // DATOS PRIMITIVOS
        // En Java tenemos los siguientes tipos de datos primitivos:

        // - DATOS NUMÉRICOS ENTEROS
        byte miByte = 12; // Números desde -128 hasta 127.
        short miShort = 12642; // Números desde -32.768 hasta el 32.767.
        int miInt = 1726171821; // Números desde -2.147.483.648 hasta 2.147.483.647.
        long miLong = 10000000000L; // Números desde -9.223.372.036.854.775.808 hasta 9.223.372.038.854.775.807.

        // - DATOS NUMÉRICOS DECIMALES
        float miFloat = 3.141592f; // Números hasta 6-7 decimales.
        double miDouble = 3.141592653; // Números hasta 15 decimales.

        // - DATOS LÓGICOS
        boolean miBoolean = true; // Almacena un valor booleano (true o false).

        // - CARACTERES
        char miChar = 'A'; // Almacena un carácter o un valor ASCII.

        /* Para declarar cadenas de texto en Java no tenemos un tipo primitivo como tal,
         * sino que se utiliza la clase String para ello. */
        String miString = "Esto es un String de prueba";

        // IMPRESIÓN POR CONSOLA
        System.out.println("¡Hola, Java!");
    }
}
