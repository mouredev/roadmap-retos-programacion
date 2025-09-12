' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 38 MOUREDEV PRO
' ------------------------------------
'* He presentado mi proyecto más importante del año: mouredev pro.
' * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
' * programación de una manera diferente.
' * Cualquier persona suscrita a la newsletter de https://mouredev.pro
' * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
' *
' * Desarrolla un programa que lea los registros de un fichero .csv y
' * seleccione de manera aleatoria diferentes ganadores.
' * Requisitos:
' * 1. Crea un .csv con 3 columnas id, email y status con valor "activo"
' *    o "inactivo" (y datos ficticios).
' *    Ejemplo: 1 | test@test.com | activo
' *             2 | test2@test.com | inactivo
' *    (El .csv no debe subirse como parte de la corrección)
' * 2. Recupera los datos desde el programa y selecciona email aleatorios.
' * Acciones:
' * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
' *    ganador de una suscripción, otro ganador de un descuento y un último
' *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
' * 2. Muestra los emails ganadores y su id.
' * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
' *    no debe tenerse en cuenta.


Imports Microsoft.VisualBasic.FileIO

Module Program
    Sub Main()
        Console.WriteLine("Usuarios ganadores de 'MOUREDEV PRO:'")
        Dim csvFile As String = "users.csv"
        Dim prizes As List(Of String) = New List(Of String) From {"Suscripción", "Descuento", "Libro"}

        Dim entries = ReadCsv(csvFile)
        If entries IsNot Nothing Then
            Dim activeEntries = GetActiveEntries(entries)
            Dim winners = SelectWinners(activeEntries, 3)
            DistributePrizes(winners, prizes)
        Else
            Console.WriteLine("No se encontraron entradas activas.")
        End If
    End Sub

    Private Function ReadCsv(filePath As String) As List(Of Dictionary(Of String, String))
        Try
            Using parser As New TextFieldParser(filePath)
                parser.TextFieldType = FieldType.Delimited
                parser.SetDelimiters(",")

                Dim headers = parser.ReadFields()
                Dim entries As New List(Of Dictionary(Of String, String))

                While Not parser.EndOfData
                    Dim fields = parser.ReadFields()
                    Dim entry As New Dictionary(Of String, String)
                    For i As Integer = 0 To headers.Length - 1
                        entry.Add(headers(i), fields(i))
                    Next
                    entries.Add(entry)
                End While

                Return entries
            End Using
        Catch ex As Exception
            Console.WriteLine($"Error reading '{filePath}': {ex.Message}")
            Return Nothing
        End Try
    End Function

    Private Function GetActiveEntries(entries As List(Of Dictionary(Of String, String))) As List(Of Dictionary(Of String, String))
        Return entries.Where(Function(entry) entry("status").ToLower() = "active").
                       Select(Function(entry) New Dictionary(Of String, String) From {
                           {"id", entry("id")},
                           {"email", entry("email")},
                           {"status", entry("status")}
                       }).ToList()
    End Function

    Private Function SelectWinners(activeEntries As List(Of Dictionary(Of String, String)), numWinners As Integer) As List(Of Dictionary(Of String, String))
        Dim rnd As New Random()
        Return activeEntries.OrderBy(Function(x) rnd.Next()).
                             Take(Math.Min(numWinners, activeEntries.Count)).
                             ToList()
    End Function

    Private Sub DistributePrizes(winners As List(Of Dictionary(Of String, String)), prizes As List(Of String))
        Dim rnd As New Random()
        prizes = prizes.OrderBy(Function(x) rnd.Next()).ToList()

        For i As Integer = 0 To Math.Min(winners.Count, prizes.Count) - 1
            Console.WriteLine($"{prizes(i),-11} -> Id({winners(i)("id")}): {winners(i)("email")}")
        Next
    End Sub
End Module
