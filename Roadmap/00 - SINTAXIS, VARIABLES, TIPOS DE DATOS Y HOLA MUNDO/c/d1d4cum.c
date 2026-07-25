#include <stdio.h>
#include <stdbool.h>

// https://www.w3schools.com/c/index.php
// Comentario de una sola línea
/*
Comentario
de varias
líneas
*/

int age = 28;
const char letter = 'D';

// Tipos de datos
char caracter = 'A';
int numero = 10;
float decimalPequeño = 10.191283;
double decimalGrande = 10.192845671829345;
bool boolean = true;

int main() {
    printf("¡Hola, C!\n");
    printf("%c\n", caracter);
    printf("%d\n", numero);
    printf("%f\n", decimalPequeño);
    printf("%.1f\n", decimalPequeño);
    printf("%.2f\n", decimalPequeño);
    printf("%lf\n", decimalGrande);
    printf("%.1lf\n", decimalGrande);
    printf("%.2lf\n", decimalGrande);

    return 0;
}
