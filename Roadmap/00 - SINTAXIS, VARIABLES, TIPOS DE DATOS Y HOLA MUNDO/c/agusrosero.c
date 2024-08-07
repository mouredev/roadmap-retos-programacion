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

#include <stdio.h>
#include <stdbool.h>

// Primera forma de crear constante
#define CONSTANTE 3.14

int main()
{
    // C no cuenta con un sitio oficial
    // COMENTARIO DE UNA LINEA
    /*
    Comentario de
    multiples lineas
    */

    // Segunda forma de crear constante
    const int SEGUNDA_CONSTANTE = 10;

    // Variables
    int variable = 23;

    // Datos primitivos
    float miFlotante = 3.334455;
    double miDouble = 12.222222333334;
    bool miBooleano = true;
    int miEntero = 20;
    char caracter = 'M';
    char miCadena[] = "Cadena";

    printf("¡Hola, C!");
    return 0;
}