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

namespace Roadmap
{
    internal class Program
    {
        static void Main(string[] args)
        {
            DateTime today = DateTime.Now;
            DateTime birthdate = new DateTime(1998, 02, 13, 07, 00, 00, 00);
            Console.WriteLine($"Han transcurrido {today.AddYears(-birthdate.Year).Year} años");

            // reto extra
            Console.WriteLine("Dia del año: " + birthdate.DayOfYear);
            Console.WriteLine("Dia de la semana: " + birthdate.ToString("dddd"));
            Console.WriteLine("Fecha corta: " + birthdate.ToString("d"));
            Console.WriteLine("Fecha larga: " + birthdate.ToString("D"));
            Console.WriteLine("Nombre del mes: " + birthdate.ToString("MMMM"));
            Console.WriteLine("Dia del mes: " + birthdate.ToString("M"));
            Console.WriteLine("Hora, minuto, segundo: " + birthdate.ToString("HH:mm:ss"));
            Console.WriteLine("Era: " + birthdate.ToString("gg"));
            Console.WriteLine("Mes del año: " + birthdate.ToString("Y"));
            Console.WriteLine("Fecha y hora en formato largo: " + birthdate.ToString("F"));
        }
    }
}
