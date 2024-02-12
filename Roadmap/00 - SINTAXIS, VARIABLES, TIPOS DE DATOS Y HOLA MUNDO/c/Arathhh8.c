/*
 * EJERCICIO:
 * 1 Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * 2 Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * 3 Crea una variable (y una constante si el lenguaje lo soporta).
 * 4 Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * 5 Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */


    /* *************** 1 ************* */
/* No existe un sitio web oficial para C, pero agrego una referencia del manual GNU
 * https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html  
*/

#include<stdio.h>

int main(int argc, char **argv){

    /* *************** 2 ************* */

    // Este es un comentario en una sola línea
    /* Este tambien es un comentario de una sola linea */

    /*
        Este es un comentario
        de varias lineas
    */
   /* *************** 3 ************* */

   int num = 5;                  /* Esta es una variable*/
   const int pi = 3.1416;        /* Esta es una constante*/
   #define PI 3.1416;            // Tambien puedes crear constantes de esta forma


    /* *************** 4 ************* */
    int numEntero;
    char caracter;
    short numCorto;
    float numFlotante;
    double numDouble;
    // En el C el tipo "Booleano no esta definido de manera nativa"
    
    /* *************** 5 ************* */
    printf("Hola C!");

    return 0;
}