class Program
{
    static void Main(string[] args)
    {
        // Pilas y Colas
        Console.WriteLine("----PILAS Y COLAS----");
        List<int> pila = new List<int> {6, 5, 4, 3, 2, 1};
        Console.WriteLine("---Pilas---");
        Console.WriteLine("Pila Inicial:");
        Mostrar(pila);
        Push(ref pila, 7);
        Console.WriteLine("Se inserta elemento 7 en la pila");
        Console.WriteLine("Pila Actual:");
        Mostrar(pila);
        Console.WriteLine("Se elimina último elemento ingresado en la pila");
        Pop(ref pila);
        Console.WriteLine("Pila Actual:");
        Mostrar(pila);

        // Colas
        Console.WriteLine("---Colas---");
        List<int> cola = new List<int> {1, 2, 3, 4, 5};
        Console.WriteLine("Cola Inicial:");
        Mostrar(cola);
        Console.WriteLine("Se agrega número 6 en la cola");
        Queue(ref cola, 6);
        Console.WriteLine("Cola Actual:");
        Mostrar(cola);
        Console.WriteLine("Se elimina primer elemento agregado a la cola");
        Dequeue(ref cola);
        Console.WriteLine("Cola Actual:");
        Mostrar(cola);
        Console.ReadLine();
        Console.Clear();

        // Ejercicio Extra
        NavegadorWeb();
        Console.Clear();
        Impresora();

    }
    static void Mostrar(List<int> lista)
    {
        if (lista.Count == 0)
        {
            Console.WriteLine("No hay elemntos por mostar...");
            return;
        }
        foreach (int i in lista)
            Console.Write($"{i},");
        Console.WriteLine();
    }
    static void Push(ref List<int> pila, int num)
    {
        pila.Reverse();
        pila.Add(num);
        pila.Reverse();
    }
    static void Pop(ref List<int> pila)
    {
        if (pila.Count == 0)
        {
            Console.WriteLine("La pila esta vacía...");
            return;
        }

        Console.WriteLine($"Elemento eliminado: {pila.First()}");
        pila.Remove(pila.First());
    }
    static void Queue(ref List<int> cola, int num)
    {
        cola.Add(num);
    }
    static void Dequeue(ref List<int> cola) 
    { 
        if (cola.Count == 0)
        {
            Console.WriteLine("La cola está vacía...");
            return;
        }
        Console.WriteLine($"Elemento eliminado: {cola.First()}");
        cola.Remove(cola.First());
    }
    static void NavegadorWeb()
    {
        List<string> urls = new List<string>();
        bool salir = false;
        Console.Clear();
        Console.WriteLine("---Sistema de navegación web---");
        do
        {
            Console.WriteLine("Ingresa la url a la que deseas acceder o selecciona una de las siguientes opciones");
            Console.WriteLine("[Atrás/Adelante/Salir]");
            string opcion = Console.ReadLine();
            Console.Clear();
            if (opcion.ToLower() == "atrás")
            {
                if (urls.Count == 0)
                    Console.WriteLine("No es posible ir atrás");
                else
                    urls.Remove(urls.First());
            }
            else if (opcion.ToLower() == "adelante")
            {
                Console.WriteLine("No es posible ir adelante");
            }
            else if (opcion.ToLower() == "salir")
            {
                salir = true;
                Console.WriteLine("Estás saliendo del navegador...");
                Thread.Sleep(2000);
            }
            else
            {
                urls.Insert(0, opcion);
            }

            if (urls.Count == 0)
                Console.WriteLine("Te encuentras en la página de inicio.");
            else
                Console.WriteLine($"Te encuentras en el sitio {urls.First()}");
        } while (!salir);
    }
    static void Impresora()
    {
        List<string> documentos = new List<string>();
        bool salir = false;

        do
        {
            Console.WriteLine("---Sistema de impresión---");
            Console.WriteLine("Ingresa el nombre de un documento para agregarlo a la cola de impresión.");
            Console.WriteLine("O utiliza el comando \"imprimir\" para imprimir el siguiente documento");
            Console.WriteLine("Utiliza el comando \"salir\" para salir del sistema...");

            string opcion = Console.ReadLine();
            Console.Clear();
            if (opcion.ToLower() == "imprimir")
            {
                if (documentos.Count == 0)
                    Console.WriteLine("La cola está vacía...");
                else
                {
                    Console.WriteLine($"Imprimiendo documento \"{documentos.First()}\"");
                    Thread.Sleep(1000);
                    Console.WriteLine($"El documento \"{documentos.First()}\" se imprimío correctamente...");
                    documentos.Remove(documentos.First());
                }
            }
            else if (opcion.ToLower() == "salir")
            {
                salir = true;
                Console.WriteLine("Saliendo del sistema de impresión...");
                Thread.Sleep(2000);
            }
            else
            {
                documentos.Add(opcion);
                Console.WriteLine($"Se agregó el documento \"{opcion}\" a la cola de impresión...");
            }

            if (documentos.Count == 0)
                Console.WriteLine("No hay documentos pendientes por imprimir...");
        } while (!salir);
    }
}
