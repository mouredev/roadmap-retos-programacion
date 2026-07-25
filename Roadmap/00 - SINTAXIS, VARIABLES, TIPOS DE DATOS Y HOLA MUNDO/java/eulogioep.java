// URL del sitio web oficial de Java
// https://www.oracle.com/java/

// Diferentes formas de crear comentarios en Java:

// 1. Comentario de una línea

/*
 * 2. Comentario
 * de varias
 * líneas
 */

/**
 * 3. Comentario de documentación (Javadoc)
 * Se usa para generar documentación automática del código
 */

 public class eulogioep {
    public static void main(String[] args) {
        // Creación de una variable
        String miVariable = "Hola, Java!";

        // Creación de una constante
        final int MI_CONSTANTE = 42;

        // Variables representando tipos de datos primitivos en Java
        byte miByte = 127;
        short miShort = 32767;
        int miInt = 2147483647;
        long miLong = 9223372036854775807L;
        float miFloat = 3.14f;
        double miDouble = 3.14159265359;
        boolean miBoolean = true;
        char miChar = 'A';

        // Impresión del texto solicitado
        System.out.println("¡Hola, Java!");

        // Impresión de los valores de las variables (opcional, para verificación)
        System.out.println("miVariable: " + miVariable);
        System.out.println("MI_CONSTANTE: " + MI_CONSTANTE);
        System.out.println("miByte: " + miByte);
        System.out.println("miShort: " + miShort);
        System.out.println("miInt: " + miInt);
        System.out.println("miLong: " + miLong);
        System.out.println("miFloat: " + miFloat);
        System.out.println("miDouble: " + miDouble);
        System.out.println("miBoolean: " + miBoolean);
        System.out.println("miChar: " + miChar);
    }
}