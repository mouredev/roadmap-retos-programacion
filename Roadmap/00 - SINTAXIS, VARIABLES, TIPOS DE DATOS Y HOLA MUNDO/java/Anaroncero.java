public class Anaroncero {
    public static void main(String[] args) {
 
    /*
     * EJERCICIO:
     * - Crea un comentario en el código y coloca la URL del sitio web oficial del
     *   lenguaje de programación que has seleccionado.
     * - Representa las diferentes sintaxis que existen de crear comentarios
     *   en el lenguaje (en una línea, varias...).
     * - Crea una variable (y una constante si el lenguaje lo soporta).
     * - Crea variables representando todos los tipos de datos primitivos
     *   del lenguaje (cadenas de texto, enteros, booleanos...).
     * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
     *
     * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
     * debemos comenzar por el principio.
     */


    // 1.
    // https://www.java.com/es/

    // 2.
    /* Comentario 
       varias 
       líneas */

    // Comentario en una línea

    // 3.
    String variable = "anaroncero";
    final String variable2 = "usuario";

    // 4.
    // enteros
    byte num1 = 1; // –128 a 127
    short num2 = 30000; // –32,768 a 32,767
    int num3 = 2000000000; // –2,147,483,648 a 2,147,483,647
    long num4 = 9000000; // –9,223,372,036,854,775,808 a 9,223,372,036,854,775,807

    // decimales
    float pi = 3.1415926535f; // 4 bytes 
    double e = 2.718281828459045235360; // 8 bytes 

    // carácter
    char c = 'A';
    char cnumerico = 78;

    // alfanuméricos
    String cadena = "Hola Mundo";

    // booleanos
    boolean verdadero = true;
    boolean falso = false;

    // 5.
    System.out.println("Hola JAVA!");
}    
}
