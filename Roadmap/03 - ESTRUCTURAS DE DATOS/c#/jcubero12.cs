/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
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

// ESTRUCTURAS DE DATOS
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Collections.Concurrent;
class Program
{
    static void Main(string[] args)
    {
        //Arreglos
        int[] nums = { 1, 2, 3, };
        Console.WriteLine(nums[0]); // 1

        // Listas
        List<int> numbers = new List<int> { 1, 2, 3 };
        numbers.Add(4);
        numbers.Remove(2);

        foreach (int num in numbers)
        {
            Console.WriteLine(num); // 1 3 4
        }

        // Diccionarios 
        Dictionary<string, int> phoneBook = new Dictionary<string, int>
        {
            {"Juan", 1234567890},
            {"Pedro", 9876543210}
        };
        phoneBook.Add("Ana", 5555555555);
        foreach (var contact in phoneBook)
        {
            Console.Write($"Nombre: {contact.Key}, Número: {contact.Value}\n");
        }

        //Queues basada en fifo
        Queue<int> queue = new Queue<int>();
        queue.Enqueue(1);
        queue.Enqueue(2);
        queue.Enqueue(3);
        Console.WriteLine(queue.Dequeue()); // 1

        //Stacks basada en lifo
        Stack<int> stack = new Stack<int>();
        stack.Push(1);
        stack.Push(2);
        stack.Push(3);
        Console.WriteLine(stack.Pop()); // 3

        //Hashset no permite duplicados y no ordena los elementos
        HashSet<int> set = new HashSet<int> { 1, 2, 3 };
        set.Add(3); //No se agrega porque ya está en el set
        set.Remove(4);
        foreach (int num in set)
        {
            Console.WriteLine(num);
        }

        //Linkedlist permite insertar y eliminar elementos en cualquier lugar
        LinkedList<string> linkedList = new LinkedList<string>();
        linkedList.AddLast("Node1");
        linkedList.AddLast("Node2");
        linkedList.AddFirst("Node0");
        foreach (string node in linkedList)
        {
            Console.WriteLine(node);
        }

        //SortList permite ordenar los elementos por clave
        SortedList<int, string> sortedList = new SortedList<int, string>
        {
            { 2, "B" },
            { 1, "A" },
            { 3, "C" }
        };
        foreach (var item in sortedList)
        {
            Console.WriteLine($"Key: {item.Key}, Value: {item.Value}");
        }

        //Observable collections permite notificar a sus observadores cuando cambia su contenido
        ObservableCollection<string> observable = new ObservableCollection<string>();
        observable.CollectionChanged += (sender, e) =>
        {
            Console.WriteLine($"Action: {e.Action}");
        };
        observable.Add("Item1"); // Notifica el cambio

        //Tuples son estructuras de datos que contienen varios valores
        var tuple = (1, "Alice", true);
        Console.WriteLine($"ID: {tuple.Item1}, Name: {tuple.Item2}, Active: {tuple.Item3}");

        //KeyValyePair permite crear pares de valores
        KeyValuePair<int, string> kvp = new KeyValuePair<int, string>(1, "Alice");
        Console.WriteLine($"Key: {kvp.Key}, Value: {kvp.Value}");

        //BitArray permite manipular bits
        BitArray bits = new BitArray(4);
        bits[0] = true;
        bits[1] = false;
        bits[2] = true;
        bits[3] = false;
        foreach (bool bit in bits)
        {
            Console.WriteLine(bit);
        }

        //CurrentQueue Colecciones seguras para entornos multihilo del espacio de nombres
        ConcurrentQueue<int> concurrentQueue = new ConcurrentQueue<int>();
        concurrentQueue.Enqueue(1);
        concurrentQueue.Enqueue(2);
        if (concurrentQueue.TryDequeue(out int result))
        {
            Console.WriteLine(result); // Imprime "1"
        }

        //Span Permite manipular segmentos de memoria sin crear copias
        Span<int> numbers = stackalloc int[] { 1, 2, 3, 4, 5 };
        numbers[0] = 10;
        foreach (var number in numbers)
        {
            Console.WriteLine(number);
        }

        Agenda ListaContactos = new Agenda();

        while (true)
        {
            ShowMenu();
            Console.Write("Elige una opción: ");
            int option = int.Parse(Console.ReadLine());

            switch (option)
            {
                case 1:
                    Console.Write("Nombre del contacto a buscar: ");
                    string name = Console.ReadLine();
                    ListaContactos.SearchContact(name);
                    break;
                case 2:
                    Console.Write("Nombre del contacto: ");
                    string name2 = Console.ReadLine();
                    Console.Write("Número de teléfono: ");
                    string phone = Console.ReadLine();
                    ListaContactos.AddContact(name2, phone);
                    break;
                case 3:
                    Console.WriteLine("Nombre Contacto a actualizar: ")
                    string UpdateName = Console.ReadLine();
                    Console.WriteLine("Nuevo número de teléfono: ")
                    string UpdatePhone = Console.ReadLine();
                    ListaContactos.UpdateContact(UpdateName, UpdatePhone);
                    break;
                case 4:
                    Console.WriteLine("Nombre Contacto a eliminar: ")
                    string DeleteName = Console.ReadLine();
                    ListaContactos.DeleteContact(DeleteName);
                case 5:
                    ListaContactos.AllContacts();
                    break;
                case 6:
                    return;
                default:
                    Console.WriteLine("Opción no válida");
                    break;
            }
        }

        static void ShowMenu()
        {
            Console.WriteLine("\n--- Agenda de Contactos ---");
            Console.WriteLine("1# Buscar contacto");
            Console.WriteLine("2# Crear contacto");
            Console.WriteLine("3# Actualizar contacto");
            Console.WriteLine("4# Eliminar contacto");
            Console.WriteLine("5# Todos los contactos");
            Console.WriteLine("6# Salir");
        }

        public class Agenda()
    {
        private Dictionary<string, string> contacts = new Dictionary<string, string>();

        public void AddContact(string name, string phone)
        {
            if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(phone) || !phone.All(char.IsDigit) || phone.Length != 11)
            {
                Console.WriteLine("Error: Invalid data");
                return;
            }
            else
            {
                contacts.Add(name, phone);
                Console.WriteLine($"Contact {name} added with phone number {phone}");
            }
        }

        public void SearchContact(string name)
        {
            if (TryGetValue(name, out string phone))
            {
                Console.WriteLine($"Contact {name} found with phone number {phone}");
                return;
            }
            else
            {
                Console.WriteLine($"Contact {name} not found");
                return;
            }
        }

        public void UpdateContact(string name, string newPhone)
        {
            if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(newPhone) || !newPhone.All(char.IsDigit) || newPhone.Length != 11)
            {
                Console.WriteLine("Error: Invalid data");
            }
            else
            {
                if (contacts.ContainsKey(name))
                {
                    contacts[name] = newPhone;
                }
                else
                {
                    Console.WriteLine($"Contact {name} not found");
                }
            }
            return;
        }

        public void DeleteContact(string name)
        {
            if (contacts.ContainsKey(name))
            {
                contacts.Remove(name);
                Console.WriteLine($"Contact {name} deleted");
            }
            else
            {
                Console.WriteLine($"Contact {name} not found");
            }
        }

        public void AllContacts()
        {
            Console.WriteLine("All contacts:");
            foreach (var contact in contacts)
            {
                Console.WriteLine($"Name: {contact.Key}, Phone: {contact.Value}");
            }
        }
    }
}
}


    
