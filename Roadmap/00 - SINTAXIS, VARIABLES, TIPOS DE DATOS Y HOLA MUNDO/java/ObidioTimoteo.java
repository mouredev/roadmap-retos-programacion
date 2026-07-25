/*
Reto de Programación 00: Sintaxis, Variables, Tipos de Datos y Hola Mundo
Lenguaje: Java
*/

/*
    * 1. Crea un comentario en el código y coloca la URL del sitio web oficial del
    * lenguaje de programación que has seleccionado.
    */

    // Sitio oficial de Java: https://www.java.com/

    /*
    * 2. Representa las diferentes sintaxis que existen de crear comentarios
    * en el lenguaje (en una línea, varias...).
    */

    // Comentario en línea

    /* 
    * Comentario
    * en bloque
    */

   /** 
    * Comentario de documentación (Javadoc).
    * Se utiliza para documentar el proyecto.
    */

public class ObidioTimoteo {

    // 3. Crea una variable y una constante

    // Variable
    String nombre = "Obidio";
    
    // Constante
    final double PI = 3.1416;

    /* 
    * 4. Crea variables representando todos los tipos de datos primitivos
    * del lenguaje (cadenas de texto, enteros, booleanos...).
    */

    byte myByte = 120;              // Rango:   -128 a 127
    short myShort = 1200;           // Rango:   -32.768 a 32.767
    int myInt = 10000000;           // Rango:   -2^31 a 2^31-1
    long mYLong = 100000000000000L; // Rango:   -2^63 a 2^63-1

    float myFloat = 3.14f;                  // Se debe añadir 'f' al final
    double myDouble = 3.141592653589793;    // Mayor precisión que float

    char myCaracter = 'a';          // Solo un carácter
    boolean myBoolean = true;       // true o false

    /* 
    * 5. Imprime por terminal el texto:
    * "¡Hola, [y el nombre de tu lenguaje]!"
    */

    public static void main(String[] args) {
        
        System.out.println("Hola, Java!");
        
    }    

}