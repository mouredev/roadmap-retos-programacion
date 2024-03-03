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

int Fibonacci(int x)
{
    if (x <= 0)
    {
        Console.WriteLine("No se acepta el numero 0 o valores negativos");
        return 0;
    }
    else if (x == 1)
    {
        return 0;
    }
    else if (x == 2)
    {
        return 1;
    }
    else
    {
        return Fibonacci(x - 1) + Fibonacci(x - 2);
    }
}

Console.WriteLine(Fibonacci(5));