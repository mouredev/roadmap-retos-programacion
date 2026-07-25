namespace exs50;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
__________________________________________
#50 PLANIFICADOR DE OBJETIVOS DE AÑO NUEVO
------------------------------------------
* EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 * 
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado 
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *   
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
*/

using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;

class Goal
{
    public required string Name { get; init; }
    public required int Quantity { get; init; }
    public required string Units { get; init; }
    public required int Months { get; init; }
}

class ObjectivePlanner
{
    private readonly List<Goal> _goals = [];
    private readonly List<string> _months;
    private readonly Dictionary<int, List<int>> _pendingMonthly = [];

    public ObjectivePlanner()
    {
        _months = Enumerable.Range(1, 12)
            .Select(m => CultureInfo.CurrentCulture.DateTimeFormat.GetMonthName(m))
            .ToList();
    }

    private void Add()
    {
        if (_goals.Count >= 10)
        {
            Console.WriteLine("\nMáximo de 10 objetivos alcanzado.");
            return;
        }

        try
        {
            Console.Write("Meta: ");
            var name = Console.ReadLine()?.Trim() ?? string.Empty;

            Console.Write("Cantidad: ");
            var quantity = int.Parse(Console.ReadLine() ?? "0");

            Console.Write("Unidades: ");
            var units = Console.ReadLine()?.Trim() ?? string.Empty;

            Console.Write("Plazo (en meses): ");
            var monthCount = Math.Min(int.Parse(Console.ReadLine() ?? "0"), 12);

            if (!string.IsNullOrEmpty(name) && quantity > 0 && 
                !string.IsNullOrEmpty(units) && monthCount > 0)
            {
                var goal = new Goal
                {
                    Name = name,
                    Quantity = quantity,
                    Units = units,
                    Months = monthCount
                };

                var goalId = _goals.Count;
                _goals.Add(goal);

                var (monthly, extra) = Math.DivRem(quantity, monthCount);
                _pendingMonthly[goalId] = Enumerable.Range(0, monthCount)
                    .Select(m => monthly + (m < extra ? 1 : 0))
                    .ToList();

                Console.WriteLine("\nObjetivo añadido exitosamente.");
            }
            else
            {
                Console.WriteLine("\nDatos inválidos.");
            }
        }
        catch (FormatException)
        {
            Console.WriteLine("\nError: Ingrese valores numéricos válidos.");
        }
    }

    private Dictionary<string, List<string>>? CalculatePlan()
    {
        if (_goals.Count == 0)
            return null;

        var plan = new Dictionary<string, List<string>>();

        for (var goalId = 0; goalId < _goals.Count; goalId++)
        {
            var goal = _goals[goalId];
            var monthlyQuantities = _pendingMonthly[goalId];

            for (var month = 0; month < monthlyQuantities.Count; month++)
            {
                var quantity = monthlyQuantities[month];
                if (quantity > 0)
                {
                    var monthName = _months[month];
                    if (!plan.ContainsKey(monthName))
                        plan[monthName] = [];

                    plan[monthName].Add(
                        $"[ ] {goal.Name} ({quantity} {goal.Units}/mes). " +
                        $"Total: {goal.Quantity}.");
                }
            }
        }

        return plan.Where(kvp => kvp.Value.Count != 0)
                  .ToDictionary(kvp => kvp.Key, kvp => kvp.Value);
    }

    private void SavePlan()
    {
        var plan = CalculatePlan();
        if (plan is null)
        {
            Console.WriteLine("\nNo hay planificación para guardar.");
            return;
        }

        var filename = $"plan_{DateTime.Now:yyyyMMdd_HHmm}.txt";
        try
        {
            using var writer = new StreamWriter(filename, false, Encoding.UTF8);
            foreach (var (month, tasks) in plan)
            {
                writer.WriteLine($"{month}:");
                foreach (var task in tasks)
                {
                    writer.WriteLine($"  {task}");
                }
                writer.WriteLine();
            }

            Console.WriteLine($"\nPlan guardado en {filename}.");
        }
        catch (IOException)
        {
            Console.WriteLine("\nError al guardar el archivo.");
        }
    }

    private void DisplayPlan()
    {
        var plan = CalculatePlan();
        if (plan is not null)
        {
            foreach (var (month, tasks) in plan)
            {
                Console.WriteLine($"\n{month}:");
                foreach (var task in tasks)
                {
                    Console.WriteLine($"  {task}");
                }
            }
        }
    }

    public void Run()
    {
        Console.Clear();

        while (true)
        {
            Console.WriteLine("\nGestor de Objetivos:");
            Console.WriteLine("1. Añadir objetivo");
            Console.WriteLine("2. Calcular plan detallado");
            Console.WriteLine("3. Guardar planificación");
            Console.WriteLine("4. Salir");

            Console.Write("\nSeleccione una opción: ");
            var option = Console.ReadLine()?.Trim();

            switch (option)
            {
                case "1":
                    Add();
                    break;
                case "2":
                    DisplayPlan();
                    break;
                case "3":
                    SavePlan();
                    break;
                case "4":
                    Console.WriteLine("\n¡Adiós!");
                    return;
                default:
                    Console.WriteLine("\nOpción inválida.");
                    break;
            }
        }
    }
}

class Program
{
    static void Main()
    {
        var planner = new ObjectivePlanner();
        planner.Run();
    }
}
