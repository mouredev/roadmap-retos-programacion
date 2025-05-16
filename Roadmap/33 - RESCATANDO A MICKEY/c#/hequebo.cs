class Program
{
    static string[,] maze =
    {
        {"🐭", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"},
        {"⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"},
        {"⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"},
        {"⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"},
        {"⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️"},
        {"⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "🚪"}
    };
    static void Main(string[] args)
    {
        Console.WriteLine("---El laberinto de Mickey Mouse----");
        Random random = new Random();
        ShowMaze(maze);
        Console.WriteLine("¡Ayuda a Mickey a encontrar la salida!");
        Console.WriteLine("Utiliza las teclas W,A,S y D para moverte.");
        bool cleared = false;
        Mickey mickey = new Mickey();
        do
        {
            string? direction = Console.ReadLine();
            mickey.Move(direction, ref maze, ref cleared);
            ShowMaze(maze);

        } while (!cleared);

    }

    static void ShowMaze(string[,] maze) 
    {
        for (int i = 0; i < 6; i++)
        {
            for (int j = 0; j < 6; j++)
                Console.Write(maze[i, j]);
            Console.WriteLine();
        }
    }
}
class Mickey
{
    private int[] _position;

    public Mickey()
    {
        _position = new int[] {0, 0};
    }

    public void Move(string? direction, ref string[,] maze, ref bool cleared)
    {
        string current = "";
        switch (direction?.ToLower())
        {
            case "w":
                if (_position[0] == 0)
                {
                    Console.WriteLine("No es posible moverse hacia arriba...");
                    break;
                }
                if (maze[_position[0] - 1, _position[1]] == "⬛️")
                {
                    Console.WriteLine("Un obstaculo impide moverse hacia arriba");
                    break;
                }
                _position[0] -= 1;

                Console.WriteLine("Se mueve hacia arriba");
                current = maze[_position[0], _position[1]];
                maze[_position[0], _position[1]] = "🐭";
                maze[_position[0] + 1, _position[1]] = "⬜️";
                break;
            case "a":
                if (_position[1] == 0)
                {
                    Console.WriteLine("No es posible moverse hacia la izquierda...");
                    break;
                }
                if (maze[_position[0], _position[1] - 1] == "⬛️")
                {
                    Console.WriteLine("Un obstaculo impide moverse hacia la izquierda");
                    break;
                }
                _position[1] -= 1;

                Console.WriteLine("Se mueve hacia la izquierda");
                current = maze[_position[0], _position[1]];
                maze[_position[0], _position[1]] = "🐭";
                maze[_position[0], _position[1] + 1] = "⬜️";
                break;
            case "s":
                if (_position[0] == 5)
                {
                    Console.WriteLine("No es posible moverse hacia abajo...");
                    break;
                }
                if (maze[_position[0] + 1, _position[1]] == "⬛️")
                {
                    Console.WriteLine("Un obstaculo impide moverse hacia abajo");
                    break;
                }
                _position[0] += 1;

                Console.WriteLine("Se mueve hacia abajo");
                current = maze[_position[0], _position[1]];
                maze[_position[0], _position[1]] = "🐭";
                maze[_position[0] - 1, _position[1]] = "⬜️";
                break;
            case "d":
                if (_position[1] == 5)
                {
                    Console.WriteLine("No es posible moverse hacia la derecha...");
                    break;
                }
                if (maze[_position[0], _position[1] + 1] == "⬛️")
                {
                    Console.WriteLine("Un obstaculo impide moverse hacia la derecha");
                    break;
                }
                _position[1] += 1;

                Console.WriteLine("Se mueve hacia la derecha");
                current = maze[_position[0], _position[1]];
                maze[_position[0], _position[1]] = "🐭";
                maze[_position[0], _position[1] - 1] = "⬜️";
                break;
            default:
                Console.WriteLine("Dirección no válida...");
                break;
        }
        if (current == "🚪")
        {
            Console.WriteLine("¡Mickey ha salido del laberinto!");
            cleared = true;
        }
    }
}