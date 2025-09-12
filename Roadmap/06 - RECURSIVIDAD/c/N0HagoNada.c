#include <stdio.h>
#include <stdlib.h>

void NumerosCienaCero(int n);

unsigned long long fibonnaci(int n);

unsigned long long factorial(int n);

void main()
{
    unsigned long long fibo = fibonnaci(50);
    printf("Calculo fibonnaci para 50: %llu\n", fibo);
    unsigned long long fact = factorial(20);
    printf("\n Calculo factorial de 20: %llu\n", fact);
    printf("********************* Numeros del cien a cero **********************\n");
    NumerosCienaCero(100);
}

void NumerosCienaCero(int n)
{
    if (n <= 0)
    {
        return;
    }
    printf("%d\t", n);
    NumerosCienaCero(n - 1);
}
unsigned long long factorial(int n)
{
    if (n == 1)
    {
        return 1;
    }
    long long calculo = n * factorial(n - 1);
    return calculo;
}
unsigned long long fibonnaci(int n)
{
    if (n <= 1)
        return n;
    return fibonnaci(n - 1) + fibonnaci(n - 2);
}