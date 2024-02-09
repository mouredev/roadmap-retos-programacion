// ╔══════════════════════════════════════╗
// ║ Autor:  Kenys Alvarado               ║
// ║ GitHub: https://github.com/Kenysdev  ║
// ║ 2024 -  C#                           ║
// ╚══════════════════════════════════════╝
class Program
{
    static void Main()
    {
        // -----------------
        // Arrays(Arreglos):
        // -----------------
        // - Colección de elementos del mismo tipo almacenados en posiciones contiguas de memoria.
        // - Acceso rápido a elementos por índice.
        // Declarar e inicializar
        var numeros = new int[2];
        var palabras = new string[] { "Hola", "Mundo" };

        // Inserción:
        numeros[0] = 1;
        numeros[1] = 2;

        // Acceder:
        Console.WriteLine(numeros[0]);

        // Modificar:
        palabras[1] = "Ben";

        // Ordenación:
        Array.Sort(numeros);

        // Iteración:
        for (int i = 0; i < numeros.Length; i++)
        {
            Console.WriteLine("Índice " + i + ": " + numeros[i]);
        }
        // Nota: Los arreglos en C# son de tamaño fijo después de la inicialización.

        // -------------
        // List(Listas):
        // -------------
        // - Dinámicas y redimensionables, permiten almacenar elementos del mismo tipo.
        // - Flexibilidad en la manipulación de datos.
        // Declarar e inicializar
        var nombres = new List<string>();
        var abc = new List<string> { "a", "c", "d" };

        // Inserción:
        nombres.Add("Ben"); // Agrega elemento al final de la lista.
        abc.Insert(1, "b"); // Agrega un elemento en una posición específica.

        // Acceder:
        Console.WriteLine(abc[1]);

        // Modificar:
        nombres[0] = "Zoe";

        // Eliminacion:
        abc.Remove("a");
        abc.RemoveAt(1); // por indice
        abc.RemoveAll(x => x == "c"); // todas las ocurrencias

        // Ordenación:
        abc.Sort();

        // Iteración:
        foreach (string i in abc)
        {
            Console.WriteLine(i);
        }

        // --------------------------
        // Dictionary(Diccionarios ):
        // --------------------------
        // - Asocian claves únicas con valores, permitiendo búsquedas eficientes.
        // - Almacenar y recuperar datos con base en claves.
        // Declarar
        var nombre_edad = new Dictionary<string, int>();
        var dic = new Dictionary<string, int>
        {
            {"a", 1},
            {"b", 2}
        };
        // Inserción:
        nombre_edad["Zoe"] = 21;
        dic.Add("c", 3);

        // Acceder:
        Console.WriteLine(dic["b"]);
        // No mostrar excepción en caso de no existir.
        if (dic.TryGetValue("b", out var valor_))
        {
            Console.WriteLine(valor_);
        }
        // Modificar:
        nombre_edad["Zoe"] = 27;

        // Eliminacion:
        dic.Remove("c");

        // Iteración:
        foreach (int valor in dic.Values) // o dic.Keys
        {
            Console.WriteLine(valor);
        }

        // -------------
        // Queue(Colas):
        // -------------
        // - Estructura FIFO (Primero en entrar, primero en salir).
        // - Modelar procesos secuenciales.
        // Declarar
        var cola = new Queue<string>();

        // Inserción:
        cola.Enqueue("Joe");

        // Acceder:
        Console.WriteLine(cola.Peek()); // Mostrar el primero sin eliminarlo.
        Console.WriteLine(cola.Dequeue()); // Mostrar el primero y eliminarlo
        Console.WriteLine(cola.Count); // Obtener la cantidad de elementos.

        // Eliminacion:
        cola.Clear(); //  Elimina todos los elementos.

        // Iteración:
        foreach (var elemento in cola)
        {
            Console.WriteLine(elemento);
        }

        // -------------
        // Stack(Pilas):
        // -------------
        // - Estructura LIFO (Último en entrar, primero en salir).
        // - Gestión de llamadas a funciones, historial de navegación(Undo/Redo).
        // Declarar
        var miPila = new Stack<int>();

        // Apilar elementos:
        miPila.Push(1);
        miPila.Push(2);

        // Ver el elemento en la cima de la pila sin quitarlo
        Console.WriteLine(miPila.Peek());

        // Desapilar un elemento:
        Console.WriteLine(miPila.Pop());

        // Imprimir todos los elementos de la pila:
        foreach (var elemento in miPila)
        {
            Console.WriteLine(elemento);
        }

        // ------------------
        // HashSet(Conjuntos):
        // ------------------
        // - Colección sin duplicados, sin orden definido.
        // - Verificación de pertenencia y eliminación de duplicados.
        // Declarar e inicializar
        var miConjunto = new HashSet<int>();
        var otroConjunto = new HashSet<int> { 2, 3, 4 };

        // Inserción:
        miConjunto.Add(1);
        miConjunto.Add(2);

        // Buscar:
        if (otroConjunto.Contains(3))
        {
            Console.WriteLine($"El conjunto contiene el elemento {3}");
        }

        // Eliminacion:
        miConjunto.Remove(2);

        // Verificación:
        Console.WriteLine(miConjunto.Contains(1));

        // Operaciones:
        miConjunto.UnionWith(otroConjunto);     // Unión de conjuntos
        miConjunto.IntersectWith(otroConjunto); // Intersección de conjuntos
        miConjunto.ExceptWith(otroConjunto);    // Diferencia de conjuntos

        // Iteración:
        foreach (var elemento in otroConjunto)
        {
            Console.WriteLine(elemento);
        }

        // ---------
        // Matrices:
        // ---------
        // - Estructura bidimensional organizada en filas y columnas.
        // - Representar datos tabulares.
        // Declarar e inicializar
        var mtx1 = new int[3, 3];
        var mtx2 = new int[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };

        // asignación:
        mtx1[0, 0] = 1;
        mtx1[0, 1] = 2;
        mtx1[0, 2] = 3;

        // Acceder:
        Console.WriteLine(mtx1[0, 1]);

        // Iteración:
        int filas = mtx2.GetLength(0);
        int columnas = mtx2.GetLength(1);
        for (int i = 0; i < filas; i++)
        {
            for (int j = 0; j < columnas; j++)
            {
                Console.Write(mtx2[i, j] + " ");
            }
            Console.WriteLine();
        }

        // --------------
        // Tuple(tuplas):
        // --------------
        // - Agrupación de elementos heterogéneos como una entidad única.
        // - Son inmutables.
        // - Devolver múltiples valores desde un método.
        // Declarar e inicializar
        var miTupla = (1, "hola", 3.14, true);
        var tuplaConNombres = (numero: 1, saludo: "hola", pi: 3.14, esCierto: true);
        object item1 = 1;
        object item2 = "hola";
        var miTupla2 = new ValueTuple<object, object>(item1, item2);

        // Acceder:
        Console.WriteLine(miTupla.Item1);
        Console.WriteLine(tuplaConNombres.saludo);

        // ---------
        // Ejercicio:
        // ---------
        /*
        * Crea una agenda de contactos por terminal.
        * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
        * - Cada contacto debe tener un nombre y un número de teléfono.
        * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
        *   los datos necesarios para llevarla a cabo.
        * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
        *   (o el número de dígitos que quieras)
        * - También se debe proponer una operación de finalización del programa.
        */
        while (true)
        {
            Agenda();
        }
    }

