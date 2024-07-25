' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* ITERACIONES
'-----------------------------------------------

Module Program
    '* EJERCICIO #1:
    '* Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
    '* números del 1 al 10 mediante iteración.
    '*
    '* EJERCICIO #2:
    '* Escribe el mayor número de mecanismos que posea tu lenguaje
    '* para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?

    Sub Main()
        '_____________________________
        Console.WriteLine("(1). for")
        For n As Integer = 1 To 10
            Console.WriteLine(n)
        Next

        '_____________________________
        Console.WriteLine(vbCrLf & "(2). while")
        Dim num As Integer = 1
        While num <= 10
            Console.WriteLine(num)
            num += 1
        End While

        '_____________________________
        Console.WriteLine(vbCrLf & "(3). foreach")
        For Each n As Integer In Enumerable.Range(1, 10)
            Console.WriteLine(n)
        Next

        '_____________________________
        Console.WriteLine(vbCrLf & "(4). do-while")
        Dim nu As Integer = 1
        Do
            Console.WriteLine(nu)
            nu += 1
        Loop While nu <= 10

        '_____________________________
        Console.WriteLine(vbCrLf & "(5). Do Until")
        Dim i As Integer = 0

        Do Until i >= 5
            Console.WriteLine(i)
            i += 1
        Loop

        '_____________________________
        Console.WriteLine(vbCrLf & "(6). LINQ")
        Dim numbers = Enumerable.Range(1, 10).ToList()
        Dim evenNumbers = From x In numbers
                          Where x Mod 2 = 0
                          Select x

        For Each num In evenNumbers
            Console.WriteLine(num)
        Next

        '_____________________________
        Console.WriteLine(vbCrLf & "(7). Iterators yield")
        For Each n As Integer In Nums()
            Console.WriteLine(n)
        Next

    End Sub

    Iterator Function Nums() As IEnumerable(Of Integer)
        For n As Integer = 1 To 10
            Yield n
        Next
    End Function

End Module
