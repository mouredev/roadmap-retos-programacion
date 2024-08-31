
class Program
{
    static void Main()
    {
        // ARRAYS
        int[] numbers = { 1, 2, 3, 4, 5, 6 }; // Insercion

        numbers[0] = 7; // Actualizacion
                        // Borrado no soportado por los Arrays.
        Array.Sort(numbers); // Ordenacion

        foreach (int number in numbers)
        {
            Console.WriteLine(number + " ");
        }

        // LISTAS
        List<string> countries = new();

        countries.Add("Spain"); // Insercion
        countries.Add("Canada");
        countries.Add("Dominican Republic");
        countries.Remove("Canada"); // Borrado
        countries[0] = "Italy"; // Actualizacion
        countries.Sort(); // Ordenacion

        foreach (var country in countries)
        {
            Console.WriteLine(country + " ");
        }

        // DICTIONARY
        Dictionary<string, int> employees = new Dictionary<string, int>
        {
            { "Esmil", 4 },
            { "Ana", 2 },
            { "Maria", 5 }
        };

        employees.Add("Alex", 11); // Insercion
        employees.Remove("Esmil"); // Borrado
        employees["Ana"] = 43; // Actualizacion
                               // No hay Ordenacion directa, se debe hacer por clave o valor

        foreach (var employee in employees)
        {
            Console.WriteLine(employee + "");
        }

        // HASHSET
        HashSet<int> set = new HashSet<int> { 1, 2, 3 };

        set.Add(5); // Insercion
        set.Remove(1); // Borrado

        set.Remove(2); // Actualizacion (Borrar y Agregar)
        set.Add(4);

        List<int> sortedSet = set.ToList();
        sortedSet.Sort(); // Ordenacion (Hay que pasarlo a List)

        foreach (var s in sortedSet)
        {
            Console.WriteLine(s + "");
        }

        // QUEUE
        Queue<int> queue = new Queue<int>();

        queue.Enqueue(5); // Insercion
        queue.Enqueue(2);
        queue.Enqueue(8);
        queue.Enqueue(1);
        queue.Enqueue(3);

        queue.Dequeue(); // Borrado

        // Actualizacion (no se puede directamente, se debe reconstruir la cola)
        Queue<int> updatedQueue = new Queue<int>(queue.Select(x => x == 2 ? 4 : x));

        List<int> sortedQueue = updatedQueue.ToList(); // Ordenacion (Hay que pasarlo a list)
        sortedQueue.Sort();

        foreach (var item in sortedQueue)
        {
            Console.Write(item + " ");
        }

        // STACK
        Stack<int> stack = new Stack<int>();

        stack.Push(5); // Insercion
        stack.Push(2);
        stack.Push(8);
        stack.Push(1);
        stack.Push(3);

        stack.Pop(); // Borrado

        // Actualizacion (no se puede directamente, se debe reconstruir la Pila)
        Stack<int> updatedStack = new Stack<int>(stack.Select(x => x == 8 ? 9 : x));

        List<int> sortedStack = updatedStack.ToList();
        sortedStack.Sort(); // Ordenacion (Hay que pasarlo a list)

        foreach (var item in sortedStack)
        {
            Console.Write(item + " ");
        }

        // LINKEDLIST
        LinkedList<int> linkedList = new LinkedList<int>();

        linkedList.AddLast(5); // Insercion
        linkedList.AddLast(2);
        linkedList.AddLast(8);
        linkedList.AddLast(1);
        linkedList.AddLast(3);
        linkedList.AddLast(7);

        linkedList.Remove(8); // Borrado

        // Actualización (no es directa, se debe manejar con nodos)
        LinkedListNode<int> node = linkedList.Find(2);
        node.Value = 4;

        List<int> sortedLinkedList = linkedList.ToList();
        sortedLinkedList.Sort(); // Ordenacion (Hay que pasarlo a list)

        foreach (var item in sortedLinkedList)
        {
            Console.Write(item + " ");
        }

        // EJERCICIO EXTRA AGENDA
        AgendaContactos.Iniciar();

    }
}

public class AgendaContactos
{
    static Dictionary<string, string> agenda = new Dictionary<string, string>();


    public static void Iniciar()
    {
        while (true)
        {
            Console.WriteLine("------ Agenda ------");
            Console.WriteLine("");
            Console.WriteLine("Seleccione una operación:");
            Console.WriteLine("1. Insertar contacto");
            Console.WriteLine("2. Buscar contacto");
            Console.WriteLine("3. Actualizar contacto");
            Console.WriteLine("4. Eliminar contacto");
            Console.WriteLine("5. Finalizar programa");

            var option = Console.ReadLine();

            switch (option)
            {
                case "1":
                    InsertarContacto();
                    break;
                case "2":
                    BuscarContacto();
                    break;
                case "3":
                    ActualizarContacto();
                    break;
                case "4":
                    EliminarContacto();
                    break;
                case "5":
                    Console.WriteLine("Finalizando Programa...");
                    return;
                default:
                    Console.WriteLine("Opcion no valida, intente de nuevo por favor!");
                    break;
            }


        }
    }

    public static void InsertarContacto()
    {
        Console.WriteLine("Inserte el nombre del Contacto: ");
        var nombre = Console.ReadLine();

        Console.WriteLine("Inserte el numero del contacto: ");
        var telefono = Console.ReadLine();

        if (nombre == null)
        {
            Console.WriteLine("Nombre Invalido, Intente nuevamente");
            return;
        }

        if (telefono.Length > 11 || !long.TryParse(telefono, out _) || telefono == null)
        {
            Console.WriteLine("Telefono Invalido, intente nuevamente");
            return;
        }

        if (agenda.ContainsKey(nombre))
        {
            Console.WriteLine("EL nombre ya existe en la agenda!");
            return;
        }

        agenda[nombre] = telefono;
    }

    public static void BuscarContacto()
    {
        Console.Write("Ingrese el nombre del contacto:");
        var nombre = Console.ReadLine();

        if (nombre == null)
        {
            Console.WriteLine("Nombre Invalido!");
            return;
        }

        if (agenda.ContainsKey(nombre))
        {
            Console.WriteLine($"Nombre: {nombre}, Telefono: {agenda[nombre]}");
        }
        else
        {
            Console.WriteLine("Contacto! no encontrado!");
        }
    }

    public static void ActualizarContacto()
    {
        Console.Write("Ingrese el nombre del contacto: ");
        var nombre = Console.ReadLine();

        if (nombre == null)
        {
            Console.WriteLine("Nombre Invalido!");
            return;
        }

        if (agenda.ContainsKey(nombre))
        {
            Console.Write("Ingrese el nuevo numero (max 11 dígitos): ");
            string telefono = Console.ReadLine();

            if (telefono.Length > 11 || !long.TryParse(telefono, out _) || telefono == null)
            {
                Console.WriteLine("Número de teléfono no válido.");
                return;
            }

            agenda[nombre] = telefono;
            Console.WriteLine("Contacto actualizado correctamente.");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    public static void EliminarContacto()
    {
        Console.Write("Ingrese el nombre del contacto: ");
        var nombre = Console.ReadLine();

        if (nombre == null)
        {
            Console.WriteLine("Nombre Invalido!");
            return;
        }

        if (agenda.ContainsKey(nombre))
        {
            agenda.Remove(nombre);
            Console.WriteLine("Contacto Eliminado correctamente.");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }
}