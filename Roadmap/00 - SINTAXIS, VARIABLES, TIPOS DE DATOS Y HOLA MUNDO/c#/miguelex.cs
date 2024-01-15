class miguelex
{
    // Documentación en https://learn.microsoft.com/es-es/dotnet/csharp/

    // Comentario en una linea

    /* Comentario
       en varias 
       líneas */

    static void Main(string[] args)
    {
        // Declaración de variables y constantes
        string lenguaje = "C#";
        const double PI = 3.1416;

        // Tipos primitivos
        int entero = 10;
        double numDecimal = 10.5;
        char caracter = 'a';
        string cadena = "Hola mundo";
        bool booleano = true;

        // Imprimir por pantalla
        Console.WriteLine($"Hola {lenguaje}");
        Console.WriteLine("El valor de la variable es: " + entero);
        Console.WriteLine($"El valor del caracter es: {caracter}");
    }
}