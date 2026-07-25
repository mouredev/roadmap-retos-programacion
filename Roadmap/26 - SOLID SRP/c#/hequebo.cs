/*
 * El Principio de Resposabilidad Única (SRP)
 * de los principios SOLID nos dice que una
 * clase solo debe de encargarse de una 
 * responsabilidad, para que sea más fácil
 * su modificación y correción de errores
 */
class Program
{
    static int idUser = 1;
    static int idLoan = 1;
    static void Main(string[] args)
    {
        var post = new Post("hequebo", "Hola Mundo", DateTime.Now);
        post.SavePost();
        post.SharePost();

        var postSRP = new PostSRP("hequebo", "Hola Mundo", DateTime.Now);
        var postDB = new PostDB(postSRP);
        var postReq = new PostRequest(postSRP);
        postDB.SavePost();
        postReq.SharePost();

        Console.ReadLine();
        Console.Clear();

        LibrarySRP library = new LibrarySRP();
        bool salir = false;

        do
        {
            Menu();
            int option = 0;
            int.TryParse(Console.ReadLine(), out option);
            switch (option)
            {
                case 1:
                    RegisterBook(ref library);
                    break;
                case 2:
                    RegisterUser(ref library);
                    break;
                case 3:
                    LoanBook(ref library);
                    break;
                case 4:
                    ReturnBook(ref library);
                    break;
                case 5:
                    salir = true;
                    Console.Clear();
                    Console.WriteLine("Hasta la próxima...");
                    Thread.Sleep(1000);
                    break;
                default:
                    Console.WriteLine("Opción no válida...");
                    break;
            }
        } while (!salir);

    }
    static void Menu()
    {
        Console.WriteLine("---Sistema de biblioteca---");
        Console.WriteLine("1.- Agregar libro");
        Console.WriteLine("2.- Agregar Usuario");
        Console.WriteLine("3.- Pedir libro");
        Console.WriteLine("4.- Devolver libro");
        Console.WriteLine("5.- Salir");
        Console.WriteLine("Elija opción deseada");
    }
    static void RegisterBook(ref LibrarySRP library)
    {
        Console.Clear();
        Console.WriteLine("Ingrsa titulo del libro");
        string title = Console.ReadLine();
        Console.WriteLine("Ingresa Nombre del autor");
        string author = Console.ReadLine();
        Console.WriteLine("Ingresa número de copias a registrar");
        int copies = int.Parse(Console.ReadLine());
        var book = new Book(title, author, copies);
        library.RegisterBook(book);
        Console.Clear();
        Console.WriteLine("Libro registrado correctamente...");
        Console.WriteLine($"Título: {title}, Autor: {author}, Copias: {copies}");
    }
    static void RegisterUser(ref  LibrarySRP library)
    {
        Console.Clear();
        Console.WriteLine("Ingresa Nombre del usuario");
        string name = Console.ReadLine();
        Console.WriteLine("Ingresa Correo del usuario");
        string email = Console.ReadLine();
        var user = new User(name, email, idUser);
        library.RegisterUser(user);
        
        Console.Clear();
        Console.WriteLine("Usuario registrado correctamente...");
        Console.WriteLine($"ID: {idUser}, Nombre: {name}, Correo: {email}");

        idUser++;
    }
    static void LoanBook(ref LibrarySRP library)
    {
        Console.Clear();
        Console.WriteLine("Ingresa título de libro a pedir");
        string title = Console.ReadLine();
        if (!library.SearchBook(title))
            return;
        if (library.GetCopies(title) == 0)
        {
            Console.WriteLine($"No hay copias disponibles de {title}");
            return;
        }
        Console.WriteLine("Ingresa nombre de usuario");
        string name = Console.ReadLine();
        var user = library.SearchUser(name);
        if (user == null)
            return;
        var loan = new Loan(idLoan, title, user.Id);
        library.LoanBook(loan);
        Console.Clear();
        Console.WriteLine("Se realizó préstamo correctamente...");
        Console.WriteLine($"Titulo {title}, Usuario: {user.Name}");
        idLoan++;
    }
    static void ReturnBook(ref  LibrarySRP library)
    {
        Console.Clear();
        Console.WriteLine("Ingresa nombre de libro a regresar");
        string title = Console.ReadLine();
        Console.WriteLine("Ingresa nombre de usuario que regresa el libro");
        string name = Console.ReadLine();
        var user = library.SearchUser(name);
        if (user == null)
            return;
        var loan = library.SearchLoan(title, user.Id);
        if (loan == null)
        {
            Console.WriteLine("No existe el préstamo");
            return;
        }
        library.ReturnBook(loan);
        Console.Clear();
        Console.WriteLine("El libro se regresó correctamente...");
    }
}
#region Incorrecto
/*
 * INCORRECTO
 * La siguiente clase tiene tres responsabilidades
 * diferentes:
 * 1.- Tener la información de la publicación
 * 2.- Guardar la publicación en Base de Datos
 * 3.- Compartir la publicación
 */

