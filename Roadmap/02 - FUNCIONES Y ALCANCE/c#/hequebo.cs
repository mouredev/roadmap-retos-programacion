class Program
{

    // Variables Globales
    static string variableGlobal = "Esta es una variable global";
    static void Main(String[] args)
    {
        HolaMundo();
        SaludoPersonalizado("Emilio");

        Console.WriteLine("Bienvenido a la calculador de IMC");
        Console.WriteLine("Ingresa tu peso en kg:");
        decimal peso = decimal.Parse(Console.ReadLine());
        Console.WriteLine("Ingresa tu altura en mts");
        decimal altura = decimal.Parse(Console.ReadLine());
        decimal imc = CalcularIMC(peso, altura);
        imc = Math.Round(imc, 2);
        Console.WriteLine($"Tu IMC es de {imc}");

        double random = GenerarNumeroAleatorio();
        Console.WriteLine($"El número generado de manera aleatoria es {random}");

        double resultado = MultiplicacionConNumeroAleatorio(3.15);
        Console.WriteLine($"El resultado de la multiplicación es {resultado}");

        //Funciones creadas dentro del lenguaje
        int year = DateTime.Now.Year;
        bool isLeapYeay = DateTime.IsLeapYear(year); // La función IsLeapYear() existe dentro del lenguaje
        if (isLeapYeay)
            Console.WriteLine($"El año {year} es un año bisiesto");
        else
            Console.WriteLine($"El año {year} no es un año bisiesto");

        Console.WriteLine(variableGlobal);
        Variables();

        int count = Extra("Fizz", "Buzz");
        Console.WriteLine($"Los números se imprmieron {count} veces");
    }

    // FUNCIONES
    // 1.- Función sin parámetros ni retorno de datos
    static void HolaMundo()
    {
        Console.WriteLine("Hola Mundo");
    }


    // 2.- Función con parametros y sin retorno de datos

    static void SaludoPersonalizado(string nombre)
    {
        Console.WriteLine($"Hola, {nombre}");
    }



    // 3.- Función con parámetros y retorno de datos

    static decimal CalcularIMC(decimal peso, decimal altura)
    {
        decimal imc = peso / (altura * altura);

        return imc;
    }


    // 4.- Función sin parámetros y con retorno de datos

    static double GenerarNumeroAleatorio()
    {
        double random = new Random().NextDouble();
        random = random * 50;
        random = Math.Round(random, 2);

        return random;
    }



    // Funciones dentro de funciones

    static double MultiplicacionConNumeroAleatorio(double num)
    {
        int random = GenerarRandom();
        double resultado = num * random;

        int GenerarRandom()
        {
            int random = new Random().Next();
            return random;
        }
        return resultado;
    }

    static void Variables()
    {
        variableGlobal = "Al ser global puedo utilizarla aquí";
        string variableLocal = "Esta variable solo existe dentro de esta función";
        Console.WriteLine(variableGlobal);
        Console.WriteLine(variableLocal);
    }

    //Ejercicio Extra 
    static int Extra(string str1, string str2)
    {
        int count = 0;
        for (int i = 1; i <= 100; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
                Console.WriteLine(str1 + str2);
            else if (i % 3 == 0)
                Console.WriteLine(str1);
            else if (i % 5 == 0)
                Console.WriteLine(str2);
            else
            {
                Console.WriteLine(i);
                count++;
            }
        }
        return count;
    }


}