using System.ComponentModel;

List<int> cola = new List<int> {1,2,3,4,5};

EnqueuePush(cola, 10);

DequeueList(cola);

Console.WriteLine();

//// ====================

List<int> pila = new List<int> { 6, 7, 8, 9, 10 };

EnqueuePush(pila, 11);

PopList(pila);


// === METODOS ===

void EnqueuePush(List<int> collection, int number) // Este método funciona para ambos tipos de colección, tanto para "Pilas" y "Colas"
{                                                   // ya que en realidad son Listas imitando ser otro tipo de colección.
    collection.Add(number);                         // Este simula el comportamiento del método Enqueue de una Cola o Push de una Pila

    foreach (int i in collection)
    {
        Console.Write($"{i} ");
    }
    Console.WriteLine("\n");
}

// Método de recuperación para la Queue
void DequeueList(List<int> queue) // Este método recupera el primer elemento que se a introducido dentro de la "Cola"
{                                 // simulando el comportamiento del método Dequeue.
    int recovered = queue[0];
    queue.RemoveAt(0);
    Console.WriteLine($"El elemento recuperado es: {recovered}");
}

// Método de recuperación para la Stack

void PopList(List<int> stack) // Este elemento recupera el ultimo elemento que se a introducido dentro de la "Pila"
{                                       // simulando el comportamiento del método Pop.
    int recovered = stack.Count - 1;
    int element = stack[recovered];
    stack.RemoveAt(recovered);
    Console.WriteLine($"El elemento recuperado es: {element}");

    Console.WriteLine("\n");
}

// === EXTRA ===

Console.WriteLine("=== Impresora === \n");

Console.WriteLine("Ingrese palabras (documentos) para que se vayan acumulando en la cola de la impresora, si desea ir imprimiendo los 'documentos'");
Console.WriteLine("escriba la palabra 'imprimir'. \n");
Console.WriteLine("Si ya no desea seguir trabajando con la impresora, escriba 'salir' \n");

List<string> documentation = new List<string>();

bool exit = false;

while (!exit)
{
    string instruction = Console.ReadLine();
    instruction = instruction.ToLower();

    if (instruction == "salir")
    {
        exit = true;
    }
    else if (instruction == "imprimir")
    {
        if (documentation.Count() > 0)
        {
            PrintDocumentation();
        }
        else
        {
            Console.WriteLine("Ya no hay elementos en la cola para imprimir");
        }
    }
    else if (instruction != "imprimir")
    {
        AddDocumentation(instruction);
    }
}

Console.WriteLine();

// ====== Métodos para la impresora ======

void AddDocumentation(string doc)
{
    documentation.Add(doc);
}

void PrintDocumentation()
{
    string recovered = documentation[0];
    documentation.RemoveAt(0);
    Console.Write("imprimiendo");

    for (int i = 0; i <= 5; i++)
    {
        Thread.Sleep(500);
        Console.Write(".");
    }

    Console.WriteLine();
    Console.WriteLine(recovered);
}

// ====================================

Console.WriteLine("=== Navegador Web === \n");

Console.WriteLine("Para moverse por el navegador web puede hacerlo con los comandos 'adelante' y 'atras'");
Console.WriteLine("Si desea cerrar el navegador, escriba 'cerrar' \n");

List<string> navWeb = new List<string> {"Pagina Principal"};

Console.WriteLine(navWeb[0], "\n");

bool navBool = false;

while (!navBool)
{
    string page = Console.ReadLine();
    Console.WriteLine();

    if (page == "adelante")
    {
        Forward();
    }
    else if (page == "atras")
    {
        Back();
    }
    else if (page == "cerrar")
    {
        navBool = true;
    }
    else
    {
        Console.WriteLine("Comando no valido, solo se admite 'adelante' o 'atras'");
    }
}

// ====== Métodos para el navegador web ======

void Forward()
{
    int recovered = navWeb.Count - 1;
    string element = navWeb[recovered];

    if (element == "Pagina Principal")
    {
        navWeb.Add("Menú");
        int lastI = navWeb.Count - 1;
        string valueLastI = navWeb[lastI];
        Console.WriteLine(valueLastI, "\n");
    }
    else if (element == "Menú")
    {
        navWeb.Add("Submenú");
        int lastI = navWeb.Count - 1;
        string valueLastI = navWeb[lastI];
        Console.WriteLine(valueLastI, "\n");
    }
    else if (element == "Submenú")
    {
        navWeb.Add("Opciones");
        int lastI = navWeb.Count - 1;
        string valueLastI = navWeb[lastI];
        Console.WriteLine(valueLastI, "\n");
    }
    else if (element == "Opciones")
    {
        navWeb.Add("Configuración");
        int lastI = navWeb.Count - 1;
        string valueLastI = navWeb[lastI];
        Console.WriteLine(valueLastI, "\n");
    }
    else
    {
        Console.WriteLine("Ya no se puede ir mas para adelante \n");
    }
}

void Back() 
{
    int recovered = navWeb.Count - 1;
    string element = navWeb[recovered];

    if (element == "Pagina Principal")
    {
        Console.WriteLine("Ya no se puede ir mas para atras");
    }
    else
    {
        element = navWeb[recovered - 1];
        navWeb.RemoveAt(recovered);
        Console.WriteLine(element, "\n");
    }
}
