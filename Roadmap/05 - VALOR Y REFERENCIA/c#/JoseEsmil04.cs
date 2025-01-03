

namespace _05_Valor_Referencia
{
	class Program
	{
		static void Main(string[] args)
		{
			// Asignacion de Variables por valor
			int a = 10;
			int b = a;
			b = 50;

			Console.WriteLine($"a sigue siendo {a} y b ahora es {b}");

			string nombre = "JoseEsmil";
			string nombre2 = nombre;
			nombre2 = "Jose";

			Console.WriteLine($"nombre: {nombre} | nombre2: {nombre2}");

			// Asignacion de Variables por referencia
			Vehiculo honda1 = new() { Marca = "Honda", Modelo = "Civic" };
			Vehiculo honda2 = honda1;
			honda2.Modelo = "Accord";

			Console.WriteLine($"honda1.Modelo: { honda1.Modelo } | honda2.Modelo: {honda2.Modelo}");

			int[] numeros = { 1, 2, 3, 4, 5, 6, 7 };
			int[] numeros2 = numeros;
			numeros2[0] = 545;

			Console.WriteLine($"Se modifico el numeros[0] por referencia {string.Join(',', numeros)}");


			// Funcion por Valor
			int num1 = 50;
			FuncionPorValor(num1);

			Console.WriteLine($"El valor de la variable num1 sigue igual {num1}");

			// Funcion Por referencia
			int num2 = 45;
			FuncionPorReferencia(ref num2);

			Console.WriteLine($"El valor de num2 ahora cambia a {num2}");


			/***** Ejercicios Extra ***/

			// Intercambio por valor
			int num3 = 5, num4 = 10;
			Intercambios.PorValor(num3, num4, out int nuevoNum3, out int nuevoNum4); // (out) para crear nuevas Variables

			Console.WriteLine($"Originales: num3 = {a}, num4 = {num4}"); // Originales: a = 5, b = 10"
			Console.WriteLine($"Nuevos: nuevoNum3 = {nuevoNum3}, nuevoNum4 = {nuevoNum4}"); // Se crean dos variables con los valores intercambiados


			// Intercambio por referencia
			int num5 = 12, num6 = 6;
			Intercambios.PorReferencia(ref num5, ref num6); // (ref) para cambiar valores por referencia

			Console.WriteLine($"Originales: num5: {num5}, num6: {num6}"); // Originales: num5 ahora es 12 y num6 es 6
			Console.WriteLine($"Intercambiados: num5: {num5}, num6: {num6}"); // Intercambiados: Igual por la referencia
		}

		class Vehiculo
		{
			public string Marca { get; set; }
			public string Modelo { get; set; }
		}

		static void FuncionPorValor(int num1)
		{
			num1 += 50;
		}

		static void FuncionPorReferencia(ref int num2)
		{
			num2 += 45;
		}


		class Intercambios
		{
			public static void PorValor(int num3, int num4, out int nuevoNum3, out int nuevoNum4)
			{
				int temporal = num3;
				num3 = num4;
				num4 = temporal;
				nuevoNum3 = num3;
				nuevoNum4 = num4;
			}

			public static void PorReferencia(ref int num5, ref int num6)
			{
				int temporal = num5;
				num5 = num6;
				num6 = temporal;
			}
		}
	}
}