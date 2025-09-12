' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* FECHAS
'-----------------------------------------------
Imports System.Globalization

Module Program
    Sub Main(args As String())
        '* EJERCICIO 1
        '* Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
        '* - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
        '* - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
        '* Calcula cuántos años han transcurrido entre ambas fechas

        Dim currentDateTime As DateTime = DateTime.Now
        Dim birthDate As DateTime = New DateTime(1995, 10, 20, 2, 30, 0)

        Dim difference As TimeSpan = currentDateTime - birthDate
        Dim years As Integer = difference.Days \ 365
        Dim months As Integer = (difference.Days Mod 365) \ 30
        Dim days As Integer = (difference.Days Mod 365) Mod 30

        Console.WriteLine(
            years & " años, " &
            months & " meses y " &
            days & " días"
        )

        '* EJERCICIO 2
        '* Utilizando la fecha de tu cumpleaños, formatéala y muestra su 
        '  resultado de 10 maneras diferentes.

        Console.WriteLine("
        Formatos de fecha:
        -----------------------
        1. Predeterminado -> " & birthDate.ToString() & "
        2. Fecha larga    -> " & birthDate.ToString("D") & "
        3. dd-MM-yyyy     -> " & birthDate.ToString("dd-MM-yyyy") & "
        4. Nombre del mes -> " & birthDate.ToString("MMMM") & "
        5. Mes abreviado  -> " & birthDate.ToString("MMM") & "
        6. Nombre del día -> " & birthDate.ToString("dddd") & "
        7. Día abreviado  -> " & birthDate.ToString("ddd") & "
        8. Hora(24 horas) -> " & birthDate.ToString("HH:mm:ss") & "
        9. Hora(12 horas) -> " & birthDate.ToString(
            "hh:mm tt", CultureInfo.InvariantCulture) & "
        0. Personalizado  -> " & birthDate.ToString(
            "Born on dddd, dd'th of' MMMM yyyy 'at' hh:mm:ss tt"))

    End Sub
End Module
