' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------------
'* RESCATANDO A MICKEY
'-----------------------------------------------------
' * ¡Disney ha presentado un montón de novedades en su D23! 
' * Pero... ¿Dónde está Mickey?
' * Mickey Mouse ha quedado atrapado en un laberinto mágico 
' * creado por Maléfica.
' * Desarrolla un programa para ayudarlo a escapar.
' * Requisitos:
' * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
' * 2. Los valores de las celdas serán:
' *    - ⬜️ Vacío
' *    - ⬛️ Obstáculo
' *    - 🐭 Mickey
' *    - 🚪 Salida
' * Acciones:
' * 1. Crea una matriz que represente el laberinto (no hace falta
' * que se genere de manera automática).
' * 2. Interactúa con el usuario por consola para preguntarle hacia
' * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
' * 3. Muestra la actualización del laberinto tras cada desplazamiento.
' * 4. Valida todos los movimientos, teniendo en cuenta los límites
' * del laberinto y los obtáculos. Notifica al usuario.
' * 5. Finaliza el programa cuando Mickey llegue a la salida.

Imports System.Text

Module Program
    Sub Main()
        Console.OutputEncoding = Encoding.UTF8
        ' These are the default values. You can change them here.
        Dim config As New Dictionary(Of String, String) From {
            {"title", "RESCUING MICKEY"},
            {"size", "7, 7"},
            {"empty", "⬜️"},
            {"obstacle", "⬛️"},
            {"mouse", "🐭"},
            {"exit", "🚪"}
        }

        Dim maze As New Maze(config)
        Dim game As New Game(config, maze)
        game.Play()
    End Sub
End Module

Class Game
    Private ReadOnly _config As Dictionary(Of String, String)
    Private ReadOnly _maze As Maze

    Public Sub New(config As Dictionary(Of String, String), maze As Maze)
        _config = config
        _maze = maze
    End Sub

    Private Shared Function RestartOrExit(msg As String) As Boolean
        While True
            Console.WriteLine(msg)
            Console.Write("Y/N: ")
            Dim option_ = Console.ReadLine().ToLower()
            Select Case option_
                Case "y"
                    Return True
                Case "n"
                    Return False
                Case Else
                    Console.WriteLine("❌Invalid key.❌")
            End Select
        End While
        Return False
    End Function

    Public Sub Play()
        For Each kvp In _config
            Console.WriteLine($"{kvp.Key}: {kvp.Value}")
        Next

        _maze.Create()
        While True
            _maze.PrintMaze()
            Console.WriteLine("Use the keys: (W, S, A, D)." & vbCrLf & "To restart: R. To exit: 9.")
            Console.Write("Key: ")
            Dim option_ = Console.ReadLine().ToLower()
            Select Case option_
                Case "w"
                    _maze.Up()
                Case "s"
                    _maze.Down()
                Case "d"
                    _maze.Right()
                Case "a"
                    _maze.Left()
                Case "r"
                    If RestartOrExit("😮Do you want to restart?😮") Then
                        _maze.Create()
                    End If
                Case "9"
                    If RestartOrExit("😮Do you want to exit?😮") Then
                        Return
                    End If
                Case Else
                    Console.WriteLine("❌Invalid key.❌")
            End Select

            If _maze.VerifyWin() Then
                Console.WriteLine("🏆Congratulations, you managed to get me out.🏆")
                If RestartOrExit("🤔Do you want to play again?🤔") Then
                    _maze.Create()
                Else
                    Console.WriteLine("Bye")
                    Return
                End If
            End If
        End While
    End Sub
End Class

Class Data
    Protected _config As Dictionary(Of String, String)
    Protected _maze As List(Of List(Of String))
    Protected _positionMouse As Tuple(Of Integer, Integer)
    Protected _exitLocation As Tuple(Of Integer, Integer)
    Protected _width As Integer
    Protected _height As Integer
    Protected _obstacleChar As String
    Protected _emptyChar As String
    Protected _mouseChar As String
    Protected _exitChar As String

    Public Sub New(config As Dictionary(Of String, String))
        _config = config
        _maze = New List(Of List(Of String))
        _positionMouse = New Tuple(Of Integer, Integer)(0, 0)
        _exitLocation = New Tuple(Of Integer, Integer)(0, 0)

        Dim size = config("size").Split(","c)
        _width = Integer.Parse(size(0))
        _height = Integer.Parse(size(1))
        _obstacleChar = _config("obstacle")
        _emptyChar = _config("empty")
        _mouseChar = _config("mouse")
        _exitChar = _config("exit")
    End Sub

    Public Sub PrintMaze()
        Console.WriteLine("--------------------------------------")
        For Each row In _maze
            Console.WriteLine(String.Join("", row))
        Next
        Console.WriteLine("--------------------------------------")
    End Sub
