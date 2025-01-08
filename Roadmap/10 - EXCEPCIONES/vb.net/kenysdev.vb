' ╔═════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado              ║
' ║ GitHub: https://github.com/Kenysdev ║
' ║ 2024 -  VB.NET                      ║
' ╚═════════════════════════════════════╝
'-----------------------------------------------
'EXCEPCIONES
'-----------------------------------------------
'- Representan una forma de controlar el comportamiento de un programa
'cuando se produce un error.
Module Program
    Sub Main()
        Dim a As Integer = 7
        Dim b As Integer = 0

        ' Capturar excepción
        Try
            Dim r As Integer = a / b
        Catch ex As System.ArithmeticException
            Console.WriteLine("Error de división por cero")
        End Try

        ' Cuando se desconoce el tipo de excepción
        Dim myList() As Integer = {1, 2, 3}
        Try
            Console.WriteLine(myList(7))
        Catch ex As Exception
            Console.WriteLine("Excepción")
        End Try

        ' Saber qué excepción ha ocurrido
        Try
            Dim r As Integer = Integer.Parse("uno") + 2
        Catch ex As Exception
            Console.WriteLine($"Excepción: {ex.GetType()}")
        End Try

        ' Capturar diferentes excepciones
        Try
            'Dim r As Integer = Integer.Parse("uno") + 2
            Dim r As String = 7 + "txt"
        Catch ex As FormatException
            Console.WriteLine("Error al convertir")
        Catch ex As Exception
            Console.WriteLine("Error de tipos")
        End Try

        ' Uso de finally
        ' Se ejecuta siempre, haya o no una excepción.
        Try
            Dim r As Double = a \ b
        Catch ex As Exception
            Console.WriteLine("Excepción")
        Finally
            Console.WriteLine("Bloque finally")
        End Try

        ' Uso de throw para ejecutar una excepción
        'Throw New DivideByZeroException("Error de división")
        'Throw New IndexOutOfRangeException()
        'Throw New InvalidCastException("..")

        ' Definiendo excepcion personalizada
        Try
            Throw New CustomException("Mensaje de error personalizado")
        Catch ex As CustomException
            Console.WriteLine($"Excepción personalizada: {ex.Message}")
        End Try

        ' Ejercicio
        Console.WriteLine(vbCrLf & "___________" & vbCrLf & "Ejercicio:")
        Operation(10, "uno")
        Operation(10, 0)
        Operation(10, 5)
        Operation(10, 2)
    End Sub

    Sub Division(a As Integer, b As Integer)
        If b Mod 2 <> 0 Then
            Throw New OddNumberError()
        Else
            Dim r As Integer = a / b
            Console.WriteLine($"{vbCrLf}- El resultado es: {r}")
        End If
    End Sub

    Sub Operation(a As Integer, b As Object)
        Try
            Division(a, CInt(b))
            Console.WriteLine("- No hubo errores.")
        Catch ex As InvalidCastException
            Console.WriteLine($"{vbCrLf}Error: No se permite texto. -> {ex.GetType()}")
        Catch ex As System.ArithmeticException
            Console.WriteLine($"{vbCrLf}Error: No es posible dividir entre 0. -> {ex.GetType()}")
        Catch ex As OddNumberError
            Console.WriteLine($"{vbCrLf}Error: no dividir entre impares. -> {ex.GetType()}")
        Finally
            Console.WriteLine("- Operación terminada.")
        End Try
    End Sub
End Module
' Heredar clase 
Class CustomException
    Inherits Exception
    Sub New(message As String)
        MyBase.New(message)
    End Sub
End Class

Class OddNumberError
    Inherits Exception
    Sub New()
        MyBase.New()
    End Sub
End Class
