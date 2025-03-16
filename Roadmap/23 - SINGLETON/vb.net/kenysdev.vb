' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* PATRONES DE DISEÑO: SINGLETON
'-----------------------------------------------

'* EJERCICIO #1:
'* Explora el patrón de diseño "singleton" y muestra cómo crearlo
'* con un ejemplo genérico.

Public Class Singleton

    ' Constructor privado para evitar la instanciación directa.
    Private Sub New()
    End Sub

    ' Propiedad compartida que devuelve la única instancia de la clase.
    Public Shared ReadOnly Property Instance As Singleton = New Singleton()
End Class


'-----------------------------------------------
'* EJERCICIO #2
'* Utiliza el patrón de diseño "singleton" para representar una clase que
'* haga referencia a la sesión de usuario de una aplicación ficticia.
'* La sesión debe permitir asignar un usuario (id, username, nombre y email),
'* recuperar los datos del usuario y borrar los datos de la sesión.

Public Class UserSession
    Private _userId As Integer
    Private _userName As String
    Private _name As String
    Private _email As String

    Private Sub New()
    End Sub

    Public Shared ReadOnly Property Instance As UserSession = New UserSession()

    Public Sub SetUser(userId As Integer, userName As String, name As String, email As String)
        _userId = userId
        _userName = userName
        _name = name
        _email = email
    End Sub

    Public Function GetUser() As Dictionary(Of String, Object)
        Dim userDetails As New Dictionary(Of String, Object) From {
            {"id", _userId},
            {"username", _userName},
            {"name", _name},
            {"email", _email}
        }
        Return userDetails
    End Function

    Public Sub Logout()
        _userId = 0
        _userName = Nothing
        _name = Nothing
        _email = Nothing
    End Sub
End Class

'-----------------------------------------------
Module Program

    Sub Main()
        Console.WriteLine("EJERCICIO #1")
        Dim singleton1 As Singleton = Singleton.Instance
        ' singleton2 accede a la misma instancia que singleton1.
        Dim singleton2 As Singleton = Singleton.Instance

        ' Comprobación de igualdad de referencias.
        Console.WriteLine(singleton1 Is singleton2)

        '-----------------------------------------------
        Console.WriteLine("EJERCICIO #2")
        Dim login_user1 As UserSession = UserSession.Instance
        login_user1.SetUser(1, "Zoe_1", "Zoe", "Zoe@gm.com")
        Dim userDetails1 As Dictionary(Of String, Object) = login_user1.GetUser()
        For Each kvp In userDetails1
            Console.WriteLine($"{kvp.Key}: {kvp.Value}")
        Next

        login_user1.Logout()

        Dim login_user2 As UserSession = UserSession.Instance
        login_user2.SetUser(2, "Ben_1", "Ben", "Ben@gm.com")
        Dim userDetails2 As Dictionary(Of String, Object) = login_user2.GetUser()
        For Each kvp In userDetails2
            Console.WriteLine($"{kvp.Key}: {kvp.Value}")
        Next

        login_user2.Logout()

    End Sub

End Module
