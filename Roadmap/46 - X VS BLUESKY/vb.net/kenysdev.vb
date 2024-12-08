' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 46 X VS BLUESKY
' ------------------------------------
'* EJERCICIO:
' * La alternativa descentralizada a X, Bluesky, comienza a atraer
' * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
' * 
' * Implementa un sistema que simule el comportamiento de estas
' * redes sociales.
' * 
' * Debes crear las siguientes operaciones:
' * - Registrar un usuario por nombre e identificador único.
' * - Un usuario puede seguir/dejar de seguir a otro.
' * - Creación de post asociado a un usuario. Debe poseer
' *   texto (200 caracteres máximo), fecha de creación 
' *   e identificador único.   
' * - Eliminación de un post.
' * - Posibilidad de hacer Like (y eliminarlo) en un post.
' * - Visualización del feed de un usuario con sus 10 publicaciones
' *   más actuales ordenadas desde la más reciente.
' * - Visualización del feed de un usuario con las 10 publicaciones
' *   más actuales de los usuarios que sigue ordenadas 
' *   desde la más reciente.
' *   
' * Cuando se visualiza un post, debe mostrarse:
' * ID de usuario, nombre de usuario, texto del post, 
' * fecha de creación y número total de likes.
' * 
' * Controla errores en duplicados o acciones no permitidas.

Imports System
Imports System.Collections.Generic
Imports System.Linq
Imports Microsoft.Extensions.Logging
Imports Microsoft.Extensions.DependencyInjection

Public Class Posts
    Private ReadOnly _postDt As New Dictionary(Of Integer, Dictionary(Of Integer, PostData))
    Private ReadOnly _logger As ILogger(Of Posts)

    Public Sub New(logger As ILogger(Of Posts))
        _logger = logger
    End Sub

    Public Class PostData
        Public Property Content As String = String.Empty
        Public Property Timestamp As DateTime
        Public Property Likes As New HashSet(Of Integer)
    End Class

    Private Function VerifyPost(idUser As Integer, idPost As Integer, nameFuncStr As String) As Boolean
        Dim userPosts As Dictionary(Of Integer, PostData) = Nothing
        If Not _postDt.TryGetValue(idUser, userPosts) Then
            _logger.LogError("{NameFunc}: El ID {IdUser} no tiene posts.", nameFuncStr, idUser)
            Return False
        End If

        If Not userPosts.ContainsKey(idPost) Then
            _logger.LogError("{NameFunc}: El Post ({IdPost}) no existe.", nameFuncStr, idPost)
            Return False
        End If

        Return True
    End Function

    Public Sub CreatePost(idUser As Integer, content As String)
        If content.Length > 200 Then
            _logger.LogError("'create_post': content > 200 caracteres.")
            Return
        End If

        Dim userPosts As Dictionary(Of Integer, PostData) = Nothing
        If Not _postDt.TryGetValue(idUser, userPosts) Then
            userPosts = New Dictionary(Of Integer, PostData)()
            _postDt(idUser) = userPosts
        End If

        Dim idPost = userPosts.Count + 1
        userPosts(idPost) = New PostData With {
            .Content = content,
            .Timestamp = DateTime.Now,
            .Likes = New HashSet(Of Integer)()
        }

        _logger.LogInformation("El ID {IdUser} creó un post(ID: {IdPost}).", idUser, idPost)
    End Sub

    Public Sub DeletePost(idUser As Integer, idPost As Integer)
        If VerifyPost(idUser, idPost, "DeletePost") Then
            _postDt(idUser).Remove(idPost)
            _logger.LogInformation("El post: {IdPost} de usuario: {IdUser} ha sido eliminado.", idPost, idUser)
        End If
    End Sub

    Public Sub LikePost(idUser As Integer, idAuthor As Integer, idPost As Integer)
        If VerifyPost(idAuthor, idPost, "LikePost") Then
            _postDt(idAuthor)(idPost).Likes.Add(idUser)
            _logger.LogInformation("El usuario {IdUser} dio like al post {IdPost} de usuario {IdAuthor}.",
                idUser, idPost, idAuthor)
        End If
    End Sub

    Public Sub RemoveLike(idUser As Integer, idAuthor As Integer, idPost As Integer)
        If VerifyPost(idAuthor, idPost, "RemoveLike") Then
            _postDt(idAuthor)(idPost).Likes.Remove(idUser)
            _logger.LogInformation("El usuario {IdUser} anuló el like al post {IdPost} de usuario {IdAuthor}.",
                idUser, idPost, idAuthor)
        End If
    End Sub

    Public Function GetRecentPosts(idUser As Integer, Optional limit As Integer = 10) As List(Of PostData)
        Dim userPosts As Dictionary(Of Integer, PostData) = Nothing
        If _postDt.TryGetValue(idUser, userPosts) Then
            Return userPosts.Values _
                .OrderByDescending(Function(p) p.Timestamp) _
                .Take(limit) _
                .ToList()
        End If

        Return New List(Of PostData)()
    End Function
