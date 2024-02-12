// https://developer.oracle.com/languages/java.html
//  https://dev.java/


public class KingSaul22 {

    public static void main(String[] args) {

        //COMENTARIOS:

        //Este es un comentario de una sola linea.

        /*
        Este comentario
        incluye distintas
        lineas.
         */

        /**
         * Este comentario es usado para Javadoc.
         */


        //VARIABLE/CONSTANTE:

        //Escribimos el tipo de variable, seguido del nombre que le daremos.
        int variable;
        //A lo hora de crear constantes, colocamos la palabra 'final' antes del tipo de la variable.
        final int CONSTANTE = 0;


        //VARIABLES PRIMITIVAS:

        //Las variables char almacenan un caracter.
        char letter = 'S';
        //Variable de tipo boolean, indican Si o No; siempre se inicializan con el valor 'false'.
        boolean isValid = true;
        
        /*
        Las siguientes variables almacenarán numeros enteros,
        cada una tiene una capacidad medida en bits.

        Cabe destacar que las variables de tipo 'long' se les da el valor acabado en una 'L'.
         */
        byte bits8 = 8;
        short bits16 = 16;
        int bits32 = 32;
        long bits64 = 64L;

        //Para variables de números con decimales usamos los siguientes tipos,
        //donde uno almacena 64 bits y otro 32, el cual se declara acabado en 'F'.
        float decimal32 = 3.2F;
        double decimal64 = 6.4;


        //IMPRESION POR CONSOLA:

        System.out.println("¡Hola, Java!");
    }
}
