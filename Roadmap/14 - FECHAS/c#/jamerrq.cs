/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */

using System;
using System.Globalization;

class Dates
{
    static void Main(string[] args)
    {
        DateTime today = DateTime.Now;
        DateTime birthDate = new DateTime(2000, 02, 21, 12, 00, 00, 00);
        Console.WriteLine($"Han transcurrido {today.AddYears(-birthDate.Year).Year} años");
        Console.WriteLine("#1 Dia del año: " + birthDate.DayOfYear);
        Console.WriteLine("#2 Dia de la semana: " + birthDate.ToString("dddd"));
        Console.WriteLine("#3 Fecha corta: " + birthDate.ToString("d"));
        Console.WriteLine("#4 Fecha larga: " + birthDate.ToString("D"));
        Console.WriteLine("#5 Nombre del mes: " + birthDate.ToString("MMMM"));
        Console.WriteLine("#6 Dia del mes: " + birthDate.ToString("M"));
        Console.WriteLine("#7 Hora, minuto, segundo: " + birthDate.ToString("HH:mm:ss"));
        Console.WriteLine("#8 Era: " + birthDate.ToString("gg"));
        Console.WriteLine("#9 Mes del año: " + birthDate.ToString("Y"));
        Console.WriteLine("#10 Fecha y hora en formato largo: " + birthDate.ToString("F"));
    }
}
