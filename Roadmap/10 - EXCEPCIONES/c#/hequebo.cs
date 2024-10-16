class Program
{
    static void Main(string[] args)
    {
        // Excepeciones
        int[] numeros = new int[10];
        for (int i = 0; i < numeros.Length; i++)
        {
            numeros[i] = i;
        }
        int a = new Random().Next(15);
        int c = new Random().Next(1);
        try
        {
            Console.WriteLine($"Intentando acceder al índice {a}");
            int b = numeros[a];
            Console.WriteLine($"Intentando dividir {b} entre {c}");
            c = b / c;
        }
        catch (IndexOutOfRangeException ex)
        {
            Console.WriteLine($"No fue posible acceder al índice {a}");
            Console.WriteLine(ex.Message);
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine("No es posible dividir entre 0");
            Console.WriteLine(ex.Message);
        }
        finally
        {
            Console.WriteLine("Este es el final del bloque try-catch");
        }
        Console.ReadLine();
        Console.Clear();

        // Ejercicio extra
        bool salir = false;
        do
        {
            Console.Clear();
            List<int> list1 = new List<int>();
            int longitud = new Random().Next(15);
            for (int i = 0; i < longitud; i++)
                list1.Add(new Random().Next(100));
            try
            {
                ProcesarParametros(list1);
                Console.WriteLine("Parámetros correctos");
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine(ex.Message);
            }
            catch (IndexOutOfRangeException ex)
            {
                Console.WriteLine(ex.Message);
                foreach (int i in list1)
                    Console.Write($"{i}, ");
                Console.WriteLine();
            }
            catch (NotEnoughException ex)
            {
                Console.WriteLine(ex.Message);
                Console.WriteLine(list1.Sum());
            }
            finally
            {
                Console.WriteLine("Fin del programa");
            }

            Console.WriteLine("Deseas intentar de nuevo? S/N");
            string respuesta = Console.ReadLine();
            if (respuesta.ToLower() == "n")
                salir = true;
        } while(!salir);



    }

    static void ProcesarParametros(List<int> list)
    {
        if (list.Count == 0)
        {
            throw new ArgumentException("La lista de parámetros no puede estar vacía");
        }
        if (list.Count > 10)
        {
            throw new IndexOutOfRangeException("La lista no puede contener más de 10 elementos");
        }
        if (list.Sum() < 200)
        {
            throw new NotEnoughException("La suma de los elementos es menor a 200");
        }
    }
}
class NotEnoughException : Exception
{
    public NotEnoughException(string message) : base(message) { }
}