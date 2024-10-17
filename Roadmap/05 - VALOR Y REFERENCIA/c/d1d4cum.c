#include <stdio.h>

/*
// Variables por valor
int age1 = 28;
printf("Edad 1: %d\n", age1);

int age2 = age1;
printf("Edad 2: %d\n", age1);
age2 = 30;
printf("Edad 1: %d\n", age1);
printf("Edad 2: %d\n", age2);

// Variables por referencia usando punteros
int* age3 = &age1;
printf("Edad 1: %d\n", age1);
*age3 = 45;
printf("Edad 1: %d\n", age1);
*/

int valor1 = 1;
int valor2 = 2;
int newValor1;
int newValor2;

void valor(int valor1, int valor2) {
    int old1 = valor1;
    int old2 = valor2;

    valor2 = old1;
    valor1 = old2;

    newValor1 = valor1;
    newValor2 = valor2;
}

void reference(int *valor1, int *valor2) {
    int old1 = *valor1;
    int old2 = *valor2;

    *valor1 = old2;
    *valor2 = old1;

    newValor1 = *valor1;
    newValor2 = *valor2;
}

int main() {
    printf("**Paso por valor**\n");
    valor(valor1, valor2);
    printf("Valor 1 original: %d\n", valor1);
    printf("Valor 2 original: %d\n", valor2);
    printf("Valor 1 nuevo: %d\n", newValor1);
    printf("Valor 2 nuevo: %d\n", newValor2);

    printf("**Paso por referencia**\n");
    reference(&valor1, &valor2);
    printf("Valor 1 original: %d\n", valor1);
    printf("Valor 2 original: %d\n", valor2);
    printf("Valor 1 nuevo: %d\n", newValor1);
    printf("Valor 2 nuevo: %d\n", newValor2);

    return 0;
}
