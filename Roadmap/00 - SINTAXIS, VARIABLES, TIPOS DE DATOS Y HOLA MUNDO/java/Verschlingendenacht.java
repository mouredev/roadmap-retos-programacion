public class Verschlingendenacht {
    public static void main(String[] args){

        ////////////////////////////////////////
        //REQUISITO 1: LINK OFICIAL DEL LENGUAJE
        //https://www.java.com/es/
        ////////////////////////////////////////

        ////////////////////////////////////////
        //REQUISITO 2: REPRESENTACION DE COMENTARIOS EN JAVA

        //comentario de línea definido por un doble slash al inicio   <------

        /*
        Hola, esto es un comentario de bloque
        Estoy definidio por un slash seguido de un asterisco al inicio
        Luego de mi comentario, un asterisco seguido de un slash invertido al final.
         */
        ////////////////////////////////////////

        ////////////////////////////////////////
        //REQUISITO 3: VARIABLE Y CONSTANTE

        var x = "soy una variable de valor manipulable";
        final var Y = "soy una variable de valor constante, nadie me puede cambiar";
        ////////////////////////////////////////

        ////////////////////////////////////////
        //REQUISITO 4: DATOS PRIMITIVOS EN JAVA

        //Para texto:
        String miCadena = "Java!";
        char miCaracter = 'a';

        //Para numeros enteros:
        byte miByte = 127;
        short miShort = -32768;
        int miEntero = 2147483647;
        long miLong = -9223372036854775808L;

        //Para numeros de punto flotante:
        float miFloat = 3.14159f;
        double miDouble = 3.14159265358979323846d;

        //Para booleanos:
        boolean miBooleano1 = true;
        boolean miBooleano2 = false;
        ////////////////////////////////////////

        ////////////////////////////////////////
        //REQUISITO 5: IMPRESION POR TERMINAL
        System.out.println("¡Hola, "+miCadena);
        ////////////////////////////////////////
    }
}
