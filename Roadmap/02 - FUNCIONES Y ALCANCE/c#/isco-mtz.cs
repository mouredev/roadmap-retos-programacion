using System;

internal class Program
{
    // Variables globales válidas (dentro de la clase)
    static int globalCounter = 0;
    static string globalMessage = "Soy una variable global";

    static void Main(string[] args)
    {
        Console.WriteLine("=== 1. Funciones sin parámetros ni retorno ===");
        FuncionSinParametros();

        Console.WriteLine("\n=== 2. Funciones con parámetros ===");
        FuncionConUnParametro("Carlos");
        FuncionConDosParametros(10, 20);

        Console.WriteLine("\n=== 3. Funciones con retorno ===");
        int resultado = Sumar(7, 5);
        Console.WriteLine($"Resultado de Sumar(7, 5) = {resultado}");

        Console.WriteLine("\n=== 4. Funciones dentro de funciones (¿se puede?) ===");
        FuncionesAnidadas();

        Console.WriteLine("\n=== 5. Uso de funciones del lenguaje (built-in) ===");
        UsoDeFuncionesDelLenguaje();

        Console.WriteLine("\n=== 6. Variable LOCAL vs GLOBAL ===");
        VariablesLocalYGlobal();

        // Ejercicio extra
        // Llamamos a la función y recibimos el resultado
        Console.WriteLine("\n=== 7. Reto Extra ===");
        int vecesNumero = ImprimirNumeros("Fizz", "Buzz");

        Console.WriteLine();
        Console.WriteLine($"Cantidad de veces que se imprimió un número: {vecesNumero}");
    }

    // 1. Función sin parámetros ni retorno
    static void FuncionSinParametros()
    {
        Console.WriteLine("Soy una función sin parámetros y sin retorno.");
    }

    // 2. Funciones con parámetros
    static void FuncionConUnParametro(string nombre)
    {
        Console.WriteLine($"Hola {nombre}, esta función recibe un parámetro.");
    }

    static void FuncionConDosParametros(int a, int b)
    {
        Console.WriteLine($"Los parámetros son: {a} y {b}. Su suma es: {a + b}");
    }

    // 3. Función con retorno
    static int Sumar(int x, int y)
    {
        return x + y;
    }

    // 4. Funciones locales dentro de otra función
    static void FuncionesAnidadas()
    {
        Console.WriteLine("C# permite funciones locales dentro de un método:");

        int FuncionLocal(int n)
        {
            return n * 2;
        }

        Console.WriteLine($"FuncionLocal(10) = {FuncionLocal(10)}");
    }

    // 5. Funciones built-in
    static void UsoDeFuncionesDelLenguaje()
    {
        Console.WriteLine("Ejemplos de funciones built-in:");
        Console.WriteLine("hola mundo".ToUpper());
        Console.WriteLine(Math.Sqrt(16));
        Console.WriteLine(DateTime.Now);
    }

    // 6. Variable local vs global
    static void VariablesLocalYGlobal()
    {
        int localCounter = 5;

        Console.WriteLine($"Variable LOCAL = {localCounter}");
        Console.WriteLine($"Variable GLOBAL antes = {globalMessage}");

        globalMessage = "La variable global cambió";

        Console.WriteLine($"Variable GLOBAL después = {globalMessage}");
    }

    /// <summary>
    /// 7. Recibe dos textos y retorna cuántas veces se imprimieron números reales.
    /// </summary>
    static int ImprimirNumeros(string texto3, string texto5)
    {
        int contadorNumeros = 0; // Lleva el conteo de cuántas veces se imprimió un número

        // Recorremos los números del 1 al 100
        for (int i = 1; i <= 100; i++)
        {
            bool multiplo3 = (i % 3 == 0); // true si i es múltiplo de 3
            bool multiplo5 = (i % 5 == 0); // true si i es múltiplo de 5

            if (multiplo3 && multiplo5)
            {
                // Si es múltiplo de 3 y 5
                Console.WriteLine(texto3 + texto5);
            }
            else if (multiplo3)
            {
                // Solo múltiplo de 3
                Console.WriteLine(texto3);
            }
            else if (multiplo5)
            {
                // Solo múltiplo de 5
                Console.WriteLine(texto5);
            }
            else
            {
                // No es múltiplo ni de 3 ni de 5 ⇒ imprimimos el número
                Console.WriteLine(i);
                contadorNumeros++; // Contamos esta impresión
            }
        }

        return contadorNumeros;
    }    
}