class Post
{
    private string _username;
    private string _content;
    private DateTime _postDate;

    public Post(string username, string content, DateTime postDate)
    {
        _username = username;
        _content = content;
        _postDate = postDate;
    }

    public void SavePost() => Console.WriteLine("Se guarda publicación en base de datos...");
    

    public void SharePost() => Console.WriteLine("Se comparte publicación...");
}
#endregion
#region Correcto
/*
 * CORRECTO
 * Como en el ejemplo anterior existen
 * tres responsaibilidades, siguiendo
 * el princicipio SRP se deben de crear
 * tres clases diferentes
 */
class PostSRP
{
    private string _username;
    private string _content;
    private DateTime _postDate;

    public PostSRP(string username, string content, DateTime postDate)
    {
        _username = username;
        _content = content;
        _postDate = postDate;
    }
}

/*
 * La clases que no se encargan
 * de la información reciben en su 
 * constructor un objeto de la clase
 * con esa responsabilidad
 */
class PostDB
{
    private PostSRP _post;
    
    public PostDB(PostSRP post)
    {
        _post = post;
    }
    public void SavePost() => Console.WriteLine("Guardando en BD...");
}
class PostRequest
{
    private PostSRP _post;

    public PostRequest(PostSRP post)
    {
        _post = post;
    }

    public void SharePost() => Console.WriteLine("Se comparte publicación...");
}
#endregion
// Ejercicio Extra
// Incorrecto
#region ExtraIncorrecto
class Library
{
    private List<(string Title, string Author, int Copies)> _books;
    private List<(string Name, string Email, int Id)> _users;
    private List<(int IdLoan, string BookTitle, int IdUser)> _loans;
    private int _id = 0;
    private int _idLoan = 0;

    public Library()
    {
        _books = new List<(string, string, int)> ();
        _users = new List<(string, string, int)> ();
        _loans = new List<(int, string, int)> ();
    }

    public void RegisterBook(string title, string author, int copies) =>
        _books.Add((title, author, copies));
    public void RegisterUser(string name, string email)
    {
        _id++;
        _users.Add((name, email, _id));
    }
    public void LoanBook(string title, int idUser) 
    {
        if (_books.Where(b => b.Title == title).Count() == 0) 
        {
            Console.WriteLine("No existe el libro");
            return;
        }
        if (_books.Where(b => b.Title == title).Select(b => b.Copies).FirstOrDefault() == 0)
        {
            Console.WriteLine("No hay copias disponibles..");
        }
        if (_users.Where(u => u.Id == idUser).Count() == 0)
        {
            Console.WriteLine("Usuario no existe");
            return;
        }
        _loans.Add((_idLoan, title, idUser));
    }
    public void ReturnBook(string title, int idUser)
    {
        if (_loans.Where(l => l.BookTitle == title && l.IdUser == idUser).Count() == 0) 
        {
            Console.WriteLine("No hay registro de este préstamo");
            return;
        }
        int idLoan = _loans.Where(l => l.BookTitle == title && l.IdUser == idUser).Select(l => l.IdLoan).FirstOrDefault();
        var book = _books.Where(b => b.Title == title).Select(b => b).FirstOrDefault();
        book.Copies++;
        _loans.Remove((idLoan, title, idUser));

    }
}
#endregion
// Correcto
class Book
{
    private string _title;
    private string _author;
    private int _copies;

