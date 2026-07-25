using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;

class Program
{
    //Diccionario para la agenda
    static Dictionary<string, string> agenda = new Dictionary<string, string>();
    static void Main()
    {

        // ---Estructuras de datos---
        Console.WriteLine("EJEMPLOS DE ESTRUCTURAS");

        //Arrays - Arreglos
        string[] abc = new string[5] { "a", "b", "c", "d", "e" };  //Datos de tamaño fijo

        //List - Listas 
        List<int> myList = new List<int> { 2, 4, 6, 8, };  //Datos dinámicos
        myList.Add(3); // Inserción
        myList.Remove(6); //Eliminar
        myList[1] = 7;  //Actualizar
        myList.Sort();  //Ordenación
        Console.WriteLine("Lista " + string.Join(", ", myList));

        //Tuplas
        var usuario = ("XPERIARGLUNA", 19, "C#"); //Agrupa valores en una sola variable

        Console.WriteLine($"Nombre de usuario: {usuario.Item1}");
        Console.WriteLine($"Edad del usuario: {usuario.Item2}");
        Console.WriteLine($"Lenguaje del usuario: {usuario.Item3}");

        //HashSet - Conjuntos
        HashSet<string> pokedex = new HashSet<string>(); //Evita datos duplicados, pero no se pueden ordenar
        string[] pokemones = { "Pikachu", "Charmander", "Bulbasur", "Pikachu" };

        foreach (string pokemon in pokemones)
        {
            if (pokedex.Add(pokemon)) //Intento de captura del pokemón
                Console.WriteLine($"¡Has capturado a {pokemon}!");
            else
                Console.WriteLine($"Ya tienes capturado a {pokemon}, sigue buscando... ");
        }
        Console.WriteLine("\n Pokedex actual: " + string.Join(" , ", pokedex));

        // Diccionario - Dictionary 
        Dictionary<int, string> menu = new Dictionary<int, string>()
        {
            { 1, "Hamburguesa" },
            { 2, "Papas Fritas" },
            { 3, "Pizza" },
            { 4, "Postre" }
        };

        Console.WriteLine("\n Menú original:");
        foreach (var item in menu)
        {
            Console.WriteLine($"{item.Key}, {item.Value}");
        }

        menu[4] = "Alitas";
        menu.Remove(3);
        menu[2] = "Boneless";
        //No hay ordenación ya que se usan claves para búsqueda rápida 

        Console.WriteLine("\n Menú actualizado:");
        foreach (var item in menu)
        {
            Console.WriteLine($"{item.Key}, {item.Value}");
        }

        // Pilas - Stack
        Stack<int> pila = new Stack<int>();
        pila.Push(9); //Inserción
        pila.Push(18);
        pila.Push(27);

        Console.WriteLine("Sacando de la pila(Pop): " + pila.Pop()); //Quita el último elemento añadido de la pila

        Console.WriteLine("Cima de la pila (Peek): " + pila.Peek()); //Ver que hay en la cima de la pila
                                                                     //no se puede ordenar, sigue el principio LIFO

        // Cola - Queue
        Queue<int> cola = new Queue<int>();
        cola.Enqueue(9);
        cola.Enqueue(18); //Inserción
        cola.Enqueue(27);
        int primero = cola.Dequeue(); // Quita el primer elemento añadido de la cola
                                      // No se puede ordenar, sigue el principio FIFO        
        Console.WriteLine($"Primer elemento: {primero}");

        foreach (var item in cola)
        {
            Console.WriteLine(item);
        }

        //LinkedList
        LinkedList<int> myLinkedList = new LinkedList<int>(new int[] { 3, 1, 3, 1, 6, 9});
        myLinkedList.AddLast(2); //Inserción al final
        myLinkedList.AddFirst(4); //Inserción al inicio
        myLinkedList.Remove(3); // Borrado 

        foreach (var item in myLinkedList)
        {
            Console.WriteLine(item);
        }

        //Agenda Interactiva
        Console.WriteLine("\n AGENDA DE CONTACTOS");

        while (true)
        {
            Console.WriteLine("\nOpciones:");
            Console.WriteLine("1. Agregar contacto");
            Console.WriteLine("2. Buscar contacto");
            Console.WriteLine("3. Actualizar contacto");
            Console.WriteLine("4. Eliminar contacto");
            Console.WriteLine("5. Mostrar todos los contactos");
            Console.WriteLine("6. Salir");
            Console.Write("Elige una opción: ");
            string opcion = Console.ReadLine();

            switch (opcion)
            {
                case "1": AgregarContacto(); break;
                case "2": BuscarContacto(); break;
                case "3": ActualizarContacto(); break;
                case "4": EliminarContacto(); break;
                case "5": MostrarTodos(); break;
                case "6": Console.WriteLine("¡Hasta la próxima!"); return;
                default: Console.WriteLine("❌ Opción inválida."); break;
            }
        }
    }

    // Funciones para la agenda
    static void AgregarContacto()
    {
        Console.Write("Nombre: ");
        string nombre = Console.ReadLine();

        Console.Write("Teléfono (máx 11 dígitos): ");
        string telefono = Console.ReadLine();

        if (EsTelefonoValido(telefono))
        {
            agenda[nombre] = telefono;
            Console.WriteLine("✅ Contacto agregado.");
        }
        else
        {
            Console.WriteLine("❌ Teléfono no válido.");
        }
    }

    static void BuscarContacto()
    {
        Console.Write("Nombre a buscar: ");
        string nombre = Console.ReadLine();

        if (agenda.ContainsKey(nombre))
            Console.WriteLine($"➡️ {nombre}: {agenda[nombre]}");
        else
            Console.WriteLine("❌ Contacto no encontrado.");
    }

    static void ActualizarContacto()
    {
        Console.Write("Nombre del contacto: ");
        string nombre = Console.ReadLine();

        if (agenda.ContainsKey(nombre))
        {
            Console.Write("Nuevo teléfono: ");
            string telefono = Console.ReadLine();
            if (EsTelefonoValido(telefono))
            {
                agenda[nombre] = telefono;
                Console.WriteLine("✅ Contacto actualizado.");
            }
            else
            {
                Console.WriteLine("❌ Teléfono no válido.");
            }
        }
        else
        {
            Console.WriteLine("❌ Contacto no encontrado.");
        }
    }

    static void EliminarContacto()
    {
        Console.Write("Nombre a eliminar: ");
        string nombre = Console.ReadLine();

        if (agenda.Remove(nombre))
            Console.WriteLine("🗑️ Contacto eliminado.");
        else
            Console.WriteLine("❌ Contacto no encontrado.");
    }

    static void MostrarTodos()
    {
        Console.WriteLine("\n📒 Contactos guardados:");
        foreach (var contacto in agenda)
            Console.WriteLine($"- {contacto.Key}: {contacto.Value}");
    }

    static bool EsTelefonoValido(string telefono)
    {
        return telefono.Length <= 11 && long.TryParse(telefono, out _);
    }
