// Página: https://en.cppreference.com/w/c

// Comentario en una línea.

/*
   Comentario de varias líneas.
   Aquí puedes añadir información... 
   :p
*/

#include <stdio.h>
#include <stdbool.h>             // Para usar booleanos en C

// Constante con '#define'
#define PI 3.14159             

// Constante con 'const'  
const int MAX_USERS = 100;       

float radio = PI;                // Variable global usando '#define'

int main(void)
{
    int usuarios_actuales = MAX_USERS - 10;    // Variable local usando 'const'

    // Datatypes (Sistemas de 32 y 64 bits)
    char a = 'C';                              // 1 byte  | Range: -128 a 127 (modern systems)
    short b = -15;                             // 2 bytes | Range: -32,768 a 32,767
    int c = 1024;                              // 4 bytes | Range: -2,147,483,648 a 2,147,483,647
    unsigned int d = 128;                      // 4 bytes | Range: 0 a 4,294,967,295
    long e = 123456;                           // 4 bytes (32-bit) / 8 bytes (64-bit)
    float f = 15.678;                          // 4 bytes | ~6-7 dígitos de precisión
    double g = 123123.123123;                  // 8 bytes | ~15-16 dígitos de precisión
    bool h = true;                             // 1 byte  | Values: true (1) o false (0)

    printf("¡Hola, %c!\n", a);  // Imprime "¡Hola, C!" usando el valor de la variable 'a' (char)
}