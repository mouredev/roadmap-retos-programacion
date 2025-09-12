' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝

' # PILAS Y COLAS
' ---------------
Module Program
    Sub Main(args As String())
        '' Pilas(stack - LIFO):
        '- Sigue el principio LIFO (last in, first out), significa que
        '  el último elemento añadido, es el primero en ser retirado. */

        'Dim myStack As New Stack(Of Integer)()
        Dim myStack As New Stack()
        myStack.Push(111) ' Agregar elemento.
        myStack.Push("Hola")
        myStack.Push(3.14)

        Console.WriteLine($"
        Eliminar y obtener:   {myStack.Pop()}
        Obtener sin eliminar: {myStack.Peek()}
        Total de elementos:   {myStack.Count}
        Verificar si existe:  {myStack.Contains(5)}
        Obtener elementos:    {String.Join(", ", myStack.ToArray())}")

        ' ___________________________________________
        '' Colas (Queue - FIFO):
        '- Estructura de datos que sigue el principio FIFO(First In, First Out)
        '- El primer elemento que se inserta es el primero en ser retirado. */

        'Dim myQueue As New Queue()
        Dim myQueue As New Queue(Of Integer)
        myQueue.Enqueue(1) ' Agregar elemento.
        myQueue.Enqueue(2)
        myQueue.Enqueue(3)

        Console.WriteLine($"
        Eliminar y obtener:   {myQueue.Dequeue()}
        Obtener sin eliminar: {myQueue.Peek()}
        Total de elementos:   {myQueue.Count}
        Verificar si existe:  {myQueue.Contains(5)}
        Obtener elementos:    {String.Join(", ", myQueue.ToArray())}")

        ' Ejercicios:
        ' ____________________________________________
        '1 Ejercicio usando la implementación de pilas:
        'Simula el mecanismo adelante/atrás de un navegador web.
        '- Crea un programa en el que puedas navegar a una página o indicarle que te quieres 
        '  desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
        '- Las palabras "adelante", "atrás" desencadenan esta acción, el resto 
        '  se interpreta como el nombre de una nueva web. */

        ' ____________________________________________
        '2 Ejercicio usando la implementación de Colas:
        'Simula el mecanismo de una impresora compartida.
        '- recibe documentos y los imprime cuando así se le indica.
        '- La palabra "imprimir" imprime un elemento de la cola.
        '- El resto de palabras se interpretan como nombres de documentos.

        Home()

    End Sub

    ReadOnly msgHome As String = "
    ----------------------------------
    Usar: '1' para simulador_navegador.
          '2' para simulador_impresora.
          'Otra tecla' para salir.
    ----------------------------------"
    ReadOnly msgNav As String = "
    ------------------------------------------------
    Usar: '<' para página anterior.
          '>' para página adelante.
          'h' Ver historial completo.
          'x' para salir. 
    Escribir web para agregar:
    ------------------------------------------------"
    ReadOnly msgPrinter As String = "
    ------------------------------------------------
    Usar: 'p' Imprimir.
          'l' Ver documentos pendientes.
          'x' para salir.
    Escribir nombre de documento para enviar a cola: 
    ------------------------------------------------"
    Sub Home()
        Console.WriteLine(msgHome)
        Console.Write("____________" & vbCrLf & "Acción: ")
        Dim action As String = Console.ReadLine()
        Select Case action
            Case "1"
                Dim navManager As New NavigationManager()
                Console.WriteLine(msgNav)
                navManager.SelectAction()
            Case "2"
                Dim queueManager As New PrinterQueueManager()
                Console.WriteLine(msgPrinter)
                queueManager.SelectAction()
            Case Else
                Console.WriteLine("Bye")
        End Select
    End Sub

    Public Class NavigationManager
        Private history As New Stack(Of String)(New String() {"Inicio"})
        Private backHistory As New Stack(Of String)()
        Private forwardHistory As New Stack(Of String)()

        Public Sub SelectAction()
            Console.Write("____________" & vbCrLf & " Acción: ")
            Dim action As String = Console.ReadLine()

            If action.Length > 0 Then
                Select Case action
                    Case "<"
                        Back()
                    Case ">"
                        Forward()
                    Case "x"
                        Home()
                    Case "h"
                        TheHistory()
                    Case Else
                        NewWeb(action)
                End Select
            Else
                Console.WriteLine("Eres muy gracioso xD.")
                SelectAction()
            End If
        End Sub

        Private Sub NewWeb(url As String)
            backHistory.Push(history.Peek())
            forwardHistory.Clear()
            history.Push(url)
            Web(url)
            SelectAction()
        End Sub

        Private Sub Back()
            If backHistory.Count > 0 Then
                forwardHistory.Push(history.Peek())
                history.Push(backHistory.Pop())
                Web(history.Peek())
            Else
                Console.WriteLine("No hay página previa.")
            End If
            SelectAction()
        End Sub

        Private Sub Forward()
            If forwardHistory.Count > 0 Then
                backHistory.Push(history.Peek())
                history.Push(forwardHistory.Pop())
                Web(history.Peek())
            Else
                Console.WriteLine("No hay página siguiente.")
            End If
            SelectAction()
        End Sub

        Private Sub Web(url As String)
            Console.WriteLine($"{backHistory.Count} <-[Actual:{url}]-> {forwardHistory.Count}")
        End Sub

        Private Sub TheHistory()
            If history.Count > 0 Then
                For Each item As String In history
                    Console.WriteLine(item)
                Next
            Else
                Console.WriteLine("Historial vacío.")
            End If
            SelectAction()
        End Sub
    End Class

    '--------------------------------------------------------------------
    Public Class PrinterQueueManager
        Private docQueue As New Queue(Of String)()

        Public Sub SelectAction()
            Console.Write("____________" & vbCrLf & " Acción: ")
            Dim action As String = Console.ReadLine()

            If action.Length > 0 Then
                Select Case action
                    Case "p"
                        PrintDoc()
                    Case "l"
                        QueuePending()
                    Case "x"
                        Home()
                    Case Else
                        SendDoc(action)
                End Select
            Else
                Console.WriteLine("Eres muy gracioso xD.")
                SelectAction()
            End If
        End Sub

        Private Sub PrintDoc()
            If docQueue.Count > 0 Then
                Console.WriteLine($"
            {docQueue.Dequeue()} -> ha sido impreso.
            {docQueue.Count} -> archivos faltantes.")
            Else
                Console.WriteLine("No hay archivos.")
            End If
            SelectAction()
        End Sub

        Private Sub QueuePending()
            If docQueue.Count > 0 Then
                For Each doc As String In docQueue
                    Console.WriteLine(doc)
                Next
            Else
                Console.WriteLine("No hay archivos.")
            End If
            SelectAction()
        End Sub

        Private Sub SendDoc(doc As String)
            docQueue.Enqueue(doc)
            Console.WriteLine("Archivo agregado a cola de impresión.")
            SelectAction()
        End Sub
    End Class
End Module
