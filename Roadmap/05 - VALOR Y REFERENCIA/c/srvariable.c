/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

#include <stdio.h>

void unmodifier(int num);
void modifier(int *num);
int *swap_value(int num1, int num2);
int *swap_reference(int *num1, int *num2);

int main(void)
{
    /* === 1 === */
    // Asignación por valor
    // num es igual a 200 y another_num a
    int num = 200;
    int another_num = 20123;

    // Asignación por referencia
    // Puntero que apunta a una dirección de memoria
    int *ptr_num = &num;

    // Asignación por valor
    // Puntero que
    int *ptr_ptr = ptr_num;

    /* === EXTRA === */
    // Modificando num y another_num usando punteros
    // que apuntan a sus referencias
    printf("                        num    another_num    ptr_num    ptr_ptr\n");
    printf("Original %18d %14d %10d %10d\n", num, another_num, *ptr_num, *ptr_ptr);
    // Modifico num a 3
    num = 3;
    printf("Modifico num %14d %14d %10d %10d\n", num, another_num, *ptr_num, *ptr_ptr);
    // Dereferencio ptr_num y le asigno 6
    *ptr_num = 6;
    printf("Modifico ptr_num %10d %14d %10d %10d\n", num, another_num, *ptr_num, *ptr_ptr);
    // Dereferencio ptr_ptr y le asigno 27
    *ptr_ptr = 27;
    printf("Modifico ptr_ptr %10d %14d %10d %10d\n", num, another_num, *ptr_num, *ptr_ptr);
    // Reasigno ptr_num a la dirección de memoria de another_num
    ptr_num = &another_num;
    printf("Reasigno ptr_num %10d %14d %10d %10d\n", num, another_num, *ptr_num, *ptr_ptr);
    // Dereferencio ptr_num y le asigno 0
    *ptr_num = 0;
    printf("Modifico ptr_num %10d %14d %10d %10d\n", num, another_num, *ptr_num, *ptr_ptr);
    *ptr_ptr = 89213;
    printf("Modifico ptr_ptr %10d %14d %10d %10d\n", num, another_num, *ptr_num, *ptr_ptr);
    // Reasigno ptr_num a la dirección de memoria de another_num
    ptr_num = ptr_ptr;
    printf("Reasigno ptr_num %10d %14d %10d %10d\n", num, another_num, *ptr_num, *ptr_ptr);
    printf("\n\n\n");

    /* === 2 === */
    printf("Pre unmodifier: %d\n", num);
    unmodifier(num);
    printf("Post unmodifier: %d\n\n", num);
    printf("Pre modifier: %d\n", num);
    modifier(&num);
    printf("Post modifier: %d\n", num);
    printf("\n\n\n");

    /* === DIFICULTAD EXTRA === */
    int num1 = 9;
    int num2 = 6;
    int *temp = NULL;
    printf("                        num1    num2    temp[0]    temp[1]\n");
    printf("Pre swap_value %13d %7d          ?          ?\n", num1, num2);
    temp = swap_value(num1, num2);
    printf("Post swap_value %12d %7d %10d %10d\n", num1, num2, temp[0], temp[1]);
    printf("Pre swap_reference %9d %7d          ?          ?\n", num1, num2);
    temp = swap_reference(&num1, &num2);
    printf("Post swap_reference %8d %7d %10d %10d\n", num1, num2, temp[0], temp[1]);
    return (0);
}

void modifier(int *num)
{
    printf("***Dentro de la función modifier\n");
    printf("Valor de num: %d\n", *num);
    *num = 123;
    printf("***Modificando num...\n");
    printf("Valor de num: %d\n", *num);
    printf("***Saliendo de la función modifier\n");
}

void unmodifier(int num)
{
    printf("***Dentro de la función unmodifier\n");
    printf("Valor de num: %d\n", num);
    num = 123;
    printf("***Modificando num...\n");
    printf("Valor de num: %d\n", num);
    printf("***Saliendo de la función unmodifier\n");
}

int *swap_value(int num1, int num2)
{
    int temp = num1;
    num1 = num2;
    num2 = temp;
    int res[2] = {num1, num2};
    int *ptr_res = res;
    return (ptr_res);
}

int *swap_reference(int *num1, int *num2)
{
    int temp = *num1;
    *num1 = *num2;
    *num2 = temp;
    int res[2] = {*num1, *num2};
    int *ptr_res = res;
    return (ptr_res);
}
