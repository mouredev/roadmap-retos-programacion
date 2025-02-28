using System;
public class Program
{
	/// <summary>
	/// Método que imprime un saludo en la consola.
	/// </summary>
	public void Saludar()
	{
		Console.WriteLine("¡Hola, mundo! Con comentario para documentación XML\n");
	}

	public static void Main()
	{
		Console.WriteLine("** Sitio oficial C#: https://dotnet.microsoft.com/es-es/languages/csharp\n");
		Console.WriteLine("* Comentarios: https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/tokens/comments\n");

		// Este es un comentario de una sola línea			
		Console.WriteLine("¡Hola, mundo! Con comentario de una sola línea."); // También se puede colocar al final de una línea de código

		/* Este es un comentario
		 de varias líneas.
		 Puede abarcar múltiples líneas. */
		Console.WriteLine("¡Hola, mundo! Con comentario de varias líneas.");

		Program programa = new Program();
		programa.Saludar();

		//Declaración implícita con var.
		Console.WriteLine("* Tipos de datos primitivos: https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/built-in-types\n");
		Console.WriteLine("* Declaración implícita con var.\n");
		var numero = 10;        // Se infiere como int
		var precio = 99.99;     // Se infiere como double
		var mensaje = "¡Hola!"; // Se infiere como string
		Console.WriteLine("var numero = 10;        // Se infiere como int");
		Console.WriteLine("var precio = 99.99;     // Se infiere como double");
		Console.WriteLine($"var mensaje = \"{mensaje}\"; // Se infiere como string\n");

		Console.WriteLine($"{numero},{precio},{mensaje}\n");

		//Declaración explícita con tipos primitivos
		Console.WriteLine("* Declaración explícita con tipos primitivos\n");
		int numeroEntero = 10;
		double precioDecimal = 99.99;
		bool esActivo = true;
		char letra = 'A';
		string mensajeString = "¡Hola, mundo!";
		Console.WriteLine("int numeroEntero = 10;");
		Console.WriteLine("double precioDecimal = 99.99;");
		Console.WriteLine("bool esActivo = true;");
		Console.WriteLine("char letra = 'A';");
		Console.WriteLine($"string mensajeString = \"{mensajeString}\";\n");
		Console.WriteLine(numeroEntero);
		Console.WriteLine(precioDecimal);
		Console.WriteLine(esActivo);
		Console.WriteLine(letra);
		Console.WriteLine(mensajeString + "\n");

		//Declaración de constantes (const)
		Console.WriteLine("* Declaración de constantes(const)\n");
		const double PI = 3.1416;
		const string saludo = "¡Hola, mundo!";
		Console.WriteLine("const double PI = 3.1416;");
		Console.WriteLine($"const string saludo = \"{saludo}\";\n");
		Console.WriteLine(PI);
		Console.WriteLine(saludo + "\n");


		Console.WriteLine("¡Hola, C# !");
	}
}