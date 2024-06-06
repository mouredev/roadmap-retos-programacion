/*
 * EJERCICIO: Implementa los mecanismos de introducción y recuperación de
 * elementos propios de las pilas (stacks - LIFO) y las colas (queue - FIFO)
 * utilizando una estructura de array o lista (dependiendo de las posibilidades
 * de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el
 *   mecanismo adelante/atrás de un navegador web. Crea un programa en el que
 *   puedas navegar a una página o indicarle que te quieres desplazar adelante o
 *   atrás, mostrando en cada caso el nombre de la web. Las palabras "adelante",
 *   "atras" desencadenan esta acción, el resto se interpreta como el nombre de
 *   una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el
 *   mecanismo de una impresora compartida que recibe documentos y los imprime
 *   cuando así se le indica. La palabra "imprimir" imprime un elemento de la
 *   cola, el resto de palabras se interpretan como nombres de documentos.
*/

using System;

class Stack<T>(int size)
{
    readonly T[] stack = new T[size];
    private int top = -1;
    readonly int size = size;

    public void Push(T item)
    {
        if (top == size - 1)
        {
            Console.WriteLine("Stack is full!");
            return;
        }
        stack[++top] = item;
    }

    public T? Pop()
    {
        if (top == -1)
        {
            Console.WriteLine("Stack is empty!");
            return default;
        }
        return stack[top--];
    }

    public T? Peek()
    {
        if (top == -1)
        {
            Console.WriteLine("Stack is empty!");
            return default;
        }
        return stack[top];
    }
}

class Queue<T>(int size)
{
    readonly T[] queue = new T[size];
    private int front = -1;
    private int rear = -1;
    readonly int size = size;

    public void Enqueue(T item)
    {
        if (rear == size - 1)
        {
            Console.WriteLine("La cola está llena!");
            return;
        }
        queue[++rear] = item;
        if (front == -1)
        {
            front = 0;
        }
    }

    public T? Dequeue()
    {
        if (front == -1)
        {
            Console.WriteLine("No hay elementos en la cola!");
            return default;
        }
        T item = queue[front];
        if (front == rear)
        {
            front = -1;
            rear = -1;
        }
        else
        {
            front++;
        }
        return item;
    }

    public T? Peek()
    {
        if (front == -1)
        {
            Console.WriteLine("Queue is empty!");
            return default;
        }
        return queue[front];
    }
}

class History
{
    private readonly Stack<string> back = new(10);
    private readonly Stack<string> forward = new(10);

    public void GoTo(string page)
    {
        back.Push(page);
    }

    public string Back()
    {
        if (back.Peek() == null)
        {
            return "about:blank";
        }
        forward.Push(back.Pop()!);
        return back.Peek()!;
    }

    public string Forward()
    {
        if (forward.Peek() == null)
        {
            return "about:blank";
        }
        back.Push(forward.Pop()!);
        return back.Peek()!;
    }

    public string Current()
    {
        return back.Peek() ?? "about:blank";
    }
}
class StacksAndQueues
{

    // Pilas
    static void Stacks()
    {
        Console.WriteLine("> Crear una pila de 5 elementos");
        Console.WriteLine("Stack stack = new Stack(3);");
        Stack<int> stack = new(3);
        Console.WriteLine("> Agregar elementos a la pila");
        Console.WriteLine("stack.Push(1);");
        stack.Push(1);
        Console.WriteLine("stack.Push(2);");
        stack.Push(2);
        Console.WriteLine("stack.Push(3);");
        stack.Push(3);
        Console.WriteLine("> Sacar elementos de la pila");
        Console.WriteLine("stack.Pop();");
        Console.WriteLine(stack.Pop());
        Console.WriteLine("stack.Pop();");
        Console.WriteLine(stack.Pop());
    }

