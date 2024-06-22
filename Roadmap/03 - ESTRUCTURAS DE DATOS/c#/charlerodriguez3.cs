/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */


// List
Console.WriteLine("Lista:");
List<int> lista = new List<int>();
lista.Add(3); // Inserción
lista.Add(1);
lista.Add(2);
lista.Insert(1, 4); // Inserción en índice específico
lista.RemoveAt(2); // Borrado por índice
lista[0] = 5; // Actualización por índice
lista.Sort(); // Ordenación
foreach (var item in lista)
{
    Console.Write(item + " ");
}
Console.WriteLine();

// Dictionary
Console.WriteLine("\nDiccionario:");
Dictionary<string, int> diccionario = new Dictionary<string, int>();
diccionario.Add("uno", 1); // Inserción
diccionario.Add("dos", 2);
diccionario["tres"] = 3; // Actualización
diccionario.Remove("dos"); // Borrado por clave
foreach (var kvp in diccionario)
{
    Console.WriteLine($"{kvp.Key}: {kvp.Value}");
}

// Queue
Console.WriteLine("\nCola:");
Queue<int> cola = new Queue<int>();
cola.Enqueue(1); // Inserción
cola.Enqueue(2);
cola.Enqueue(3);
int primerElemento = cola.Dequeue(); // Borrado (toma y elimina el primer elemento)
Console.WriteLine($"Primer elemento: {primerElemento}");
foreach (var item in cola)
{
    Console.Write(item + " ");
}
Console.WriteLine();

// Stack
Console.WriteLine("\nPila:");
Stack<int> pila = new Stack<int>();
pila.Push(1); // Inserción
pila.Push(2);
pila.Push(3);
int ultimoElemento = pila.Pop(); // Borrado (toma y elimina el último elemento)
Console.WriteLine($"Último elemento: {ultimoElemento}");
foreach (var item in pila)
{
    Console.Write(item + " ");
}
Console.WriteLine();

// HashSet
Console.WriteLine("\nConjunto:");
HashSet<int> conjunto = new HashSet<int>();
conjunto.Add(1); // Inserción
conjunto.Add(2);
conjunto.Add(3);
conjunto.Remove(2); // Borrado
conjunto.Add(3); // No permite duplicados, entonces no se añadirá nuevamente
foreach (var item in conjunto.OrderBy(x => x))
{
    Console.Write(item + " ");
}
Console.WriteLine();



/*
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

 class Contacto
{
    public string Nombre { get; set; }
    public string Telefono { get; set; }
}

class Program
{
    static List<Contacto> agenda = new List<Contacto>();

    static void Main()
    {
        bool salir = false;

        while (!salir)
        {
            Console.WriteLine("\nSeleccione una operación:");
            Console.WriteLine("1. Mostrar todos los contactos");
            Console.WriteLine("2. Buscar contacto");
            Console.WriteLine("3. Añadir contacto");
            Console.WriteLine("4. Actualizar contacto");
            Console.WriteLine("5. Eliminar contacto");
            Console.WriteLine("6. Salir");

            Console.Write("\nOpción: ");
            string opcion = Console.ReadLine();

            switch (opcion)
            {
                case "1":
                    MostrarContactos();
                    break;
                case "2":
                    BuscarContacto();
                    break;
                case "3":
                    AgregarContacto();
                    break;
                case "4":
                    ActualizarContacto();
                    break;
                case "5":
                    EliminarContacto();
                    break;
                case "6":
                    salir = true;
                    Console.WriteLine("¡Hasta luego!");
                    break;
                default:
                    Console.WriteLine("Opción no válida. Por favor, elija una opción válida.");
                    break;
            }
        }
    }

    static void MostrarContactos()
    {
        Console.WriteLine("\nLista de contactos:");
        foreach (var contacto in agenda)
        {
            Console.WriteLine($"Nombre: {contacto.Nombre}, Teléfono: {contacto.Telefono}");
        }
    }

    static void BuscarContacto()
    {
        Console.Write("Introduce el nombre del contacto a buscar: ");
        string nombre = Console.ReadLine();
        Contacto contactoEncontrado = agenda.Find(c => c.Nombre.Equals(nombre, StringComparison.OrdinalIgnoreCase));
        if (contactoEncontrado != null)
        {
            Console.WriteLine($"Nombre: {contactoEncontrado.Nombre}, Teléfono: {contactoEncontrado.Telefono}");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    static void AgregarContacto()
    {
        Console.Write("Nombre del contacto: ");
        string nombre = Console.ReadLine();
        Console.Write("Teléfono del contacto: ");
        string telefono = Console.ReadLine();

        if (!EsNumeroTelefonoValido(telefono))
        {
            Console.WriteLine("Número de teléfono no válido.");
            return;
        }

        agenda.Add(new Contacto { Nombre = nombre, Telefono = telefono });
        Console.WriteLine("Contacto añadido correctamente.");
    }

    static void ActualizarContacto()
    {
        Console.Write("Introduce el nombre del contacto a actualizar: ");
        string nombre = Console.ReadLine();
        Contacto contacto = agenda.Find(c => c.Nombre.Equals(nombre, StringComparison.OrdinalIgnoreCase));
        if (contacto != null)
        {
            Console.Write("Nuevo nombre del contacto: ");
            string nuevoNombre = Console.ReadLine();
            Console.Write("Nuevo teléfono del contacto: ");
            string nuevoTelefono = Console.ReadLine();

            if (!EsNumeroTelefonoValido(nuevoTelefono))
            {
                Console.WriteLine("Número de teléfono no válido.");
                return;
            }

            contacto.Nombre = nuevoNombre;
            contacto.Telefono = nuevoTelefono;
            Console.WriteLine("Contacto actualizado correctamente.");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    static void EliminarContacto()
    {
        Console.Write("Introduce el nombre del contacto a eliminar: ");
        string nombre = Console.ReadLine();
        Contacto contacto = agenda.Find(c => c.Nombre.Equals(nombre, StringComparison.OrdinalIgnoreCase));
        if (contacto != null)
        {
            agenda.Remove(contacto);
            Console.WriteLine("Contacto eliminado correctamente.");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    static bool EsNumeroTelefonoValido(string telefono)
    {
        long numero;
        return long.TryParse(telefono, out numero) && telefono.Length <= 11; // Validar que el teléfono sea numérico y tenga hasta 11 dígitos
    }

 