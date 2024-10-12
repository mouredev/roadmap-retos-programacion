namespace exs38;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
MOUREDEV PRO
------------------------------------
* He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
*/

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Program
{
    static List<Dictionary<string, string>>? ReadCsv(string filePath)
    {
        try
        {
            var lines = File.ReadAllLines(filePath);
            var headers = lines[0].Split(',');
            return lines.Skip(1).Select(line => 
                line.Split(',')
                    .Select((value, index) => new { Header = headers[index], Value = value })
                    .ToDictionary(item => item.Header, item => item.Value)
            ).ToList();
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error reading '{filePath}': {e.Message}");
            return null;
        }
    }

    static List<Dictionary<string, string>> GetActiveEntries(List<Dictionary<string, string>> entries)
    {
        return entries.Where(entry => entry["status"]
                      .Equals("active", StringComparison.CurrentCultureIgnoreCase))
                      .Select(entry => new Dictionary<string, string>
                      {
                          ["id"] = entry["id"],
                          ["email"] = entry["email"],
                          ["status"] = entry["status"]
                      })
                      .ToList();
    }

    static List<Dictionary<string, string>> SelectWinners(List<Dictionary<string, string>> activeEntries, int numWinners)
    {
        var random = new Random();
        return activeEntries.OrderBy(x => random.Next()).Take(Math.Min(numWinners, activeEntries.Count)).ToList();
    }

    static void DistributePrizes(List<Dictionary<string, string>> winners, List<string> prizes)
    {
        var random = new Random();
        prizes = [.. prizes.OrderBy(x => random.Next())];
        for (int i = 0; i < Math.Min(winners.Count, prizes.Count); i++)
        {
            Console.WriteLine($"{prizes[i],-11} -> Id({winners[i]["id"]}): {winners[i]["email"]}");
        }
    }

    static void Main()
    {
        Console.WriteLine("Usuarios ganadores de 'MOUREDEV PRO:'");
        string csvFile = "users.csv";
        var prizes = new List<string> { "Suscripción", "Descuento", "Libro" };

        var entries = ReadCsv(csvFile);
        if (entries != null && entries.Count >= 3)
        {
            var activeEntries = GetActiveEntries(entries);
            var winners = SelectWinners(activeEntries, 3);
            DistributePrizes(winners, prizes);
        }
        else
        {
            Console.WriteLine("Debe haber más de 3 entradas activas.");
        }
    }
}
