using System;

internal class Program
{
    static void Main(string[] args)
    {
        int a = 100;
        int b = 2;

        //Operadores aritméticos
        Console.WriteLine($"Suma: {a}+{b}={a+b}");
        Console.WriteLine($"Resta:{a}-{b}={a-b} ");
        Console.WriteLine($"Multiplicación: {a}*{b}={a*b}");
        Console.WriteLine($"División: {a}/{b}={a/b}");
        Console.WriteLine($"Módulo: {a}%{b}={ab}");

        //Operadres lógicos
        Console.WriteLine($"{a} == {b} ? {a==b}");
        Console.WriteLine($"{a} > {b} ? {a>b}");
        Console.WriteLine($"{a} < {b} ? {a<b}");
        Console.WriteLine($"{a} !< {b} ? {a!<b}");

        b = 4;
        if()
        Console.WriteLine($"{a} >= {b} ? {a>=b}");

        //Console.WriteLine($"{a}{b}{ab}");

        //Operadores de asignación
        a = b = 2; //cuando queremos asignar 1 o más variables al mismo valor, podemos asignarlas así
        a = 4;

        //Operador de identidad
        int? c = null;

        Console.WriteLine(a is int);
        Console.WriteLine(c is null);

        //Operador de pertenencia
        int[] array = [2, 4, 8];
        Console.WriteLine(b in array);

        //Operación con bits
        Console.WriteLine(a & b);

        a = 100;
        b = 2;
        int resultado = 100;

        //Iterativo, bucles for, while, dowhile y foreach
        for (int i = 0; i < 10; i++)
        {
            resultado = resultado * b;
        }
        Console.WriteLine(resultado);

        resultado = 100;
        while (resultado > 0)
        {
            resultado = resultado / b;
        }

        resultado = 100;
        do
        {
            resultado = resultado / b;
        } while (resultado > 0);

        foreach (int numero in array)
        {
            Console.WriteLine(numero);
        }

        //Excepciones

        try
        {
            resultado = resultado / 0;
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex);
        }

        //Dificultad extra
        for (int i = 10; i <= 55; i++)
        {
            if (i % 2 == 0 && i != 16 && i % 3 != 0)
                Console.WriteLine(i);
        }
    }
}