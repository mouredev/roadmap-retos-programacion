using System;
using System.Diagnostics;
using System.IO;

class GitCLI
{
    static void Main()
    {
        var cli = new GitCommandLine();
        cli.Run();
    }
}

/// <summary>
/// Clase principal que gestiona la interacción con el usuario y el flujo del programa
/// </summary>
class GitCommandLine
{
    private bool exit = false;  // Controla el ciclo del menú principal
    private string _directory;  // Almacena el directorio de trabajo actual

    /// <summary>
    /// Inicia el menú principal del CLI y espera la selección del usuario
    /// </summary>
    public void Run()
    {
        while (!exit)
        {
            ShowMenu();
            string choice = Console.ReadLine();
            HandleChoice(choice);
        }
    }

    /// <summary>
    /// Muestra el menú principal de opciones para el usuario
    /// </summary>
    private void ShowMenu()
    {
        Console.WriteLine("\nMenú de Git CLI:");
        Console.WriteLine("1. Establecer directorio de trabajo");
        Console.WriteLine("2. Configurar autenticación en GitHub");
        Console.WriteLine("3. Crear nuevo repositorio");
        Console.WriteLine("4. Crear nueva rama");
        Console.WriteLine("5. Cambiar de rama");
        Console.WriteLine("6. Renombrar rama");
        Console.WriteLine("7. Mostrar archivos pendientes de commit");
        Console.WriteLine("8. Hacer commit");
        Console.WriteLine("9. Mostrar historial de commits");
        Console.WriteLine("10. Eliminar rama");
        Console.WriteLine("11. Establecer repositorio remoto");
        Console.WriteLine("12. Hacer pull");
        Console.WriteLine("13. Hacer push");
        Console.WriteLine("14. Crear README.md");
        Console.WriteLine("15. Salir");
        Console.Write("Selecciona una opción: ");
    }

    /// <summary>
    /// Ejecuta la acción seleccionada por el usuario en el menú
    /// </summary>
    /// <param name="choice">Opción seleccionada por el usuario</param>
    private void HandleChoice(string choice)
    {
        switch (choice)
        {
            case "1": SetWorkingDirectory(); break;
            case "2": ConfigureGitHubAuthentication(); break;
            case "3": GitCommands.CreateNewRepo(_directory); break;
            case "4": GitCommands.CreateNewBranch(); break;
            case "5": GitCommands.SwitchBranch(); break;
            case "6": GitCommands.RenameBranch(); break;
            case "7": GitCommands.ShowUnstagedFiles(); break;
            case "8": GitCommands.CommitChanges(); break;
            case "9": GitCommands.ShowCommitHistory(); break;
            case "10": GitCommands.DeleteBranch(); break;
            case "11": GitCommands.SetRemoteRepository(); break;
            case "12": GitCommands.PullChanges(); break;
            case "13": GitCommands.PushChanges(); break;
            case "14": GitCommands.CreateReadMe(_directory); break;
            case "15": exit = true; Console.WriteLine("Saliendo..."); break;
            default: Console.WriteLine("Opción inválida. Por favor, elige una opción válida."); break;
        }
    }

    /// <summary>
    /// Configura el directorio de trabajo para los comandos de Git.
    /// Verifica que el directorio exista y maneja errores de forma controlada
    /// </summary>
    private void SetWorkingDirectory()
    {
        Console.Write("Ingresa la ruta del directorio de trabajo: ");
        string directory = Console.ReadLine();

        // Validación de existencia del directorio
        if (Directory.Exists(directory))
        {
            try
            {
                _directory = directory;
                Console.WriteLine($"Directorio cambiado a: {directory}");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error al cambiar el directorio: " + e.Message);
            }
        }
        else
        {
            Console.WriteLine($"El directorio '{directory}' no existe. Por favor, ingresa una ruta válida.");
        }
    }

