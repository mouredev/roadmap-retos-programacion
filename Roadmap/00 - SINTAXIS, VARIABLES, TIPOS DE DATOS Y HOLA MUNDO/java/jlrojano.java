// Reto 1 de programacion 2024 por MoureDev

/*
EJERCICIO:
    1. Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
    2. Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
    3. Crea una variable (y una constante si el lenguaje lo soporta).
    4. Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

public class jlrojano {



    // 1. URL del sitio oficial: https://www.java.com/

    // 2. Una linea comentada
    /*
       2. Varias lineas...
       ... comentadas
     */


    public static void main(String[] args) {

        // 3. Crea una variable (y una constante si el lenguaje lo soporta).
        // VARIABLE
        var myVar = 100;
        // CONSTANTE
        final var MY_VAR = false;
        // 4. Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
        byte bByte = 127;
        short sShort = 32767;
        int iInt = 2^32;
        long lLong = 2^63L;
        float fFloat = 123;
        double dMyDouble = 12e306D;
        boolean bMybool = true;
        char cMyChar = 'c';


        // 5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        System.out.println("¡Hola, java!");

    }
}
