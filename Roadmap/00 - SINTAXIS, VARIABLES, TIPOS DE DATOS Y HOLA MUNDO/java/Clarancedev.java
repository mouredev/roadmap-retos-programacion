/**
 * #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
 * @author clarancedev
 * @version 1.0
 * @date 2025-04-05
 */

// Página web oficial de Java: https://www.java.com/en/

// Esta es la sintaxis para comentarios de una sola linea.

/*
Esta es la sintaxis para
comentarios de varias líneas.
 */
 
public class Clarancedev {

    public static final String CONSTANTE_STRING = "Soy una constante de tipo String";

    public static void main(String[] args) {

        // Java tiene 8 tipos de variables primitivos:
        byte soyByte = 0; // Almaceno valores numéricos enteros. Rango: de -128 a 127
        boolean soyBoolean = true; // Almaceno 2 valores: verdadero o falso
        char soyChar = 'c'; // Almaceno un solo caracter, o valor de tipo ASCII
        double soyDouble = 0.0; // Almaceno valores numéricos decimales. Rango: hasta 16 dígitos decimales
        float soyFloat = 0.0f; // Almaceno valores numéricos decimales. Rango: hasta 7 dígitos decimales, añadiendo siempre la letra "f" al final
        int soyInt = 0; // Almaceno valores numéricos enteros. Rango: de -2.147.483.648 a 2.147.483.647
        long soyLong = 0; // Almaceno valores numéricos enteros. Rango: de -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807
        short soyShort = 0; //Almaceno valores numéricos enteros. Rango: de -32.768 a 32.767

        // Esta es la variable para cadenas de texto en Java, aunque ojo, no es una variable primitiva:
        String soyString = "¡Hola, Java!";

        // Así se imprime por la terminal con Java:
        System.out.println(soyString);
    }
}
