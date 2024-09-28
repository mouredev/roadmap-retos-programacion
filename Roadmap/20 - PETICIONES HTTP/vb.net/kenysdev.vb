' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* PETICIONES HTTP
'-----------------------------------------------

Imports System.Net.Http
Imports System.Text.Json

Module Program
    ' EJERCICIO:
    ' Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
    ' una petición a la web que tú quieras, verifica que dicha petición
    ' fue exitosa y muestra por consola el contenido de la web.

    Private ReadOnly client As New HttpClient()

    Async Function GetUser(userId As Integer) As Task(Of Dictionary(Of String, Object))
        Try
            Dim url As String = $"https://jsonplaceholder.typicode.com/users/{userId}"
            Dim response As HttpResponseMessage = Await client.GetAsync(url)

            If response.IsSuccessStatusCode Then
                Dim json As String = Await response.Content.ReadAsStringAsync()
                Return JsonSerializer.Deserialize(Of Dictionary(Of String, Object))(json)
            Else
                Console.WriteLine($"Id: {userId} No encontrado")
                Console.WriteLine(response.StatusCode)
                Return New Dictionary(Of String, Object)()
            End If
        Catch ex As HttpRequestException
            Console.WriteLine("Error de conexión")
            Return New Dictionary(Of String, Object)()
        End Try
    End Function

    Sub PrintUser(userData As Dictionary(Of String, Object))
        If userData.Count > 0 Then
            Console.WriteLine(
                $"Usuario con id: '{userData("id")}':" & vbCrLf &
                $"Nombre:  {userData("name")}" & vbCrLf &
                $"Usuario: {userData("username")}" & vbCrLf &
                $"Email:   {userData("email")}" & vbCrLf &
                $"Teléfono: {userData("phone")}" & vbCrLf
            )
        End If
    End Sub

    Async Function MainAsync() As Task
        Dim client As New HttpClient()

        Dim u1 = Await GetUser(1)
        PrintUser(u1)

        Dim u2 = Await GetUser(2)
        PrintUser(u2)

        Dim u3 = Await GetUser(777) ' no existente
        PrintUser(u3)

        client.Dispose()
    End Function

    Sub Main()
        MainAsync().Wait()
    End Sub

End Module
