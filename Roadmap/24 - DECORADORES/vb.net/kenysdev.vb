' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* DECORADORES
'-----------------------------------------------

'* EJERCICIO #1:
'* Explora el concepto de "decorador" y muestra cómo crearlo
'* con un ejemplo genérico.

' Interfaz
Public Interface ISayHello
    Sub SayHello(ByVal first_name As String, ByVal last_name As String)
End Interface

' Componente Concreto
Public Class HelloSpeaker
    Implements ISayHello

    Public Sub SayHello(ByVal first_name As String, ByVal last_name As String) Implements ISayHello.SayHello
        Console.WriteLine($"Hola, {first_name} {last_name}!")
    End Sub
End Class

' Decorador Base
Public MustInherit Class DecoratorBase
    Implements ISayHello
    Protected _helloSpeaker As ISayHello

    Public Sub New(ByVal helloSpeaker As ISayHello)
        _helloSpeaker = helloSpeaker
    End Sub

    Public Overridable Sub SayHello(ByVal first_name As String, ByVal last_name As String) Implements ISayHello.SayHello
        _helloSpeaker.SayHello(first_name, last_name)
    End Sub
End Class

' Decorador Concreto
Public Class MyDecorator
    Inherits DecoratorBase

    Public Sub New(ByVal helloSpeaker As ISayHello)
        MyBase.New(helloSpeaker)
    End Sub

    Public Overrides Sub SayHello(ByVal first_name As String, ByVal last_name As String)
        Console.WriteLine("Antes de llamar a la función.")
        MyBase.SayHello(first_name, last_name)
        Console.WriteLine("Después de llamarla.")
    End Sub
End Class

'-----------------------------------------------
'* EJERCICIO #2
'* Utiliza el patrón de diseño "singleton" para representar una clase que
'* haga referencia a la sesión de usuario de una aplicación ficticia.
'* La sesión debe permitir asignar un usuario (id, username, nombre y email),
'* recuperar los datos del usuario y borrar los datos de la sesión.

' Interfaz
Public Interface IFunction
    Sub Execute(ParamArray args As Object())
End Interface

' Componente Concreto
Public Class FunctionComponent
    Implements IFunction
    Private ReadOnly _name As String

    Public Sub New(ByVal name As String)
        _name = name
    End Sub

    Public Sub Execute(ParamArray args As Object()) Implements IFunction.Execute
        Console.WriteLine(vbCrLf + $"La función '{_name}':")
    End Sub
End Class

' Decorador Base
Public MustInherit Class CallCountDecorator
    Implements IFunction
    Protected _function As IFunction
    Protected _calls As Integer

    Public Sub New(ByVal functionComponent As IFunction)
        _function = functionComponent
        _calls = 0
    End Sub

    Public Sub Execute(ParamArray args As Object()) Implements IFunction.Execute
        _calls += 1
        _function.Execute(args)
        Console.WriteLine($"Ha sido llamada {_calls} veces")
    End Sub
End Class

' Decorador Concreto
Public Class CountCallsDecorator
    Inherits CallCountDecorator

    Public Sub New(ByVal functionComponent As IFunction)
        MyBase.New(functionComponent)
    End Sub
End Class

'-----------------------------------------------
Module Program
    Sub Main()
        Console.WriteLine("EJERCICIO #1")

        Dim helloSpeaker As ISayHello = New HelloSpeaker()
        Dim decoratedHelloSpeaker As ISayHello = New MyDecorator(helloSpeaker)
        decoratedHelloSpeaker.SayHello("Zoe", "Roy")

        '-----------------------------------------------
        Console.WriteLine(vbCrLf + "EJERCICIO #2")

        Dim functionA As IFunction = New CountCallsDecorator(New FunctionComponent("A"))
        Dim functionB As IFunction = New CountCallsDecorator(New FunctionComponent("B"))

        functionA.Execute()
        functionA.Execute()
        functionA.Execute()

        functionB.Execute()
        functionB.Execute()

    End Sub
End Module
