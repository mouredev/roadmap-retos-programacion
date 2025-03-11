using Microsoft.Extensions.Logging;
using System.Diagnostics;
using System.Globalization;

partial class Program
{
    static void Main(string[] args)
    {
        /*
         * En .Net se puede hacer uso de la API ILogger
         * para registrer el comportamiento de la 
         * aplicación y detectar errores.
         * Usamos la interface ILoggerFactory para 
         * configurar donde queremos enviar los mensajes
         * del log, en este caso se envían a la consola
         */
        using ILoggerFactory factory = LoggerFactory.Create(builder => builder.AddConsole());
        /*
         * Creamos un ILogger e indicamos la categoria
         * (Program). La categoria es un string asociada
         * a cada mensaje del log. Se usa para agrupar
         * mensajes de una misma clase.
         */
        ILogger logger = factory.CreateLogger("Program");
        /*
         * Cada uno de los metodos siguientes realizan
         * el registro  en cada uno de los diferentes
         * niveles dependiendo de la gravedad del 
         * evento registrado.
         */
        logger.LogTrace("Trace Log");
        logger.LogDebug("Debug Log");
        logger.LogInformation("Information Log");
        logger.LogWarning("Warning Log");
        logger.LogError("Error Log");
        logger.LogCritical("Critical Log");

        // Ejercicio

        Console.ReadLine();
        Console.Clear();
        var tasks = new Dictionary<string, string>();
        bool salir = false;
        do
        {
            Menu();
            int option = 0;
            int.TryParse(Console.ReadLine(), out option);

            switch (option)
            {
                case 1:
                    AddTask(ref tasks, logger);
                    break;
                case 2:
                    RemoveTask(ref tasks, logger);
                    break;
                case 3:
                    salir = true;
                    Console.Clear();
                    Console.WriteLine("Hasta la proxima...");
                    Thread.Sleep(1000);
                    break;
                default:
                    Console.WriteLine("Opción no válida...");
                    break;
            }
        } while (!salir);


    }
    static void Menu()
    {
        Console.WriteLine("---Gestión de tareas---");
        Console.WriteLine("1.- Agregar tarea");
        Console.WriteLine("2.- Eliminar tarea");
        Console.WriteLine("3.- Salir");
        Console.WriteLine("Elija la opción deseada...");
    }
    static void AddTask(ref Dictionary<string, string> tasks, ILogger logger)
    {
        Console.Clear();
        Stopwatch sp = new Stopwatch();
        sp.Start();
        Console.WriteLine("Ingresa nombre de tarea");
        string name = Console.ReadLine();
        Console.WriteLine("Ingresa descripción de la tarea");
        string description = Console.ReadLine();
        tasks.Add(name, description);
        sp.Stop();
        LogAddedTask(logger, (int) sp.ElapsedMilliseconds / 1000);
        
    }

    [LoggerMessage(level: LogLevel.Information, Message = "Se agrega tarea en {time} segundos")]
    static partial void LogAddedTask(ILogger logger, int time);
    static void RemoveTask(ref Dictionary<string, string> tasks, ILogger logger)
    {
        Console.Clear();
        if (tasks.Count == 0)
        {
            Console.WriteLine("No hay tareas registradas...");
            return;
        }
        Stopwatch sp = new Stopwatch();
        sp.Start();
        Console.WriteLine("Ingresa nombre de tarea");
        string name = Console.ReadLine();
        tasks.Remove(name);
        sp.Stop();
        LogTaskDeleted(logger, (int) sp.ElapsedMilliseconds / 1000);
        
    }
    [LoggerMessage(level: LogLevel.Information, Message = "Se elimina tarea en {time} segundos")]
    static partial void LogTaskDeleted(ILogger logger, int time);
}
    
