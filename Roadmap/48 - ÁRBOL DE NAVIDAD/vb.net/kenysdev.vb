' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 48 ÁRBOL DE NAVIDAD
' ------------------------------------
'* EJERCICIO:
' * ¡Ha comenzado diciembre! Es hora de montar nuestro
' * árbol de Navidad...
' * 
' * Desarrolla un programa que cree un árbol de Navidad
' * con una altura dinámica definida por el usuario por terminal.
' * 
' * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
' * 
' *     *
' *    ***
' *   *****
' *  *******
' * *********
' *    |||
' *    |||
' *
' * El usuario podrá seleccionar las siguientes acciones:
' * 
' * - Añadir o eliminar la estrella en la copa del árbol (@)
' * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
' * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
' * - Apagar (*) o encender (+) las luces (conservando su posición)
' * - Una luz y una bola no pueden estar en el mismo sitio
' *
' * Sólo puedes añadir una estrella, y tantas luces o bolas
' * como tengan cabida en el árbol. El programa debe notificar
' * cada una de las acciones (o por el contrario, cuando no
' * se pueda realizar alguna).

Imports System
Imports System.Threading
Imports System.Collections.Generic

Public Class ChristmasTree
    Private ReadOnly _size As Integer
    Private ReadOnly _matrix(,) As Char
    Private ReadOnly _starRow As Integer
    Private ReadOnly _starCol As Integer
    Private ReadOnly _treeTop As New List(Of Tuple(Of Integer, Integer))
    Private ReadOnly _balls As New List(Of Tuple(Of Integer, Integer))
    Private ReadOnly _lights As New List(Of Tuple(Of Integer, Integer))

    Public Sub New(size As Integer)
        _size = size
        _matrix = New Char(_size - 1, (size * 2) - 2) {}
        _starRow = 0
        _starCol = size - 1

        For i As Integer = 0 To _size - 1
            For j As Integer = 0 To (size * 2) - 2
                _matrix(i, j) = " "c
            Next
        Next
    End Sub

    Public Sub PrintTree()
        Console.WriteLine()
        For i As Integer = 0 To _size - 1
            For j As Integer = 0 To (_size * 2) - 2
                Console.Write(_matrix(i, j))
            Next
            Console.WriteLine()
        Next

        Dim spaces As Integer = (_size * 2 - 4) \ 2
        Console.WriteLine(New String(" "c, spaces) & "|||")
        Console.WriteLine(New String(" "c, spaces) & "|||")
    End Sub

    Public Sub CreateTree()
        Dim center As Integer = _size - 1
        For i As Integer = 0 To _size - 1
            Dim asterisks As New String("*"c, (i * 2) + 1)
            For j As Integer = 0 To asterisks.Length - 1
                Dim col As Integer = center - i + j
                _matrix(i, col) = asterisks(j)
                _treeTop.Add(New Tuple(Of Integer, Integer)(i, col))
            Next
        Next

        _treeTop.RemoveAt(0)
    End Sub

    Public Sub AddRemoveStar()
        If _matrix(_starRow, _starCol) = "*"c Then
            _matrix(_starRow, _starCol) = "@"c
        Else
            _matrix(_starRow, _starCol) = "*"c
        End If
    End Sub

    Public Sub AddBalls()
        If _treeTop.Count < 2 Then
            Console.WriteLine("Ya no hay espacio para poner bolas.")
            Return
        End If

        Dim rnd As New Random()
        Dim positions As New List(Of Tuple(Of Integer, Integer))
        For i As Integer = 0 To 1
            Dim idx As Integer = rnd.Next(_treeTop.Count)
            positions.Add(_treeTop(idx))
            _treeTop.RemoveAt(idx)
        Next

        For Each pos In positions
            _balls.Add(pos)
            _matrix(pos.Item1, pos.Item2) = "o"c
        Next
    End Sub

    Public Sub RemoveBalls()
        If _balls.Count = 0 Then
            Console.WriteLine("No hay bolas que eliminar.")
            Return
        End If

        Dim rnd As New Random()
        Dim positions As New List(Of Tuple(Of Integer, Integer))
        For i As Integer = 0 To 1
            If _balls.Count > 0 Then
                Dim idx As Integer = rnd.Next(_balls.Count)
                positions.Add(_balls(idx))
                _balls.RemoveAt(idx)
            End If
        Next

        For Each pos In positions
            _treeTop.Add(pos)
            _matrix(pos.Item1, pos.Item2) = "*"c
        Next
    End Sub

    Public Sub AddLights()
        If _treeTop.Count < 3 Then
            Console.WriteLine("Ya no hay espacio para poner luces.")
            Return
        End If

        Dim rnd As New Random()
        Dim positions As New List(Of Tuple(Of Integer, Integer))
        For i As Integer = 0 To 2
            Dim idx As Integer = rnd.Next(_treeTop.Count)
            positions.Add(_treeTop(idx))
            _treeTop.RemoveAt(idx)
        Next

        For Each pos In positions
            _lights.Add(pos)
            _matrix(pos.Item1, pos.Item2) = "+"c
        Next
    End Sub

    Public Sub RemoveLights()
        If _lights.Count = 0 Then
            Console.WriteLine("No hay luces que eliminar.")
            Return
        End If

        Dim rnd As New Random()
        Dim positions As New List(Of Tuple(Of Integer, Integer))
        For i As Integer = 0 To 2
            If _lights.Count > 0 Then
                Dim idx As Integer = rnd.Next(_lights.Count)
                positions.Add(_lights(idx))
                _lights.RemoveAt(idx)
            End If
        Next

        For Each pos In positions
            _treeTop.Add(pos)
            _matrix(pos.Item1, pos.Item2) = "*"c
        Next
    End Sub

    Public Sub OnOffLights()
        If _lights.Count = 0 Then
            Console.WriteLine("No hay luces.")
            Return
        End If

        For Each pos In _lights
            If _matrix(pos.Item1, pos.Item2) = "*"c Then
                _matrix(pos.Item1, pos.Item2) = "+"c
            Else
                _matrix(pos.Item1, pos.Item2) = "*"c
            End If
        Next
    End Sub

    Public Sub AutomaticLights()
        While True
            Console.Clear()
            For Each pos In _lights
                If _matrix(pos.Item1, pos.Item2) = "*"c Then
                    _matrix(pos.Item1, pos.Item2) = "+"c
                Else
                    _matrix(pos.Item1, pos.Item2) = "*"c
                End If
            Next
            PrintTree()
            Thread.Sleep(1000)
        End While
    End Sub
