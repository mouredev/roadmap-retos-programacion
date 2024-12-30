using System.Diagnostics;

class Git
{
    public void ChangeDirectory(string path)
    {
        if (!Directory.Exists(path))
            Console.WriteLine("El directorio indicado no existe...");
        else
            Environment.CurrentDirectory = path;
        Console.WriteLine($"El directorio actual es: {Environment.CurrentDirectory}");
    }
    public void CreateRepository()
    {
        if (Directory.Exists($@"{Environment.CurrentDirectory}\.git"))
        {
            Console.WriteLine("Se encuentra dentro de un repositorio...");
            return;
        }
        RunCommand("git init");
        RunCommand("git branch -M main");
        Console.WriteLine("Se ha inicializado el repositorio");
    }
    public void CreateBranch(string branchName) => RunCommand($"git branch {branchName}");
    public void Checkout(string branchName) => RunCommand($"git checkout {branchName}");
    public void ShowPendingFiles() => RunCommand("git status");
    public void Commit(string commitMessage)
    {
        RunCommand("git add .");
        RunCommand($"git commit -m \"{commitMessage}\"");
    }
    public void ShowCommitHistory() => RunCommand("git log --oneline");
    public void DeleteBranch(string branchName) => RunCommand($"git branch -d {branchName}");
    public void SetRemoteRepository(string url)
    {
        RunCommand($"git remote add origin {url}");
        RunCommand("git push -u origin main");
    }
    public void Pull() => RunCommand("git pull");
    public void Push()
    {
        string? branchName = RunCommand("git branch --show-current");
        RunCommand($"git push origin {branchName}");
    }
    private string? RunCommand(string command)
    {
        var process = new Process();
        process.StartInfo.FileName = "cmd.exe";
        process.StartInfo.Arguments = $"/c {command}";
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.RedirectStandardOutput = true;
        process.StartInfo.RedirectStandardError = true;

        process.Start();

        string output = process.StandardOutput.ReadToEnd();
        string error = process.StandardError.ReadToEnd();
        process.WaitForExit();
        if (command.Contains("--show-current"))
            return output;
        if (!string.IsNullOrEmpty(output))
            Console.WriteLine(output);
        if (!string.IsNullOrEmpty(error))
            Console.WriteLine(error);
        
        return null;
    }
}
class Program
{
    static void Main(string[] args)
    {
        Environment.CurrentDirectory = Environment.GetEnvironmentVariable("DEFAULT_DIRECTORY");
        Console.WriteLine("---Git y Github CLI---");
        bool exit = false;
        Git git = new Git();
        do
        {
            Menu();

            int option = 0;
            int.TryParse(Console.ReadLine(), out option);

            switch (option)
            {
                case 1:
                    Console.Clear();
                    Console.WriteLine("Ingresa el directorio completo:");
                    string path = Console.ReadLine();
                    git.ChangeDirectory(path);
                    break;
                case 2:
                    Console.Clear();
                    git.CreateRepository();
                    break;
                case 3:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre de la nueva rama:");
                    Console.WriteLine("Ten en cuenta que es necesario realizar un " +
                        "commit a tu rama principal antes de crear una nueva rama");
                    string? branchName = Console.ReadLine();
                    git.CreateBranch(branchName);
                    break;
                case 4:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre de la rama a la que quieres cambiar:");
                    branchName = Console.ReadLine();
                    git.Checkout(branchName);
                    break;
                case 5:
                    Console.Clear();
                    git.ShowPendingFiles();
                    break;
                case 6:
                    Console.Clear();
                    Console.WriteLine("Ingresa el mensaja de tu commit:");
                    string? commitMessage = Console.ReadLine();
                    git.Commit(commitMessage);
                    break;
                case 7:
                    Console.Clear();
                    git.ShowCommitHistory();
                    break;
                case 8:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre de la rama que quieres eliminar:");
                    branchName = Console.ReadLine();
                    git.DeleteBranch(branchName);
                    break;
                case 9:
                    Console.Clear();
                    Console.WriteLine("Ingresa la url del remositorio remoto:");
                    string? url = Console.ReadLine();
                    git.SetRemoteRepository(url);
                    break;
                case 10: 
                    Console.Clear();
                    git.Pull();
                    break;
                case 11:
                    Console.Clear();
                    git.Push();
                    break;
                case 12:
                    Console.Clear();
                    exit = true;
                    Console.WriteLine("Hasta la próxima...");
                    Thread.Sleep(1000);
                    break;
                default:
                    Console.WriteLine("La opción no es válida...");
                    break;
            }
        } while (!exit);
    }
    static void Menu()
    {
        Console.WriteLine("1.- Establecer Directorio.");
        Console.WriteLine("2.- Crear un nuevo repositorio.");
        Console.WriteLine("3.- Crear una nueva rama.");
        Console.WriteLine("4.- Cambiar de rama.");
        Console.WriteLine("5.- Mostrar ficheros pendientes de hacer commit.");
        Console.WriteLine("6.- Hacer Commit.");
        Console.WriteLine("7.- Mostrar historial de commits");
        Console.WriteLine("8.- Eliminar una rama.");
        Console.WriteLine("9.- Establecer repositorio remoto.");
        Console.WriteLine("10.- Hacer pull.");
        Console.WriteLine("11.- Hacer push");
        Console.WriteLine("12.- Salir.");
        Console.WriteLine("Seleccione una opción...");
    }
}