    public string Title
    {
        get
        {
            return _title;
        }
        set
        {
            _title = value;
        }
    }

    public string Author
    {
        get
        {
            return _author;
        }
        set
        {
            _author = value;
        }
    }

    public int Copies
    {
        get
        {
            return _copies;
        }
        set
        {
            _copies = value;
        }
    }

    public Book(string title, string author, int copies)
    {
        _title = title;
        _author = author;
        _copies = copies;
    }
}
class BookService
{
    private List<Book> _books;
    public BookService()
    {
        _books = new List<Book>();
    }

    public void RegisterBook(Book book)
    {
        _books.Add(book);
    }
    public bool SearchBook(string title)
    {
        if (string.IsNullOrEmpty(title))
            return false;
        if (_books.Where(b => b.Title == title).Count() == 0)
        {
            Console.WriteLine($"No se encontro el libro: {title}");
            return false;
        }
        return true;
    }
    public int GetCopies(string title) =>
        _books.Where(b => b.Title == title).Select(b => b.Copies).FirstOrDefault();
    public void LoanBook(string title)
    {
        var book = _books.Where(b => b.Title == title).FirstOrDefault();
        book.Copies--;
    }
    public void ReturnBook(string title)
    {
        var book = _books.Where(b => b.Title == title).FirstOrDefault();
        book.Copies++;
    }
}

class User
{
    private string _name;
    private string _email;
    private int _id;

    public string Name
    {
        get
        {
            return _name;
        }
        set
        {
            _name = value;
        }
    }
    public string Email
    {
        get
        {
            return _email;
        }
        set
        {
            _email = value;
        }
    }

    public int Id
    {
        get
        {
            return _id;
        }
    }

    public User(string name, string email, int id)
    {
        _name = name;
        _email = email;
        _id = id;
    }
}
class UserService
{
    private List<User> _users;
    public UserService()
    {
        _users = new List<User>();
    }
    public void RegisterUser(User user) => _users.Add(user);
    public User SearchUser(string name)
    {
        if (_users.Where(u  => u.Name == name).Count() == 0)
        {
            Console.WriteLine($"No existe usuario {name}");
            return null;
        }
        return _users.Where(u => u.Name == name).FirstOrDefault();
    }
    
}

class Loan
{
    private int _id;
    private string _title;
    private int _userId;

    public int Id { get { return _id; } }
    public string Title { get { return _title; } }
    public int UserId {  get { return _userId; } }

    public Loan(int id, string title, int userId)
    {
        _id = id;
        _title = title;
        _userId = userId;
    }
}

class LoanService
{
    private List<Loan> _loans;

    public LoanService()
    {
        _loans = new List<Loan>();
    }

    public void LoanBook(Loan loan)
    {
        _loans.Add(loan);
    }

    public void ReturnBook(Loan loan)
    {
        _loans.Remove(loan);
    }
    public Loan SearchLoan(string title, int id)
    {
        if (_loans.Count == 0)
        {
            Console.WriteLine("No hay préstamos activos");
            return null;
        }
        var loan = _loans.Where(l => l.Title == title && l.UserId == id).FirstOrDefault();
        return loan;
    }
}

class LibrarySRP
{
    private BookService _bookService;
    private UserService _userService;
    private LoanService _loanService;

    public LibrarySRP()
    {
        _bookService = new BookService();
        _userService = new UserService();
        _loanService = new LoanService();
    }

    public void RegisterBook(Book book) => _bookService.RegisterBook(book);
    public bool SearchBook(string title) => _bookService.SearchBook(title);
    public int GetCopies(string title) => _bookService.GetCopies(title);
    public void RegisterUser(User user) => _userService.RegisterUser(user);  
    public User SearchUser(string name) => _userService.SearchUser(name);
    public void LoanBook(Loan loan)
    {
        _loanService.LoanBook(loan);
        _bookService.LoanBook(loan.Title);
    }
    public Loan SearchLoan(string title, int id) => _loanService.SearchLoan(title, id);
    public void ReturnBook(Loan loan)
    {
        _loanService.ReturnBook(loan);
        _bookService.ReturnBook(loan.Title);
    }
    
}
    
