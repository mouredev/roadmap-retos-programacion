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

#include <stdio.h>
#include <stdbool.h>

int    main(int argc, char **argv)
{
    /* ==== 1 ==== */
    // En C no existe sitio web oficial, asi que muestro
    // el manual de GNU
    // https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html

    /* ==== 2 ==== */

    // Esto es un comentario en línea.
    /* Esto también es un comentario en línea. */
    /*
     * Esto es un comentario
     * en
     * varias líneas.
     */

    // NOTA: En los comentarios de varias líneas no es necesario
    // poner asterisco al principio, solo en el último para poder
    // cerrar el comentario (*/).

    /* ==== 3 ==== */
    const char	x; // Utilizando const se evita que el valor cambie.

    /* ==== 4 ==== */
    char                    lang = 'C'; // Este es el generalmente utilizado
    unsigned char           uchar;
    int                     number; // Este es el generalmente utilizado
    unsigned int            unumber;
    short int               snumber;
    unsigned short int      usnumber;
    long int                lint;
    unsigned long int       ulint;
    long long int           llint;
    unsigned long long int  ullint;
    float                   position = 1259.32f; // Este es el generalmente utilizado
    double                  sqrt2 = 1.41421356237; // Este es el generalmente utilizado
    long double             pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342L;

    /* Bonus */
    // En C no existe el tipo Strings. Para tener algo similar
    // están los arrays de caracteres, con la característica de que
    // terminan con el carácter nulo.
    char                    hellostring[] = "Hola"; // Esto sería un array de 5 caracteres. {'H', 'o', 'l', 'a', '\0'}

    // Tampoco existe el tipo Bool (o Boolean) por defecto. Para el
    // equivalente se suele utilizar un int con el valor 0 para
    // representar el 'False' y cualquier otro valor para 'True'.
    int                     nonprimitivebooltrue = -1;
    int                     nonprimitivebooltrue2 = 1;
    int                     nonprimitiveboolfalse = 0;
    
    // También puedes incluir la librería stdbool.h que incluye
    // el tipo de dato bool.
    bool                    abool = true;
    bool                    abool2 = false;

    /* ==== 5 ==== */
    printf("¡%s, %c!\n", hellostring, lang); // Imprime por pantalla "¡Hola, C!" seguido de un salto de línea.
    // NOTA: Para utilizar esta función necesitas incluir la librería
    // stdio.h
}
