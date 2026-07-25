using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp4
{
    internal class Program
    {
        static void Saludar()      //Función sin parámetro ni retorno
        {
            Console.WriteLine("¡Hola,C#");
        }

        static void SaludarPersona(string nombre) //Función con un parámetro
        {
            Console.WriteLine($"Hola, {nombre}");
        }

        static int Sumar(int valor1, int valor2) //Función con varios parametros y retorno
        { 
            return valor1 + valor2;
        }

        static int OperaciónCompleja(int x)  //Función dentro de otra
        { 
            int Cuadrado(int n)
            { 
                return n * n;
            }
            return Cuadrado(x) + x;
        }

        //Función ya creadas por el lenguaje
        static void FuncionBuiltIn()
        {
            string texto = "Hola Mundo";
            Console.WriteLine($"Texto en minúsculas: {texto.ToLower()}");
        }

        //Variables Locales y Globales
        static string variableGlobal = "Soy global";

        static void PruebaVariables()
        {
            string variableLocal = "Soy local";
            Console.WriteLine($"Dentro de la función: {variableGlobal}");
            Console.WriteLine($"Dentro de la función: {variableLocal}");
        }

        //EXTRA
        static int ImprimirNúmeros(string parametro1, string parametro2)
        {
            int contador = 0;
            for (int i = 1; i <= 100; i++)
            {
                string output = "";
                if (i % 3 == 0)
                {
                    output += parametro1;
                }

                if (i % 5 == 0)
                {
                    output += parametro2;
                }
                if(string.IsNullOrEmpty(output))
                {
                    Console.WriteLine(i);
                    contador++;
                }
            else
                {
                    Console.WriteLine(output);
                }
            }
            return contador;
        }

        static void Main(string[] args)
        {
            // 1. Función sin parámetros ni retorno
            Saludar();

            // 2. Función con un parámetro
            SaludarPersona("Jesús");

            // 3. Función con múltiples parámetros y retorno
            int resultadoSuma = Sumar(7, 8);
            Console.WriteLine($"Resultado de la suma: {resultadoSuma}");

            // 4. Función dentro de función
            int resultadoOperacion = OperaciónCompleja(5);
            Console.WriteLine($"Resultado de operación compleja: {resultadoOperacion}");

            // 5. Uso de funciones incorporadas
            FuncionBuiltIn();

            // 6. Variables globales y locales
            PruebaVariables();
            // Console.WriteLine(variableLocal); // Esto daría error porque la variable es local

            // DIFICULTAD EXTRA
            int vecesImpresoNumero = ImprimirNúmeros("Fizz", "Buzz");
            Console.WriteLine($"Números impresos en lugar de texto: {vecesImpresoNumero}");
        }
    }
}
