class Program
{
    static void Main(string[] args)
    {
        /*
         * No creamos un objeto de la clase, en
         * su lugar accedemos a la instancia ya
         * existente
         */
        var singleton = Singleton.Instance;
        var singleton2 = Singleton.Instance;
        /*
         * Ambas variable acceden a la misma instancia
         * por lo que si las comparamos podemos ver 
         * que son iguales
         */
        Console.WriteLine($"singleton == singleton2 es {singleton == singleton2}");

        // Ejercicio Extra
        var userSession = UserSession.GetInstance();
        userSession.SetUser(1, "Hequebo", "Emilio Quezada", "emilioqzb@gmail.com");
        Console.WriteLine(userSession.GetUser());

        var userSession2 = UserSession.GetInstance();
        Console.WriteLine(userSession2.GetUser());
        userSession2.ClearUser();
        
        var userSession3 = UserSession.GetInstance();
        userSession3.ClearUser();
        Console.WriteLine(userSession3.GetUser());
    }
}
/*
 * Singleton es un patrón de diseño para la
 * creación de objetos que consiste en que 
 * solo exista un solo objeto en todo la 
 * aplicación y no se puedan crear más 
 * instancias.
 */
class Singleton
{
    /*
     * Creamos un atributo privado solo de 
     * lectura que será del mismo tipo de la 
     * clase en el cual estara el objeto que
     * se creara una vez se compile la 
     * solución
     */
    private static readonly Singleton _instance = new Singleton();
    /*
     * Para poder accedera a la instancia 
     * creamos una propiedad que regresa el
     * atributo privado
     */
    public static Singleton Instance {  get { return _instance; } }
    /*
     * Para evitar crear objetos de esta clase
     * agregamos un contructor privado
     */
    private Singleton() { }
}

class UserSession
{
    private static UserSession _instance = null;
    private int _id;
    private string _username;
    private string _name;
    private string _email;

    /*
     * Una alternativa a tenere la instancia como
     * solo de lectura es crearla como nula y a
     * través de un metodo crear el objeto si es
     * que no ha sido creado antes
     */
    public static UserSession GetInstance()
    {
        if (_instance == null)
            _instance = new UserSession();
        return _instance;
    }

    public string GetUser()
    {
        return $"Id: {_id}, Usuario: {_username}, Nombre: {_name},  Correo: {_email}";
    }
    public void SetUser(int id, string username, string name, string emmail)
    {
        _id = id;
        _username = username;
        _name = name;
        _email = emmail;
    }
    public void ClearUser()
    {
        _id = 0;
        _username = "";
        _name = "";
        _email = "";
    }
}
