package Ejercicio00;

public class Ejercicio00 {
    public static void main(String[] args) {
        //Documentación oficial Java en: https://dev.java/

        /*
        EJERCICIO:
         * - Crea un comentario en el código y coloca la URL del sitio web oficial del
         *   lenguaje de programación que has seleccionado.
         * - Representa las diferentes sintaxis que existen de crear comentarios
         *   en el lenguaje (en una línea, varias...).
         * - Crea una variable (y una constante si el lenguaje lo soporta).
         * - Crea variables representando todos los tipos de datos primitivos
         *   del lenguaje (cadenas de texto, enteros, booleanos...).
         * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        */

        String ejemploVariable = "Esta es una variable";
         final int MI_CONSTANTE = 15; //Constante

        //Datos primitivos:
        char ejChar = 's';
        short ejShort = 3;
        int ejInt = 2024;
        float ejFloat = 1.5f;
        double ejDouble = 45.67;
        boolean ejBoolean = true;
        boolean ejBoolean2 = false;

        String lenguaje = "Java";
        System.out.println("Hola, " + lenguaje + "!");



    }
}
