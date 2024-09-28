using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace R10___2024
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Código que podría lanzar una excepción
                int resultado = Dividir(10, 0);
                Console.WriteLine(" El resultado es: " + resultado);
            }
            catch (DivideByZeroException ex)
            {
                // Manejo de la excepción DivideByZeroException
                Console.WriteLine(" Error: División por cero");
            }
            catch (Exception ex)
            {
                // Manejo de cualquier otra excepción
                Console.WriteLine(" Ocurrió un error: " + ex.Message);
            }
            finally
            {
                // Código que se ejecutará siempre
                Console.WriteLine(" Finalizando programa...");
            }


            //Dificultad adicional:
            ProcesarParams(1, 0); //Error parametro cero
            ProcesarParams(-7, 7);//Error numero negativo
            ProcesarParams(1, 1); //Suma normal sin error

            Console.ReadKey();

        }

        static int Dividir(int dividendo, int divisor)
        {
            if (divisor == 0)
            {
                // Lanzar una excepción si el divisor es cero
                throw new DivideByZeroException();
            }
            return dividendo / divisor;
        }

        static void ProcesarParams(int p1, int p2)
        {
            try
            {
                if (!(p1 is int) || !(p2 is int))
                {
                    throw new ArgumentException(" Los parámetros no son números");
                }
                else if (p1 == 0 || p2 == 0)
                {
                    throw new ArgumentException(" Los numeros son cero");
                }
                else if (p1 < 0 || p2 < 0)
                {
                    throw new ArgumentException(" Alguno de los numeros es negativo");
                }
                else
                {
                    Console.WriteLine(" "+p1 + p2);
                    Console.Write(" No se ha producido ningún error");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(" Se ha producido un error: "+ex.Message);
            }
            finally
            {
                Console.WriteLine(" La ejecución ha finalizado");
            }
        }
    }
}
