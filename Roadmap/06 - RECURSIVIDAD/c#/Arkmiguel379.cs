int Resta(int x)
{
    if (x == 0)
    {
        return x;
    }
    else
    {
        Console.WriteLine(x);

        return Resta(x - 1);
    }
}

Console.WriteLine(Resta(100));

Console.WriteLine();


// ====== EXTRA ======

Console.WriteLine("=== CALCULO FACTORIAL ===");
int Factorial(int x)
{
    if (x == 0)
    {
        return 1;
    }

    return x * Factorial(x - 1);
}

Console.WriteLine(Factorial(5));

Console.WriteLine();


Console.WriteLine("=== CALCULO SUCESION FIBONACCI === \n");

int a = 0;

int b = a + 1;

int c = a + b;

int Fibonacci(int x)
{
    if (x == 0)
    {
        return b - a;
    }

    a = b;
    b = c;
    c = a + b;

    return Fibonacci(x - 1);
}

Console.WriteLine(Fibonacci(9)); // Según la posición que se le pase a la función, ella mostrará el valor de la sucesión de Fibonacci
                                 // que se encuentra en esa posición, teniendo presente que 0 es la posición 1.

