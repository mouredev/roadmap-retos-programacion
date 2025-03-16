/*
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


// https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html
// https://en.wikibooks.org/wiki/C_Programming
// https://devdocs.io/c/

// Comment in one line

/**
 * comment
 * in
 * block
 */

#include <stdio.h>

#define CONSTANT "This is a constant"


int main() {

    // Variables
    char letter = 'a';
    int integer = 1;
    float floating = 10.5;
    double double_floating = -1.35;
        
    printf("Hello C!\n");
    printf("This is a constant: %s\n", CONSTANT);
    printf("This is a char: %c\n", letter);
    printf("This is an integer: %d\n", integer);
    printf("This is a float: %g\n", floating);
    printf("This is a double: %lf\n", double_floating);
    return 0;
}

