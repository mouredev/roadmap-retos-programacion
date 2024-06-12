/*
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


// Comentarios

// Comentarios de una línea.

/* 
* Comentarios de varias líneas.
* Esto es otra línea de comentario.
*/

/*
* He encontrado varias webs donde se habla de c y su estructura, pero no hay una página oficial de documentación en si o por lo menos yo no la he encontrado.
* https://learn.microsoft.com/es-es/cpp/c-language/organization-of-the-c-language-reference?view=msvc-170 - Página web de Microsoft.
* https://devdocs.io/c/ - Documentación de varios lenguajes de programación entre ellos c.
* https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html - Otra documentación.
*/

#include <stdio.h>

int main() {

// Variables y constantes. Datos Primitivos

// Enteros: Los enteros representan números sin parte decimal. Se utilizan para almacenar valores numéricos enteros, positivos o negativos.

int numeroPositivo = 5;
int numeroNegativo = -65;

printf("Impresión de valores enteros positivos: %i y enteros negativos: %i\n", numeroPositivo, numeroNegativo);

// Coma flotante: Son los números que poseen una parte decimal, los hay de dos tipos float y double, float es menos preciso que double, y se double se deberia utilizar para operaciones matemáticas que necesiten mayor precisión.

float decimalPositivo = 15.1548;
double decimalMasPreciso = 65.14785421658;

printf("Impresión de valores de coma flotante float: %f y double %.15lf\n", decimalPositivo, decimalMasPreciso);

// Caracteres: Son tipos de datos que representan símbolos individuales, como letras, números o otros caracteres especiales.

char caracterLetra = 'A';
char caracterNumero = '9';

printf("Impresión de valores carácter o char, por ejemplo letras: %c, o números: %c\n", caracterLetra, caracterNumero);

// Constantes: Son valores que no cambian durante la ejecución del programa.

#define PI 3.14159

const int DIAS_SEMANA = 7;

printf("Constantes preprocesadas: %.5f y constantes declaradas: %i.\n", PI, DIAS_SEMANA);

// Para imprimir en consola se utiliza printf("")

const char LENGUAJE = 'C';

printf("Hola, %c!!!\n", LENGUAJE);

}
