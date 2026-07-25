class User
{
    private int _id;
    private string? _userName;
    private List<User> _following;
    private List<User> _followers;

    public int Id { get { return _id; } }
    public string? UserName {  get { return _userName; } }
    public List<User> Following { get { return _following; } }
    public List<User> Followers { get { return _followers; } }

    public User(int id, string? userName)
    {
        _id = id;
        _userName = userName;
        _following = new List<User>();
        _followers = new List<User>();
    }

    public void FollowUser(User user) => _following.Add(user);
    public void UnFollowUser(User user) => _following.Remove(user);
    public void AddFollower(User user) => _followers.Add(user);
    public void RemoveFollower(User user) => _followers.Remove(user);
}
class Post
{
    private int _id;
    private User _user;
    private string _content;
    private DateTime _creationDate;
    private List<User> _likes;

    public int Id { get { return _id; } }
    public User User { get { return _user; } }
    public string Content { get { return _content; } }
    public DateTime CreationDate { get { return _creationDate; } }
    public List<User> Likes { get { return _likes; } }

    public Post(int id, User user, string content)
    {
        _id = id;
        _user = user;
        _content = content;
        _creationDate = DateTime.Now;
        _likes = new List<User>();
    }

    public void AddLike(User user) => _likes.Add(user);
    public void RemoveLike(User user) => _likes.Remove(user);
}
class SocialNetwork
{
    private List<User> _users;
    private List<Post> _posts;
    private int _userId = 1;
    private int _postId = 1;

