using System;
class Program
{
    static void Main()
    {
        List<string> nombres = new List<string>() { "Anna", "Carlos" };
        try
        {
            Console.WriteLine(nombres[2]);
        }
        catch (Exception ex)
        {
            // Manejo genérico para cualquier excepción.
            Console.WriteLine($"Ocurrió un error: {ex.Message}");
        }
    }
}