End Class

Public Module Program
    Private Const MenuText As String = "
1 - Agregar/Remover estrella.
2 - Agregar bolas.    | 3 - Quitar bolas.
4 - Agregar luces.    | 5 - Quitar luces.
6 - Encender/Apagar luces.
7 - Luces automáticas.| 8 - Salir
"

    Private Sub ShowMenu(tree As ChristmasTree)
        While True
            tree.PrintTree()
            Console.WriteLine(MenuText)
            Console.Write("Opción: ")
            Dim option_ As String = Console.ReadLine()

            Select Case option_
                Case "1"
                    tree.AddRemoveStar()
                Case "2"
                    tree.AddBalls()
                Case "3"
                    tree.RemoveBalls()
                Case "4"
                    tree.AddLights()
                Case "5"
                    tree.RemoveLights()
                Case "6"
                    tree.OnOffLights()
                Case "7"
                    tree.AutomaticLights()
                Case "8"
                    Return
                Case Else
                    Console.WriteLine("Opción inválida.")
            End Select
        End While
    End Sub

    Private Function GetSize() As Integer
        While True
            Console.Write("Tamaño: ")
            Dim sizeStr As String = Console.ReadLine()
            Dim size As Integer

            If Integer.TryParse(sizeStr, size) AndAlso size Mod 2 <> 0 AndAlso size >= 3 Then
                Return size
            End If

            Console.WriteLine("Debe ser un número impar >= 3.")
        End While
        Return 3
    End Function

    Public Sub Main()
        Dim size As Integer = GetSize()
        Dim christmasTree As New ChristmasTree(size)
        christmasTree.CreateTree()
        ShowMenu(christmasTree)
    End Sub
End Module
