// PÁGINA OFICIAL DE JAVA
// https://www.java.com/es/

// COMENTARIOS EN JAVA

// Utilizar "//" para un comentario de una sola línea
// Utilizar "/*" y "*/" para un bloque de comentarios de 2 o más líneas
// Tambien se puede utilizar al iniciar el bloque de comentarios "/*", para cada linea "*" y para finalizar el bloque "*/"

/*
 * Este es un bloque 
 * de comentarios en donde 
 * utilizamos varias lineas 
 * y en cada linea, se 
 * añade un "*"
 */


public class PPSystemsMX {

    // Declaración de una variable
    String miVariable = "Mi variable es de tipo String";

    // Declaración de una constante
    final String miConstante = "Mi Constante es de tipo String";

    //Tipo de datos primitivos

    // Byte acepta valores entre -128 to 127
    byte miByte = 1;

    // Short acepta valores entre -32,768 to 32,767
    short miShort = 32767;

    // int acepta valores entre -2,147,483,648 to 2,147,483,647
    int miInt = 1000000000;

    // long acepta valores entre -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
    long miLong = 1000000000;

    // float acepta valores en coma flotante de precisión simple de 32 bits
    float miFloat = 1.123456f;

    // double acepta valores en coma flotante de precisión simple de 64 bits
    double miDouble = 12345.1234567890;

    // char acepta un solo carácter de 16 bits.
    char miChar = 'l'; 

    // boolean representa un valor de verdad, true o false
    boolean miBoolean = false;

    public static void main(String[] args) {
        //Impresión de texto en la terminal
        System.out.println("¡Hola, Java!");
    }
}
