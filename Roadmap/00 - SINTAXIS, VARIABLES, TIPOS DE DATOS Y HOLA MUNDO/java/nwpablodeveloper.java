

// https://www.java.com/es/

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

 
public class nwpablodeveloper {
    
    // Variable
    static public String unaVariable;
    
    // Constante
    static final String _lenguaje  = "Java" ; 
    
    // Variables con tipos de datos primitivos enteros
    static public byte tipoByte = 127;              // Max permitido
    static public short tipoShort = 32767; 
    static public int tipoInteger = 2147483647;

    // Variables con tipos de datos primitivos flotantes
    static public long tipoLong = 9223372036854775807L; // Max permitido poner L al final
    static public float tipoFloat = 3.4028235E38F; // Max permitido. Poner F para representar numeros flotantes
    static public double tipoDouble = 1.7976931348623157E308; // Max permitido

    // Variables con tipos de datos primitivos character
    static public char tipoCharSimbolo = 'P';
    static public char tipoCharUnicode = '\u0050'; // https://en.wikipedia.org/wiki/List_of_Unicode_characters
    static public char tipoCharDecimal = 80;
    
    public static void main(String[] args) {
        
        System.out.println("¡Hola, " + _lenguaje +  " !");
        
    }


    
}