    // Colas
    static void Queues()
    {
        Console.WriteLine("> Crear una cola de 5 elementos");
        Console.WriteLine("Queue queue = new Queue(3);");
        Queue<int> queue = new(3);
        Console.WriteLine("> Agregar elementos a la cola");
        Console.WriteLine("queue.Enqueue(1);");
        queue.Enqueue(1);
        Console.WriteLine("queue.Enqueue(2);");
        queue.Enqueue(2);
        Console.WriteLine("queue.Enqueue(3);");
        queue.Enqueue(3);
        Console.WriteLine("> Sacar elementos de la cola");
        Console.WriteLine("queue.Dequeue();");
        Console.WriteLine(queue.Dequeue());
        Console.WriteLine("queue.Dequeue();");
        Console.WriteLine(queue.Dequeue());
    }

    static void NavegadorWeb()
    {
        // Historial de navegación
        History history = new();

        // Mensaje de bienvenida
        Console.WriteLine("Bienvenido al historial de navegación web\n");
        Console.WriteLine("Empezarás en la página about:blank\n");
        Console.WriteLine("Disfruta de tu navegación!\n");

        static void menu()
        {
            Console.WriteLine("Menú:\n");
            Console.WriteLine("1. Navegar a una página");
            Console.WriteLine("2. Retroceder");
            Console.WriteLine("3. Avanzar");
            Console.WriteLine("4. Página actual");
            Console.WriteLine("5. Salir\n");
        }
        while (true)
        {
            menu();
            Console.Write("> Tu opción: ");
            string option = Console.ReadLine() ?? "";
            switch (option)
            {
                case "1":
                    Console.Write("Página: ");
                    string page = Console.ReadLine() ?? "about:blank";
                    history.GoTo(page);
                    Console.WriteLine($"* Navegando a {page}\n");
                    break;
                case "2":
                    Console.WriteLine($"* Retrocediendo a {history.Back()}\n");
                    break;
                case "3":
                    Console.WriteLine($"* Avanzando a {history.Forward()}\n");
                    break;
                case "4":
                    Console.WriteLine($"* Página actual: {history.Current()}\n");
                    break;
                case "5":
                    Console.WriteLine("Nos vemos!");
                    return;
            }
        }
    }

    // Impresora
    static void Impresora()
    {
        // Cola de impresión
        Queue<string> printer = new(10);

        static void menu()
        {
            Console.WriteLine("Menú:\n");
            Console.WriteLine("1. Imprimir un documento");
            Console.WriteLine("2. Agregar un documento a la cola");
            Console.WriteLine("3. Salir\n");
        }
        while (true)
        {
            menu();
            Console.Write("Opción: ");
            string option = Console.ReadLine() ?? "";
            switch (option)
            {
                case "1":
                    Console.WriteLine("Imprimiendo: ");
                    Console.WriteLine($"{printer.Dequeue()}\n");
                    break;
                case "2":
                    Console.Write("Ingresa el nombre del documento: ");
                    string document = Console.ReadLine() ?? "unknown";
                    printer.Enqueue(document);
                    Console.WriteLine($"Documento {document} agregado a la cola\n");
                    break;
                case "3":
                    return;
                default:
                    Console.WriteLine("Opción inválida");
                    break;
            }
        }
    }

    static void Extra()
    {
        // Menu
        Console.WriteLine("1. Navegador web");
        Console.WriteLine("2. Impresora");
        Console.Write("Opción: ");
        string option = Console.ReadLine() ?? "";
        switch (option)
        {
            case "1":
                NavegadorWeb();
                break;
            case "2":
                Impresora();
                break;
            default:
                Console.WriteLine("Opción inválida");
                break;
        }
    }

    static void Main()
    {
        Console.WriteLine("========================================");
        Console.WriteLine("=============== PILAS ==================");
        Console.WriteLine("========================================\n");
        Stacks();
        Console.WriteLine("========================================");
        Console.WriteLine("=============== COLAS ==================");
        Console.WriteLine("========================================\n");
        Queues();
        Console.WriteLine("\n========================================\n");
        Console.WriteLine("============ EJERCICIO EXTRA ===========");
        Console.WriteLine("========================================\n");
        Extra();
    }
}
