namespace exs46;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
46 X VS BLUESKY
------------------------------------

 * EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.   
 * - Eliminación de un post.
 * - Posibilidad de hacer like (y eliminarlo) en un post.
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *   
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post, 
 * fecha de creación y número total de likes.
 * 
 * Controla errores en duplicados o acciones no permitidas.
*/

using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Extensions.Logging;

public class Posts(ILogger<Posts> logger)
{
    private readonly Dictionary<int, Dictionary<int, PostData>> _postDt = [];
    private readonly ILogger<Posts> _logger = logger;

    public class PostData
    {
        public string Content { get; set; } = "";
        public DateTime Timestamp { get; set; }
        public HashSet<int> Likes { get; set; } = [];
    }

    private bool VerifyPost(int idUser, int idPost, string nameFunc)
    {
        if (!_postDt.TryGetValue(idUser, out Dictionary<int, PostData>? value))
        {
            _logger.LogError("'{NameFunc}': El ID {IdUser} no tiene posts.", nameFunc, idUser);
            return false;
        }

        if (!value.ContainsKey(idPost))
        {
            _logger.LogError("'{NameFunc}': El Post ({IdPost}) no existe.", nameFunc, idPost);
            return false;
        }

        return true;
    }

    public void CreatePost(int idUser, string content)
    {
        if (content.Length > 200)
        {
            _logger.LogError("'create_post': content > 200 caracteres.");
            return;
        }

        if (!_postDt.TryGetValue(idUser, out Dictionary<int, PostData>? value))
        {
            value = [];
            _postDt[idUser] = value;
        }

        var idPost = value.Count + 1;
        value[idPost] = new PostData
        {
            Content = content,
            Timestamp = DateTime.Now,
            Likes = []
        };

        _logger.LogInformation("El ID {IdUser} creó un post(ID: {IdPost}).", idUser, idPost);
    }

    public void DeletePost(int idUser, int idPost)
    {
        if (VerifyPost(idUser, idPost, "DeletePost"))
        {
            _postDt[idUser].Remove(idPost);
            _logger.LogInformation("El post: {IdPost} de usuario: {IdUser} ha sido eliminado.", idPost, idUser);
        }
    }

    public void LikePost(int idUser, int idAuthor, int idPost)
    {
        if (VerifyPost(idAuthor, idPost, "LikePost"))
        {
            _postDt[idAuthor][idPost].Likes.Add(idUser);
            _logger.LogInformation("El usuario {IdUser} dio like al post {IdPost} de usuario {IdAuthor}.", 
                idUser, idPost, idAuthor);
        }
    }

    public void RemoveLike(int idUser, int idAuthor, int idPost)
    {
        if (VerifyPost(idAuthor, idPost, "RemoveLike"))
        {
            _postDt[idAuthor][idPost].Likes.Remove(idUser);
            _logger.LogInformation("El usuario {IdUser} anuló el like al post {IdPost} de usuario {IdAuthor}.",
                idUser, idPost, idAuthor);
        }
    }

    public List<PostData> GetRecentPosts(int idUser, int limit = 10)
    {
        if (_postDt.TryGetValue(idUser, out Dictionary<int, PostData>? value))
        {
            return value.Values
                .OrderByDescending(p => p.Timestamp)
                .Take(limit)
                .ToList();
        }

        return [];
    }
}

public class Users(ILogger<Users> logger)
{
    private readonly Dictionary<int, UserData> _usersDt = [];
    private readonly ILogger<Users> _logger = logger;

    private class UserData
    {
        public string Name { get; set; } = "";
        public HashSet<int> Following { get; set; } = [];
        public HashSet<int> Followers { get; set; } = [];
    }

    private bool IdExists(int id, string nameFunc)
    {
        if (_usersDt.ContainsKey(id))
            return true;

        _logger.LogWarning("'{NameFunc}': ID: {Id} no encontrada.", nameFunc, id);
        return false;
    }

    public void AddUser(string name)
    {
        var id = _usersDt.Count + 1;
        _usersDt[id] = new UserData
        {
            Name = name,
            Following = [],
            Followers = []
        };

        _logger.LogInformation("Usuario {Id}-{Name} registrado.", id, name);
    }

    public void FollowUser(int id, int toId)
    {
        if (IdExists(id, "FollowUser") && IdExists(toId, "FollowUser"))
        {
            _usersDt[id].Following.Add(toId);
            _usersDt[toId].Followers.Add(id);
            _logger.LogInformation("ID: {Id} está siguiendo a ID: {ToId}.", id, toId);
        }
    }

    public void UnfollowUser(int id, int toId)
    {
        if (IdExists(id, "UnfollowUser") && IdExists(toId, "UnfollowUser"))
        {
            _usersDt[id].Following.Remove(toId);
            _usersDt[toId].Followers.Remove(id);
            _logger.LogInformation("El ID: {Id} dejó de seguir al ID: {ToId}.", id, toId);
        }
    }

    public string GetName(int idUser)
    {
        if (IdExists(idUser, "GetName"))
        {
            return _usersDt[idUser].Name;
        }

        return "";
    }
}

public class Program(ILogger<Posts> postsLogger, ILogger<Users> usersLogger)
{
    private readonly Posts _posts = new(postsLogger);
    private readonly Users _users = new(usersLogger);

    private void PrintFeed(int idUser)
    {
        var name = _users.GetName(idUser);
        if (string.IsNullOrEmpty(name))
        {
            Console.WriteLine($"Usuario ID: {idUser} no encontrado.");
            return;
        }

        var last10 = _posts.GetRecentPosts(idUser, 10);
        Console.WriteLine($"\nFeed\n_______\nID: '{idUser}' - Nombre: '{name}'");
        
        if (last10.Count == 0)
        {
            Console.WriteLine("No tiene publicaciones.");
            return;
        }

        foreach (var post in last10)
        {
            Console.WriteLine($"_______\n{post.Content}");
            Console.WriteLine($"Creado: '{post.Timestamp}'");
            Console.WriteLine($"Likes: '{post.Likes.Count}'");
        }
    }

    public void Run()
    {
        // CLI
    }

    public void Tests()
    {
        _users.AddUser("Ken"); // id=1
        _users.AddUser("Zoe"); // id=2

        _users.FollowUser(1, 2);
        _users.FollowUser(2, 1);
        _users.UnfollowUser(2, 1);

        _posts.CreatePost(2, "Primer post."); // id=1
        _posts.CreatePost(2, "Segundo post."); // id=2
        _posts.DeletePost(2, 2);
        _posts.CreatePost(2, "Otro post."); // id=2
        _posts.LikePost(1, 2, 1);
        _posts.RemoveLike(1, 2, 1);
        _posts.LikePost(1, 2, 2);

        PrintFeed(2);
        PrintFeed(1);
    }

    public static void Main()
    {
        using var loggerFactory = LoggerFactory.Create(builder =>
        {
            builder
                .SetMinimumLevel(LogLevel.Debug)
                .AddConsole();
        });

        var postsLogger = loggerFactory.CreateLogger<Posts>();
        var usersLogger = loggerFactory.CreateLogger<Users>();

        var program = new Program(postsLogger, usersLogger);
        program.Tests();
        //program.Run();
    }
}
