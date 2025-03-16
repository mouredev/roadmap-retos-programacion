' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
'-----------------------------------------------
'- Una entidad de software que está abierta a extensión, pero cerrada a modificación, 
'  esto significa que debemos poder extender el comportamiento de una clase sin 
'  necesidad de modificar su código fuente original.

'_______________________________________________
'* EJERCICIO #1
'* Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
'* y crea un ejemplo simple donde se muestre su funcionamiento
'* de forma correcta e incorrecta.

Public MustInherit Class Product
    Public Property Name As String
    Public Property Price As Decimal

    Public Sub New(name As String, price As Decimal)
        Me.Name = name
        Me.Price = price
    End Sub

    Public MustOverride Function ApplyDiscount() As Decimal

    Public Function FinalPrice() As Decimal
        Return Price - ApplyDiscount()
    End Function
End Class

' Extensión
Public Class ElectronicsProduct
    Inherits Product

    Public Sub New(name As String, price As Decimal)
        MyBase.New(name, price)
    End Sub

    Public Overrides Function ApplyDiscount() As Decimal
        Return Price * 0.05D ' Descuento del 5%
    End Function
End Class

' Extensión
Public Class ClothingProduct
    Inherits Product

    Public Sub New(name As String, price As Decimal)
        MyBase.New(name, price)
    End Sub

    Public Overrides Function ApplyDiscount() As Decimal
        If Price > 50 Then
            Return 10
        Else
            Return 0
        End If
    End Function
End Class

'__________________________
'* EJERCICIO #2
'* Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
'* Requisitos:
'* - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
'* Instrucciones:
'* 1. Implementa las operaciones de suma, resta, multiplicación y división.
'* 2. Comprueba que el sistema funciona.
'* 3. Agrega una quinta operación para calcular potencias.
'* 4. Comprueba que se cumple el OCP.

Public MustInherit Class Calculator
    Protected a As Double
    Protected b As Double

    Public Sub New(a As Double, b As Double)
        Me.a = a
        Me.b = b
    End Sub

    Public MustOverride Function MathOperation() As Double

    Public Sub PrintResult()
        Console.WriteLine($"Es: {MathOperation()}")
    End Sub
End Class

Public Class Sum
    Inherits Calculator

    Public Sub New(a As Double, b As Double)
        MyBase.New(a, b)
    End Sub

    Public Overrides Function MathOperation() As Double
        Console.WriteLine($"Suma de {a} + {b}:")
        Return a + b
    End Function
End Class

Public Class Subtraction
    Inherits Calculator

    Public Sub New(a As Double, b As Double)
        MyBase.New(a, b)
    End Sub

    Public Overrides Function MathOperation() As Double
        Console.WriteLine($"Resta de {a} - {b}:")
        Return a - b
    End Function
End Class

Public Class Multiplication
    Inherits Calculator

    Public Sub New(a As Double, b As Double)
        MyBase.New(a, b)
    End Sub

    Public Overrides Function MathOperation() As Double
        Console.WriteLine($"Multiplicación de {a} * {b}:")
        Return a * b
    End Function
End Class

Public Class Division
    Inherits Calculator

    Public Sub New(a As Double, b As Double)
        MyBase.New(a, b)
    End Sub

    Public Overrides Function MathOperation() As Double
        Console.WriteLine($"División de {a} / {b}:")
        If b <> 0 Then
            Return a / b
        Else
            Throw New ArgumentException("DivisionErrorbyZero.")
        End If
    End Function
End Class

' Extensión
Public Class Pow
    Inherits Calculator

    Public Sub New(a As Double, b As Double)
        MyBase.New(a, b)
    End Sub

    Public Overrides Function MathOperation() As Double
        Console.WriteLine($"Potencia de {a} ^ {b}:")
        Return Math.Pow(a, b)
    End Function
End Class


'__________________________
Public Module Program
    Public Sub ProcessProduct(product As Product)
        Console.WriteLine($"Producto: {product.Name}, Precio final: {product.FinalPrice()}")
    End Sub

    Public Sub Main()
        Dim laptop As New ElectronicsProduct("Laptop", 700)
        Dim pants As New ClothingProduct("Pants", 55D)

        ProcessProduct(laptop)
        ProcessProduct(pants)

        '__________________________________________________
        ' exs 2
        Dim Sum As New Sum(2, 2)
        Sum.PrintResult()

        Dim Subtraction As New Subtraction(2, 2)
        Subtraction.PrintResult()

        Dim Multiplication As New Multiplication(2, 2)
        Multiplication.PrintResult()

        Dim Division As New Division(2, 2)
        Division.PrintResult()

        Dim Pow As New Pow(2, 2)
        Pow.PrintResult()

    End Sub
End Module
