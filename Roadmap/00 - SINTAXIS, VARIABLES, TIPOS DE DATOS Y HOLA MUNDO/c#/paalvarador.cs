namespace DefaultNamespace;

public class paalvarador
{
    // 1. Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
    // Primer comentario en C# (https://learn.microsoft.com/en-us/dotnet/csharp/)
    
    // 2. Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
    
    // Comentario de una línea
    /*
     * Comentario de varias lineas
     */
    
    // 3. Crea una variable (y una constante si el lenguaje lo soporta).
    private var nombre = "Pablo Antonio Alvarado";
    private const string iva = "15%";
    
    // 4. Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    private string nombreCompleto = "Pablo Antonio Alvarado Ruiz";
    private int edad = 32;
    private float estatura = 1.68f;
    private double peso = 70.5;
    private bool estado = true;
    private char inicial = 'P';
    private string[] nombres = ["Pablo", "Xavier", "Santiago", "Diana"];
    private List<string> nombres2 = new List<string>() { "Pablo", "Xavier", "Santiago", "Diana" };
    private Dictionary<string, string> nombres3 = new Dictionary<string, string>()
    {
        { "Pablo", "Antonio" },
        { "Xavier", "Santiago" },
        { "Diana", "Alvarado" }
    };
    
    // 5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
    Console.WriteLine("!Hola, C#!")
}