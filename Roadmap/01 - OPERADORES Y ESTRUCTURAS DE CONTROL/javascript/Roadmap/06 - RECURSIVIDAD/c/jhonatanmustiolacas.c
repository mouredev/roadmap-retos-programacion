/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */
// Cabecera
#include <stdio.h>

// Funciones de cabecera
void                imprimir_del_cien_al_cero_recursivo(int numero);
long long int       calculo_feactorial_recursivo(int numero);
long long int       fibonacci_en_recursivo(int posicion);

// Definiciones
#define MINIMO 0
#define MAXIMO 100
#define FACTORIAL numero * calculo_feactorial_recursivo(numero - 1)
#define FIBONACCI fibonacci_en_recursivo(posicion - 2) + fibonacci_en_recursivo(posicion - 1)


// Main
int main(void)
{
    imprimir_del_cien_al_cero_recursivo(MAXIMO);

    int numero = 5;
    printf("El factorial de %d es %d\n", numero, calculo_feactorial_recursivo(numero));

    printf("El fibonacci en la posición %d es %d\n", numero, fibonacci_en_recursivo(numero));
}

// Funciones
void imprimir_del_cien_al_cero_recursivo(int numero)
{
    if (numero < MINIMO)
    {
        return ;
    }
    printf("%d\n", numero);
    imprimir_del_cien_al_cero_recursivo(numero - 1);
}

long long int calculo_feactorial_recursivo(int numero)
{
    if (numero == MINIMO)
    {
        return 1;
    }
    return FACTORIAL;
}

long long int fibonacci_en_recursivo(int posicion)
{
    if (posicion == 1)
    {
        return 1;
    }
    else if (posicion == 0)
    {
        return 0;
    }
    else
    {
        return FIBONACCI;
    }
}