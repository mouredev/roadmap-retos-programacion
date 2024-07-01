' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* SOLID: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
'-----------------------------------------------
'# Se centra en la claridad, la cohesión y la separación de intereses.
'# Cada clase debe tener una única razón para cambiar.
'# Los metodos de una clase deben estar estrechamente relacionadas.

'_______________________________________________
'* EJERCICIO
'* Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
'* Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
'* de forma correcta e incorrecta.

'__________________________
' SIN APLICAR EL PRINCIPIO:
Public Class NoSRP
    Private ReadOnly customers As New List(Of String)()
    Private ReadOnly suppliers As New List(Of String)()

    Public Sub AddCustomer(name As String)
        customers.Add(name)
    End Sub

    Public Sub AddSupplier(name As String)
        suppliers.Add(name)
    End Sub

    Public Sub RemoveCustomer(name As String)
        customers.Remove(name)
    End Sub

    Public Sub RemoveSupplier(name As String)
        suppliers.Remove(name)
    End Sub
End Class

'__________________________
' APLICANDO SRP:
Public Class Customers
    Private ReadOnly customers As New List(Of String)()

    Public Sub Add(name As String)
        customers.Add(name)
    End Sub

    Public Sub Remove(name As String)
        customers.Remove(name)
    End Sub
End Class

Public Class Suppliers
    Private ReadOnly suppliers As New List(Of String)()

    Public Sub Add(name As String)
        suppliers.Add(name)
    End Sub

    Public Sub Remove(name As String)
        suppliers.Remove(name)
    End Sub
End Class
