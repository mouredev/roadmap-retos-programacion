// Sitio oficial C# - URL : https://dotnet.microsoft.com/es-es/languages/csharp

using System;
					
public class Program
{
		//URL DOCUMENTACION OFICIAL - Comentarios de documentación XML: https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/language-specification/documentation-comments	
	
		/// <summary>
		/// Método que imprime un saludo en la consola.
		/// </summary>
		public void Saludar()
		{
			Console.WriteLine("Hola, mundo!");
		}

		public static void Main()
		{
			
			//URL DOCUMENTACION OFICIAL: https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/tokens/comments
			
			// Este es un comentario de una sola línea
			
			Console.WriteLine("Hola, mundo!"); // También se puede colocar al final de una línea de código

			/* Este es un comentario
			 de varias líneas en C#.
			 Puede abarcar múltiples líneas. */
			 Console.WriteLine("Hola, mundo!");
			
			 Program programa = new Program();
			 programa.Saludar();
			
			
			//URL DUCUMENTACION OFICIAL - Todos los tipo de datos primitivos:  https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/built-in-types			
			//Declaración implícita con var: Solo puede usarse dentro de métodos o bloques de código.
			var numero = 10;        // Se infiere como int
			var precio = 99.99;     // Se infiere como double
			var mensaje = "Hola";   // Se infiere como string
			Console.WriteLine(numero);
			Console.WriteLine(precio);
			Console.WriteLine(mensaje);
			
			//Declaración explícita con tipos primitivos
			int numeroEntero = 10;
			double precioDecimal = 99.99;
			bool esActivo = true;
			char letra = 'A';
			string mensajeString = "Hola, mundo!";
			Console.WriteLine(numeroEntero);
			Console.WriteLine(precioDecimal);
			Console.WriteLine(esActivo);
			Console.WriteLine(letra);
			Console.WriteLine(mensajeString);
			
			//Declaración de constantes (const)
			const double PI = 3.1416;
			const string Saludo = "Hola, mundo!";
			Console.WriteLine(PI);
			Console.WriteLine(Saludo);
			

			Console.WriteLine("¡Hola, C# !");
	}
}