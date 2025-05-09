/* #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

 EJERCICIO:
 * 1 - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * 2 - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * 3 - Crea una variable (y una constante si el lenguaje lo soporta).
 * 4 - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * 5 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"*/

public class Dany3gs {
    public static void main(String[] args) {
        // 1
        //  https://www.java.com/es/

        // 2
        // Esto es un comentario de una línea en Java.
        /* Esto es un comentario de
        varias líneas en Java.
         */

        // 3 por norma general, se usa camelCase
        int varNum = 0;
        final int constante = 0;

        // 4

        // Números enteros:
        // Se pueden crear sin indicar valor, ejemplo ** byte num; **
        byte numMasPequeno = 0; //1 byte (-128 a 127)
        short numPequeno = 0; //2 bytes (-32,768 a 32,767)
        int numeroMasUsado = 0; //4 bytes (-2,147,483,648 a 2,147,483,647)
        long numMuyGrande = 0; //8 bytes (-9,223,372,036,854,775,808 a 9,223,372,036,854,775,807)
        // Números reales:

        float numFloat = 0.0f; //4 bytes. números de punto flotante, indicar con f al final
        double numDouble = 0.0; //8 bytes coma flotantes hasta 15 decimales
        String texto = "variable para texto"; //no primitivo, es un objeto por eso comienza en mayúscula
        boolean boleano = true;
        char caracter = 'a'; //con comillas simples

        // 5
        System.out.println("¡Hola, Java!");
    }
}
