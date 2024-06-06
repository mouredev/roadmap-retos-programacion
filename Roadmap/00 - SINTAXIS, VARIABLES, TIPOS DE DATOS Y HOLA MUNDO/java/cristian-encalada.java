package reto00;

/*
 * 1. Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 */

// https://www.java.com/en/

/*
 * 2. Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
*/

// Comentario de una sola línea

/*
 * Comentario de múltiples líneas
 * @author Cristian Encalada
 */

/**
 * Documentation type comment
 */

/*
3. Crea una variable (y una constante si el lenguaje lo soporta).

    int myVar = 10;

    final int MIN_VALUE = 1;
*/

public class sintaxisVariables00 {  
// variable a nivel de objeto
public  int objectVariable = 9;
// variable a nivel de clase
public  static int classVariable = 15;
    public static void main(String[] args) {
        // variable local
        int localVariable = 10;

        /*
        * 4. Crea variables representando todos los tipos de datos primitivos
        *   del lenguaje (cadenas de texto, enteros, booleanos...).
       */

        int myInt = 10; // 4 byte/32 bits - range: -2e31 to 2e-31-1
        short myShort;  // 16 bits - range: -32,768 to 32,767 - better for integers
        long myLong = 123456L;  // 64 bits - range: -2e63 to 2e-63-1
        double myDouble = 5.5d; // 64 bits - range: 4.9e-324 to 1.8e+308
        float myFloat = 9.99f; // 4 byte (32 bits) - range:  1.40129846432481707e-45 to 3.40282346638528860e+38
        boolean myBool = false; 
        byte myByte = -128;  // 8 bits - range: -128 to 127
        char myChar = 'Z';
        String myString = "¡Hola, Java!";
        
        
        //  5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        System.out.println(myString);
    }
    
}