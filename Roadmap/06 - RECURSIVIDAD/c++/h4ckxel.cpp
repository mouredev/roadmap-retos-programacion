#include <iostream>

void PrintNumbers(int number)
{
    if(number >= 0)
    {
        printf("%d\n", number);
        PrintNumbers(number-1);
    }

    return;
}

int Factorial(int number)
{
    if(number==0)
        return 1;
    else
        return (number * Factorial(number-1));
}

int Fibonacci(int number)
{
    if(number == 0)
        return 0;
    else if(number == 1)
        return 1;
    else
        return ((Fibonacci(number-1) + Fibonacci(number-2)));
}

int main()
{
    PrintNumbers(100);
    printf("\n5! = %d\n\n", Factorial(5));

    for(int i=1; i<11; i++)
    {
        printf("Valor de la %d%c posicion en la sucesion de Fibonacci: %d\n", i, 167, Fibonacci(i));
    }
    
    return 0;
}