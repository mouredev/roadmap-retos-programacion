/*
 * EJERCICIO:
 * 1) Crea un comentario en el código y coloca la URL del sitio web oficial del
 *      lenguaje de programación que has seleccionado.
 * 2) Representa las diferentes sintaxis que existen de crear comentarios
 *      en el lenguaje (en una línea, varias...).
 * 3) Crea una variable (y una constante si el lenguaje lo soporta).
 * 4) Crea variables representando todos los tipos de datos primitivos
 *      del lenguaje (cadenas de texto, enteros, booleanos...).
 * 5) Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

 public class LewisOneil {
    // 1) URL web Java: https://www.oracle.com/java/

    // 2.1) Esto es un comentario en una línea
    
    /* 
     * 2.2) Esto es un bloque
     *      de comentarios
     */
    
    /**
     * 2.3) Comentario JavaDoc
     */
    
    // 3.1) Variable
    static String variable = "¡Hola, ";
    
    // 3.2) Constante
    static final String CONSTANTE = "Java!";
    
    // 4) Tipos de datos primitivos
    byte bite = 127;            // byte
    short corto = 23;           // entero corto
    int entero = 23;            // entero
    long largo = 23L;           // entero largo
    float flotante = 30.23f;    // decimal, precisión simple
    double doble = 23.30;       // decimal, precisión doble
    boolean boleano = true;     // booleano
    char caracter = 'c';        // carácter
    
    public static void main(String[] args) {

        // 5) Imprimir por terminal
        System.out.println(variable + CONSTANTE);
    }

}