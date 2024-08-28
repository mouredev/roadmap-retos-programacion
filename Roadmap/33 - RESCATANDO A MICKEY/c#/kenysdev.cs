namespace exs33;
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
-----------------------------------------------------
* RESCATANDO A MICKEY
-----------------------------------------------------
 * EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23! 
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico 
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;

class Program
{
    static void Main()
    {
        // These are the default values. You can change them here.
        var config = new Dictionary<string, string>
        {
            { "title", "RESCUING MICKEY" },
            { "size", "7, 7" },
            { "empty", "⬜️" },
            { "obstacle", "⬛️" },
            { "mouse", "🐭" },
            { "exit", "🚪" }
        };

        var maze = new Maze(config);
        var game = new Game(config, maze);
        game.Play();
    }
}

class Game(Dictionary<string, string> config, Maze maze)
{
    private readonly Dictionary<string, string> _config = config;
    private readonly Maze _maze = maze;

    private static bool RestartOrExit()
    {
        while (true)
        {
            Console.Write("Y/N: ");
            var option = Console.ReadLine()!.ToLower();
            switch (option)
            {
                case "y": return true;
                case "n": return false;
                default: Console.WriteLine("❌Invalid key.❌");
                    break;
            }
        }
    }

    public void Play()
    {
        foreach (var (key, value) in _config)
        {
            Console.WriteLine($"{key}: {value}");
        }

        _maze.Create();
        while (true)
        {
            _maze.PrintMaze();
            Console.WriteLine("Use the keys: (W, S, A, D).\nTo restart: R. To exit: 9.");
            Console.Write("Key: ");
            var option = Console.ReadLine()!.ToLower();
            switch (option)
            {
                case "w": _maze.Up(); break;
                case "s": _maze.Down(); break;
                case "d": _maze.Right(); break;
                case "a": _maze.Left(); break;
                case "r":
                    Console.WriteLine("😮Do you want to restart?😮");
                    if (RestartOrExit())
                    {
                        _maze.Create();
                    }
                    break;
                case "9":
                    Console.WriteLine("😮Do you want to exit?😮");
                    if (RestartOrExit())
                    {
                        return;
                    }
                    break;
                default:
                    Console.WriteLine("❌Invalid key.❌");
                    break;
            }

            if (_maze.VerifyWin())
            {
                Console.WriteLine("🏆Congratulations, you managed to get me out.🏆");
                Console.WriteLine("🤔Do you want to play again?🤔");
                if (RestartOrExit())
                {
                    _maze.Create();
                }
                else
                {
                    Console.WriteLine("Bye");
                    return;
                }
            }
        }
    }
}

class Data
{
    protected Dictionary<string, string> _config;
    protected List<List<string>> _maze;
    protected Tuple<int, int> _positionMouse;
    protected Tuple<int, int> _exitLocation;
    protected int _width;
    protected int _height;
    protected string _obstacleChar;
    protected string _emptyChar;
    protected string _mouseChar;
    protected string _exitChar;

    public Data(Dictionary<string, string> config)
    {
        _config = config;
        _maze = [];
        _positionMouse = new Tuple<int, int>(0, 0);
        _exitLocation = new Tuple<int, int>(0, 0);

        var size = config["size"].Split(',');
        _width = int.Parse(size[0]);
        _height = int.Parse(size[1]);
        _obstacleChar = _config["obstacle"];
        _emptyChar = _config["empty"];
        _mouseChar = _config["mouse"];
        _exitChar = _config["exit"];
    }

    public void PrintMaze()
    {
        Console.WriteLine("--------------------------------------");
        foreach (var row in _maze)
        {
            Console.WriteLine(string.Join("", row));
        }
        Console.WriteLine("--------------------------------------");
    }
}

class Moves(Dictionary<string, string> config) : Data(config)
{
    private void CanMove(int y, int x, int oldY, int oldX)
    {
        int rows = _maze.Count;
        int cols = _maze[0].Count;
        if (y < 0 || x < 0 || y >= rows || x >= cols)
        {
            Console.WriteLine("🚨I can't jump over the edges.🚨");
            return;
        }

        if (_maze[y][x] == _obstacleChar)
        {
            Console.WriteLine("🚨You pushed me against the wall.🚨");
            return;
        }

        _positionMouse = new Tuple<int, int>(y, x);
        Console.WriteLine("✅Correct move.✅");
        _maze[oldY][oldX] = _emptyChar;
        _maze[y][x] = _mouseChar;
    }

    public void Up()
    {
        var (y, x) = _positionMouse;
        CanMove(y - 1, x, oldY: y, oldX: x);
    }

    public void Down()
    {
        var (y, x) = _positionMouse;
        CanMove(y + 1, x, oldY: y, oldX: x);
    }

    public void Right()
    {
        var (y, x) = _positionMouse;
        CanMove(y, x + 1, oldY: y, oldX: x);
    }

    public void Left()
    {
        var (y, x) = _positionMouse;
        CanMove(y, x - 1, oldY: y, oldX: x);
    }
}

class Maze(Dictionary<string, string> config) : Moves(config)
{
    private void CreatePaths(int x, int y)
    {
        _maze[y][x] = _emptyChar;
        var directions = new List<(int, int)> { (0, 1), (1, 0), (0, -1), (-1, 0) };
        foreach (var (dx, dy) in directions.OrderBy(x => Guid.NewGuid()))
        {
            int nx = x + dx * 2, ny = y + dy * 2;
            if (0 < nx && nx < _width - 1 && 0 < ny && ny < _height - 1 && _maze[ny][nx] == _obstacleChar)
            {
                _maze[y + dy][x + dx] = _emptyChar;
                CreatePaths(nx, ny);
            }
        }
    }

    public void Create()
    {
        if (_width % 2 == 0) _width++;
        if (_height % 2 == 0) _height++;

        _maze = [];
        for (int i = 0; i < _height; i++)
        {
            _maze.Add(Enumerable.Repeat(_obstacleChar, _width).ToList());
        }

        int initialX = new Random().Next(1, _width - 1) | 1;
        int initialY = new Random().Next(1, _height - 1) | 1;
        CreatePaths(initialX, initialY);

        _maze[0][1] = _mouseChar;
        _maze[_height - 1][_width - 2] = _exitChar;
        _positionMouse = new Tuple<int, int>(0, 1);
        _exitLocation = new Tuple<int, int>(_height - 1, _width - 2);
    }

    public bool VerifyWin()
    {
        var (y, x) = _exitLocation;
        return _maze[y][x] == _mouseChar;
    }
}
