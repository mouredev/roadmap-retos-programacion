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

// Manual de C del proyecto GNU https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html

// Comentario de una línea

/*
 Comentario
 de varias
 líneas
*/

#include "stdio.h"

int main(void){
    // Variable & const
    int num = 9;
    const int year = 2024;

    // primitive data types
    int my_integer = 5;
    char my_str = 'B';
    float my_float = 5.5;
    double my_double = 56.998;
    long my_long = 123456879;
    short my_short = 123;
    unsigned int my_unsigned_int = 50;
    signed int my_signed_int = -70;
    unsigned long int my_u_l_int = 12345555678;
    signed long int my_s_l_int = -1233324554;

    // Terminal print
    char language = 'C';
    printf("¡Hola, %c!\n", language);
    return (0);
}