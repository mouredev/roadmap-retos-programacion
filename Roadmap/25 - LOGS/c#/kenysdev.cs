#pragma warning disable CA1050 // for namespace Name
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* LOGS
------------------------------------------
Mas info: https://nlog-project.org/
          
*/
using NLog;

// __________________________________
class Program {

    private static readonly Logger logger = LogManager.GetCurrentClassLogger();
    static void Main() {
        /*
        * EJERCICIO #1:
        * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
        * un ejemplo con cada nivel de "severidad" disponible.
        */
        logger.Trace("Trace");
        logger.Debug("Debug");
        logger.Info("Info");
        logger.Warn("Warnin");
        logger.Error("Error");
        logger.Fatal("Fatal");

        //__________________________________
        Console.WriteLine("\nEJERCICIO #2");
        ProgramTask tasks = new();

        tasks.Add("a", "1");
        tasks.Add("b", "2");
        tasks.Add("c", "3");

        tasks.Delete("b");
        tasks.ShowList();
    }
}

/*
__________________________________
* EJERCICIO #2:
* Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
* y listar dichas tareas.
* - Añadir: recibe nombre y descripción.
* - Eliminar: por nombre de la tarea.
* Implementa diferentes mensajes de log que muestren información según la 
* tarea ejecutada (a tu elección).
* Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
*/
class ProgramTask {
    private static readonly Logger logger = LogManager.GetCurrentClassLogger();
    private readonly Dictionary<string, string> tasks;

    public ProgramTask() {
        tasks = [];
        logger.Debug("Se inició instancia de la clase ProgramTask.");
    }

    public void Add(string name, string description) {
        tasks[name] = description;
        logger.Info("Se agregó una tarea.");
    }

    public void Delete(string name) {
        if (tasks.Remove(name)) {
            logger.Info($"Tarea '{name}' eliminada.");
        } else {
            Console.WriteLine();
            logger.Warn($"No se encontró la tarea '{name}'.");
        }
    }

    public void ShowList() {
        logger.Info("Lista de tareas");
        foreach (var task in tasks) {
            Console.WriteLine($"{task.Key} -- {task.Value}");
        }
    }
}
