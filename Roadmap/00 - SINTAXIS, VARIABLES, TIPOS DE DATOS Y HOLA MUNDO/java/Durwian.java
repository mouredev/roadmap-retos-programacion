/* EJERCICIO1:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */


class Durwian{

    // URL web sitio oficial: https://www.java.com

    // Comentario de una línea con dos slash

    /*
     * Comentario en 
     * varias líneas.
     * Con slash y asterisco.
     */

    private String variable = "Hola mundo";
    
    private static final Integer CONSTANTE = 2024;


    //Tipos de variables primitivos
    
    byte ochoBits;
    int entero;
    short enteroPequeno;
    long enteroGrande;
    float decimal;
    double decimalDoble;
    boolean bolano;
    char caracter;

    // Tipos estructurados

    String palabra;
    String[] arreglo;
    Durwian tipoObjeto;

    public static void main (String [ ] args) {
        System.out.println("¡Hola, Java!");
    }
}
