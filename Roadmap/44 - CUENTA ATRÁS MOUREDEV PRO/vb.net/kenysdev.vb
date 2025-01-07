' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 44 CUENTA ATRÁS MOUREDEV PRO
' ------------------------------------
'* EJERCICIO
'* ¡El 12 de noviembre lanzo mouredev pro!
' * El campus de la comunidad para estudiar programación de
' * una manera diferente: https : //mouredev.pro
' *
' * Crea un programa que funcione como una cuenta atrás.
' *
' * - Al iniciarlo tendrás que indicarle el día, mes, año,
' *   hora, minuto y segundo en el que quieres que finalice.
' * - Deberás transformar esa fecha local a UTC.
' * - La cuenta atrás comenzará y mostrará los días, horas,
' *   minutos y segundos que faltan.
' * - Se actualizará cada segundo y borrará la terminal en
' *   cada nueva representación del tiempo restante.
' * - Una vez finalice, mostrará un mensaje.
' * - Realiza la ejecución, si el lenguaje lo soporta, en
' *   un hilo independiente.

Imports System
Imports System.Threading

Public Class ReverseTimer
    Private ReadOnly _endDate As DateTime
    Private ReadOnly _countdownThread As Thread
    Private _isRunning As Boolean = True

    Public Sub New(endDate As String)
        _endDate = DateTime.Parse(endDate).ToUniversalTime()
        _countdownThread = New Thread(AddressOf RunCountdown)
    End Sub

    Private ReadOnly Property TimeRemaining As TimeSpan
        Get
            Return If(_endDate > DateTime.UtcNow, _endDate - DateTime.UtcNow, TimeSpan.Zero)
        End Get
    End Property

    Private Sub RunCountdown()
        While _isRunning AndAlso TimeRemaining > TimeSpan.Zero
            Console.Clear()
            Console.WriteLine("Tiempo restante:")
            Console.WriteLine(FormatTimeRemaining())

            Thread.Sleep(1000)
        End While

        If TimeRemaining <= TimeSpan.Zero Then
            Console.WriteLine("¡Cuenta atrás finalizada!")
        End If
    End Sub

    Private Function FormatTimeRemaining() As String
        Dim delta = TimeRemaining
        Return $"{delta.Days} dias, {delta.Hours} horas, " &
               $"{delta.Minutes} minutos, {delta.Seconds} segundos."
    End Function

    Public Sub Start()
        _countdownThread.Start()
    End Sub

    Public Sub [Stop]()
        _isRunning = False
        _countdownThread.Join()
    End Sub
End Class

Public Module Program
    Public Sub Main()
        Try
            Dim endDate = "2024-12-31T23:59:59.999999"
            Dim timer = New ReverseTimer(endDate)

            ' Ctrl+C
            AddHandler Console.CancelKeyPress,
                Sub(sender, e)
                    e.Cancel = True
                    timer.Stop()
                End Sub

            timer.Start()

        Catch ex As Exception
            Console.WriteLine($"Error: {ex.Message}")
        End Try
    End Sub
End Module
