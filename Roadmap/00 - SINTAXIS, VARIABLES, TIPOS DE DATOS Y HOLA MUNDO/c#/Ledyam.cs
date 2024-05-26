class ledyamdev
{
    // Documentación en https://learn.microsoft.com/es-es/dotnet/csharp/

    // Comentario de una linea

    /* Comentario
        de 
       varias 
       líneas */

    static void Main(string[] args)
    {
// Declaración de variables 
        string lenguaje = "C#";
// Constante
        const double GRAVEDAD = 9.8;

        // Tipos de datos primitivos
        int entero = 1;
        double decimal = 2.5;
        char caracter = 'l';
        string cadena = "HELLO";
        bool booleano = true;

        // Imprimir por pantalla
        Console.WriteLine($"Hola {lenguaje}");
        Console.WriteLine("El valor de la variable es: " + entero);
        Console.WriteLine($"El valor del caracter es: {caracter}");
    }
}
