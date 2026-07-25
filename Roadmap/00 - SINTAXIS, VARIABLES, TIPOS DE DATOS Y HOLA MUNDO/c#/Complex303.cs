using System;

// https://dotnet.microsoft.com/es-es/languages/csharp
// Este es un comentario de una sola linea

/* Una constante es un valor fijo que no puede cambiar una vez asignado.
Se declara usando la palabra clave const y debe inicializarse al momento de declararla. */

///Son como los comentarios multilinea,
///Se usan para describir funciones, clases o metodos, y se pueden leer desde herramientas como Visual Studio para autocompletar y documentaci�n autom�tica.

class Program  // Todo dentro de una clase
{
    static void Main() // Metodo principal
    {
        string nombre = "Eddy"; //variable

        const cantidad_de_libros = 23; //constante

        //Tipo de datos primitivos en C#

        int edad = 23;
        double area = 23.45; //tambien se puede usar float y decimal
        char letra = 'E';
        bool es_hombre = true;
        string mensaje = "Hola";

        Console.WriteLine("Hola, C#!!");
        Console.WriteLine("=================================")
        Console.WriteLine($"La edad es: {edad}");
        Console.WriteLine("El area del triangulo es: " + area);
        Console.WriteLine("La letra es: " + letra);


    }
}






