' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-------------------------------------------------
'* SOLID: PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)
'-------------------------------------------------
' - Cualquier objeto de una subclase debe comportarse de manera consistente con los objetos de
'   la clase base, cumpliendo con los contratos definidos por la interfaz de la clase base.


Public MustInherit Class ClassBase
    Public MustOverride Sub MethodBase()
End Class

Public Class SubClass1
    Inherits ClassBase

    Public Overrides Sub MethodBase()
        Console.WriteLine("SubClass1")
    End Sub
End Class

Public Class SubClass2
    Inherits ClassBase

    Public Overrides Sub MethodBase()
        Console.WriteLine("SubClass2")
    End Sub
End Class

'__________________________
'* EJERCICIO
'* Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
'* cumplir el LSP.
'* Instrucciones:
'* 1. Crea la clase Vehículo.
'* 2. Añade tres subclases de Vehículo.
'* 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
'* 4. Desarrolla un código que compruebe que se cumple el LSP.

' ____________________________________________________
' Clase Base
Public MustInherit Class Vehicle
    ' Propiedades
    Public ReadOnly Property Brand As String
    Public ReadOnly Property Model As String

    ' Constructor
    Public Sub New(brand As String, model As String)
        Me.Brand = brand
        Me.Model = model
    End Sub

    ' Métodos abstractos
    Public MustOverride Function Accelerate() As String
    Public MustOverride Function Brake() As String
End Class

' ____________________________________________________
' Clase derivadas
Public Class Car
    Inherits Vehicle

    Public Sub New(brand As String, model As String)
        MyBase.New(brand, model)
    End Sub

    Public Overrides Function Accelerate() As String
        Dim properties As String = $"{Brand} - {Model}"
        Return $"Acelerando auto: {properties}"
    End Function

    Public Overrides Function Brake() As String
        Dim properties As String = $"{Brand} - {Model}"
        Return $"Frenando auto: {properties}"
    End Function
End Class

' ____________________________________________________
Class Motorcycle
    Inherits Vehicle

    Public Sub New(brand As String, model As String)
        MyBase.New(brand, model)
    End Sub

    Public Overrides Function Accelerate() As String
        Dim properties As String = $"{Brand} - {Model}"
        Return $"Acelerando Motocicleta: {properties}"
    End Function

    Public Overrides Function Brake() As String
        Dim properties As String = $"{Brand} - {Model}"
        Return $"Frenando Motocicleta: {properties}"
    End Function
End Class

' ____________________________________________________
Public Class Truck
    Inherits Vehicle

    Public Sub New(brand As String, model As String)
        MyBase.New(brand, model)
    End Sub

    Public Overrides Function Accelerate() As String
        Dim properties As String = $"{Brand} - {Model}"
        Return $"Acelerando Camión: {properties}"
    End Function

    Public Overrides Function Brake() As String
        Dim properties As String = $"{Brand} - {Model}"
        Return $"Frenando Camión: {properties}"
    End Function
End Class

' ____________________________________________________
Public Module Program
    Public Sub Main()
        ' Exs 1

        Dim TrySubClass1 As ClassBase = New SubClass1
        Dim TrySubClass2 As ClassBase = New SubClass2

        TrySubClass1.MethodBase()
        TrySubClass2.MethodBase()

        '_____________________________________________
        ' Exs 2

        Dim Car As Vehicle = New Car("Honda", "Civic")
        TestSubClass(Car)

        Dim Motorcycle As Vehicle = New Motorcycle("Kawasaki", "Ninja")
        TestSubClass(Motorcycle)

        Dim Truck As Vehicle = New Truck("Ford", "Raptor")
        TestSubClass(Truck)

    End Sub

    Public Sub TestSubClass(SubClass As Vehicle)
        Console.WriteLine(vbCrLf + "Propiedades:")
        Console.WriteLine($"{SubClass.Brand} - {SubClass.Model}")

        Console.WriteLine(vbCrLf + "Métodos:")
        Console.WriteLine(SubClass.Accelerate())
        Console.WriteLine(SubClass.Brake())
    End Sub
End Module
