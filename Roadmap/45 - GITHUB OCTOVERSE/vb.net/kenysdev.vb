' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 45 GITHUB OCTOVERSE
' ------------------------------------
'* EJERCICIO:
'* GitHub ha publicado el Octoverse 2024, el informe
'* anual del estado de la plataforma:
'* https://octoverse.github.com
'*
'* Utilizando el API de GitHub, crea un informe asociado
'* a un usuario concreto.
'* 
'* - Se debe poder definir el nombre del usuario
'*   sobre el que se va a generar el informe.
'*   
'* - Crea un informe de usuario basándote en las 5 métricas
'*   que tú quieras, utilizando la informración que te
'*   proporciona GitHub. Por ejemplo:
'*   - Lenguaje más utilizado
'*   - Cantidad de repositorios
'*   - Seguidores/Seguidos
'*   - Stars/forks
'*   - Contribuciones
'*   (lo que se te ocurra)

Imports System.Net.Http
Imports System.Text.Json

Public Class GitHubApi
    Private ReadOnly _client As New HttpClient()
    Private _userData As Dictionary(Of String, JsonElement)

    Public Sub New(userName As String)
        _userData = GetUserDataAsync(userName).Result
    End Sub

    Private Async Function GetUserDataAsync(userName As String) As Task(Of Dictionary(Of String, JsonElement))
        Try
            _client.DefaultRequestHeaders.Add("User-Agent", "Mozilla/5.0")
            Dim response = Await _client.GetStringAsync($"https://api.github.com/users/{userName}")
            Return JsonSerializer.Deserialize(Of Dictionary(Of String, JsonElement))(response)
        Catch ex As HttpRequestException
            Console.WriteLine($"Error: {ex.Message}")
            Return New Dictionary(Of String, JsonElement)()
        End Try
    End Function

    Private Function VerifyStatus() As Boolean
        Dim status As JsonElement
        If _userData.TryGetValue("message", status) AndAlso status.GetString() = "Not Found" Then
            Console.WriteLine("Usuario no encontrado.")
            Return False
        End If
        Return True
    End Function

    Private Function GetRepoInfo(repo As JsonElement) As String
        Dim name As JsonElement
        Dim lang As JsonElement
        Dim stars As JsonElement
        Dim forks As JsonElement

        Return $"Lang: {If(repo.TryGetProperty("language", lang), lang.GetString(), "Desconocido")}
Repo: {If(repo.TryGetProperty("full_name", name), name.GetString(), "Desconocido")}
Stars: {If(repo.TryGetProperty("stargazers_count", stars), stars.GetInt32(), 0)}
Forks: {If(repo.TryGetProperty("forks_count", forks), forks.GetInt32(), 0)}"
    End Function

    Public Sub PrintBasicInfo()
        If Not VerifyStatus() Then Return

        Dim name As JsonElement
        Dim created As JsonElement
        Dim repos As JsonElement
        Dim gists As JsonElement
        Dim followers As JsonElement
        Dim following As JsonElement

        Console.WriteLine($"-------------------------------------------
Nombre: {If(_userData.TryGetValue("name", name), name.GetString(), "Desconocido")}
Creación: {If(_userData.TryGetValue("created_at", created), created.GetString(), "Desconocido")}
Repos: {If(_userData.TryGetValue("public_repos", repos), repos.GetInt32(), 0)}
Gists: {If(_userData.TryGetValue("public_gists", gists), gists.GetInt32(), 0)}
Seguidores: {If(_userData.TryGetValue("followers", followers), followers.GetInt32(), 0)}
Seguidos: {If(_userData.TryGetValue("following", following), following.GetInt32(), 0)}
-------------------------------------------")
    End Sub

    Public Async Function PrintReposInfoAsync() As Task
        If Not VerifyStatus() Then Return

        Dim reposUrl As JsonElement
        If _userData.TryGetValue("repos_url", reposUrl) Then
            Dim reposResponse = Await _client.GetStringAsync(reposUrl.GetString())
            Dim repos = JsonSerializer.Deserialize(Of List(Of JsonElement))(reposResponse)

            Dim languages As New Dictionary(Of String, Integer)()
            Console.WriteLine("Repositorios publicos:")

            For Each repo In repos
                Console.WriteLine(vbCrLf + GetRepoInfo(repo))

                Dim language As JsonElement
                If repo.TryGetProperty("language", language) Then
                    Dim lang = language.GetString()
                    If Not String.IsNullOrEmpty(lang) Then
                        If languages.ContainsKey(lang) Then
                            languages(lang) += 1
                        Else
                            languages(lang) = 1
                        End If
                    End If
                End If
            Next

            Dim mostUsedLang = languages.OrderByDescending(Function(x) x.Value).FirstOrDefault()
            Console.WriteLine(vbCrLf + $"Total de repositorios: '{repos.Count}'")
            Console.WriteLine($"El lenguaje más utilizado: '{mostUsedLang.Key}'({mostUsedLang.Value})")
        End If
    End Function

    Public Shared Sub Main()
        Console.WriteLine("Informe sobre los datos del usuario en GitHub")
        Console.Write("Usuario: ")
        Dim userName = Console.ReadLine()

        Task.Run(Async Function()
                     Dim github = New GitHubApi(userName)
                     Await github.PrintReposInfoAsync()
                     github.PrintBasicInfo()
                 End Function).GetAwaiter().GetResult()
    End Sub
End Class
