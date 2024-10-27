class Program
{
    static void Main(string[] args)
    {
        /*
         * Para obtener la fecha actual se puede utilizar
         * la propiedad UtcNow o Now de la clase DateTime
         * la cual devuelve un objeto de tipo DateTime
         */
        var fechaActual = DateTime.UtcNow;
        Console.WriteLine($"Fecha Actual: {fechaActual}");
        /*
         * Para crear una fecha personalizada se puede instanciar
         * un objeto de la clase DateTime y a su constructor le
         * podemos envíar varias combinaciones de parámetros
         * una de ellas siendo (año, mes, día, hora, minutos y segundos)
         */
        var fechaNacimiento = new DateTime(1997, 07, 28, 8, 15, 3);
        Console.WriteLine($"Fecha de Nacimiento: {fechaNacimiento}");
        /*
         * Para calcular la edad restamos la propiedad Year de nuestras
         * fechas y si en la fecha actual no se ha cumplido años se
         * ajusta restando un año a la edad
         */
        int edad = (fechaActual.Year - fechaNacimiento.Year);
        if (fechaActual < fechaNacimiento.AddYears(edad))
            edad--;
        Console.WriteLine($"La edad es de {edad} años");

        // Ejercicio extra
        Console.WriteLine($"1. Día del mes: {fechaNacimiento.ToString("dd")}");
        Console.WriteLine($"2. Día de la semana: {fechaNacimiento.ToString("dddd")}");
        Console.WriteLine($"3. Fecha corta: {fechaNacimiento.ToString("d")}");
        Console.WriteLine($"4. Fecha larga: {fechaNacimiento.ToString("D")}");
        Console.WriteLine($"5. Día y mes: {fechaNacimiento.ToString("M")}");
        Console.WriteLine($"6. Mes en dos dígitos: {fechaNacimiento.ToString("MM")}");
        Console.WriteLine($"7. Nombre del mes: {fechaNacimiento.ToString("MMMM")}");
        Console.WriteLine($"8. Hora minutos y segundos {fechaNacimiento.ToString("hh:m:ss")}");
        Console.WriteLine($"9. Año a dos dígitos: {fechaNacimiento.ToString("yy")}");
        Console.WriteLine($"10. Año a cuatro dígitos: {fechaNacimiento.ToString("yyyy")}");
    }   
}