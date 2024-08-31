public class JerrySantana {
    public static void main(String[] args) {
        // Esta es la página oficial del lenguaje, en español -> https://www.java.com/es/
        // En este link encontramos tutoriales para empezar en el lenguaje -> https://dev.java/learn/getting-started/

        // Sintaxis de comentraios

        // Esta forma de comentar, utilizando dos diagonales, nos sirve para realizar comentarios en una sola línea o al final de una línea.
        /* Para comentar código en una misma línea utilizamos esta notación. */
        /*
        Para realizar comentarios multilínea utilizamos,
        de igual manera, este formato.
        */
        /**
         * También están los comentarios de documentación, los cuales se utilizan para describir los
         * elementos de nuestro programa como clases, interfaces, constructores, etc... Estos comentarios
         * pueden o no ir acompañados de etiquetas que simplifican la explicación y los usos del programa.
         * Para más información sobre estos comentario, visita este link: https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html
         *
         * A partir de estos comentarios algunos IDE's crean el lllamado Javadoc, el cual es la documentación
         * del funcionamientos y usos sobre todo el código de un programa.
         */

        // Declaración de variables y constantes.
        int variable = 0;   // Esto es una variable de tipo entero.
        final int constant = 1;    // Esto es una constante de tipo entero.

        // Tipos de datos primitivos
        byte mimimumSize = 125; // Para representar valores en un rango de -128 hasta 127 y no ocupar tanta memoria. Tamaño de 8 bit.
        short smallSize =  32700; // Para representar valores en un rango de -32768 hasta 32767 y no ocupar mucha memoria. Tamaño de 16 bit.
        int normalSize = 2003947423; // Para representar valores en un rango de -2^31 hasta 2^31 menos 1. Tamaño de 32 bit.
        long bigSize = 29832829; // Para representar valores en un rango de -2^63 hasta 2^63 menos 1. Tamaño de 64 bit.
        float regularSize = 123.5f; // Para representar valores decimales sin ocupar mucha memoria. Tamaño de 32 bit. No recomendado para valores precisos.
        double aBigSize = 123.5; // Para representar valores decimanles ocupando más memoria. Tamaño de 64 bit. No recomendado para valores precisos.
        boolean logicValue = true; // Para representar los valores lógicos verdadero y falso (true, false). Representa un bit de información.
        char character = 'a'; // Para representar un caracter unicode de 16 bit.

        System.out.println("¡Hola, Java!");
    }
}