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

 
using System.Reflection.Metadata;

namespace AppParaRetos
{
    public class estuardodev
    {
        public static void Main(string[] args)
        {
            // Ejercicio
            Console.WriteLine("-------------------");
            try
            {
                Console.WriteLine("Ingresa un numero para dividir 10: ");
                var numero = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine(10 / numero);
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
                Console.WriteLine("Siguó el programa luego del error");
            }
            Console.WriteLine("-------------------");

            try
            {
                ProcesarParametros("parametro");
                Console.WriteLine("No se ha producido ningún error.");
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine("Error de argumento: " + ex.Message);
            }
            catch (FormatException ex)
            {
                Console.WriteLine("Error de formato: " + ex.Message);
            }
            catch (ProcesamientoException ex)
            {
                Console.WriteLine("Error personalizado: " + ex.Message);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error general: " + ex.Message);
            }

            Console.WriteLine("La ejecucción finalizo.");
        }

        // Difucltad Extra
        public static void ProcesarParametros(string parametro)
        {
            if (string.IsNullOrEmpty(parametro))
            {
                throw new ArgumentException("El parámetro no puede ser nulo ni vacío.");
            }

            throw new ProcesamientoException("Se ha producido un error personalizado.");
        }
    }

    public class ProcesamientoException : Exception
    {

        public ProcesamientoException(String mensaje) : base("Problema: " + mensaje)
        {
        }

    }
}
