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

#include <stdio.h>

void             imprimir_del_100_al_0(int num);
unsigned int     factorial(unsigned int num);
unsigned int     fibonacci(unsigned int pos);
void             imprimir_string(char *str, int index);
void             imprimir_string_al_reves(char *str, int index);

// Variables globales que servirán para la dificultad extra
unsigned int    num1 = 0;
unsigned int    num2 = 1;

int main(void)
{
    printf("Imprimir del 100 al 0 con recursividad\n");
    
    /* === 1 === */
    imprimir_del_100_al_0(100);
    printf("\n\n\n");

    /* === DIFICULTAD EXTRA === */
    // Calcular el factorial
    unsigned int num;
    printf("Factorial de un número\n");
    printf("Introduce un número: ");
    scanf("%u", &num);
    printf("%u! %u\n\n\n", num, factorial(num));

    // Encontrar un elemento en la sucesión de Fibonacci
    unsigned int pos;
    printf("La sucesión de Fibonacci es 0, 1, 1, 2, 3, 5, 8, 13, 21...\n");
    printf("Introduce una posición: ");
    scanf("%u", &pos);
    printf("La posición %u de la sucesión de Fibonacci es: %u\n\n\n", pos, fibonacci(pos));

    // EXTRA
    char str[] = "Hola";
    // Imprimir el string con recursividad
    printf("Imprimir el string \"%s\" del derecho: ", str);
    imprimir_string(str, 0);
    printf("\n");
    printf("Imprimir el string \"%s\" del revés: ", str);
    imprimir_string_al_reves(str, 0);
    printf("\n");

    return (0);
}

void imprimir_del_100_al_0(int num)
{
    // Caso base: Si el número es menor que 0 se sale de la función
    if (num < 0)
        return ;

    // Caso recursivo: Imprime el número y se llama a sí misma con un
    // número menos que el original, hasta que llegue al caso base
    printf("%d ", num);
    imprimir_del_100_al_0(num - 1);
}

unsigned int factorial(unsigned int num)
{
    // Caso base: Si el número es menor que 2 devuelve 1
    // Esto se debe a que 0! y 1! es igual a 1
    if (num < 2)
        return (1);

    // Caso recursivo: Devuelve el número por el factorial del número
    // menos uno.
    // Es decir, si el número es 5 tendremos:
    // 5 * factorial(4)
    // 4 * factorial(3)
    // 3 * factorial(2)
    // 2 * factorial(1)
    // Y luego volvería a la función original:
    // 2 * 1 = 2
    // 3 * 2 = 6
    // 4 * 6 = 24
    // 5 * 24 = 120
    // Por lo que el resultado sería 120
    return (num * factorial(num - 1));
}

unsigned int fibonacci(unsigned int pos)
{
    unsigned int        temp;
                            
    // Caso base: Si la posición es 1, devuelve el num1 (0)
    // Si la posición es 2, devuelve num2, que tendrá o 1 (valor original) 
    // o el valor en la posición indicada
    if (pos == 1)
        return (num1);
    else if (pos == 2)
        return (num2);

    // Caso recursivo: Obtengo el siguiente valor en la sucesión y
    // llamo a la función con la posición - 1, hasta que llegue al caso
    // base
    temp = num1 + num2;
    num1 = num2;
    num2 = temp;
    return (fibonacci(pos - 1));
}

void imprimir_string(char *str, int index)
{
    // Caso base: Si el carácter es nulo, se sale
    if (str[index] == '\0')
        return ;
    // Imprimo el carácter y luego llamo a la función con index + 1
    printf("%c", str[index]);
    imprimir_string(str, index + 1);
}

void imprimir_string_al_reves(char *str, int index)
{
    // Caso base: Si el carácter es nulo, se sale
    if (str[index] == '\0')
        return ;
    // Llamo a la función con index + 1 y luego imprimo el carácter
    imprimir_string_al_reves(str, index + 1);
    printf("%c", str[index]);
}
