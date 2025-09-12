/*
    EJERCICIO:
    1) Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
    2) Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
    3) Crea una variable (y una constante si el lenguaje lo soporta).
    4) Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    5) Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

// 1) https://docs.oracle.com/en/java/javase/21/index.html

// 2) Comentario de una linea y varias

/*
    Comentario de varias lineas

 */

public class Darubiano {
    public static void main(String[] args) {

        // 3) Variable y constante
        String variable = "Java";
        final String constante = "Texto constante";

        // 4) Tipos de variables primitivas
        // Tipos numericos java
        byte numeroByte = 10;
        short numeroShort = 1;
        int numeroInt = 123;
        long numeroLong = 123456789L;
        float numeroFloat = 3.14F;
        double numeroDouble = 123.123D;
        // Tipos numericos java Objecto, pueden ser Nulos
        Byte numeroByteObjeto = 10;
        Short numeroShortObjeto = 1;
        Integer numeroIntObjeto = 159;
        Long numeroLongObjeto = 123456789L;
        Float numeroFloatObjeto = 3.14F;
        Double numeroDoubleObjeto = 123.123D;

        // Tipos texto java
        char textoChar = 'H';
        String textoString = "Texto";
        // Tipos texto java Objecto, pueden ser Nulos
        Character textoCharObjeto = 'H';
        String textoStringObjeto = "Texto";

        // Tipo boleano
        boolean valorVerdadero = true;
        boolean valorFalso = false;
        // Tipos boleano java Objecto, pueden ser Nulos
        Boolean valorVerdaderoObjecto = true;
        Boolean valorFalsoObjecto = false;

        // Tipos Lista
        Integer[] listaNumeros = { 1, 2, 3, 4, 5 };

        // 5) print java
        System.out.println("¡Hola, Java!");
    }
}
