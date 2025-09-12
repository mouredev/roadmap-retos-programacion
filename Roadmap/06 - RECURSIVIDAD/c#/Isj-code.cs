// Funcion recursiva directa, se llama a si misma
void FuncionRecursiva(int i){
    
    if (i >= 0)
    {
        Console.WriteLine($"Numero: {i}");
        i--;
        FuncionRecursiva(i);
    }
}

FuncionRecursiva(100);

// ## Opcional

// Factorial
int Factorial(int i)
{
    if (i < 0)
    {
        Console.WriteLine("No son permitidos los numeros negativos"); 
    }
    if (i > 1)
    {
        return i *= Factorial(i - 1);
    }
    return i;
}

Console.WriteLine("El Factorial de 4: " + Factorial(4));

// Fibonacci

int Fibonacci(int i)
{
    if (i < 0)
    {
        return 0;
    }else if (i == 0)
    {
        return 0;
    }else if (i == 1)
    {
        return 1;
    }
    else
    {
        return (Fibonacci(i - 1) + Fibonacci(i - 2)); 
    }
}

Console.WriteLine($"La posicion Fibonacci de 8: " + Fibonacci(8));
