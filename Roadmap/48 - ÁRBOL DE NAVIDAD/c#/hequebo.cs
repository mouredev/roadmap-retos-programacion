class ChristmasTree
{
    private int _height;
    private int _width;
    private int _center;
    private char[,] _tree;
    private List<(int, int)> _balls;
    private List<(int, int)> _lights;
    private bool _lightsOn;

    public ChristmasTree(int height)
    {
        _height = height;
        _width = _height * 2 - 1;
        _tree = new char[_width, _height + 2];
        _center = _width / 2;
        _balls = new List<(int, int)>();
        _lights = new List<(int, int)>();
        _lightsOn = false;

        for (int i = 0; i < _width; i++)
            for (int j = 0; j < _height + 2; j++)
                _tree[i, j] = ' ';

        for (int i = 0; i < _height; i++)
            for (int j = _center - i; j <= _center + i; j++)
                _tree[j, i] = '*';

        for (int i = _height; i < _height + 2; i++)
            for (int j = _center - 1; j <= _center + 1; j++)
                _tree[j, i] = '|';
        DrawTree();
    }
    private void DrawTree()
    {
        for (int i = 0; i < _height + 2; i++)
        {
            for (int j = 0; j < _width; j++)
                Console.Write(_tree[j, i]);
            Console.WriteLine();
        }
    }
    public void AddStar()
    {
        if (_tree[_center, 0] == '@')
            Console.WriteLine("El arbol ya tiene una estrella...");
        else
        {
            _tree[_center, 0] = '@';
            Console.WriteLine("Se ha agregado una estrella al árbol...");
        }
            
        DrawTree();
    }
    public void RemoveStar()
    {
        if (_tree[_center, 0] != '@')
            Console.WriteLine("El arbol no cuenta con una estrella...");
        else
        {
            _tree[_center, 0] = '*';
            Console.WriteLine("Se quitado la estrella en el árbol");
        }
            
        DrawTree();
    }
    public void AddBalls()
    {
        var availableSpots = GetAvailableSpots();
        if (availableSpots.Count < 2)
            Console.WriteLine("No hay espacio suficiente para añadir más esferas...");
        else
        {
            _balls.AddRange(new List<(int, int)> {
            (availableSpots[0].Item1, availableSpots[0].Item2),
            (availableSpots[1].Item1, availableSpots[1].Item2)
            }
            );
            _tree[availableSpots[0].Item1, availableSpots[0].Item2] = 'o';
            _tree[availableSpots[1].Item1, availableSpots[1].Item2] = 'o';
            Console.WriteLine("Se han agregado dos esferas al árbol...");
        }
        DrawTree();
    }
    public void RemoveBalls()
    {
        if (_balls.Count < 2)
            Console.WriteLine("No ha suficientes esferas para quitar...");
        else
        {
            Random random = new Random();
            var balls = _balls.OrderBy(a => random.Next()).ToList();

            _tree[balls[0].Item1, balls[0].Item2] = '*';
            _tree[balls[1].Item1, balls[1].Item2] = '*';

            _balls.Remove((balls[0].Item1, balls[0].Item2));
            _balls.Remove((balls[1].Item1, balls[1].Item2));
            Console.WriteLine("Se han removido dos esferas del árbol...");
        }
        DrawTree();
    }
    public void AddLights()
    {
        var availableSpots = GetAvailableSpots();
        if (availableSpots.Count < 3)
            Console.WriteLine("No hay espacios suficientes para colocar las luces");
        else
        {
            _lights.AddRange(new List<(int, int)>
            {
                (availableSpots[0].Item1, availableSpots[0].Item2),
                (availableSpots[1].Item1, availableSpots[1].Item2),
                (availableSpots[2].Item1, availableSpots[2].Item2)
            });

            _tree[availableSpots[0].Item1, availableSpots[0].Item2] = _lightsOn ? '+' : '*';
            _tree[availableSpots[1].Item1, availableSpots[1].Item2] = _lightsOn ? '+' : '*';
            _tree[availableSpots[2].Item1, availableSpots[2].Item2] = _lightsOn ? '+' : '*';

            Console.WriteLine("Se agregaron tres luces al árbol...");
        }
        DrawTree();
    }
    public void RemoveLights()
    {
        if (_lights.Count < 3)
            Console.WriteLine("No ha suficientes luces para quitar...");
        else
        {
            Random random = new Random();
            var lights = _lights.OrderBy(l => random.Next()).ToList();

            _tree[lights[0].Item1, lights[0].Item2] = '*';
            _tree[lights[1].Item1, lights[1].Item2] = '*';
            _tree[lights[2].Item1, lights[2].Item2] = '*';

            _lights.Remove((lights[0].Item1, lights[0].Item2));
            _lights.Remove((lights[1].Item1, lights[1].Item2));
            _lights.Remove((lights[2].Item1, lights[2].Item2));
            Console.WriteLine("Se han removido tres luces del árbol...");
        }
        DrawTree();
    }
    public void ToggleLights(bool turnOn)
    {
        if (_lights.Count == 0)
            Console.WriteLine("No hay luces disponibles...");
        else
        {
            _lightsOn = turnOn;
            foreach (var light in _lights)
                _tree[light.Item1, light.Item2] = _lightsOn ? '+' : '*';
        }
        DrawTree();

    }
    public void LightAnimation()
    {
        int i = 0;
        while (i < 30)
        {
            Console.Clear();
            ToggleLights(!_lightsOn);
            i++;
            Thread.Sleep(600);
        }
    }
    private List<(int, int)> GetAvailableSpots()
    {
        List<(int, int)> availableSpots = new List<(int, int)>();

        for (int i = 0; i < _height; i++)
        {
            for (int j = 0; j < _width; j++)
            {
                if (_tree[j, i] == '*' && !_lights.Contains((j, i)))
                    availableSpots.Add((j, i));
            }
        }
        availableSpots.Remove((_center, 0));
        Random random = new Random();
        availableSpots = availableSpots.OrderBy(a => random.Next()).ToList();
        return availableSpots;
    }
}
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("----ARBOL DE NAVIDAD----");
        Console.WriteLine("Ingresa la altura de tu árbol");
        int.TryParse(Console.ReadLine(), out int height);
        if (height <= 3)
        {
            Console.WriteLine("La altura de tu árbol debe de ser por lo menos de tres (3) unidades...");
            return;
        }
        ChristmasTree tree = new ChristmasTree(height);
        bool exit = false;

        do
        {
            Menu();
            int.TryParse(Console.ReadLine() , out int option);
            switch (option)
            {
                case 1:
                    Console.Clear();
                    tree.AddStar();
                    break;
                case 2:
                    Console.Clear();
                    tree.RemoveStar();
                    break;
                case 3: 
                    Console.Clear();
                    tree.AddBalls();
                    break;
                case 4:
                    Console.Clear();
                    tree.RemoveBalls();
                    break;
                case 5:
                    Console.Clear();
                    tree.AddLights();
                    break;
                case 6:
                    Console.Clear();
                    tree.RemoveLights();
                    break;
                case 7:
                    Console.Clear();
                    tree.ToggleLights(true);
                    break;
                case 8:
                    Console.Clear();
                    tree.ToggleLights(false);
                    break;
                case 9:
                    tree.LightAnimation();
                    break;
                case 10:
                    Console.Clear();
                    exit = true;
                    Console.WriteLine("Hasta la próxima y feliz navidad...");
                    Thread.Sleep(1000);
                    break;
                default:
                    Console.Clear();
                    Console.WriteLine("Opción no válida...");
                    break;
            }
        } while (!exit);
    }
    static void Menu()
    {
        Console.WriteLine("----ACCIONES DISPONIBLES----");
        Console.WriteLine("1.- Agregar una estrella en la copa.");
        Console.WriteLine("2.- Remover estrella de la copa.");
        Console.WriteLine("3.- Agregar esferas.");
        Console.WriteLine("4.- Remover esferas.");
        Console.WriteLine("5.- Agregar luces.");
        Console.WriteLine("6.- Remover luces.");
        Console.WriteLine("7.- Encender luces.");
        Console.WriteLine("8.- Apagar luces.");
        Console.WriteLine("9.- Animación de luces.");
        Console.WriteLine("10.- Salir.");
        Console.WriteLine("Selecciona la opción deseada...");
    }
}