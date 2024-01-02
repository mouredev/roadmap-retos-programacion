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

// documentacion oficial: https://devdocs.io/c/

// Comentario de una linea

/*
    Comentario en
    varias lineas
*/

// header con algunas funcionalidades basicas
#include <stdio.h>
#include <stdlib.h> // contiene NULL y memoria dinamica
#include <string.h> // contiene funciones de string

// Hay varias formas de crear constante:
// Forma 1: #define

#define CONSTANTE ((int)5)

// Forma 2: enum
enum COLOR
{
    red,
    blue,
    grey,
    yellow
};
/*
    Cada constante perteneciente a COLOR empieza por orden numerico
    ejemplo: red = 0; blue = 1;
    Tambien se puede poner algun valor y los siguientes incrementan 1 en 1
*/
// ej2:
enum DIAS_SEMANA
{
    lunes = 1,
    martes,
    miercoles,
    jueves,
    viernes
    //   Aqui lunes = 1; martes = 2; ...

};

int main()
{
    // forma 3: palabra reservada 'const'
    const int numero = 3;

    // VARIABLES:

    // enteras:
    int num = 5;
    unsigned int bit = 1;

    long grande = 46648987;

    // punto flotante:
    float radio = 1.5;
    double promedio;

    // vectores:
    int vector[5] = {1, 2, 4, 6, 7}; // vector tipo int

    // punteros
    int *p;
    p = &vector[0];

    // caracter:
    char c;
    c = 'a';

    // strings:
    // forma 1: memoria estatica
    char str[10] = "hola mundo";

    // forma 2: punteros y/o memoria dinamica
    char *pString;
    pString = (char *)malloc(sizeof(char) * 5); // complejo no?
    // le ingresamos un texto al string
    strcpy(pString, "hola");

    // imprimimos en terminal

    printf("Hola, lenguaje C\n");
    printf("imprimimos entero: %d\n", num);
    printf("imprimimos long: %ld\n", grande);
    printf("imprimimos vector enteros: ");
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", vector[i]);
    }
    printf("\n");
    printf("imprimimos puntero a entero: ");
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", *(p + i));
    }
    printf("\n");

    printf("imprimimos flotante: %f\n", radio);
    printf("imprimimos caracter: %c\n", c);
    printf("imprimimos string1: %s\n", str);
    printf("imprimimos string2: %s\n", pString);

    // liberamos memoria del puntero a string (recomendable)
    free(pString);

    return 0;
}