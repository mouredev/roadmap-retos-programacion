class Program
{
    static async Task Main(string[] args)
    {
        await RunTask("Task 1", 2);

        // Ejercicio extra
        Task taskC = RunTask("Task C", 3);
        Task taskB = RunTask("Task B", 2);
        Task taskA = RunTask("Task A", 1);
        
        await Task.WhenAll(taskC, taskB, taskA);
        await RunTask("Task D", 1);
    }
    
    static async Task RunTask(string name, int seconds)
    {
        Console.WriteLine($"Se inicia ejecución de función {name} a las {DateTime.Now.TimeOfDay}");
        await Task.Delay(seconds * 1000);
        Console.WriteLine($"Finaliza la ejecución de {name} a las {DateTime.Now.TimeOfDay}");
    }
}