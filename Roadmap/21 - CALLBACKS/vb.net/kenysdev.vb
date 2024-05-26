' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* CALLBACKS
'-----------------------------------------------

Module Program
    '* EJERCICIO #1
    '* Explora el concepto de callback en tu lenguaje creando un ejemplo
    '* simple (a tu elección) que muestre su funcionamiento.

    Delegate Sub CallbackDelegate(summands As String, result As Integer)

    Sub SumNumbers(a As Integer, b As Integer, callback As CallbackDelegate)
        Dim result As Integer = a + b
        callback($"{a} + {b}", result)
    End Sub

    Sub MyCallback(summands As String, result As Integer)
        Console.WriteLine($"La suma de {summands} es: {result}")
    End Sub

    '* EJERCICIO #2
    '* Crea un simulador de pedidos de un restaurante utilizando callbacks.
    '* Estará formado por una función que procesa pedidos.
    '* Debe aceptar el nombre del plato, una callback de confirmación, una
    '* de listo y otra de entrega.
    '* - Debe imprimir un confirmación cuando empiece el procesamiento.
    '* - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
    '*   procesos.
    '* - Debe invocar a cada callback siguiendo un orden de procesado.
    '* - Debe notificar que el plato está listo o ha sido entregado.

    Async Function ProcessOrder(name As String, confirm As Func(Of String, Task),
                                prepare As Func(Of String, Task),
                                serving As Func(Of String, Task)) As Task
        Console.WriteLine($"-----{vbCrLf}* Procesando: '{name}'{vbCrLf}-----{vbCrLf}")
        Await confirm(name)
        Await prepare(name)
        Await serving(name)
    End Function

    Function TimeRandom() As Integer
        Dim random As New Random()
        Return random.Next(1, 11)
    End Function

    Async Function ConfirmOrder(ByVal name As String) As Task
        Dim time As Integer = TimeRandom()
        Console.WriteLine($"* Confirmando {name}, espere {time} segundos.")
        Await Task.Delay(time * 1000)
        Console.WriteLine($"- '{name}', ha sido confirmado.{vbCrLf}")
    End Function

    Async Function PrepareOrder(ByVal name As String) As Task
        Dim time As Integer = TimeRandom()
        Console.WriteLine($"* Preparando, espere {time} segundos.")
        Await Task.Delay(time * 1000)
        Console.WriteLine($"- '{name}', esta Listo.{vbCrLf}")
    End Function

    Async Function ServingOrder(ByVal name As String) As Task
        Dim time As Integer = TimeRandom()
        Console.WriteLine($"* Sirviendo, espere {time} segundos.")
        Await Task.Delay(time * 1000)
        Console.WriteLine($"- '{name}', ha sido entregado.{vbCrLf}")
    End Function

    Async Function Order(ByVal dishName As String) As Task
        Await ProcessOrder(dishName, AddressOf ConfirmOrder, AddressOf PrepareOrder, AddressOf ServingOrder)
    End Function

    Async Function OrdersList() As Task
        Await Order("Baleadas")
        Await Order("Tamales")
        Await Order("Enchiladas")
    End Function

    Sub Main()
        Console.WriteLine("EJERCICIO #1")
        SumNumbers(6, 6, AddressOf MyCallback)
        SumNumbers(5, 2, AddressOf MyCallback)

        Console.WriteLine(vbCrLf & "EJERCICIO #2")
        OrdersList().Wait()
    End Sub

End Module
