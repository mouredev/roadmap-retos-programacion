/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  C#                            ║
╚═══════════════════════════════════════╝
-----------------------------------------------
* FECHAS
-----------------------------------------------
- Mas info: 
https://www.netmentor.es/entrada/trabajando-con-fechas
https://learn.microsoft.com/en-us/dotnet/api/system.datetime?view=net-8.0

_______________________________________________
* EJERCICIO 1
* Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
* - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
* - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
* Calcula cuántos años han transcurrido entre ambas fechas.
"""
*/
using System.Globalization;

DateTime currentDateTime = DateTime.Now;
DateTime birthDate = new DateTime(1995, 10, 20, 2, 30, 0);

TimeSpan difference = currentDateTime - birthDate;
int years = difference.Days / 365;
int months = (difference.Days % 365) / 30;
int days = (difference.Days % 365) % 30;

Console.WriteLine(@$"
Juanito tiene: 
{years} años,
{months} meses y
{days} días.");

/* ____________________________________________
# EJERCICIO 2
* Utilizando la fecha de tu cumpleaños, formatéala y muestra su 
  resultado de 10 maneras diferentes.
*/

Console.WriteLine($@"
1. Predeterminado -> {birthDate}
2. Fecha larga    -> {birthDate.ToString("D")}
3. dd-MM-yyyy     -> {birthDate.ToString("dd-MM-yyyy")}
4. Nombre del mes -> {birthDate.ToString("MMMM")}
5. Mes abreviado  -> {birthDate.ToString("MMM")}
6. Nombre del día -> {birthDate.ToString("dddd")}
7. Día abreviado  -> {birthDate.ToString("ddd")}
8. Hora(24 horas) -> {birthDate.ToString("HH:mm:ss")}
9. Hora(12 horas) -> {birthDate.ToString(
    "hh:mm tt", CultureInfo.InvariantCulture)}
0. Personalizado  -> {birthDate.ToString(
    "Born on dddd, dd'th of' MMMM yyyy 'at' hh:mm:ss tt")}
");

