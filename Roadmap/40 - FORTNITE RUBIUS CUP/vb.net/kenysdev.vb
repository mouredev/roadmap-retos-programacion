' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 40 FORTNITE RUBIUS CUP
' ------------------------------------
'* EJERCICIO
'* ¡Rubius tiene su propia skin en Fortnite!
'* Y va a organizar una competición para celebrarlo.
'* Esta es la lista de participantes:
'* https//x.com/Rubiu5/status/1840161450154692876
'*
'* Desarrolla un programa que obtenga el número de seguidores en
'* Twitch de cada participante, la fecha de creación de la cuenta 
'* y ordene los resultados en dos listados.
'* - Usa el API de Twitch: https : //dev.twitch.tv/docs/api/reference
'*   (NO subas las credenciales de autenticación)
'* - Crea un ranking por número de seguidores y por antigüedad.
'* - Si algún participante no tiene usuario en Twitch, debe reflejarlo.


Imports System.Net.Http
Imports System.Text.Json
Imports DotNetEnv

Public Class Twitch
    Private ReadOnly clientId As String
    Private ReadOnly clientSecret As String
    Private accessToken As String

    Public Sub New(clientId As String, clientSecret As String)
        Me.clientId = clientId
        Me.clientSecret = clientSecret
    End Sub

    Public Class UserData
        Public Property Username As String
        Public Property CreatedAt As DateTime
        Public Property Followers As Integer
    End Class

    Public Async Function EnsureAccessTokenAsync() As Task
        If String.IsNullOrEmpty(accessToken) Then
            Using client As New HttpClient()
                Dim tokenContent As New FormUrlEncodedContent(New Dictionary(Of String, String) From {
                    {"client_id", clientId},
                    {"client_secret", clientSecret},
                    {"grant_type", "client_credentials"}
                })

                Dim tokenResponse = Await client.PostAsync("https://id.twitch.tv/oauth2/token", tokenContent)

                If Not tokenResponse.IsSuccessStatusCode Then
                    Throw New Exception($"Error al obtener el token: {tokenResponse.StatusCode}")
                End If

                Dim tokenJson = Await tokenResponse.Content.ReadAsStringAsync()
                Dim tokenData = JsonDocument.Parse(tokenJson).RootElement
                Me.accessToken = tokenData.GetProperty("access_token").GetString()
            End Using
        End If
    End Function

    Private Shared Async Function GetFollowers(client As HttpClient, idUser As String) As Task(Of Integer)
        Dim response = Await client.GetAsync($"https://api.twitch.tv/helix/channels/followers?broadcaster_id={idUser}")
        Dim json = Await response.Content.ReadAsStringAsync()
        Dim data = JsonDocument.Parse(json).RootElement
        Return data.GetProperty("total").GetInt32()
    End Function

    Public Async Function GetUserData(userName As String) As Task(Of UserData)
        Using client As New HttpClient()
            client.DefaultRequestHeaders.Add("Client-Id", clientId)
            client.DefaultRequestHeaders.Add("Authorization", $"Bearer {accessToken}")

            Dim response = Await client.GetAsync($"https://api.twitch.tv/helix/users?login={userName}")
            Dim json = Await response.Content.ReadAsStringAsync()
            Dim data = JsonDocument.Parse(json).RootElement

            Dim userArray = data.GetProperty("data").EnumerateArray().FirstOrDefault()

            If userArray.ValueKind <> JsonValueKind.Undefined Then
                Dim idUser = userArray.GetProperty("id").GetString()
                Dim createdAtString = userArray.GetProperty("created_at").GetString()

                If Not String.IsNullOrEmpty(createdAtString) Then
                    Dim createdAt = DateTime.Parse(createdAtString)
                    Dim totalFollowers = Await GetFollowers(client, idUser)

                    Return New UserData With {
                        .Username = userName,
                        .CreatedAt = createdAt,
                        .Followers = totalFollowers
                    }
                End If
            End If
        End Using

        Return Nothing
    End Function
End Class

Module Program
    Private Sub PrintRankings(usersData As List(Of Twitch.UserData))
        Dim byFollowers = usersData.OrderByDescending(Function(x) x.Followers).ToList()
        Dim byDate = usersData.OrderBy(Function(x) x.CreatedAt).ToList()

        Console.WriteLine(vbCrLf & "Ranking por número de seguidores:")
        For i = 0 To byFollowers.Count - 1
            Console.WriteLine($"{i + 1} - {byFollowers(i).Username}: {byFollowers(i).Followers:N0} seguidores")
        Next

        Console.WriteLine(vbCrLf & "Ranking por antigüedad:")
        For i = 0 To byDate.Count - 1
            Console.WriteLine($"{i + 1} - {byDate(i).Username}: Creado el {byDate(i).CreatedAt:dd/MM/yyyy}")
        Next
    End Sub

    Public Async Function ProcessUsers(users As List(Of String), Tw As Twitch) As Task
        Dim usersData As New List(Of Twitch.UserData)
        Dim notFoundUsers As New List(Of String)

        Console.WriteLine("Obteniendo datos...")

        For Each name In users
            Dim userData = Await Tw.GetUserData(name)
            If userData IsNot Nothing Then
                usersData.Add(userData)
            Else
                notFoundUsers.Add(name)
            End If
        Next

        PrintRankings(usersData)

        If notFoundUsers.Count > 0 Then
            Console.WriteLine(vbCrLf & "Usuarios no encontrados:")
            For Each user In notFoundUsers
                Console.WriteLine(user)
            Next
        End If
    End Function

    Public Async Function Run() As Task
        DotNetEnv.Env.Load()
        Dim clientId = Environment.GetEnvironmentVariable("TWITCH_CLIENT_ID")
        Dim clientSecret = Environment.GetEnvironmentVariable("TWITCH_CLIENT_SECRET")

        Dim Tw = New Twitch(clientId, clientSecret)
        Await Tw.EnsureAccessTokenAsync()

        Dim users As New List(Of String) From {
            "abby", "ache", "adricontreras", "agustin", "alexby", "ampeter", "ander", "arigameplays",
            "arigeli", "auronplay", "axozer", "beniju", "bycalitos", "byviruzz", "carrera", "celopan",
            "cheeto", "crystalmolly", "darioemehache", "dheyo",
            "djmario", "doble", "elvisa", "elyas360", "folagor", "grefg", "guanyar", "hika",
            "hiper", "ibai", "ibelky", "illojuan", "imantado", "irinaisasia", "jesskiu", "jopa",
            "jordiwild", "kenaisouza", "keroro", "kiddkeo",
            "kikorivera", "knekro", "koko", "kronnozomber", "leviathan", "litkillah", "lolalolita", "lolito",
            "luh", "luzu", "mangel", "mayichi", "melo", "missasinonia", "mixwell", "mrjagger",
            "nategentile", "nexxuz", "nia", "nilojeda",
            "nissaxter", "ollie", "orslok", "outconsumer", "papigavi", "paracetamor", "patica", "paulagonu",
            "pausenpaii", "perxitaa", "plex", "polispol", "quackity", "recuerdop", "reven", "rivers",
            "robertpg", "roier", "rojuu", "rubius",
            "shadoune", "silithur", "spoksponha", "spreen", "spursito", "staxx", "suzyroxx", "vicens",
            "vituber", "werlyb", "xavi", "xcry", "xokas", "zarcort", "zeling", "zorman"}

        Await ProcessUsers(users, Tw)
    End Function

    Public Sub Main()
        Run().Wait()
    End Sub
End Module
