system user;

Public class{
    static void Main (string[] args)
    {
        //Llamada inicial a la funcion recursiva para imprimir números del 100 al 0
        console.WriteLine("Imprimiendo números del 100 al 0:");
        ImprimirNumeros(100);

        //Calcular y mostrar el factorial de un número
        int numeroFactorial = 5;
        Console.WriteLine($"\nEl factorial de {numeroFactorial} es: {Factorial(numeroFactorial)}");

        //Calcular y mostrar el elemento de fibonacci en la posicion dada
        int posicionFibonacci = 10;
        Console.WriteLine($"El elemento en la posicion {posicionFibonacci} de la sucesion de Fibonacci es: {Fibonacci(posicionFibonacci)}");
    }
    //Funcion recursiva para imprimir números del 100 al 0
    static void ImprimirNumeros (int n)
    {
        //Caso base: si n es menor que 0, detiene la recursion
        if (n < 0)
        {
            return;
        }

        //Imprime el número actual
        Console.WriteLine(n);

        // Llamada recursiva con el siguente número
        ImprimirNumeros(n - 1);
    }
    
    //Funcion recursiva para calcular el factorial de un número
    static int Factorial(int n)
    {
        //Caso base: el factorial de 0 o 1 es 1
        if (n <= 1)
        {
            return 1;
        }

        // Llamada recursiva
        return n * Factorial(n - 1);
    }

    //Funcion recursiva para calcular el valor de un elemento en la sucesion de Fibonacci

    static int Fibonacci(int n)
    {
        // Caso base: el primer y segundo elemento son 0 y 1, respectivamente
        if (n <= 0)
        {
            return 0;
        }
        else if (n == 1)
        {
            return 1;
        }
        //Llamada recursiva
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
  /*
  
  -Explicación del Código
  
Imprimir números del 100 al 0:
La función ImprimirNumeros(int n) imprime los números desde n hasta 0 utilizando recursión.

Calcular el factorial de un número:
La función Factorial(int n) calcula el factorial de n utilizando recursión. El caso base es n <= 1.

Calcular el valor en la sucesión de Fibonacci:
La función Fibonacci(int n) calcula el valor en la posición n de la sucesión de Fibonacci utilizando recursión. Los casos base son n <= 0 y n == 1.

-Ejecución del Código

Imprimir números del 100 al 0:
La función ImprimirNumeros(100) comienza con 100 e imprime cada número hasta llegar a 0.

Factorial:
La función Factorial(5) calcula 5 * 4 * 3 * 2 * 1 = 120 y lo imprime.

Fibonacci:
La función Fibonacci(10) calcula el 10º elemento de la sucesión de Fibonacci (que es 55) y lo imprime.
*/

}