    /// <summary>
    /// Configura las credenciales de autenticación para GitHub
    /// </summary>
    private void ConfigureGitHubAuthentication()
    {
        Console.WriteLine("Configurando autenticación de GitHub...");
        Console.Write("Ingresa tu nombre de usuario de GitHub: ");
        string username = Console.ReadLine();
        Console.Write("Ingresa tu PAT (Personal Access Token): ");
        string token = Console.ReadLine();
        GitCommands.ConfigureAuthentication(username, token);
    }
}

/// <summary>
/// Clase que encapsula los comandos de Git para realizar diversas operaciones
/// </summary>
static class GitCommands
{
    /// <summary>
    /// Crea un nuevo repositorio Git en el directorio especificado
    /// </summary>
    /// <param name="directory">Directorio de trabajo</param>
    public static void CreateNewRepo(string directory)
    {
        if (!string.IsNullOrEmpty(directory))
        {
            Console.WriteLine("Inicializando un nuevo repositorio Git...");
            RunCommand("git init", directory);
        }
        else
        {
            Console.WriteLine("No se ha configurado un directorio de trabajo. Establécelo antes de crear un repositorio.");
        }
    }

    /// <summary>
    /// Crea una nueva rama en el repositorio actual
    /// </summary>
    public static void CreateNewBranch()
    {
        Console.Write("Ingresa el nombre de la nueva rama: ");
        string branch = Console.ReadLine();
        if (!string.IsNullOrWhiteSpace(branch))
            RunCommand($"git checkout -b {branch}");
        else
            Console.WriteLine("El nombre de la rama no puede estar vacío.");
    }

    /// <summary>
    /// Cambia a la rama especificada por el usuario
    /// </summary>
    public static void SwitchBranch()
    {
        Console.Write("Ingresa el nombre de la rama a la que deseas cambiar: ");
        string branch = Console.ReadLine();
        if (BranchExists(branch))
            RunCommand($"git checkout {branch}");
        else
            Console.WriteLine($"La rama '{branch}' no existe.");
    }

    /// <summary>
    /// Renombra una rama existente.
    /// </summary>
    public static void RenameBranch()
    {
        Console.Write("Ingresa el nuevo nombre para la rama: ");
        string newBranchName = Console.ReadLine();

        // Ejecutar el comando para renombrar la rama
        RunCommand($"git branch -M {newBranchName}");
    }

    /// <summary>
    /// Muestra los archivos pendientes de ser commit
    /// </summary>
    public static void ShowUnstagedFiles() => RunCommand("git status --short");

    /// <summary>
    /// Realiza un commit con todos los cambios actuales
    /// </summary>
    public static void CommitChanges()
    {
        Console.Write("Ingresa el mensaje para el commit: ");
        string message = Console.ReadLine();
        if (!string.IsNullOrWhiteSpace(message))
        {
            RunCommand("git add .");
            RunCommand($"git commit -m \"{message}\"");
        }
        else
        {
            Console.WriteLine("El mensaje de commit no puede estar vacío.");
        }
    }

    /// <summary>
    /// Muestra el historial de commits del repositorio actual
    /// </summary>
    public static void ShowCommitHistory() => RunCommand("git log --oneline");

    /// <summary>
    /// Elimina una rama especificada
    /// </summary>
    public static void DeleteBranch()
    {
        Console.Write("Ingresa el nombre de la rama a eliminar: ");
        string branch = Console.ReadLine();
        if (BranchExists(branch))
            RunCommand($"git branch -d {branch}");
        else
            Console.WriteLine($"La rama '{branch}' no existe.");
    }

    /// <summary>
    /// Establece el repositorio remoto para el repositorio local
    /// </summary>
    public static void SetRemoteRepository()
    {
        Console.Write("Ingresa la URL del repositorio remoto: ");
        string remoteUrl = Console.ReadLine();
        if (Uri.IsWellFormedUriString(remoteUrl, UriKind.Absolute))
            RunCommand($"git remote add origin {remoteUrl}");
        else
            Console.WriteLine("La URL es inválida.");
    }

