// C no tiene una pagina principal del sitio web, pero existe un libro llamado the language of c muy util
//Elegi el lenguaje de programacion c 
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
int main(){
// Este es un comentario de una sola línea

/*
Este es un comentario
de múltiples líneas
*/

/**
 * Este es un comentario de documentación
 * que puede ser utilizado por herramientas como Doxygen.
 */

// Declaración de variables de tipos de datos primitivos
int entero = 10;                // Entero
float flotante = 3.14;          // Número de punto flotante
double doble = 3.14159265359;   // Número de punto flotante de doble precisión
char caracter = 'A';            // Carácter
bool booleano = true;           // Booleano (requiere <stdbool.h>)

// Declaración de cadenas de caracteres
char cadena[] = "Hola, mundo";  // Cadena de caracteres

// Imprimir un mensaje en la terminal
printf("¡Hola, C!\n");
}