End Class

Class Moves
    Inherits Data

    Public Sub New(config As Dictionary(Of String, String))
        MyBase.New(config)
    End Sub

    Private Sub CanMove(y As Integer, x As Integer, oldY As Integer, oldX As Integer)
        Dim rows = _maze.Count
        Dim cols = _maze(0).Count
        If y < 0 OrElse x < 0 OrElse y >= rows OrElse x >= cols Then
            Console.WriteLine("🚨I can't jump over the edges.🚨")
            Return
        End If

        If _maze(y)(x) = _obstacleChar Then
            Console.WriteLine("🚨You pushed me against the wall.🚨")
            Return
        End If

        _positionMouse = New Tuple(Of Integer, Integer)(y, x)
        Console.WriteLine("✅Correct move.✅")
        _maze(oldY)(oldX) = _emptyChar
        _maze(y)(x) = _mouseChar
    End Sub

    Public Sub Up()
        Dim y = _positionMouse.Item1
        Dim x = _positionMouse.Item2
        CanMove(y - 1, x, oldY:=y, oldX:=x)
    End Sub

    Public Sub Down()
        Dim y = _positionMouse.Item1
        Dim x = _positionMouse.Item2
        CanMove(y + 1, x, oldY:=y, oldX:=x)
    End Sub

    Public Sub Right()
        Dim y = _positionMouse.Item1
        Dim x = _positionMouse.Item2
        CanMove(y, x + 1, oldY:=y, oldX:=x)
    End Sub

    Public Sub Left()
        Dim y = _positionMouse.Item1
        Dim x = _positionMouse.Item2
        CanMove(y, x - 1, oldY:=y, oldX:=x)
    End Sub
End Class

Class Maze
    Inherits Moves

    Public Sub New(config As Dictionary(Of String, String))
        MyBase.New(config)
    End Sub

    Private Sub CreatePaths(x As Integer, y As Integer)
        _maze(y)(x) = _emptyChar
        Dim directions = New List(Of (Integer, Integer)) From {(0, 1), (1, 0), (0, -1), (-1, 0)}
        For Each direction In directions.OrderBy(Function(unused) Guid.NewGuid())
            Dim dx = direction.Item1
            Dim dy = direction.Item2
            Dim nx = x + dx * 2
            Dim ny = y + dy * 2
            If 0 < nx AndAlso nx < _width - 1 AndAlso 0 < ny AndAlso ny < _height - 1 AndAlso _maze(ny)(nx) = _obstacleChar Then
                _maze(y + dy)(x + dx) = _emptyChar
                CreatePaths(nx, ny)
            End If
        Next
    End Sub

    Public Sub Create()
        If _width Mod 2 = 0 Then _width += 1
        If _height Mod 2 = 0 Then _height += 1

        _maze.Clear()
        For i = 0 To _height - 1
            _maze.Add(Enumerable.Repeat(_obstacleChar, _width).ToList())
        Next

        Dim rnd As New Random()
        Dim initialX = rnd.Next(1, _width - 1) Or 1
        Dim initialY = rnd.Next(1, _height - 1) Or 1
        CreatePaths(initialX, initialY)

        _maze(0)(1) = _mouseChar
        _maze(_height - 1)(_width - 2) = _exitChar
        _positionMouse = New Tuple(Of Integer, Integer)(0, 1)
        _exitLocation = New Tuple(Of Integer, Integer)(_height - 1, _width - 2)
    End Sub

    Public Function VerifyWin() As Boolean
        Dim y = _exitLocation.Item1
        Dim x = _exitLocation.Item2
        Return _maze(y)(x) = _mouseChar
    End Function
End Class
