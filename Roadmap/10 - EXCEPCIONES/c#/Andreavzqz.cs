using System;

namespace ManejoDeExcepciones
{

    //Excepción personalizada
    public class ExcepcionPersonalizada : Exception
    {
        public ExcepcionPersonalizada(string mensaje) { }
    }

    class Program
    {
        static void Main(string [] args)
        {

            // Parte 1: Forzar un error dividiendo por cero y capturarlo
            try
            {
                int resultado = 10 / 0;
            }

            catch (DivideByZeroException ex)
            {
                Console.WriteLine($"Error: {ex.Menssage}");
            }

            // Parte 2: Funcion que lanza diferentes excepciones
            try
            {
                ProcesarParametros(0);
                ProcesarParametros(-1);
                ProcesarParametros(100);
            }

            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine($"Error de rango: {ex.Menssage}");
            }

            catch (ArgumentException ex)
            {
                Console.WriteLine($"Error de argumento: {ex.Menssage}");
            }

            catch (ExcepcionPersonalizada ex)
            {
                Console.WriteLine($"Error personalizado: {ex.Menssage}");
            }

            catch (Exception ex)
            {
                Console.WriteLine($"Error desconocido: {ex.Menssage}");
            }

            finally
            {
                Console.WriteLine("La ejecucion ha finalizado.");
            }
        }

        // Funcion que lanza diferentes excepciones
        static void ProcesarParametros(int valor)
        {
            if (valor == 0)
            {
                throw new ArgumentOutOfRangeException(nameof(valor), "El valor no puede ser cero");
            }

            else if (valor < 0)
            {
                throw new ArgumentException("El valor no puede ser negativo.");
            }

            else if (valor > 10)
            {
                throw new ExcepcionPersonalizada("El valor no puede ser mayor que 10.");
            }

            else 
            {
                Console.WriteLine("Parametro procesado correctamente.");
            }
        }
    }
  /*

Explicación

Excepción personalizada:
Creamos una clase ExcepcionPersonalizada que hereda de Exception y define un constructor que toma un mensaje de error.

Main:
Parte 1: Intentamos dividir por cero y capturamos la excepción DivideByZeroException.
Parte 2: Llamamos a la función ProcesarParametros con diferentes valores que pueden causar excepciones. Capturamos cada tipo de excepción específica (ArgumentOutOfRangeException, ArgumentException y ExcepcionPersonalizada), así como una excepción general Exception para cualquier otro tipo de error no previsto. Finalmente, usamos un bloque finally para imprimir que la ejecución ha finalizado.

Función ProcesarParametros:
Lanza una ArgumentOutOfRangeException si el valor es cero.
Lanza una ArgumentException si el valor es negativo.
Lanza una ExcepcionPersonalizada si el valor es mayor que 10.


*/
}
