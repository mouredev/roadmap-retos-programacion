/*    #03 ESTRUCTURAS DE DATOS
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Text.RegularExpressions;

class Program
{
    static void Main()
    {
        //***  Arrays  ***
        //son colecciones de elementos del mismo tipo con un tamaño fijo.
        int[] numeros = new int[5] { 1, 2, 3, 4, 5 };

        //*** Listas ***
        //son colecciones dinámicas que pueden crecer o reducirse según sea necesario.
        List<string> nombres = new List<string>() { "Ana", "Carlos", "Elena" };
        nombres.Add("David");
        nombres.Remove("Ana"); //se puede por valor "Ana"
                               //nombres.RemoveAt(0) o por indice "0", tambien por condiciones
                               //numeros.RemoveAll(n => n % 2 == 0); Elimina todos los números pares
        nombres[1] = "JP"; //actualiza el indice 1
        nombres.Sort(); // Ordena alfabeticamente
        List<int> azar = new List<int>() { 5, 1, 4, 2, 3 };
        azar.Sort(); // Ordena de menor a mayor


        //*** Dictionary<TKey, TValue> ***
        //almacenan pares clave-valor para un acceso rápido a los datos.

        Dictionary<string, int> edades = new Dictionary<string, int>()
        {
            {"Chata", 30},
            {"JP", 31}
        };

        //agregar una entrada
        edades["Elena"] = 22;

        //*** Queue ***
        //Las colas siguen el principio FIFO(First In, First Out).

        Queue<string> cola = new Queue<string>();
        cola.Enqueue("Primero");
        cola.Enqueue("Segundo");

        //*** Stack  ***
        //Las pilas siguen el principio LIFO(Last In, First Out).

        Stack<int> pila = new Stack<int>();
        pila.Push(1);
        pila.Push(2);

        /* DIFICULTAD EXTRA (opcional):
        * Crea una agenda de contactos por terminal.
        * - Debes implementar funcionalidades de búsqueda, inserción, actualización
        *   y eliminación de contactos.
        * - Cada contacto debe tener un nombre y un número de teléfono.
        * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
        *   y a continuación los datos necesarios para llevarla a cabo.
        * - El programa no puede dejar introducir números de teléfono no númericos y con más
        *   de 11 dígitos (o el número de dígitos que quieras).
        * - También se debe proponer una operación de finalización del programa.
        */

        Dictionary<string, string> telefonos = new Dictionary<string, string>() { };
        string opciones = $"\nIndique la operacion a realizar digitando el numero de entre estas opciones:" +
                          $"\n1.Crear contacto" +
                          $"\n2.Buscar contacto" +
                          $"\n3.Actualizar contacto" +
                          $"\n4.Eliminar contacto" +
                          $"\n5.Mostrar directorio completo" +
                          $"\n6.Salir de la aplication.";
        int opcion;

        Console.WriteLine("*** Bienvenido al directorio ***" + opciones);

        do
        {
            opcion = validarOpcion();
            switch (opcion)
            {
                case 1:
                    Console.WriteLine("Por favor, ingresa el nombre: ");
                    string nombre = validarNombre();
                    Console.WriteLine("Por favor, ingresa el telefono: ");
                    string telefono = validarTelefono();
                    telefonos[nombre] = telefono;
                    break;

                case 2:
                    Console.WriteLine("Por favor ingrese el nombre a buscar: ");
                    string buscarNombre = validarNombre();

                    if (telefonos.ContainsKey(buscarNombre))
                    {
                        Console.WriteLine($"El telefono de {buscarNombre} existe y es {telefonos[buscarNombre]}");
                    }
                    else
                    {
                        Console.WriteLine($"{buscarNombre} no se encuentra en el directorio.");
                    }
                    break;

                case 3:
                    Console.WriteLine("Por favor ingrese el nombre de quien desea actualizar el telefono: ");
                    string actualizarNombre = validarNombre();

                    if (telefonos.ContainsKey(actualizarNombre))
                    {
                        Console.WriteLine($"Ingrese el nuevo telefono de {actualizarNombre}:");
                        telefonos[actualizarNombre] = validarTelefono();
                    }
                    else
                    {
                        Console.WriteLine($"{actualizarNombre} no se encuentra en el directorio.");
                    }
                    break;

                case 4:
                    Console.WriteLine("Por favor ingrese el nombre de quien desea remover del directorio: ");
                    string borrarNombre = validarNombre();

                    if (telefonos.ContainsKey(borrarNombre))
                    {
                        telefonos.Remove(borrarNombre);
                        Console.WriteLine($"{borrarNombre} ha sido removido del directorio.");
                    }
                    else
                    {
                        Console.WriteLine($"{borrarNombre} no se encuentra en el directorio.");
                    }
                    break;

                case 5:
                    Console.WriteLine("\nDirectorio completo:");
                    foreach (var i in telefonos)
                    {
                        Console.WriteLine($"\nNombre: { i.Key} - Teléfono: { i.Value} ");
                    }
                    break;

                case 6:
                    break;
 
            }
            if (opcion != 6) // Mostrar las opciones solo si no se ha salido
            {
                Console.WriteLine(opciones);
            }
        } while (opcion != 6);
    }
    static int validarOpcion()
    {
        int cantidad;

        while (!int.TryParse(Console.ReadLine(), out cantidad) || cantidad <= 0 || cantidad >= 7)
        {
            Console.Write("Por favor, ingresa un número entre 1 y 6: ");
        }
        return cantidad;
    }
    static string validarNombre()
    {
        string input = Console.ReadLine();
        while (string.IsNullOrEmpty(input))
        {
            Console.WriteLine("El nombre no puede estar vacío. Ingresa nuevamente el nombre:");
            input = Console.ReadLine();
        }
        return input;
    }
    static string validarTelefono()
    {
        string telefono;
        while (true)
        {
            telefono = Console.ReadLine(); // Primero leemos el teléfono

            // Validamos si el teléfono tiene exactamente 10 dígitos y solo números
            if (Regex.IsMatch(telefono, @"^\d{10}$"))
            {
                break; // Si es válido, salimos del ciclo
            }
            else
            {
                Console.Write("Por favor, ingresa un telefono valido de 10 digitos: ");
            }
        }
        return telefono;
    }
}
