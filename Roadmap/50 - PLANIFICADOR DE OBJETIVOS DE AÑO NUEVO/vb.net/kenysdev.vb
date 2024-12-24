' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 50 PLANIFICADOR DE OBJETIVOS DE AÑO NUEVO
' ------------------------------------
'* EJERCICIO
' * El nuevo año está a punto de comenzar...
' * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
' *
' * Programa un gestor de objetivos con las siguientes características:
' * - Permite añadir objetivos (máximo 10)
' * - Calcular el plan detallado
' * - Guardar la planificación
' * 
' * Cada entrada de un objetivo está formado por (con un ejemplo):
' * - Meta: Leer libros
' * - Cantidad: 12
' * - Unidades: libros
' * - Plazo (en meses): 12 (máximo 12)
' *
' * El cálculo del plan detallado generará la siguiente salida:
' * - Un apartado para cada mes
' * - Un listado de objetivos calculados a cumplir en cada mes
' *   (ejemplo: si quiero leer 12 libros, dará como resultado 
' *   uno al mes)
' * - Cada objetivo debe poseer su nombre, la cantidad de
' *   unidades a completar en cada mes y su total. Por ejemplo:
' *
' *   Enero:
' *   [ ] 1. Leer libros (1 libro/mes). Total 12.
' *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
' *   Febrero:
' *   [ ] 1. Leer libros (1 libro/mes). Total 12.
' *   ...
' *   Diciembre:
' *   [ ] 1. Leer libros (1 libro/mes). Total 12.
' *
' * - Si la duración es menor a un año, finalizará en el mes
' *   correspondiente.
' *   
' * Por último, el cálculo detallado debe poder exportarse a .txt
' * (No subir el fichero)

Imports System
Imports System.IO
Imports System.Collections.Generic
Imports System.Globalization

Public Class ObjectivePlanner
    Private ReadOnly goals As New List(Of Dictionary(Of String, Object))
    Private ReadOnly months As List(Of String)
    Private ReadOnly pendingMonthly As New Dictionary(Of Integer, List(Of Integer))

    Public Sub New()
        months = Enumerable.Range(1, 12).[Select](Function(m) DateTimeFormatInfo.CurrentInfo.GetMonthName(m)).ToList()
        goals = New List(Of Dictionary(Of String, Object))
        pendingMonthly = New Dictionary(Of Integer, List(Of Integer))
    End Sub

    Private Sub Add()
        If goals.Count >= 10 Then
            Console.WriteLine(vbLf & "Máximo de 10 objetivos alcanzado.")
            Return
        End If

        Try
            Console.Write("Meta: ")
            Dim name As String = Console.ReadLine().Trim()

            Console.Write("Cantidad: ")
            Dim quantity As Integer = Integer.Parse(Console.ReadLine())

            Console.Write("Unidades: ")
            Dim units As String = Console.ReadLine().Trim()

            Console.Write("Plazo (en meses): ")
            Dim monthCount As Integer = Math.Min(Integer.Parse(Console.ReadLine()), 12)

            If Not String.IsNullOrEmpty(name) AndAlso quantity > 0 AndAlso
               Not String.IsNullOrEmpty(units) AndAlso monthCount > 0 Then

                Dim goal As New Dictionary(Of String, Object) From {
                    {"name", name},
                    {"quantity", quantity},
                    {"units", units},
                    {"months", monthCount}
                }

                Dim goalId As Integer = goals.Count
                goals.Add(goal)

                Dim monthly As Integer = quantity \ monthCount
                Dim extra As Integer = quantity Mod monthCount

                pendingMonthly(goalId) = Enumerable.Range(0, monthCount).[Select](
                    Function(m) monthly + If(m < extra, 1, 0)).ToList()

                Console.WriteLine(vbLf & "Objetivo añadido exitosamente.")
            Else
                Console.WriteLine(vbLf & "Datos inválidos.")
            End If

        Catch ex As FormatException
            Console.WriteLine(vbLf & "Error: Ingrese valores numéricos válidos.")
        End Try
    End Sub

    Private Function CalculatePlan() As Dictionary(Of String, List(Of String))
        If goals.Count = 0 Then Return Nothing

        Dim plan As New Dictionary(Of String, List(Of String))

        For goalId As Integer = 0 To goals.Count - 1
            Dim goal As Dictionary(Of String, Object) = goals(goalId)
            Dim monthlyQuantities As List(Of Integer) = pendingMonthly(goalId)

            For month As Integer = 0 To monthlyQuantities.Count - 1
                Dim quantity As Integer = monthlyQuantities(month)
                If quantity > 0 Then
                    Dim monthName As String = months(month)

                    Dim value As List(Of String) = Nothing

                    If Not plan.TryGetValue(monthName, value) Then
                        value = New List(Of String)
                        plan(monthName) = value
                    End If

                    value.Add(
                        $"[ ] {goal("name")} ({quantity} {goal("units")}/mes). " &
                        $"Total: {goal("quantity")}.")
                End If
            Next
        Next

        Return plan.Where(Function(kvp) kvp.Value.Count > 0).
               ToDictionary(Function(kvp) kvp.Key, Function(kvp) kvp.Value)
    End Function

    Private Shared Sub SavePlan(plan As Dictionary(Of String, List(Of String)))
        If plan Is Nothing Then
            Console.WriteLine(vbLf & "No hay planificación para guardar.")
            Return
        End If

        Dim filename As String = $"plan_{DateTime.Now:yyyyMMdd_HHmm}.txt"
        Try
            Using writer As New StreamWriter(filename, False, Text.Encoding.UTF8)
                For Each kvp In plan
                    writer.WriteLine($"{kvp.Key}:")
                    For Each task In kvp.Value
                        writer.WriteLine($"  {task}")
                    Next
                    writer.WriteLine()
                Next
            End Using

            Console.WriteLine(vbLf & $"Plan guardado en {filename}.")

        Catch ex As IOException
            Console.WriteLine(vbLf & "Error al guardar el archivo.")
        End Try
    End Sub

    Private Sub DisplayPlan()
        Dim plan As Dictionary(Of String, List(Of String)) = CalculatePlan()
        If plan IsNot Nothing Then
            For Each kvp In plan
                Console.WriteLine(vbLf & $"{kvp.Key}:")
                For Each task In kvp.Value
                    Console.WriteLine($"  {task}")
                Next
            Next
        End If
    End Sub

    Public Sub Run()
        Console.Clear()

        While True
            Console.WriteLine(vbLf & "Gestor de Objetivos:")
            Console.WriteLine("1. Añadir objetivo")
            Console.WriteLine("2. Calcular plan detallado")
            Console.WriteLine("3. Guardar planificación")
            Console.WriteLine("4. Salir")

            Console.Write(vbLf & "Seleccione una opción: ")
            Dim option_ As String = Console.ReadLine().Trim()

            Select Case option_
                Case "1"
                    Add()
                Case "2"
                    DisplayPlan()
                Case "3"
                    SavePlan(CalculatePlan())
                Case "4"
                    Console.WriteLine(vbLf & "¡Adiós!")
                    Return
                Case Else
                    Console.WriteLine(vbLf & "Opción inválida.")
            End Select
        End While
    End Sub
End Class

Public Module Program
    Public Sub Main()
        Dim planner As New ObjectivePlanner()
        planner.Run()
    End Sub
End Module
