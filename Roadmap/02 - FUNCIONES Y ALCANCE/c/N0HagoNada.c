#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Funciones Matemáticas
ceil(x) // Redonde al entero mas cercaco
abs(x) // valor abosulot
floor(x) -> redondea para abajo
sqrt(x) -> raiz cuadrada
fmod(x,y) -> calcula el resto de la division de x/y
pow(x,y) -> calcula x elevado y
*/
int funcRetoExtra(char *str1, char *str2);
// Variable global
int globalVar = 100;

// Función sin parámetros ni retorno
void funcionSinParametrosNiRetorno()
{
    printf("Esta función no tiene parámetros ni retorno.\n");
}

// Función con un parámetro
void funcionConUnParametro(int a)
{
    printf("Función con un parámetro, valor: %d\n", a);
}

// Función con múltiples parámetros
void funcionConMultiplesParametros(int a, float b)
{
    printf("Función con múltiples parámetros, int: %d, float: %.2f\n", a, b);
}

// Función con retorno
int funcionConRetorno(int a)
{
    return a * a;
}

// Función que utiliza una variable global
void funcionUsaVariableGlobal()
{
    printf("Acceso a variable global: %d\n", globalVar);
}

long factorial(int n)
{
    if (n <= 0)
    {
        return 1;
    }
    else
    {
        return (n * factorial(n - 1));
    }
}

int main()
{
    // Llamada a función sin parámetros ni retorno
    funcionSinParametrosNiRetorno();

    // Llamada a función con un parámetro
    funcionConUnParametro(5);

    // Llamada a función con múltiples parámetros
    funcionConMultiplesParametros(3, 3.14f);

    // Llamada a función con retorno
    int resultado = funcionConRetorno(5);
    printf("Resultado de función con retorno: %d\n", resultado);

    // Llamada a función que usa una variable global
    funcionUsaVariableGlobal();

    // Uso de una función de la biblioteca estándar de C
    printf("Uso de la función de la biblioteca estándar: %d\n", abs(-10));

    // Demostración de variable local
    int localVar = 20;
    printf("Variable local en main: %d\n", localVar);

    // Funcion recursiva
    printf("Factorial de 20 es %li\n", factorial(localVar));

    return funcRetoExtra("FIZZ", "FUZZ");
}

int funcRetoExtra(char *str1, char *str2)
{
    int rtn = 0;
    for (int i = 100; i > 0; i--)
    {
        if ((i % 3 == 0) && (i % 5 == 0))
        {
            printf("%s%s\n", str1, str2);
        }
        else if (i % 5 == 0)
        {
            printf("%s\n", str1);
        }
        else if (i % 3 == 0)
        {
            printf("%s\n", str2);
        }
        else
        {
            printf("%d\n", i);
            rtn++;
        }
    }
    return rtn;
}