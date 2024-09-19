' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 37 OASIS VS LINKIN PARK
' ------------------------------------
'* ¡Dos de las bandas más grandes de la historia están de vuelta!
'* Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
'* Desarrolla un programa que se conecte al API de Spotify y los compare.
'* Requisitos:
'* 1. Crea una cuenta de desarrollo en https//developer.spotify.com.
'* 2. Conéctate al API utilizando tu lenguaje de programación.
'* 3. Recupera datos de los endpoint que tú quieras.
'* Acciones:
'* 1. Accede a las estadísticas de las dos bandas.
'*    Por ejemplo: número total de seguidores, escuchas mensuales,
'*    canción con más reproducciones...
'* 2. Compara los resultados de, por lo menos, 3 endpoint.
'* 3. Muestra todos los resultados por consola para notificar al usuario.
'* 4. Desarrolla un criterio para seleccionar qué banda es más popular.

Imports SpotifyAPI.Web
Imports DotNetEnv

Public Class Spotify
    Private ReadOnly _spotify As SpotifyClient

    Public Sub New()
        Env.Load()
        Dim clientId = Environment.GetEnvironmentVariable("SPOTIFY_CLIENT_ID")
        Dim clientSecret = Environment.GetEnvironmentVariable("SPOTIFY_CLIENT_SECRET")

        If String.IsNullOrEmpty(clientId) OrElse String.IsNullOrEmpty(clientSecret) Then
            Throw New ArgumentException("Se debe proporcionar 'CLIENT_ID' y 'CLIENT_SECRET'.")
        End If

        Dim config = SpotifyClientConfig.CreateDefault().
            WithAuthenticator(New ClientCredentialsAuthenticator(clientId, clientSecret))

        _spotify = New SpotifyClient(config)
    End Sub

    Public Async Function GetMostPopularArtistAsync(name As String) As Task(Of FullArtist)
        Dim searchRequest As New SearchRequest(SearchRequest.Types.Artist, name) With {
            .Limit = 3
        }
        Dim searchResult = Await _spotify.Search.Item(searchRequest)

        Return searchResult?.Artists?.Items?.
            OrderByDescending(Function(artist) artist.Popularity).
            FirstOrDefault()
    End Function

    Public Async Function ArtistTopTracksAsync(artistId As String) As Task(Of ArtistsTopTracksResponse)
        Return Await _spotify.Artists.GetTopTracks(artistId, New ArtistsTopTracksRequest("US"))
    End Function
End Class

Public Class Versus
    Private ReadOnly _artist1 As FullArtist
    Private ReadOnly _artist2 As FullArtist
    Private ReadOnly _spotify As Spotify
    Private _artist1Score As Integer = 0
    Private _artist2Score As Integer = 0

    Public Sub New(artist1 As FullArtist, artist2 As FullArtist, spotifyInstance As Spotify)
        _artist1 = artist1
        _artist2 = artist2
        _spotify = spotifyInstance
    End Sub

    Private Sub ComparePopularity()
        Console.WriteLine($"Popularidad: {_artist1.Popularity} vs {_artist2.Popularity}")
        IncrementScore(_artist1.Popularity, _artist2.Popularity)
    End Sub

    Private Sub CompareFollowers()
        Console.WriteLine($"Seguidores: {_artist1.Followers.Total} vs {_artist2.Followers.Total}")
        IncrementScore(_artist1.Followers.Total, _artist2.Followers.Total)
    End Sub

    Private Async Function CompareTopTracksAsync() As Task
        Dim a1Top = Await _spotify.ArtistTopTracksAsync(_artist1.Id)
        Dim a2Top = Await _spotify.ArtistTopTracksAsync(_artist2.Id)

        Dim a1Pop = a1Top.Tracks.Take(3).Sum(Function(track) track.Popularity)
        Dim a2Pop = a2Top.Tracks.Take(3).Sum(Function(track) track.Popularity)

        Console.WriteLine($"Popularidad Top 3 canciones: {a1Pop} vs {a2Pop}")
        IncrementScore(a1Pop, a2Pop)
    End Function

    Private Sub IncrementScore(value1 As Integer, value2 As Integer)
        If value1 > value2 Then
            _artist1Score += 1
        ElseIf value2 > value1 Then
            _artist2Score += 1
        End If
    End Sub

    Private Sub ShowFinalResult()
        Console.WriteLine($"{vbCrLf}RESULTADO FINAL:")
        Console.WriteLine($"{_artist1.Name}: {_artist1Score} puntos")
        Console.WriteLine($"{_artist2.Name}: {_artist2Score} puntos")

        Dim winner = If(_artist1Score > _artist2Score, _artist1.Name,
                        If(_artist2Score > _artist1Score, _artist2.Name, "Empate"))

        Console.WriteLine($"{vbCrLf}¡{If(winner = "Empate", "Es un empate", $"'{winner}' gana el versus")}!")
    End Sub

    Public Async Function StartAsync() As Task
        Console.WriteLine($"{_artist1.Name} vs {_artist2.Name}")
        ComparePopularity()
        CompareFollowers()
        Await CompareTopTracksAsync()
        ShowFinalResult()
    End Function
End Class

Module Program
    <STAThread>
    Public Sub Main()
        Console.WriteLine("VERSUS")
        Dim spotify = New Spotify()

        Dim artist1 = spotify.GetMostPopularArtistAsync("Oasis").GetAwaiter().GetResult()
        Dim artist2 = spotify.GetMostPopularArtistAsync("Linkin Park").GetAwaiter().GetResult()

        If artist1 Is Nothing OrElse artist2 Is Nothing Then
            Console.WriteLine("Artistas no encontrados")
            Return
        End If

        Dim versus = New Versus(artist1, artist2, spotify)
        versus.StartAsync().GetAwaiter().GetResult()
    End Sub
End Module
