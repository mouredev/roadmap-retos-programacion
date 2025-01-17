' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 39 BATMAN DAY
' ------------------------------------

Public Class BatmanDay
    '__________________________________________________________________________
    '* RETO 1:
    '* Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
    '* su 100 aniversario.

    Private Shared Function ThirdSaturdayOfSeptember(year As Integer) As String
        Dim [date] = New DateTime(year, 9, 15)
        Dim daysToAdd = (CInt(DayOfWeek.Saturday) - CInt([date].DayOfWeek) + 7) Mod 7
        [date] = [date].AddDays(daysToAdd)
        Return [date].ToString("dd-MM-yyyy")
    End Function

    Public Shared Sub CalculateAnniversaryDates(totalAnniversaries As Integer)
        Console.WriteLine("Batman Day")
        Const batmanDayStart As Integer = 2014
        Dim currentYear As Integer = DateTime.Today.Year

        If currentYear < batmanDayStart Then
            Console.WriteLine("xd")
            Return
        End If

        Dim pastAnniversaries As Integer = currentYear - batmanDayStart
        Console.WriteLine($"Aniversarios que ya han pasado: {pastAnniversaries}")

        For i As Integer = 0 To totalAnniversaries - pastAnniversaries - 1
            Dim num As Integer = pastAnniversaries + i + 1
            Dim theDate As String = ThirdSaturdayOfSeptember(currentYear)
            Console.WriteLine($"- Aniversario #{num}: {theDate}")
            currentYear += 1
        Next
    End Sub

    '__________________________________________________________________________
    '* RETO 2
    '* Crea un programa que implemente el sistema de seguridad de la Batcueva. 
    '* Este sistema está diseñado para monitorear múltiples sensores distribuidos
    '* por Gotham, detectar intrusos y activar respuestas automatizadas. 
    '* Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
    '* que procese estos datos para tomar decisiones estratégicas.
    '* Requisitos:
    '* - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
    '* - Cada sensor se identifica con una coordenada (x, y) y un nivel
    '*   de amenaza entre 0 a 10 (número entero).
    '* - Batman debe concentrar recursos en el área más crítica de Gotham.
    '* - El programa recibe un listado de tuplas representando coordenadas de los 
    '*   sensores y su nivel de amenaza. El umbral de activación del protocolo de
    '*   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
    '* Acciones: 
    '* - Identifica el área con mayor concentración de amenazas
    '*   (sumatorio de amenazas en una cuadrícula 3x3).
    '* - Si el sumatorio de amenazas es mayor al umbral, activa el 
    '*   protocolo de seguridad.
    '* - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
    '*   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
    '* - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
    '*   sus amenazas, la distancia a la Batcueva y si se debe activar el
    '*   protocolo de seguridad.

    Private Shared Function CreateMap(size As (Integer, Integer), batcave As (Integer, Integer),
                                    sensors As List(Of (Integer, Integer, Integer)),
                                    threats As List(Of (Integer, Integer))) As String(,)
        Dim gotham(size.Item1 - 1, size.Item2 - 1) As String

        For i As Integer = 0 To size.Item1 - 1
            For j As Integer = 0 To size.Item2 - 1
                gotham(i, j) = "| "
            Next
        Next

        gotham(batcave.Item1, batcave.Item2) = "|B"

        For Each s In sensors
            gotham(s.Item1, s.Item2) = "|S"
        Next

        For Each t In threats
            gotham(t.Item1, t.Item2) = "|T"
        Next

        Return gotham
    End Function

    Private Shared Sub PrintMap(gotham As String(,), size As (Integer, Integer))
        Console.WriteLine(vbCrLf & "Mapa de Gotham:")

        For i As Integer = 0 To size.Item1 - 1
            For j As Integer = 0 To size.Item2 - 1
                Console.Write(gotham(i, j))
            Next
            Console.WriteLine()
        Next
    End Sub

    Private Shared Sub ScanMap(gotham As String(,), sensors As List(Of (Integer, Integer, Integer)), size As (Integer, Integer))
        Dim dangerList As New List(Of (Integer, Integer))

        For c As Integer = 0 To sensors.Count - 1
            Dim s = sensors(c)
            Dim dangerCounter As Integer = 0

            For i As Integer = s.Item1 - 1 To s.Item1 + 1
                For j As Integer = s.Item2 - 1 To s.Item2 + 1
                    If i >= 0 AndAlso i < size.Item1 AndAlso j >= 0 AndAlso j < size.Item2 AndAlso gotham(i, j) = "|T" Then
                        dangerCounter += s.Item3
                    End If
                Next
            Next

            dangerList.Add((c, dangerCounter))
        Next

        Dim maxDanger = dangerList.MaxBy(Function(x) x.Item2)
        Dim location = sensors(maxDanger.Item1)

        Console.WriteLine(vbCrLf & "Informe:")
        Console.WriteLine($"Cuadrícula más amenazada: '{location.Item1}, {location.Item2}'")
        Console.WriteLine($"Máximo nivel de alerta: '{maxDanger.Item2}'")

        If maxDanger.Item2 >= 20 Then
            Console.WriteLine("Protocolo de seguridad activado.")
            Console.WriteLine($"Distancia: '{location.Item1 + location.Item2}'")
        Else
            Console.WriteLine("No hay amenazas relevantes.")
        End If
    End Sub

    Public Shared Sub Main()
        ' Reto 1
        CalculateAnniversaryDates(100)

        ' Reto 2
        Dim size = (20, 20)
        Dim batcave = (0, 0)
        Dim sensors As New List(Of (Integer, Integer, Integer)) From {
            (2, 2, 10), (6, 8, 9), (10, 12, 8), (17, 15, 7)
        }
        Dim threats As New List(Of (Integer, Integer)) From {
            (2, 3), (2, 1), (6, 9), (17, 16), (15, 4)
        }

        Dim gotham = CreateMap(size, batcave, sensors, threats)
        PrintMap(gotham, size)
        ScanMap(gotham, sensors, size)
    End Sub

End Class
