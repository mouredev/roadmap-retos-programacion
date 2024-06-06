#include <stdio.h>

// Función para demostrar el paso de argumentos por valor
void incrementarPorValor(int x)
{
    x++;
    printf("Dentro de incrementarPorValor: %d\n", x); // Valor incrementado localmente
}

// Función para demostrar el paso de argumentos por referencia
void incrementarPorReferencia(int *x)
{
    (*x)++;                                                 // deference
    printf("Dentro de incrementarPorReferencia: %d\n", *x); // Valor incrementado en la variable original
}
// Función para intercambiar dos valores por referencia
void intercambioPorReferencia(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    // Asignación por valor
    int a = 10;
    int b = a;                                             // b ahora tiene una copia del valor de a
    b = 20;                                                // Modificar b no afecta a a
    printf("Asignación por valor - a: %d, b: %d\n", a, b); // a: 10, b: 20

    // Asignación por referencia
    int c = 30;
    int *p = &c;                                                  // p apunta a la dirección de memoria de c
    *p = 40;                                                      // Modificar el valor de *p cambia el valor de c
    printf("Asignación por referencia - c: %d, *p: %d\n", c, *p); // c: 40, *p: 40

    // Paso de argumentos a funciones por valor
    int valor = 10;
    printf("Antes de incrementarPorValor: %d\n", valor);
    incrementarPorValor(valor);
    printf("Después de incrementarPorValor: %d\n", valor); // El valor original no cambia

    // Paso de argumentos a funciones por referencia
    int referencia = 10;
    printf("Antes de incrementarPorReferencia: %d\n", referencia);
    incrementarPorReferencia(&referencia);
    printf("Después de incrementarPorReferencia: %d\n", referencia); // El valor original cambia

    /****************************************************RETO******************************************/
    int x = 1, y = 2;
    int nuevoX, nuevoY;

    // Intercambio por referencia
    nuevoX = x;
    nuevoY = y;
    intercambioPorReferencia(&nuevoX, &nuevoY);

    printf("Original: x = %d, y = %d\n", x, y);
    printf("Intercambio por referencia: nuevoX = %d, nuevoY = %d\n", nuevoX, nuevoY);

    return 0;
}