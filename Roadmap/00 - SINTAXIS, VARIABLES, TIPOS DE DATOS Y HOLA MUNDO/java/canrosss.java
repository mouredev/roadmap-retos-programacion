/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

public class canrosss {

    /* - Crea un comentario en el código y coloca la URL del sitio web oficial del */
    //Sitio Oficial de Java en Español
    //URL: https://www.java.com/es/
    
    //Comentario de una linea en Java hace esta manera con un doble backslash
   
    /* El comentario multilinea en Java se hace con un backslash y termina con asterisco backslash */ 

    //Constante
    static final String username = "canrosss";

    //Variables en sus tipos de datos primitivos
    //Enteros y char
    char nombre = 'c';
    byte edad = 38;
    short anio = 2025;
    int sueldo = 54000;  //Mexican MXN
    long distanciaLunaTierra = 384400000L; // en metros

    //puntos decimales
    float temperatura = 33.40f;
    double pi = 3.141592653589793;

    //Boolean primitivo
    Boolean isReady=false;

    public static void main(String[] args){
        System.out.println("!Hola, Java!");
    }

}
