' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* ENUMERACIONES
'-----------------------------------------------
' https://learn.microsoft.com/es-es/dotnet/visual-basic/language-reference/statements/enum-statement
' https://learn.microsoft.com/es-es/dotnet/api/system.enum?view=net-8.0


Module Program

    Enum Weekday
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7
    End Enum

    Function GetDay(ByVal num As Integer) As String
        Dim name As String = [Enum].GetName(GetType(Weekday), num)
        If name IsNot Nothing Then
            Return name
        Else
            Return "'o'"
        End If
    End Function

    Function GetNumDay(ByVal day As String) As Integer
        Dim weekday As Weekday
        If [Enum].TryParse(day, weekday) Then
            Return CType(weekday, Integer)
        Else
            Return 0
        End If
    End Function

    Enum Status
        PENDING
        SHIPPED
        DELIVERED
        CANCELED
    End Enum

    Class Order
        Private _identifier As String
        Private _status As Status = Status.PENDING

        Public Sub New(ByVal identifier As String)
            _identifier = identifier
        End Sub

        Public Sub Send()
            Console.WriteLine(vbCrLf & "Enviar:")
            If _status = Status.PENDING Then
                _status = Status.SHIPPED
                Console.WriteLine(Info())
            Else
                Invalid()
            End If
        End Sub

        Public Sub Cancelled()
            Console.WriteLine(vbCrLf & "Cancelar:")
            If _status = Status.PENDING Then
                _status = Status.CANCELED
                Console.WriteLine(Info())
            Else
                Invalid()
            End If
        End Sub

        Public Sub Delivered()
            Console.WriteLine(vbCrLf & "Entregar:")
            If _status = Status.SHIPPED Then
                _status = Status.DELIVERED
                Console.WriteLine(Info())
            Else
                Invalid()
            End If
        End Sub

        Public Function Info() As String
            Return $"{_identifier} is {_status}"
        End Function

        Private Sub Invalid()
            Console.WriteLine($"Invalid operation, {Info()}")
        End Sub


    End Class

    Sub Main()
        ' _____________________________________
        Console.WriteLine(GetDay(7))
        Console.WriteLine(GetDay(3))
        Console.WriteLine(GetDay(8))

        Console.WriteLine(GetNumDay("TUESDAY"))
        Console.WriteLine(GetNumDay("FRIDAY"))
        Console.WriteLine(GetNumDay("abc"))

        ' _____________________________________
        ' Creación de pedidos
        Dim libro1 As New Order("libro1")
        Dim libro2 As New Order("libro2")
        Dim libro3 As New Order("libro3")

        ' Positivas
        Console.WriteLine(vbCrLf & "-----")
        Console.WriteLine("Operaciones exitosas:" & vbCrLf & "-----")
        libro1.Send()
        libro1.Delivered()
        libro2.Cancelled()

        ' Negativas
        Console.WriteLine(vbCrLf & "-----")
        Console.WriteLine("Operaciones inválidas:" & vbCrLf & "-----")
        libro3.Delivered()
        libro2.Cancelled()
        libro1.Send()

        ' Información
        Console.WriteLine(vbCrLf & "-----")
        Console.WriteLine("Estado de órdenes" & vbCrLf & "-----")
        Console.WriteLine(libro1.Info())
        Console.WriteLine(libro2.Info())
        Console.WriteLine(libro3.Info())
    End Sub
End Module
