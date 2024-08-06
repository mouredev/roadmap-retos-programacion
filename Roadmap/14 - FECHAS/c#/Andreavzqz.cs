using System;
using System.Globalization;

namespace EjercicioFechas
{
    class Program
    {
        static void Main(string[] args)
        {

            //Fecha actual
            DateTime fechaActual = DateTime.Now;

            //Fecha de nacimiento
            DateTime fechaNacimiento = new DateTime(1994, 05, 13, 14, 30, 0);

            //Calcular años trasncurridos
            int edad = fechaActual.Year - fechaNacimiento.Year;
            if(fechaActual < fechaNacimiento.AddYears(edad))
            {
                edad--;
            }
            Console.WriteLine($"Años transcurridos: {edad}");


            //Dificualtad extra formateo de la fecha de nacimiento de 10 maneras diferentes
            Console.WriteLine("\nFormatos de fechas de nacimiento:");
            Console.WriteLine($"1. Dia, mes y año: {fechaNacimiento.ToString(dd/MM/yyy)}");
            Console.WriteLine($"2. Hora, minuto y segundo: {fechaNacimiento.ToString("HH:mm:ss")}");
            Console.WriteLine($"3. Dia del año: {fechaNacimiento.DayOfWeek}");
            Console.WriteLine($"4. Dia de la semana: {fechaNacimiento.DayOfWeek0}");
            Console.WriteLine($"5. Nombre del mes: {fechaNacimiento.ToString("MMM", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"6. Fecha completa corta: {fechaNacimiento.ToString("g")}");
            Console.WriteLine($"7. Fecha completa larga: {fechaNacimiento.ToString("F")}");
            Console.WriteLine($"8. Solo mes y año: {fechaNacimiento.ToString("MM/yyyy")}");
            Console.WriteLine($"9. Año en dos digitos: {fechaNacimiento.ToString("yy")}");
            Console.WriteLine($"10. Mes y nombre del dia: {fechaNacimiento.ToString("MMM dd")}");


            // Formato personalizao
            Console.WriteLine($"\nFecha actual: {fechaActual.ToString("ddd, dd MMM yyyy HH:mm:ss ")}");
        }
    }

/*

- Explicación

Fecha Actual:
Se obtiene utilizando DateTime.Now, que proporciona la fecha y hora actuales del sistema.

Fecha de Nacimiento:
Se establece utilizando el constructor de DateTime con los parámetros año, mes, día, hora, minuto y segundo.

Cálculo de Años Transcurridos:
Se calcula restando los años de ambas fechas. Si la fecha actual aún no ha alcanzado el día de cumpleaños en el año actual, se resta un año adicional.

-Dificultad Extra: Formateo de Fecha de Nacimiento: 
Se muestran 10 formatos diferentes de la fecha de nacimiento utilizando el método ToString de DateTime con diferentes especificadores de formato:
Formato "dd/MM/yyyy": Día, mes y año.
Formato "HH:mm
": Hora, minuto y segundo.
DayOfYear: Día del año.
DayOfWeek: Día de la semana.
Formato "MMMM": Nombre del mes completo.
Formato "g": Fecha completa corta.
Formato "F": Fecha completa larga.
Formato "MM/yyyy": Solo mes y año.
Formato "yy": Año en dos dígitos.
Formato "MMMM dd": Mes y nombre del día.

*/

}