    /// <summary>
    /// Realiza un pull de los cambios desde el repositorio remoto
    /// </summary>
    public static void PullChanges() => RunCommand("git pull origin");

    /// <summary>
    /// Realiza un push de los cambios al repositorio remoto
    /// </summary>
    public static void PushChanges() => RunCommand("git push origin");

    /// <summary>
    /// Crea un README.md y agrega un título al archivo en el directorio establecido.
    /// </summary>
    public static void CreateReadMe(string directory)
    {
        // Verifica que el directorio haya sido establecido
        if (string.IsNullOrEmpty(directory))
        {
            Console.WriteLine("Por favor, establece el directorio de trabajo primero.");
            return;
        }

        string readmePath = Path.Combine(directory, "README.md");

        // Verifica si el archivo ya existe
        if (!File.Exists(readmePath))
        {
            // Agrega contenido al README.md
            File.WriteAllText(readmePath, "# Readme para el contenido");
            Console.WriteLine("README.md creado con el contenido: '# Readme'");
        }
        else
        {
            Console.WriteLine("El archivo README.md ya existe en el directorio: " + directory);
        }
    }

    /// <summary>
    /// Configura las credenciales de autenticación para GitHub
    /// </summary>
    /// <param name="username">Nombre de usuario de GitHub</param>
    /// <param name="token">Token de acceso personal</param>
    public static void ConfigureAuthentication(string username, string token)
    {
        if (!string.IsNullOrWhiteSpace(username) && !string.IsNullOrWhiteSpace(token))
        {
            RunCommand($"git config --global user.name \"{username}\"");
            RunCommand($"git config --global user.password \"{token}\"");
            Console.WriteLine("Autenticación de GitHub configurada exitosamente.");
        }
        else
        {
            Console.WriteLine("El nombre de usuario y el token no pueden estar vacíos.");
        }
    }

    /// <summary>
    /// Verifica si una rama existe en el repositorio actual
    /// </summary>
    /// <param name="branch">Nombre de la rama a verificar</param>
    /// <returns>true si la rama existe, false en caso contrario</returns>
    private static bool BranchExists(string branch)
    {
        string branches = RunCommandAndGetOutput("git branch");
        return branches.Contains(branch);
    }

    /// <summary>
    /// Ejecuta un comando de Git en el sistema
    /// </summary>
    /// <param name="command">Comando a ejecutar</param>
    /// <param name="workingDirectory">Directorio de trabajo</param>
    private static void RunCommand(string command, string workingDirectory = "")
    {
        try
        {
            ProcessStartInfo processInfo = new ProcessStartInfo("cmd.exe", "/c " + command)
            {
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true,
                WorkingDirectory = workingDirectory
            };

            using (Process process = Process.Start(processInfo))
            {
                process.WaitForExit();
                string output = process.StandardOutput.ReadToEnd();
                string error = process.StandardError.ReadToEnd();

                if (!string.IsNullOrEmpty(output))
                    Console.WriteLine(output);
                if (!string.IsNullOrEmpty(error))
                    Console.WriteLine("Error: " + error);
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error al ejecutar el comando: " + ex.Message);
        }
    }

    /// <summary>
    /// Ejecuta un comando de Git y devuelve el resultado como string
    /// </summary>
    /// <param name="command">Comando a ejecutar</param>
    /// <returns>Resultado del comando</returns>
    private static string RunCommandAndGetOutput(string command)
    {
        try
        {
            ProcessStartInfo processInfo = new ProcessStartInfo("cmd.exe", "/c " + command)
            {
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            using (Process process = Process.Start(processInfo))
            {
                process.WaitForExit();
                return process.StandardOutput.ReadToEnd();
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error al ejecutar el comando: " + ex.Message);
            return string.Empty;
        }
    }
}