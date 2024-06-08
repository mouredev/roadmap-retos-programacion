/**
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 * 
 * 
 */


//https://www.java.com/es/
//este es el comentario simple de una linea
/*
 * con este podremos comentar varias linas
 * 
 */


public class LizanDev {
    
    public static void main(String[] args) {
        int numero=0;
        double decimal = 0.0;
        float otroDecimal= 0.0f;
        char caracter = 'A';
        String texto ="entre comillas introduciremos el texto";
        boolean booleano = true;
        long largo= 236297332L;
        short corto= 32767;


        String lenguaje= "Java";

        System.out.println("¡Hola, "+lenguaje);


    }

}
