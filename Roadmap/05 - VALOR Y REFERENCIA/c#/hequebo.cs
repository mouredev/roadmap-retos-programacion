class Program
{
    static void Main(string[] args)
    {
        // ASIGNACIÓN DE VARIABLES
        Console.WriteLine("---ASIGNACION DE VARIABLES----");
        // Por valor
        Console.WriteLine("--Por Valor---");
        int a = 10; // Se crea la variable 'a' y se le asigna el valor de 10 
        int b = a; // Se crea la variable 'b' y se la asigna el valor de 'a' (10)
        // En este momento ambas variable tienen el mismo valor
        Console.WriteLine($"El valor de a es {a}"); 
        Console.WriteLine($"El valor de b es {b}");
        Console.WriteLine("Se modifica el valor de 'b'");
        b = 15; // Se modifica el valor de 'b' a 15
        Console.WriteLine($"El valor de a es {a}"); // El valor de 'a' se mantiene igual
        Console.WriteLine($"El valor de b es {b}"); // El valor de 'b' se modifica
        Console.WriteLine();

        // Al crear una función y definir sus parámetros estos por defecto son asignados por valor
        Console.WriteLine($"La varibale 'a' antes de ser enviada a la función tiene el valor de {a}");
        AsignarPorValor(a);
        Console.WriteLine($"La variable 'a' después de ser ejecutada la función tiene el valor de {a}");
        Console.WriteLine();

        // Por Referencia
        Console.WriteLine("---Por Referencia---");
        var usuario1 = new Usuario("Emilio", "Quezada", "emilio@mail.com");
        var usuario2 = usuario1;
        Console.WriteLine($"El nombre de usuario1 es {usuario1.Nombre}");
        Console.WriteLine($"El nombre de usuario2 es {usuario2.Nombre}");
        Console.WriteLine("Modificamos el nombre de usuario2");
        usuario2.Nombre = "Héctor";
        Console.WriteLine($"El nombre de usuario1 es {usuario1.Nombre}");
        Console.WriteLine($"El nombre de usuario2 es {usuario2.Nombre}");

        /* Al crear una función para indicar que sus parámetros serán asignados por referencia se usa
         * la palabra 'ref' antes de la variable, tanto en su declaración como al ser llamada
         */
        Console.WriteLine();
        Console.WriteLine($"La varibale 'a' antes de ser enviada a la función tiene el valor de {a}");
        AsignarPorReferencia(ref a);
        Console.WriteLine($"La variable 'a' después de ser ejecutada la función tiene el valor de {a}");

        // Ejercicio Extra
        Console.WriteLine();
        Console.WriteLine("---Ejercicio extra---");
        a = 10;
        b = 20;
        Console.WriteLine("---Intercambio por valor---");
        Console.WriteLine($"El valor de a antes de entrar a la función es {a}");
        Console.WriteLine($"El valor de b antes de entrar a la función es es {b}");
        var result = IntercambioValor(a, b);
        Console.WriteLine("Se ejecuta la función IntercambioValor()");
        Console.WriteLine($"El valor de a después de entrar a la función es {a}");
        Console.WriteLine($"El valor de b después de entrar a la función es es {b}");
        Console.WriteLine($"La función retornó a = {result.Item1} y b = {result.Item2}");

        Console.WriteLine();
        Console.WriteLine("---Intercambio por referencia---");
        Console.WriteLine($"El valor de a antes de entrar a la función es {a}");
        Console.WriteLine($"El valor de b antes de entrar a la función es es {b}");
        result = IntercambioReferencia(ref a, ref b);
        Console.WriteLine("Se ejecuta la función IntercambioValor()");
        Console.WriteLine($"El valor de a después de entrar a la función es {a}");
        Console.WriteLine($"El valor de b después de entrar a la función es es {b}");
        Console.WriteLine($"La función retornó a = {result.Item1} y b = {result.Item2}");
    }

    static void AsignarPorValor(int a)
    {
        Console.WriteLine($"La variable enviada a la función por valor tiene el valor de {a}");
        a++;
        Console.WriteLine($"La variable 'a' dentro de la función ahora tiene el valor de {a}");
    }
    static void AsignarPorReferencia(ref int a)
    {
        Console.WriteLine($"La variable enviada a la función por referencia tiene el valor de {a}");
        a++;
        Console.WriteLine($"La variable 'a' dentro de la función ahora tiene el valor de {a}");
    }
    static (int, int) IntercambioValor(int a, int b)
    {
        int e; // Se agrega variable extra para realizar intercambio entra a y b
        e = a;
        a = b;
        b = e;
        return(a, b);
    }
    static (int, int) IntercambioReferencia(ref int a, ref int b)
    {
        int e; // Se agrega variable extra para realizar intercambio entra a y b
        e = a;
        a = b;
        b = e; 

        return (a, b);
    }
}

class Usuario
{
    private string _nombre;
    private string _apelllido;
    private string _email;

    public string Nombre { get { return _nombre; } set { _nombre = value; } }

    public Usuario(string nombre, string apellido, string email)
    {
        _nombre = nombre;
        _apelllido = apellido;
        _email = email;
    }
}