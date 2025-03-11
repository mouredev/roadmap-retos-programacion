class Program
{
    static void Main(string[] args)
    {
        // Clases
        var desarrolllador1 = new Desarrollador("Emilio Quezada", 27, "Mexicano", new List<string> { "C#", "Javascript", "VB" });
        desarrolllador1.Imprimir();
        desarrolllador1.Nombre = "Héctor Borja";
        desarrolllador1.Edad = 28;
        desarrolllador1.Nacionalidad = "Español";
        desarrolllador1.Lenguajes.Remove("VB");
        desarrolllador1.Lenguajes.Add("SQL");
        desarrolllador1.Imprimir();
        Console.ReadLine();

        // Ejercicio extra
        // Stack
        Stack stack = new Stack();
        stack.Push(1);
        stack.Push(2);
        stack.Push(3);
        stack.Push(4);
        stack.Imprmir();
        Console.WriteLine($"La pila tiene {stack.Count()} elementos...");

        int eliminado = stack.Pop();
        Console.WriteLine($"Se eliminó el elmento {eliminado}");
        eliminado = stack.Pop();
        Console.WriteLine($"Se eliminó el elmento {eliminado}");
        stack.Imprmir();
        Console.WriteLine($"La pila tiene {stack.Count()} elementos...");
        Console.ReadLine();

        // Queue
        Queue queue = new Queue();
        queue.Enqueue(1);
        queue.Enqueue(2);
        queue.Enqueue(3);
        queue.Enqueue(4);
        queue.Imprmir();
        Console.WriteLine($"La cola tiene {queue.Count()} elementos");

        eliminado = queue.Dequeue();
        Console.WriteLine($"Se eliminó el elmento {eliminado}");
        eliminado = queue.Dequeue();
        Console.WriteLine($"Se eliminó el elmento {eliminado}");
        queue.Imprmir();
        Console.WriteLine($"La cola tiene {queue.Count()} elementos");
    }
}

class Desarrollador
{
    private string _nombre;
    private int _edad;
    private string _nacionalidad;
    private List<string> _lenguajes;

    public string Nombre
    {
        get
        {
            return _nombre;
        }
        set
        {
            _nombre = value;
        }
    }
    public int Edad
    {
        get
        {
            return _edad;
        }
        set
        {
            _edad = value;
        }
    }
    public string Nacionalidad
    {
        get
        {
            return _nacionalidad;
        }
        set
        {
            _nacionalidad = value;
        }
    }
    public List<string> Lenguajes
    {
        get
        {
            return _lenguajes;
        } 
        set
        {
            _lenguajes = value;
        }
    }
    public Desarrollador(string nombre, int edad, string nacionalidad, List<string> lenguajes)
    {
        _nombre = nombre;
        _edad = edad;
        _nacionalidad = nacionalidad;
        _lenguajes = lenguajes;
    }

    public void Imprimir()
    {
        Console.WriteLine($"Nombre: {_nombre}, Edad: {_edad}, Nacionalidad: {_nacionalidad}");
        Console.WriteLine("Lenguajes: ");
        foreach (string lenguaje in _lenguajes)
            Console.Write($"{lenguaje}, ");
        Console.WriteLine();
    }
}
class Stack
{
    private List<int> _stack;

    public Stack()
    {
        _stack = new List<int>();
    }

    public void Push(int valor)
    {
        _stack.Insert(0, valor);
    }
    public int Pop()
    {
        if (_stack.Count == 0)
        {
            Console.WriteLine("La pila está vacía...");
            return -1;
        }
        int eliminado = _stack.First();
        _stack.RemoveAt(0);
        return eliminado;
    }

    public int Count()
    {
        return _stack.Count;
    }
    public void Imprmir()
    {
        if ( _stack.Count == 0 )
            Console.WriteLine("La pila está vacía");
        foreach (int elemento in _stack)
            Console.Write($"{elemento}, ");
        Console.WriteLine();
    }
}
class Queue
{
    private List<int> _queue;

    public Queue()
    {
        _queue = new List<int>();
    }

    public void Enqueue(int valor)
    {
        _queue.Add(valor);
    }
    public int Dequeue()
    {
        if (_queue.Count == 0)
        {
            Console.WriteLine("La cola está vacía...");
            return -1;
        }
        int eliminado = _queue.First();
        _queue.RemoveAt(0);
        return eliminado;
    }

    public int Count()
    {
        return _queue.Count;
    }
    public void Imprmir()
    {
        if (_queue.Count == 0)
            Console.WriteLine("La cola está vacía");
        foreach (int elemento in _queue)
            Console.Write($"{elemento}, ");
        Console.WriteLine();
    }
}
