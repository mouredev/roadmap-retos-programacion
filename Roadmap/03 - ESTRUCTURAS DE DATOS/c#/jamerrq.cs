/*
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*/

using System;

class DataStructures
{
    // Queue <T>
    // https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.queue-1?view=net-8.0
    static void Queue()
    {
        Console.WriteLine("=========");
        Console.WriteLine("Queue <T>");
        Console.WriteLine("=========");
        Console.WriteLine();

        var queue = new Queue<string>();

        queue.Enqueue("Hola");
        queue.Enqueue("C#");
        queue.Enqueue("!");

        Console.WriteLine("Método Enqueue");
        Console.WriteLine("Se utiliza para añadir un elemento al final de la cola");
        Console.WriteLine("============");

        Console.WriteLine("queue.Enqueue(\"Hola\")");
        Console.WriteLine("queue.Enqueue(\"C#\")");
        Console.WriteLine("queue.Enqueue(\"!\")");
        Console.WriteLine();

        Console.WriteLine("Método Count");
        Console.WriteLine("Se utiliza para obtener el número de elementos de la cola");
        Console.WriteLine("============");

        Console.WriteLine("queue.Count: {0}", queue.Count);
        Console.WriteLine();

        Console.WriteLine("Método Peek");
        Console.WriteLine("Se utiliza para obtener el primer elemento de la cola sin eliminarlo");
        Console.WriteLine("============");

        Console.WriteLine("queue.Peek(): {0}", queue.Peek());
        Console.WriteLine();

        Console.WriteLine("Método Dequeue");
        Console.WriteLine("Se utiliza para obtener el primer elemento de la cola y eliminarlo");
        Console.WriteLine("============");

        Console.WriteLine("queue.Dequeue(): {0}", queue.Dequeue());
        Console.WriteLine();
    }

    // Stack <T>
    // https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.stack-1?view=net-8.0
    static void Stack()
    {
        Console.WriteLine("=========");
        Console.WriteLine("Stack <T>");
        Console.WriteLine("=========");
        Console.WriteLine();

        var stack = new Stack<string>();

        stack.Push("Hola");
        stack.Push("C#");
        stack.Push("!");

        Console.WriteLine("Método Push");
        Console.WriteLine("Se utiliza para añadir un elemento al final de la pila");
        Console.WriteLine("============");

        Console.WriteLine("stack.Push(\"Hola\")");
        Console.WriteLine("stack.Push(\"C#\")");
        Console.WriteLine("stack.Push(\"!\")");
        Console.WriteLine();

        Console.WriteLine("Método Count");
        Console.WriteLine("Se utiliza para obtener el número de elementos de la pila");
        Console.WriteLine("============");

        Console.WriteLine("stack.Count: {0}", stack.Count);
        Console.WriteLine();

        Console.WriteLine("Método Peek");
        Console.WriteLine("Se utiliza para obtener el primer elemento de la pila sin eliminarlo");
        Console.WriteLine("============");

        Console.WriteLine("stack.Peek(): {0}", stack.Peek());
        Console.WriteLine();

        Console.WriteLine("Método Pop");
        Console.WriteLine("Se utiliza para obtener el primer elemento de la pila y eliminarlo");
        Console.WriteLine("============");

        Console.WriteLine("stack.Pop(): {0}", stack.Pop());
        Console.WriteLine();
    }

