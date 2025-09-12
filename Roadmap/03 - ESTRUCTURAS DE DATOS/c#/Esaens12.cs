using System;
using System.Collections.Generic;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using System.Text.Json;

namespace _03_ESTRUCTURA_DE_DATOS
{
    internal class Program
    {
        static void Main(string[] args)
        {

            /*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
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

            // --------------------
            // Listas
            // --------------------

            // Crear una lista de enteros y agregar algunos elementos iniciales
            List<int> numeros = new List<int> { 1, 2, 3 };

            // Eliminar el elemento con valor 2 de la lista
            numeros.Remove(2);

            // Actualizar el primer elemento de la lista a 10
            numeros[0] = 10;

            // Ordenar la lista en orden ascendente
            numeros.Sort();

            // --------------------
            // Colas
            // --------------------

            // Crear una cola de cadenas
            Queue<string> cola = new Queue<string>();

            // Insertar elementos en la cola
            cola.Enqueue("A");
            cola.Enqueue("B");
            cola.Enqueue("C");

            // Eliminar y retornar el primer elemento de la cola 
            cola.Dequeue();

            // Obtener el primer elemento de la cola sin eliminarlo
            string primeroCola = cola.Peek();

            // --------------------
            // Pilas
            // --------------------

            // Crear una pila de enteros
            Stack<int> pila = new Stack<int>();

            // Insertar elementos en la pila
            pila.Push(1);
            pila.Push(2);
            pila.Push(3);

            // Eliminar y retornar el último elemento insertado en la pila (LIFO - Last In, First Out)
            pila.Pop();

            // Obtener el último elemento insertado en la pila sin eliminarlo
            int topePila = pila.Peek();

            // --------------------
            // Conjuntos
            // --------------------

            // Crear un conjunto de enteros y agregar algunos elementos iniciales
            HashSet<int> conjunto = new HashSet<int> { 1, 2, 3 };

            // Eliminar el elemento con valor 2 del conjunto
            conjunto.Remove(2);

            // Verificar si el elemento con valor 1 está en el conjunto
            bool existeEnConjunto = conjunto.Contains(1);

            // --------------------
            // Diccionarios
            // --------------------

            // Crear un diccionario con claves enteras y valores de cadena, y agregar algunos elementos iniciales
            Dictionary<int, string> diccionario = new Dictionary<int, string>
            {
               {1, "Uno"},
               {2, "Dos"},
               {3, "Tres"}
            };

            // Eliminar el par clave-valor con clave 2 del diccionario
            diccionario.Remove(2);

            // Actualizar el valor asociado a la clave 1
            diccionario[1] = "Uno Modificado";

            // Obtener el valor asociado a la clave 1
            string valorDiccionario = diccionario[1];

            // --------------------
            // Mostrar resultados
            // --------------------

            // Mostrar el contenido de la lista
            Console.WriteLine("Lista: " + string.Join(", ", numeros));

            // Mostrar el primer elemento de la cola
            Console.WriteLine("Primero en la cola: " + primeroCola);

            // Mostrar el último elemento insertado en la pila
            Console.WriteLine("Tope de la pila: " + topePila);

            // Mostrar si el elemento con valor 1 existe en el conjunto
            Console.WriteLine("Existe en conjunto: " + existeEnConjunto);

            // Mostrar el valor asociado a la clave 1 en el diccionario
            Console.WriteLine("Valor en diccionario: " + valorDiccionario);

            Console.WriteLine();

            string nombre = "";
            long telefono = 0;
            string operacion = "";
            string entrada = "";
            long telefonoMod = 0;

            string filePath = "contactos.json";
            Dictionary<string, long> contactos = CargarContactos(filePath);
           
            bool continuarSwitch = true;

            while (continuarSwitch)
            {
                Console.WriteLine("bienvenido al menu de la agenda\n");

                Console.WriteLine("elija una opcion");
                Console.Write("1: busqueda\n");
                Console.Write("2: insercion\n");
                Console.Write("3: actualizacion\n");
                Console.Write("4: eliminacion\n");
                Console.Write("5: mostrar todos los contactos registrados\n");
                Console.Write("6: salir y guardar contactos\n");
                Console.Write("7: limpiar pantalla\n\n");
                int opcion = Convert.ToInt32(Console.ReadLine());

                switch (opcion)
                {
                    case 1:
                        operacion = "busqueda";
                        Console.WriteLine("haz escogido: " + operacion);

                        Console.Write("escriba el nombre del contacto a buscar: ");
                        string busqueda = Console.ReadLine().ToUpper();

                        if (contactos.TryGetValue(busqueda.ToUpper(), out telefono) || contactos.TryGetValue(busqueda.ToLower(), out telefono))
                        {
                            Console.WriteLine("\nse encontro el siguiente contacto");
                            Console.WriteLine("[" + busqueda + " - " + telefono + "]" + "\n");
                            continuarSwitch = false;

                            Console.WriteLine(@"presiona ""s"" para volver al menu");
                            string volver2 = Console.ReadLine().ToLower();

                            if (volver2 == "s")
                            {
                                continuarSwitch = true;
                            }
                            else
                            {
                                Console.WriteLine(@"presiona ""s"" para volver al menu");
                            }

                        }
                        else
                        {
                            Console.WriteLine("ERROR ERROR (no se encontro el nombre ingresado) ERROR ERROR\n");
                        }

                        break;

                    case 2:
                        operacion = "insercion";
                        Console.WriteLine("haz escogido: " + operacion);
                        bool continuar = true;

                        while (continuar)
                        {
                            for(int i = 0; i <= 1000; i++) { }
                            Console.Write("ingrese un nombre para el contacto: ");
                            nombre = Console.ReadLine();

                            try
                            {
                                Console.Write("ingrese numero telefonico: ");
                                entrada = Console.ReadLine();

                                telefono = Convert.ToInt64(entrada);
                            }
                            catch (FormatException)
                            {
                                Console.WriteLine("favor de introducir numeros solamente\n");
                            }

                            if (contactos.ContainsKey(nombre) || contactos.ContainsKey(nombre.ToLower()))
                            {
                                Console.WriteLine("ERROR ERROR (El contacto ya existe) ERROR ERROR\n");
                                break;
                            }

                            if (entrada.Length > 10 || entrada.Length < 10)
                            {
                                Console.WriteLine("ERROR ERROR (por favor ingrese un numero de 10 digitos) ERROR ERROR");
                            }
                            else
                            {
                                contactos[nombre] = telefono;
                  
                                Console.WriteLine("el contacto se guardo con exito !!!\n");
                                Console.WriteLine(nombre + " - " + telefono + "\n");

                                Console.Write("desea agregar otro contacto? (s/n): ");
                                string respuesta = Console.ReadLine();

                                if (respuesta.ToLower() != "s")
                                {
                                    continuar = false;
                                    Console.WriteLine("saliendo de " + operacion + "..........\n");
                                    continuarSwitch = true;
                                }
                                else
                                {
                                    continuar = true;
                                }
                            }
                        }

                        break;

                    case 3:
                        operacion = "actualizacion";
                        Console.WriteLine("haz escogido: " + operacion);

                        Console.Write("ingrese el nombre del contacto a cambiar su telefono: \n");
                        string cosa = Console.ReadLine().ToLower();

                        if(contactos.TryGetValue(nombre, out telefono))
                        {
                            Console.WriteLine(nombre + " - " + telefono + "\n");

                            Console.Write("ingrese el nuevo telefono: ");
                            string entradaMod = Console.ReadLine();

                            telefonoMod = Convert.ToInt64(entradaMod);

                            if (telefonoMod != telefono)
                            {
                                telefono = telefonoMod;
                            }

                            contactos[nombre] = telefono;

                            Console.WriteLine("el contacto se actualizo con exito !!! \n");

                            Console.WriteLine(nombre + " - " + telefono + "\n");

                            continuarSwitch = true;
                        }
                        else
                        {
                            Console.WriteLine("no se encontraron resultados\n");
                            continuarSwitch = true;
                        }

                        break;

                    case 4:
                        operacion = "eliminacion";
                        Console.WriteLine("haz escogido: " + operacion);
                        bool borrar = true;

                        Console.Write("ingrese el nombre del contacto a eliminar: ");
                        string busqueda2 = Console.ReadLine().ToUpper();

                        if(contactos.TryGetValue(busqueda2.ToUpper(), out telefono) || contactos.TryGetValue(busqueda2.ToLower(), out telefono))
                        {
                            Console.WriteLine(busqueda2 + " - " + telefono);
                            Console.Write("estas seguro de que quieres eliminar este contacto? (s/n): ");
                            string eliminar = Console.ReadLine().ToLower();

                            if(eliminar != "s")
                            {
                                Console.WriteLine("eliminacion cancelada");
                            }
                            else
                            {
                                contactos.Remove(busqueda2);
                                Console.WriteLine("!!! el contacto ha sido borrado con exito !!!\n");
                            }

                            continuarSwitch = true;
                        }

                        break;

                    case 5:
                        operacion = "mostrar contactos registrados\n\n";
                        Console.Write("haz escogido: " + operacion);

                        if(contactos.Count == 0)
                        {
                            Console.WriteLine("!!! aun no hay contactos registrados !!!\n");
                        }
                        else
                        {
                            continuarSwitch = false;
                            foreach(object contacto in contactos)
                            {
                                Console.WriteLine(contacto);
                            }
                            Console.WriteLine();

                            Console.WriteLine(@"presiona ""s"" para volver al menu");
                            string volver2 = Console.ReadLine().ToLower();

                            if(volver2 == "s")
                            {
                                continuarSwitch = true;
                            }
                            else
                            {
                                Console.WriteLine(@"presiona ""s"" para volver al menu");
                            }
                        }

                        break;

                    case 6:

                        GuardarContactos(filePath, contactos);
                        continuarSwitch = false;
                        Console.WriteLine("saliendo del programa..........");

                        break;

                    case 7:

                        Console.Clear();
                        break;

                    default:
                        Console.WriteLine("ERROR ERROR (opcion no disponible) ERROR ERROR");
                        break;

                }
            }
        }

        static Dictionary<string, long> CargarContactos(string filePath)
        {
            if (File.Exists(filePath))
            {
                string json = File.ReadAllText(filePath);
                return JsonSerializer.Deserialize<Dictionary<string, long>>(json, new JsonSerializerOptions { PropertyNameCaseInsensitive = true })
                       ?? new Dictionary<string, long>(StringComparer.OrdinalIgnoreCase);
            }
            else
            {
                return new Dictionary<string, long>(StringComparer.OrdinalIgnoreCase);
            }
        }

        static void GuardarContactos(string filePath, Dictionary<string, long> contactos)
        {
            string json = JsonSerializer.Serialize(contactos, new JsonSerializerOptions { WriteIndented = true });
            File.WriteAllText(filePath, json);
        }

    }
}
