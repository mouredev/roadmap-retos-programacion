using System;

class Program
{
    static void Main(string[] args)
    {
        greet();
        Console.WriteLine(returngreet());
        arg_greet("Curry");
        args_greet("Bienvenido", "Curry");
        default_arg_greet();
        default_arg_greet("Lebron");
        var (greeting, name) = multiple_return_greet();
        Console.WriteLine(greeting);
        Console.WriteLine(name);
        variable_arg_greet("Curry", "Lebron", "Durant");
        variable_key_arg_greet(("Curry", "Stephen"), ("James", "Lebron"), ("Durant", "Kevin"));
        function_inside_function();

        // Funciones del lenguaje (built-in)

        Console.WriteLine("Curry".Length); // Devuelve la longitud de la cadena
        Console.WriteLine(42.GetType()); // Devuelve el tipo de dato en tiempo de ejecución
        Console.WriteLine("curry".ToUpper()); // Convierte a mayúsculas
        Console.WriteLine("CURRY".ToLower()); // Convierte a minúsculas
        Console.WriteLine("Curry".Substring(0, 3)); // Devuelve una subcadena
        Console.WriteLine("Curry".IndexOf("r")); // Devuelve el índice de la primera ocurrencia
        Console.WriteLine("Curry".Replace("C", "K")); // Reemplaza caracteres
        Console.WriteLine("Curry".Contains("rry")); // Comprueba si contiene una subcadena
        Console.WriteLine("Curry".StartsWith("Cu")); // Comprueba si empieza con una subcadena
        Console.WriteLine("Curry".EndsWith("ry")); // Comprueba si termina con una subcadena

        local_and_global_variables();


        // extra
        int count = print_numbers("Fizz", "Buzz");
        Console.WriteLine($"Count: {count}");

    }

    /* funciones definidas por el usuario */

    //simple
    static void greet()
    {
        Console.WriteLine("Hola");
    }

    //con retorno
    static string returngreet()
    {
        return "Hola";
    }

    //argumento
    static void arg_greet(string name)
    {
        Console.WriteLine($"Hola {name}");
    }

    //argumentos
    static void args_greet(string greet, string name)
    {
        Console.WriteLine($"{greet} {name}");
    }

    //argumento prdeterminado
    static void default_arg_greet(string name = "Curry")
    {
        Console.WriteLine($"Hola {name}");
    }

    // Retorno varios valores
    static (string, string) multiple_return_greet()
    {
        return ("Hola", "Curry");
    }

    // Con un numero variable de argumentos
    static void variable_arg_greet(params string[] names)
    {
        foreach (var name in names)
        {
            Console.WriteLine($"Hola, {name}");
        }
    }

    // Con un numero variable de argumentos con palabra clave
    static void variable_key_arg_greet(params (string key, string value)[] names)
    {
        foreach (var (key, value) in names)
        {
            Console.WriteLine($"Hola, {value} ({key})");
        }
    }

    // Funciones dentro de funciones
    static void function_inside_function()
    {
        void inner_function()
        {
            Console.WriteLine("Hola desde la funcion interna");
        }
        inner_function();
    }

    // Variables locales y globales
    static string globalVariable = "Hola"; // Variable global

    static void local_and_global_variables()
    {
        string localVariable = "Csharp"; // Variable local
        Console.WriteLine($"{globalVariable} {localVariable}");
    }

    // extra

    static int print_numbers (string text1, string text2)
    {
        int Count = 0;
        for (int i = 1; i <= 100; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                Console.WriteLine($"{text1} {text2}");
            }
            else if (i % 3 == 0)
            {
                Console.WriteLine($"{text1}");
            }
            else if (i % 5 == 0)
            {
                Console.WriteLine($"{text2}");
            }
            else
            {
                Console.WriteLine(i);
                Count++;
            }
        }
        return Count;
    }
}
