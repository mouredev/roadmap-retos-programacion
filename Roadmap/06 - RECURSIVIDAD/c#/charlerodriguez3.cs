/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 *
 **/

imprimirNumerosDel1Al100(100);

static void imprimirNumerosDel1Al100(int num)
{
    if (num > -1)
    {
        Console.WriteLine(num);
        imprimirNumerosDel1Al100(num - 1);
    }
}





/*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
Console.WriteLine(FactorialNumero(5));

static int FactorialNumero(int num)
{
    if (num == 1) return num *1;
    else return num * FactorialNumero(num-1);
}


Console.WriteLine(ElementoFibonacci(11));

static int ElementoFibonacci(int pos)
{
    if (pos < 0) return 0;
    else if (pos == 1 || pos == 2) return 1;
    else return ElementoFibonacci(pos -1) + ElementoFibonacci(pos - 2);
}