    static Dictionary<string, string> miAgenda = new Dictionary<string, string>();
    static void Agenda()
    {
        Console.WriteLine(@"
    Agenda de contactos
╔═══════════════════════════╗
║ 1. Nuevo      4. Editar   ║
║ 2. Buscar     5. Eliminar ║
║ 3. Lista      6. Salir    ║
╚═══════════════════════════╝
        ");

        Console.Write("Número de opción: ");
        string option = Console.ReadLine()!;

        switch (option)
        {
            case "1": Crear();  break;
            case "2": Buscar(); break;
            case "3": Lista();  break;
            case "4": Editar(); break; 
            case "5": Eliminar(); break;
            case "6":
                Console.WriteLine("Adios");
                Environment.Exit(0);
                break;
            default:
                Console.WriteLine("Número 1 -> 6");
                break;
        }
    }
    static void Crear()
    {
        Console.WriteLine("Crear contacto o 6 para Salir");
        Console.Write("Escriba el nombre: ");
        string nombre = Console.ReadLine()!;

        if (nombre.Length < 1)
        {
            Crear();
        }
        else if (nombre == "6")
        {
            Console.WriteLine("Cancelado");
        }
        else if (miAgenda.ContainsKey(nombre))
        {
            Console.WriteLine("El nombre ya existe.");
        }
        else
        {
            Console.Write("Escriba el número: ");
            string numero = Console.ReadLine()!;

            if (int.TryParse(numero, out _) && numero.Length > 0 && numero.Length <= 11)
            {
                miAgenda[nombre] = numero;
                Console.WriteLine("Guardado");
            }
            else
            {
                Console.WriteLine("Número no válido.");
            }
        }
    }

    static void Buscar()
    {
        Console.WriteLine("Buscar contacto o 6 para Salir");
        Console.Write("Escriba el nombre:\n");
        string nombre = Console.ReadLine()!;

        if (nombre == "6")
        {
            Console.WriteLine("Cancelado");
        }
        else if (miAgenda.ContainsKey(nombre))
        {
            Console.WriteLine(miAgenda[nombre]);
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    static void Lista()
    {
        var ordenarAgenda = new SortedDictionary<string, string>(miAgenda);

        foreach (var entry in ordenarAgenda)
        {
            Console.WriteLine($"{entry.Key}: {entry.Value}");
        }
    }

    static void Editar()
    {
        Console.WriteLine("Editar contacto o 6 para Salir");
        Console.Write("Escriba el nombre: ");
        string nombre = Console.ReadLine()!;

        if (nombre == "6")
        {
            Console.WriteLine("Cancelado");
        }
        else if (miAgenda.ContainsKey(nombre))
        {
            Console.Write("Escriba el nuevo número: ");
            string nuevoNumero = Console.ReadLine()!;

            if (int.TryParse(nuevoNumero, out _) && nuevoNumero.Length > 0 && nuevoNumero.Length <= 11)
            {
                miAgenda[nombre] = nuevoNumero;
                Console.WriteLine("Contacto editado");
            }
            else
            {
                Console.WriteLine("Número no válido.");
            }
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    static void Eliminar()
    {
        Console.WriteLine("Eliminar contacto o 6 para Salir");
        Console.Write("Escriba el nombre: ");
        string nombre = Console.ReadLine()!;

        if (nombre == "6")
        {
            Console.WriteLine("Cancelado");
        }
        else if (miAgenda.ContainsKey(nombre))
        {
            miAgenda.Remove(nombre);
            Console.WriteLine("Contacto eliminado");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }
}
