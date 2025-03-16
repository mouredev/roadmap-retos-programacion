class Program
{
    static void Main(string[] args)
    {
        // Imprimir Numeros 100 al 0
        var cien = 100;
        ImprimirNumeros100Al0(cien);

        // Factorial
        var numero = 7;
        Console.WriteLine($"El Factorial de {numero} es {Factorial(numero)}");

        // Fibonacci
        var posicion = 6;
        Console.WriteLine($"El Fibonacci en la posicion {posicion} es {Fibonacci(posicion)}");
        

    }


    static void ImprimirNumeros100Al0(int num)
    {
        if(num < 0) return; // Caso base: si num es menor que 0, se acaba la recursion

        Console.WriteLine(num);


        ImprimirNumeros(--num); // Llamada Recursiva con --num (num - 1)
    }

    static int Factorial(int num)
    {
        if(num == 0) return 1; // Caso Base

        return num * Factorial(num - 1); // Llamada Recursiva
    }

    static int Fibonacci(int num)
    {
        if(num == 0) return 0; // Casos Base
        if(num == 1) return 1;

        Console.WriteLine(num);

        return Fibonacci(num - 1) + Fibonacci(num - 2); // Llamada recursiva
    }
}