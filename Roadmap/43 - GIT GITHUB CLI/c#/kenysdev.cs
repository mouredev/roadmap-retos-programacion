namespace exs43;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
43 GIT GITHUB CLI
------------------------------------

* EJERCICIO:
 * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
 *
 * Desarrolla un CLI (Command Line Interface) que permita 
 * interactuar con Git y GitHub de manera real desde terminal.
 * 
 * El programa debe permitir las siguientes opciones:
 * 1. Establecer el directorio de trabajo
 * 2. Crear un nuevo repositorio
 * 3. Crear una nueva rama
 * 4. Cambiar de rama
 * 5. Mostrar ficheros pendientes de hacer commit
 * 6. Hacer commit (junto con un add de todos los ficheros)
 * 7. Mostrar el historial de commits
 * 8. Eliminar rama
 * 9. Establecer repositorio remoto
 * 10. Hacer pull
 * 11. Hacer push
 * 12. Salir
*/

using System;
using System.Diagnostics;
using System.IO;
using System.Net;

class GitCommandTool
{
    private static readonly string MENU = """ 
    Comandos Git:: 
    ------------------------------------------------------------
    | 1. Establecer directorio       | 7. Historial de commits |
    | 2. Crear repositorio           | 8. Eliminar rama        |
    | 3. Crear rama                  | 9. Configurar remoto    |
    | 4. Cambiar rama                | 10. pull                |
    | 5. Mostrar cambios pendientes  | 11. push                |
    | 6. 'add' + 'commit'            | 12. Salir               |
    ------------------------------------------------------------
    """;

    private record GitCommand(string Name, string Command, string? Prompt = null);

    private static readonly GitCommand[] COMMANDS = 
    [
        new("Establecer directorio", "cd", "Ruta: "),
        new("Crear repositorio", "git init && git branch -M main"),
        new("Crear rama", "git branch -c", "Nombre: "),
        new("Cambiar rama", "git switch", "Nombre: "),
        new("Mostrar cambios", "git status -s"),
        new("Commit", "git add . && git commit -m", "Mensaje: "),
        new("Historial", "git log --oneline"),
        new("Eliminar rama", "git branch -d", "Nombre: "),
        new("Configurar remoto", "git remote add origin", "URL: "),
        new("Pull", "git pull origin", "rama: "),
        new("Push", "git push origin", "rama: "),
        new("Exit", "exit")
    ];

    private static bool RunCommand(string command)
    {
        try
        {
            var processInfo = new ProcessStartInfo("cmd.exe", $"/c {command}")
            {
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            using var process = Process.Start(processInfo);
            var output = process.StandardOutput.ReadToEnd();
            var error = process.StandardError.ReadToEnd();
            process.WaitForExit();

            if (!string.IsNullOrEmpty(output))
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"✅: {output.Trim()}");
                Console.ResetColor();
            }

            if (!string.IsNullOrEmpty(error))
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"❌: {error.Trim()}");
                Console.ResetColor();
            }

            return process.ExitCode == 0;
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine($"❌: Error ejecutando el comando: {ex.Message}");
            Console.ResetColor();
            return false;
        }
    }

    private static string ReadInput(string prompt)
    {
        Console.Write(prompt);
        return Console.ReadLine()?.Trim() ?? string.Empty;
    }

    private static void Execute(GitCommand cmd)
    {
        Console.WriteLine($"\n=> {cmd.Name}");
        Console.WriteLine("--------------------");

        if (cmd.Name == "Exit") {Environment.Exit(0);}

        if (string.IsNullOrEmpty(cmd.Prompt))
        {
            RunCommand(cmd.Command);
            return;
        }

        var userInput = ReadInput(cmd.Prompt);

        if (cmd.Name == "Establecer directorio")
        {
            if (!Directory.Exists(userInput))
            {
                Console.WriteLine("Esta ruta no existe.");
                return;
            }

            try
            {
                Environment.CurrentDirectory = userInput;
                Console.WriteLine($"Directorio cambiado a: {userInput}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error cambiando directorio: {ex.Message}");
            }
        }
        else
        {
            RunCommand($"{cmd.Command} {userInput}");
        }
    }

    static void Main()
    {
        while (true)
        {
            Console.WriteLine(MENU);
            Console.WriteLine($"Directorio actual: {Environment.CurrentDirectory}");
            Console.WriteLine("--------------------");

            var input = ReadInput("\nOpción: ");

            if (!int.TryParse(input, out int option) || option <= 0 || option > COMMANDS.Length)
            {
                Console.WriteLine("Opción inválida");
                continue;
            }

            if (option == COMMANDS.Length + 1)
                break;

            Execute(COMMANDS[option - 1]);
        }
    }
}