    public SocialNetwork()
    {
        _users = new List<User>();
        _posts = new List<Post>();
    }
    public void RegisterUser(string? userName)
    {
        if (string.IsNullOrEmpty(userName))
        {
            Console.WriteLine("No se ha ingresado ningún nombre de usuario...");
            return;
        }
        if (_users.Where(u => u.UserName == userName).Any())
        {
            Console.WriteLine($"El nombre de usuario {userName} ya existe...");
            return;
        }
        var user = new User(_userId, userName);
        _users.Add(user);
        Console.WriteLine("El usuario ha sido registrado correctamente");
        Console.WriteLine($"Id: {user.Id}, Nombre de Usuario: {user.UserName}");
        _userId++;
    }
    public void FollowUser(string? userName1, string? userName2)
    {
        if (string.IsNullOrEmpty(userName1) || string.IsNullOrEmpty(userName2))
        {
            Console.WriteLine("Uno de los usuarios no se ha ingresado correctamente...");
            return;
        }
        var user1 = SearchUser(userName1);
        var user2 = SearchUser(userName2);
        if (user1 == null || user2 == null)
            return;
        if (user1.Following.Contains(user2))
        {
            Console.WriteLine($"{user1.UserName} ya sigue a {user2.UserName}...");
            return;
        }
        if (user1 == user2)
        {
            Console.WriteLine($"{user1.UserName} no puede seguirse a si mismo...");
            return;
        }
        user1.FollowUser(user2);
        user2.AddFollower(user1);
        Console.WriteLine($"{user1.UserName} ahora sigue a {user2.UserName}");
    }
    public void UnfollowUser(string? userName1, string? userName2)
    {
        if (string.IsNullOrEmpty(userName1) || string.IsNullOrEmpty(userName2))
        {
            Console.WriteLine("Uno de los usuarios no se ha ingresado correctamente...");
            return;
        }
        var user1 = SearchUser(userName1);
        var user2 = SearchUser(userName2);
        if (user1 == null || user2 == null)
            return;
        if (!user1.Following.Contains(user2))
        {
            Console.WriteLine($"{user1.UserName} no seguía a {user2.UserName}...");
            return;
        }
        user1.UnFollowUser(user2);
        user2.RemoveFollower(user1);
        Console.WriteLine($"{user1.UserName} dejó de seguir a {user2.UserName}");
    }
    public void CreatePost(string? userName, string? content)
    {
        if (string.IsNullOrEmpty(userName))
        {
            Console.WriteLine("No se ingresó ningún usuario...");
            return;
        }
        var user = SearchUser(userName);
        if (user == null)
            return;
        if (string.IsNullOrEmpty(content))
        {
            Console.WriteLine("La publicación está vacía...");
            return;
        }
        if (content.Length > 200)
        {
            Console.WriteLine("La publicación no puede contener más de 200 carácteres...");
            return;
        }
        var post = new Post(_postId, user, content);
        _posts.Add(post);
        Console.WriteLine("La publicación se ha creado correctamente...");
        _postId++;
    }
    public void DeletePost(string? userName)
    {
        if (string.IsNullOrEmpty(userName))
        {
            Console.WriteLine("No se ingresó ningún usuario...");
            return;
        }
        var user = SearchUser(userName);
        if (user == null)
            return;
        var userPosts = _posts.Where(p => p.User == user).ToList();
        if (userPosts.Count == 0)
        {
            Console.WriteLine($"El usuario {user.UserName} no tiene publicaciones...");
            return;
        }
        Console.WriteLine($"------------Publicaciones de {user.UserName}------------");
        foreach (var post in userPosts) 
            ShowPost(post);
        
        Console.WriteLine();
        Console.WriteLine("Ingresa el id de la publicación a eliminar");
        var postToDelete = SearchPost();

        if (postToDelete == null)
            return;
        _posts.Remove(postToDelete);
        Console.WriteLine("Se ha eliminado la publicación correctamente");
    }
    private void ShowPost(Post post)
    {
        Console.WriteLine("-------------------------------------------------");
        Console.WriteLine($"Post ID: {post.Id}\tUsuario: {post.User.UserName}" +
        $"\n{post.Content}\n{post.Likes.Count} likes\t\t{post.CreationDate}");
    }
    private bool SearchPosts()
    {
        if (_posts.Count == 0)
        {
            Console.WriteLine("No hay publicaciones disponibles...");
            return false;
        }
        Console.WriteLine($"------------Publicaciones disponibles------------");
        foreach (var post in _posts)
            ShowPost(post);
        Console.WriteLine();
        return true;
    }
    private Post? SearchPost()
    {
        int id = 0;
        int.TryParse(Console.ReadLine(), out id);
        var post = _posts.Where(p => p.Id == id).FirstOrDefault();
        if (post == null)
            Console.WriteLine("La publicación no existe...");
        return post;
    }
    public void LikePost(string? userName) 
    {
        if (string.IsNullOrEmpty (userName))
        {
            Console.WriteLine("El usuario no se ingresó correctamente...");
            return;
        }
        var user = SearchUser(userName);
        if (user == null)
            return;
        if (!SearchPosts()) 
            return;
        
        Console.WriteLine("Ingresa el id de la publicación a dar like");
        var postToLike = SearchPost();

        if (postToLike == null)
            return;

        postToLike.AddLike(user);
        Console.WriteLine($"{user.UserName} ha dado like a la publicación de {postToLike.User.UserName}");
        ShowPost(postToLike);
    }
    public void DislikePost(string? userName)
    {
        if (string.IsNullOrEmpty(userName))
        {
            Console.WriteLine("El usuario no se ingresó correctamente...");
            return;
        }
        var user = SearchUser(userName);
        if (user == null)
            return;

        if (!SearchPosts())
            return;

        Console.WriteLine("Ingresa el id de la publicación a quitar like");
        var postToDislike = SearchPost();
        if (postToDislike == null)
            return;

        if (!postToDislike.Likes.Contains(user)) 
        {
            Console.WriteLine($"{user.UserName} no había dado like a la publicación de {postToDislike.User.UserName}");
            return;
        }
        Console.WriteLine($"{user.UserName} ha eliminado su like de la publicación de {postToDislike.User.UserName}");
        postToDislike.RemoveLike(user);
    }
    public void ShowFeed(string? userName)
    {
        if (string.IsNullOrEmpty(userName))
        {
            Console.WriteLine("No se ingresó ningún usuario...");
            return;
        }
        var feed = _posts.Where(p => p.User.UserName == userName).ToList();

        if (feed.Count == 0)
        {
            Console.WriteLine($"El usuario {userName} no tiene publicaciones...");
            return;
        }
        feed = feed.OrderByDescending(f => f.CreationDate)
            .ToList();
        if (feed.Count > 10)
            feed = feed.Slice(0, 10);
        Console.WriteLine($"------------Últimas 10 publicaciones de {userName}------------");
        foreach (var post in feed)
            ShowPost(post);
    }
    public void ShowFollowingFeed(string? userName)
    {
        if (string.IsNullOrEmpty(userName))
        {
            Console.WriteLine("No se ingresó ningún usuairo...");
            return;
        }
        var user = SearchUser(userName);
        if (user == null) 
            return;

        if (user.Following.Count == 0)
        {
            Console.WriteLine($"El usuario {user.UserName} no sigue a ninguna cuenta...");
            return;
        }

        var feed = _posts.Where(p => user.Following.Contains(p.User))
            .OrderByDescending(p => p.CreationDate)
            .ToList();
        if (feed.Count > 10)
            feed = feed.Slice(0, 10);
        Console.WriteLine($"------------Feed cuentas seguidas por {user.UserName}------------");
        foreach(var post in feed)
            ShowPost(post);
        
    }
    public User? SearchUser(string userName)
    {
        var user = _users.Where(u => u.UserName == userName).FirstOrDefault();
        if (user == null)
            Console.WriteLine($"El usuario {userName} no existe...");
        return user;
    }
}
class Program
{
    static void Main(string[] args)
    {
        var sn = new SocialNetwork();
        bool exit = false;

        do
        {
            Menu();
            int option = 0;
            int.TryParse(Console.ReadLine(), out option);
            switch (option)
            {
                case 1:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre de usuario");
                    string? userName = Console.ReadLine();
                    sn.RegisterUser(userName);
                    break;
                case 2:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre del usuario");
                    string? userName1 = Console.ReadLine();
                    Console.WriteLine("Ingresa el nombre del usuario a seguir");
                    string? userName2 = Console.ReadLine();
                    sn.FollowUser(userName1, userName2);
                    break;
                case 3:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre del usuario");
                    userName1 = Console.ReadLine();
                    Console.WriteLine("Ingresa el nombre del usuario a dejar de seguir");
                    userName2 = Console.ReadLine();
                    sn.UnfollowUser(userName1, userName2);
                    break;
                case 4:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre del usuario");
                    userName = Console.ReadLine();
                    Console.WriteLine("Ingresa el contenido de la publicación");
                    string? content = Console.ReadLine();
                    sn.CreatePost(userName, content);
                    break;
                case 5:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre del usuario");
                    userName = Console.ReadLine();
                    sn.DeletePost(userName);
                    break;
                case 6:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre del usuario");
                    userName = Console.ReadLine();
                    sn.LikePost(userName);
                    break;
                case 7:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre del usuario");
                    userName = Console.ReadLine();
                    sn.DislikePost(userName);
                    break;
                case 8:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre del usuario");
                    userName = Console.ReadLine();
                    sn.ShowFeed(userName);
                    break;
                case 9:
                    Console.Clear();
                    Console.WriteLine("Ingresa el nombre del usuario");
                    userName = Console.ReadLine();
                    sn.ShowFollowingFeed(userName);
                    break;
                case 10:
                    Console.Clear();
                    exit = true;
                    Console.WriteLine("Hasta la próxima...");
                    Thread.Sleep(1000);
                    break;
                default:
                    Console.WriteLine("Opción no válida...");
                    break;
            }
        } while (!exit);
    }
    static void Menu()
    {
        Console.WriteLine("------------MENU------------");
        Console.WriteLine("1.- Registrar usuario nuevo.");
        Console.WriteLine("2.- Seguir a un usuario.");
        Console.WriteLine("3.- Dejar de seguir a un usuario");
        Console.WriteLine("4.- Crear una publicación.");
        Console.WriteLine("5.- Eliminar una publicación.");
        Console.WriteLine("6.- Dar Like.");
        Console.WriteLine("7.- Quitar Like");
        Console.WriteLine("8.- Mostrar Feed de usuario");
        Console.WriteLine("9.- Mostrar Feed de usuarios seguidos");
        Console.WriteLine("10.- Salir.");
        Console.WriteLine("Ingrese la opción deseada...");
    }
}