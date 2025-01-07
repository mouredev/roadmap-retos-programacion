namespace exs48;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
48 ÁRBOL DE NAVIDAD
------------------------------------

 * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 * 
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 * 
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 * 
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 * 
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna).
*/

using System;
using System.Collections.Generic;
using System.Threading;

class ChristmasTree
{
    private readonly int _size;
    private readonly char[,] _matrix;
    private readonly (int Row, int Col) _star;
    private readonly List<(int Row, int Col)> _treeTop = [];
    private readonly List<(int Row, int Col)> _balls = [];
    private readonly List<(int Row, int Col)> _lights = [];

    public ChristmasTree(int size)
    {
        _size = size;
        _matrix = new char[size, size * 2 - 1];
        _star = (0, size - 1);
        
        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < size * 2 - 1; j++)
            {
                _matrix[i, j] = ' ';
            }
        }
    }

    public void PrintTree()
    {
        Console.WriteLine();
        for (int i = 0; i < _size; i++)
        {
            for (int j = 0; j < _size * 2 - 1; j++)
            {
                Console.Write(_matrix[i, j]);
            }
            Console.WriteLine();
        }

        var spaces = (_size * 2 - 4) / 2;
        Console.WriteLine(new string(' ', spaces) + "|||");
        Console.WriteLine(new string(' ', spaces) + "|||");
    }

    public void CreateTree()
    {
        var center = _size - 1;
        for (int i = 0; i < _size; i++)
        {
            var asterisks = new string('*', i * 2 + 1);
            for (int j = 0; j < asterisks.Length; j++)
            {
                var col = center - i + j;
                _matrix[i, col] = asterisks[j];
                _treeTop.Add((i, col));
            }
        }

        _treeTop.RemoveAt(0);
    }

    public void AddRemoveStar()
    {
        var (row, col) = _star;
        _matrix[row, col] = _matrix[row, col] == '*' ? '@' : '*';
    }

    public void AddBalls()
    {
        if (_treeTop.Count < 2)
        {
            Console.WriteLine("Ya no hay espacio para poner bolas.");
            return;
        }

        var random = Random.Shared;
        var positions = new List<(int Row, int Col)>();
        
        for (int i = 0; i < 2; i++)
        {
            var idx = random.Next(_treeTop.Count);
            positions.Add(_treeTop[idx]);
            _treeTop.RemoveAt(idx);
        }

        foreach (var pos in positions)
        {
            _balls.Add(pos);
            _matrix[pos.Row, pos.Col] = 'o';
        }
    }

    public void RemoveBalls()
    {
        if (_balls.Count == 0)
        {
            Console.WriteLine("No hay bolas que eliminar.");
            return;
        }

        var random = Random.Shared;
        var positions = new List<(int Row, int Col)>();
        
        for (int i = 0; i < 2 && _balls.Count > 0; i++)
        {
            var idx = random.Next(_balls.Count);
            positions.Add(_balls[idx]);
            _balls.RemoveAt(idx);
        }

        foreach (var pos in positions)
        {
            _treeTop.Add(pos);
            _matrix[pos.Row, pos.Col] = '*';
        }
    }

    public void AddLights()
    {
        if (_treeTop.Count < 3)
        {
            Console.WriteLine("Ya no hay espacio para poner luces.");
            return;
        }

        var random = Random.Shared;
        var positions = new List<(int Row, int Col)>();
        
        for (int i = 0; i < 3; i++)
        {
            var idx = random.Next(_treeTop.Count);
            positions.Add(_treeTop[idx]);
            _treeTop.RemoveAt(idx);
        }

        foreach (var pos in positions)
        {
            _lights.Add(pos);
            _matrix[pos.Row, pos.Col] = '+';
        }
    }

    public void RemoveLights()
    {
        if (_lights.Count == 0)
        {
            Console.WriteLine("No hay luces que eliminar.");
            return;
        }

        var random = Random.Shared;
        var positions = new List<(int Row, int Col)>();
        
        for (int i = 0; i < 3 && _lights.Count > 0; i++)
        {
            var idx = random.Next(_lights.Count);
            positions.Add(_lights[idx]);
            _lights.RemoveAt(idx);
        }

        foreach (var pos in positions)
        {
            _treeTop.Add(pos);
            _matrix[pos.Row, pos.Col] = '*';
        }
    }

    public void OnOffLights()
    {
        if (_lights.Count == 0)
        {
            Console.WriteLine("No hay luces.");
            return;
        }

        foreach (var (Row, Col) in _lights)
        {
            _matrix[Row, Col] = _matrix[Row, Col] == '*' ? '+' : '*';
        }
    }

    public void AutomaticLights()
    {
        while (true)
        {
            Console.Clear();
            foreach (var (Row, Col) in _lights)
            {
                _matrix[Row, Col] = _matrix[Row, Col] == '*' ? '+' : '*';
            }
            PrintTree();
            Thread.Sleep(1000);
        }
    }
}

class Program
{
    private const string Menu = @"
1 - Agregar/Remover estrella.
2 - Agregar bolas.    | 3 - Quitar bolas.
4 - Agregar luces.    | 5 - Quitar luces.
6 - Encender/Apagar luces.
7 - Luces automáticas.| 8 - Salir
";

    private static void ShowMenu(ChristmasTree tree)
    {
        while (true)
        {
            tree.PrintTree();
            Console.WriteLine(Menu);
            Console.Write("Opción: ");
            var option = Console.ReadLine();

            switch (option)
            {
                case "1": tree.AddRemoveStar(); break;
                case "2": tree.AddBalls(); break;
                case "3": tree.RemoveBalls(); break;
                case "4": tree.AddLights(); break;
                case "5": tree.RemoveLights(); break;
                case "6": tree.OnOffLights(); break;
                case "7": tree.AutomaticLights(); break;
                case "8": return;
                default: Console.WriteLine("Opción inválida."); break;
            }
        }
    }

    private static int GetSize()
    {
        while (true)
        {
            Console.Write("Tamaño: ");
            if (int.TryParse(Console.ReadLine(), out int size) && size % 2 != 0 && size >= 3)
            {
                return size;
            }
            Console.WriteLine("Debe ser un número impar >= 3.");
        }
    }

    public static void Main()
    {
        var size = GetSize();
        var christmasTree = new ChristmasTree(size);
        christmasTree.CreateTree();
        ShowMenu(christmasTree);
    }
}