    // Dictionary <TKey, TValue>
    // https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-8.0
    static void Dictionary()
    {
        Console.WriteLine("==============");
        Console.WriteLine("Dictionary <TKey, TValue>");
        Console.WriteLine("==============");
        Console.WriteLine();

        var dictionary = new Dictionary<string, string>
        {
            { "Hola", "Hello" },
            { "C#", "C#" },
            { "!", "!" }
        };

        Console.WriteLine("Método Add");
        Console.WriteLine("Se utiliza para añadir un elemento al diccionario");
        Console.WriteLine("============");

        Console.WriteLine("dictionary.Add(\"Hola\", \"Hello\")");
        Console.WriteLine("dictionary.Add(\"C#\", \"C#\")");
        Console.WriteLine("dictionary.Add(\"!\", \"!\")");
        Console.WriteLine();

        Console.WriteLine("Método Count");
        Console.WriteLine("Se utiliza para obtener el número de elementos del diccionario");
        Console.WriteLine("============");

        Console.WriteLine("dictionary.Count: {0}", dictionary.Count);
        Console.WriteLine();

        Console.WriteLine("Método ContainsKey");
        Console.WriteLine("Se utiliza para comprobar si existe una clave en el diccionario");
        Console.WriteLine("============");

        Console.WriteLine("dictionary.ContainsKey(\"Hola\"): {0}", dictionary.ContainsKey("Hola"));
        Console.WriteLine();

        Console.WriteLine("Método ContainsValue");
        Console.WriteLine("Se utiliza para comprobar si existe un valor en el diccionario");
        Console.WriteLine("============");

        Console.WriteLine("dictionary.ContainsValue(\"Hello\"): {0}", dictionary.ContainsValue("Hello"));
        Console.WriteLine();

        Console.WriteLine("Método TryGetValue");
        Console.WriteLine("Se utiliza para obtener el valor de una clave en el diccionario");
        Console.WriteLine("============");

        dictionary.TryGetValue("Hola", out string? value);
        Console.WriteLine("dictionary.TryGetValue(\"Hola\", out value): {0}", value);
        Console.WriteLine();

        Console.WriteLine("Método Remove");
        Console.WriteLine("Se utiliza para eliminar un elemento del diccionario");
        Console.WriteLine("============");

        dictionary.Remove("Hola");
        Console.WriteLine("dictionary.Remove(\"Hola\")");
        Console.WriteLine();
    }

    // List <T>
    // https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-8.0
    static void List()
    {
        Console.WriteLine("=========");
        Console.WriteLine("List <T>");
        Console.WriteLine("=========");
        Console.WriteLine();

        var list = new List<string>();

        list.Add("Hola");
        list.Add("C#");
        list.Add("!");

        Console.WriteLine("Método Add");
        Console.WriteLine("Se utiliza para añadir un elemento a la lista");
        Console.WriteLine("============");

        Console.WriteLine("list.Add(\"Hola\")");
        Console.WriteLine("list.Add(\"C#\")");
        Console.WriteLine("list.Add(\"!\")");
        Console.WriteLine();

        Console.WriteLine("Método Count");
        Console.WriteLine("Se utiliza para obtener el número de elementos de la lista");
        Console.WriteLine("============");

        Console.WriteLine("list.Count: {0}", list.Count);
        Console.WriteLine();

        Console.WriteLine("Método Contains");
        Console.WriteLine("Se utiliza para comprobar si existe un elemento en la lista");
        Console.WriteLine("============");

        Console.WriteLine("list.Contains(\"Hola\"): {0}", list.Contains("Hola"));
        Console.WriteLine();

        Console.WriteLine("Método IndexOf");
        Console.WriteLine("Se utiliza para obtener el índice de un elemento en la lista");
        Console.WriteLine("============");

        Console.WriteLine("list.IndexOf(\"Hola\"): {0}", list.IndexOf("Hola"));
        Console.WriteLine();

        Console.WriteLine("Método Remove");
        Console.WriteLine("Se utiliza para eliminar un elemento de la lista");
        Console.WriteLine("============");

        list.Remove("Hola");
        Console.WriteLine("list.Remove(\"Hola\")");
        Console.WriteLine();
    }

