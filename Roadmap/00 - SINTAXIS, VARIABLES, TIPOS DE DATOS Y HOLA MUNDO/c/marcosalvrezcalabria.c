#include <stdbool.h>
// URL del sitio web oficial de C: https://en.cppreference.com/w/c

// Comentario en una línea

/*
Comentario en varias líneas:
Este es un comentario que ocupa más de una línea.
C usa /*al inicio y *//* al final para comentarios multilínea.
*/

// Creación de una variable y una constante
int mi_variable = 42;
const double MI_CONSTANTE = 3.14159;  // En C, las constantes se definen usando la palabra clave 'const'

// Variables representando los tipos de datos primitivos de C:
char cadena_texto[] = "Hola, mundo";  // Tipo char[] (cadena de caracteres)
int entero = 10;                      // Tipo int (entero)
float flotante = 3.14f;               // Tipo float (número de coma flotante)
double doble = 2.71828;               // Tipo double (número de coma flotante de doble precisión)
bool booleano = 0;                 // Tipo _Bool (booleano, requiere incluir stdbool.h)
char caracter = 'A';                  // Tipo char (carácter individual)

// Para usar booleanos en C, es necesario incluir el header stdbool.h
#include <stdio.h>
#include <stdbool.h>

// Imprimir por terminal el texto requerido
int main() {
    printf("¡Hola, C!\n");
    return 0;
}