End Class

Public Class Users
    Private ReadOnly _usersDt As New Dictionary(Of Integer, UserData)
    Private ReadOnly _logger As ILogger(Of Users)

    Public Sub New(logger As ILogger(Of Users))
        _logger = logger
    End Sub

    Private Class UserData
        Public Property Name As String = String.Empty
        Public Property Following As New HashSet(Of Integer)
        Public Property Followers As New HashSet(Of Integer)
    End Class

    Private Function IdExists(id As Integer, nameFuncStr As String) As Boolean
        If _usersDt.ContainsKey(id) Then
            Return True
        End If

        _logger.LogWarning("'{NameFunc}': ID: {Id} no encontrada.", nameFuncStr, id)
        Return False
    End Function

    Public Sub AddUser(name As String)
        Dim id = _usersDt.Count + 1
        _usersDt(id) = New UserData With {
            .Name = name,
            .Following = New HashSet(Of Integer)(),
            .Followers = New HashSet(Of Integer)()
        }

        _logger.LogInformation("Usuario {Id}-{Name} registrado.", id, name)
    End Sub

    Public Sub FollowUser(id As Integer, toId As Integer)
        If IdExists(id, "FollowUser") AndAlso IdExists(toId, "FollowUser") Then
            _usersDt(id).Following.Add(toId)
            _usersDt(toId).Followers.Add(id)
            _logger.LogInformation("ID: {Id} está siguiendo a ID: {ToId}.", id, toId)
        End If
    End Sub

    Public Sub UnfollowUser(id As Integer, toId As Integer)
        If IdExists(id, "UnfollowUser") AndAlso IdExists(toId, "UnfollowUser") Then
            _usersDt(id).Following.Remove(toId)
            _usersDt(toId).Followers.Remove(id)
            _logger.LogInformation("El ID: {Id} dejó de seguir al ID: {ToId}.", id, toId)
        End If
    End Sub

    Public Function GetName(idUser As Integer) As String
        If IdExists(idUser, "GetName") Then
            Return _usersDt(idUser).Name
        End If

        Return String.Empty
    End Function
End Class

Public Class Program
    Private ReadOnly _posts As Posts
    Private ReadOnly _users As Users

    Public Sub New(postsLogger As ILogger(Of Posts), usersLogger As ILogger(Of Users))
        _posts = New Posts(postsLogger)
        _users = New Users(usersLogger)
    End Sub

    Private Sub PrintFeed(idUser As Integer)
        Dim name = _users.GetName(idUser)
        If String.IsNullOrEmpty(name) Then
            Console.WriteLine($"Usuario ID: {idUser} no encontrado.")
            Return
        End If

        Dim last10 = _posts.GetRecentPosts(idUser, 10)
        Console.WriteLine($"{vbCrLf}Feed{vbCrLf}________{vbCrLf}ID: '{idUser}' - Nombre: '{name}'")

        If last10.Count = 0 Then
            Console.WriteLine("No tiene publicaciones.")
            Return
        End If

        For Each post In last10
            Console.WriteLine($"________{vbCrLf}{post.Content}")
            Console.WriteLine($"Creado: '{post.Timestamp}'")
            Console.WriteLine($"Likes: '{post.Likes.Count}'")
        Next
    End Sub

    Public Sub Run()
        ' CLI
    End Sub

    Public Sub Tests()
        _users.AddUser("Ken") ' id=1
        _users.AddUser("Zoe") ' id=2

        _users.FollowUser(1, 2)
        _users.FollowUser(2, 1)
        _users.UnfollowUser(2, 1)

        _posts.CreatePost(2, "Primer post.") ' id=1
        _posts.CreatePost(2, "Segundo post.") ' id=2
        _posts.DeletePost(2, 2)
        _posts.CreatePost(2, "Otro post.") ' id=2
        _posts.LikePost(1, 2, 1)
        _posts.RemoveLike(1, 2, 1)
        _posts.LikePost(1, 2, 2)

        PrintFeed(2)
        PrintFeed(1)
    End Sub

    Public Shared Sub Main()
        Dim services = New ServiceCollection()
        services.AddLogging(Sub(builder)
                                builder.SetMinimumLevel(LogLevel.Debug)
                                builder.AddConsole()
                            End Sub)

        Using serviceProvider = services.BuildServiceProvider()
            Dim loggerFactory = serviceProvider.GetRequiredService(Of ILoggerFactory)()
            Dim postsLogger = loggerFactory.CreateLogger(Of Posts)()
            Dim usersLogger = loggerFactory.CreateLogger(Of Users)()

            Dim program = New Program(postsLogger, usersLogger)
            program.Tests()
            'program.Run()
        End Using
    End Sub
End Class
