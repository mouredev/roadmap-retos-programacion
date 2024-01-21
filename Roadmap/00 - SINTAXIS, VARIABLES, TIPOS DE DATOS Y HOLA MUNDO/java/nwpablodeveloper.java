

// #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

// https://www.java.com/es/

public class nwpablodeveloper {
        
    // Variable
    private static String unaVariable = "! Hola ";
    
    // Constante
    private static final String _lenguaje  = "desde Java ¡" ; 

    // Declaracion de variables sin datos ( undefinded )
    private static String tipoStringUndefine;
    
    // Variables con tipos de datos primitivos enteros
    private static byte tipoByte = 127;              // Max permitido
    private static short tipoShort = 32767;          // Max permitido
    private static int tipoInteger = 2147483647;     // Max permitido

    // Variables con tipos de datos primitivos flotantes
    private static long tipoLong = 9223372036854775807L;       // Max permitido poner L al final
    private static float tipoFloat = 3.4028235E38F;            // Max permitido. Poner F para representar numeros flotantes
    private static double tipoDouble = 1.7976931348623157E308; // Max permitido

    // Variables con tipos de datos primitivos character
    private static char tipoCharSimbolo = 'P';
    private static char tipoCharUnicode = '\u0050'; // https://en.wikipedia.org/wiki/List_of_Unicode_characters
    private static char tipoCharDecimal = 80;
  
    // Variables con tipos de datos primitivos de decision
    private static boolean tipoBoolean = true;

    public static void main(String[] args) {
        
        System.out.println( unaVariable + _lenguaje );
        
    }


    
}