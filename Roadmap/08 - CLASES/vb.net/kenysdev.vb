' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
Module Program

    ' # CLASES
    ' ------------
    ' - Las clases proporcionan una forma de organizar y estructurar
    '   el código de manera más modular y reutilizable.

    Public Class Person
        ' Propiedades
        Public Name As String
        Public Property Age As Integer

        ' Constructor
        Public Sub New(name As String, age As Integer)
            Me.Name = name
            Me.Age = age
        End Sub

        ' Metodo
        Public Sub Print()
            Console.WriteLine($"Nombre: {Name} - Edad: {Age}")
        End Sub
    End Class

    ' ----------------------------------------
    ' Ejercicio:
    ' ----------------------------------------
    ' - Implementa dos clases que representen las estructuras de Pila y Cola 
    '   (estudiadas en el ejercicio número 7 de la ruta de estudio)
    ' - Deben poder inicializarse y disponer de operaciones para añadir, 
    '   eliminar, retornar el número de elementos e imprimir todo su contenido.
    '_________________________________________
    ' Pilas(stack - LIFO): */
    Public Class MyStack
        Private _stack As New Stack()

        Public Sub Push(item As Object)
            _stack.Push(item)
        End Sub

        Public Function Pop() As Object
            If _stack.Count > 0 Then
                Return _stack.Pop
            Else
                Return Nothing
            End If
        End Function

        Public Function Count() As Integer
            Return _stack.Count
        End Function

        Public Sub Print()
            If _stack.Count > 0 Then
                For Each item In _stack
                    Console.WriteLine(item)
                Next
            End If
        End Sub
    End Class

    '_________________________________________
    'Colas (Queue - FIFO)
    Public Class MyQueue
        Private _queue As New Queue()

        Public Sub Enqueue(item As Object)
            _queue.Enqueue(item)
        End Sub

        Public Function Dequeue() As Object
            If _queue.Count > 0 Then
                Return _queue.Dequeue
            Else
                Return Nothing
            End If
        End Function

        Public Function Count() As Integer
            Return _queue.Count
        End Function

        Public Sub Print()
            If _queue.Count > 0 Then
                For Each item In _queue
                    Console.WriteLine(item)
                Next
            End If
        End Sub
    End Class

    '_________________________________________
    Sub Main()
        Dim Person As New Person("Ben", 21)
        Person.Print()
        Person.Age = 19
        Person.Print()

        '---------------
        Console.WriteLine("Uso de pila:")
        Dim Stack As New MyStack()
        Stack.Push("uno")
        Stack.Push(22222)
        Stack.Push(False)
        Stack.Pop()
        Stack.Print()

        '---------------
        Console.WriteLine("Uso de cola:")
        Dim Queue As New MyQueue()
        Queue.Enqueue("uno")
        Queue.Enqueue(22222)
        Queue.Enqueue(33.33)
        Queue.Dequeue()
        Queue.Print()
    End Sub
End Module
