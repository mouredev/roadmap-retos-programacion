/* ╔══════════════════════════════════════╗
   ║ Autor:  Kenys Alvarado               ║
   ║ GitHub: https://github.com/Kenysdev  ║
   ║ 2024 -  C#                           ║
   ╚══════════════════════════════════════╝
   ----------------------------------------
   # Recursividad
   ----------------------------------------
 - La recursividad es la capacidad de una función para llamarse a sí misma,ya sea 
   de forma directa o indirecta, con el propósito de resolver un problema. 
   _________________________________
// imprimiendo números del 100 al 0.
 - Ejemplo con recursividad directa
   ocurre cuando una función se llama a sí misma. */

Console.WriteLine("recursividad directa");
void Recursive(int n)
{
    Console.WriteLine(n);
    // caso base
    if (n > 0) // evitar que la función se llame indefinidamente.
    {
        Recursive(n - 1);
    }    
}

Recursive(100);

// - Ejemplo con recursividad indirecta
//   implica que varias funciones se llamen entre sí.

Console.WriteLine("recursividad indirecta");
void Sub(int n)
{
    Recursive2(n - 1);
}

void Recursive2(int n)
{
    Console.WriteLine(n);
    // caso base
    if (n > 0)
    {
        Sub(n);
    }
}

Recursive2(100);

/* ___________________________________________________________________
   Ejercicios:
   -----------
1. Calcular el factorial de un número concreto (la función recibe ese número).
   4! = 4 * 3 * 2 * 1 = 24 */
int Factorial(int n)
{
    if (n != 0)
    {
        return n * Factorial(n - 1);
    }
    else
    {
        return 1;
    }
    /* Explicación
    fac(4)
        | = 24 
     return 4 * fac(3) ->(4 * 6)
                  | = 6 
         return 3 * fac(2) ->(3 * 2)
                      | = 2 
             return 2 * fac(1) ->(2 * 1)
                          | = 1 
                 return 1 * fac(0) ->(1 * 1)
                              | = return 1 -> caso base */
}

/* ___________________________________________________________________
2. Calcular el valor de un elemento concreto (según su posición) en la 
   sucesión de Fibonacci (la función recibe la posición).
   n : |0|1|2|3|4|5|6|..
   fb: |0|1|1|2|3|5|8|..
        |+|=^   |+|=^ ..  */

int Fibonacci(int n)
{
    if (n <= 1)
    {
        return n;
    }
    else
    {
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
    /* Explicación fib(4) 
                         return 3
               fib(3)      / \    fib(2)
                / \ =2      +      / \ =1
          fib(2) + fib(1)    fib(1) + fib(0) -> caso base
          / \ =1
    fib(1) + fib(0) -> caso base  */
}
// NOTE: Este enfoque recursivo puede ser ineficiente para valores grandes de "n".

// ___________________________________________________________________
Console.WriteLine(@$"
Factorial de 4: {Factorial(4)}
Posición 4 en Fibonacci: {Fibonacci(4)}");
