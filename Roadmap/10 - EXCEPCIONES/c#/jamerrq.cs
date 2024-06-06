using System;

/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 */

namespace Roadmap10
{
    class Extra
    {
        public void Process(int a, int b)
        {
            if (b == 0)
            {
                throw new DivideByZeroException("No se puede dividir entre 0.");
            }
            else if (a < 0)
            {
                throw new ArgumentOutOfRangeException("a", "El valor de 'a' no puede ser negativo.");
            }
            else if (a > 10)
            {
                throw new Exception("El valor de 'a' no puede ser mayor que 10.");
            }
            else
            {
                Console.WriteLine(a / b);
            }
        }
    }
    class Program
    {
        void catchExtra()
        {
            Extra extra = new Extra();
            try
            {
                extra.Process(10, 0);
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
            catch (ArgumentOutOfRangeException e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
            finally
            {
                Console.WriteLine("La ejecución ha finalizado.");
            }
        }
        static void Main(string[] args)
        {
            try
            {
                int a = 10;
                int b = 0;
                Console.WriteLine(a / b);
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
            finally
            {
                Console.WriteLine("La ejecución ha finalizado.");
            }
            Console.WriteLine("========================================");
            Console.WriteLine("============== MANEJO DE ERRORES =======");
            Console.WriteLine("========================================\n");
            Program program = new Program();
            program.catchExtra();
        }
    }
}