    // Array
    // https://docs.microsoft.com/en-us/dotnet/api/system.array?view=net-8.0
    static void ArrayMethod()
    {
        Console.WriteLine("=====");
        Console.WriteLine("Array");
        Console.WriteLine("=====");
        Console.WriteLine();

        var array = new string[3];

        array[0] = "Hola";
        array[1] = "C#";
        array[2] = "!";

        Console.WriteLine("Método Length");
        Console.WriteLine("Se utiliza para obtener el número de elementos del array");
        Console.WriteLine("============");

        Console.WriteLine("array.Length: {0}", array.Length);
        Console.WriteLine();

        Console.WriteLine("Método IndexOf");
        Console.WriteLine("Se utiliza para obtener el índice de un elemento en el array");
        Console.WriteLine("============");

        Console.WriteLine("Array.IndexOf(array, \"Hola\"): {0}", Array.IndexOf(array, "Hola"));
        Console.WriteLine();

        Console.WriteLine("Método Clear");
        Console.WriteLine("Se utiliza para eliminar todos los elementos del array");
        Console.WriteLine("============");

        Array.Clear(array, 0, array.Length);
        Console.WriteLine("Array.Clear(array, 0, array.Length)");
        Console.WriteLine();
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea una agenda de contactos por terminal.
     * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
     * - Cada contacto debe tener un nombre y un número de teléfono.
     * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
     *   los datos necesarios para llevarla a cabo.
     * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
     *   (o el número de dígitos que quieras)
     * - También se debe proponer una operación de finalización del programa.
    */
    class Contact
    {
        public string Name { get; set; }
        public string Phone { get; set; }

        public Contact(string name, string phone)
        {
            Name = name;
            Phone = phone;
        }
    }

    static void Agenda()
    {
        Console.WriteLine("=======");
        Console.WriteLine("Agenda");
        Console.WriteLine("=======");
        Console.WriteLine();

        var contacts = new List<Contact>();

        while (true)
        {
            Console.WriteLine("¿Qué operación quieres realizar?");
            Console.WriteLine("1. Buscar contacto");
            Console.WriteLine("2. Añadir contacto");
            Console.WriteLine("3. Actualizar contacto");
            Console.WriteLine("4. Eliminar contacto");
            Console.WriteLine("5. Salir");
            Console.WriteLine();

            Console.Write("Opción: ");
            var option = Console.ReadLine();

            Console.WriteLine();

            switch (option)
            {
                case "1":
                    Console.Write("Nombre: ");
                    var name = Console.ReadLine();

                    var contact = contacts.Find(c => c.Name == name);

                    if (contact != null)
                    {
                        Console.WriteLine("Contacto encontrado");
                        Console.WriteLine("Nombre: {0}", contact.Name);
                        Console.WriteLine("Teléfono: {0}", contact.Phone);
                    }
                    else
                    {
                        Console.WriteLine("No se ha encontrado el contacto");
                    }

                    break;
                case "2":
                    Console.WriteLine("¿Qué contacto quieres añadir?");
                    Console.Write("Nombre: ");
                    var name2 = Console.ReadLine();

                    Console.Write("Teléfono: ");
                    var phone = Console.ReadLine();

                    if (name2 != null && phone != null)
                        contacts.Add(new Contact(name2, phone));

                    break;
                case "3":
                    Console.WriteLine("¿Qué contacto quieres actualizar?");
                    Console.Write("Nombre: ");
                    var name3 = Console.ReadLine();

                    var contact3 = contacts.Find(c => c.Name == name3);

                    if (contact3 != null)
                    {
                        Console.Write("Teléfono: ");
                        string? phone3 = Console.ReadLine();

                        if (phone3 != null)
                            contact3.Phone = phone3;
                    }
                    else
                    {
                        Console.WriteLine("No se ha encontrado el contacto");
                    }

                    break;
                case "4":
                    Console.WriteLine("¿Qué contacto quieres eliminar?");
                    Console.Write("Nombre: ");
                    var name4 = Console.ReadLine();

                    var contact4 = contacts.Find(c => c.Name == name4);

                    if (contact4 != null)
                    {
                        contacts.Remove(contact4);
                    }
                    else
                    {
                        Console.WriteLine("No se ha encontrado el contacto");
                    }

                    break;
                case "5":
                    return;
                default:
                    Console.WriteLine("Opción no válida");
                    break;
            }

            Console.WriteLine();
        }
    }


    static void Main()
    {
        bool runExtra = true;
        Queue();
        Console.WriteLine();
        Stack();
        Console.WriteLine();
        Dictionary();
        Console.WriteLine();
        List();
        Console.WriteLine();
        ArrayMethod();
        if (runExtra)
        {
            Console.WriteLine();
            Agenda();
        }
    }
}
