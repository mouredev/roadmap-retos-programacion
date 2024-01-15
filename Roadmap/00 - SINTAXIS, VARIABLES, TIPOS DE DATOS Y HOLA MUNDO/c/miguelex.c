// Documentación en https://devdocs.io/c/

// Comentario de una linea

/* Comentario
en varias
lineas */

#include <stdio.h>

int main()
{
    // Declaramos una variable
    char lenguaje = 'C';

    // Declaramos constante
    const float PI = 3.1415;

    // Tipos primitivos en C
    char letra = 'a';
    int numero = 5;
    float decimalSimple = 0.25;
    double decimalDoble = -5.10;
    long enteroLargo = 12025865L;
    short enteroCorto = 100;
    unsigned enteroSinSigno = 10;
    unsigned long enteroLargoSinSigno = 9889898989898UL;
    unsigned short entroCortoSinSigno = 122;

    // Imprimimos por consola
    printf("Hola, %c!\n", lenguaje);

    return 0;
}
