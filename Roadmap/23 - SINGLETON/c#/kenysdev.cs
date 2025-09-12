#pragma warning disable CA1050
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* PATRONES DE DISEÑO: SINGLETON
------------------------------------------

* EJERCICIO #1:
* Explora el patrón de diseño "singleton" y muestra cómo crearlo
* con un ejemplo genérico.
*/
public class Singleton {
    private static Singleton _instance;

    // Constructor privado para evitar la instanciación directa.
    private Singleton() { }

    // Método estático que devuelve la única instancia de la clase.
    public static Singleton Instance {
        get {
            // Si la instancia aún no ha sido creada, la crea.
            _instance ??= new Singleton();
            return _instance;
        }
    }
}

/*
__________________________________
* EJERCICIO #2:
* Utiliza el patrón de diseño "singleton" para representar una clase que
* haga referencia a la sesión de usuario de una aplicación ficticia.
* La sesión debe permitir asignar un usuario (id, username, nombre y email),
* recuperar los datos del usuario y borrar los datos de la sesión.
*/

public class UserSession {
    private static UserSession _instance;
    private int _userId;
    private string _userName;
    private string _name;
    private string _email;
    private UserSession() { }

    public static UserSession Instance {
        get {
            // Si la instancia aún no ha sido creada, la crea.
            _instance ??= new UserSession();
            return _instance;
        }
    }

    // Método para establecer los detalles del usuario.
    public void SetUser(int userId, string userName, string name, string email) {
        _userId = userId;
        _userName = userName;
        _name = name;
        _email = email;
    }

    public Dictionary<string, object> GetUser() {
        Dictionary<string, object> userDetails = new() {
            { "id", _userId },
            { "username", _userName },
            { "name", _name },
            { "email", _email }
        };
        return userDetails;
    }

    public void Logout() {
        _userId = 0;
        _userName = null;
        _name = null;
        _email = null;
    }
}

// __________________________________
class Program {    
    static void Main() {
        Console.WriteLine("EJERCICIO #1");

        Singleton singleton1 = Singleton.Instance;
        
        // singleton2 accede a la misma instancia que singleton1.
        Singleton singleton2 = Singleton.Instance;

        // Comprobación de igualdad de referencias.
        Console.WriteLine(singleton1 == singleton2);

        // __________________________________
        Console.WriteLine("EJERCICIO #2");
        
        var login_user1 = UserSession.Instance;
        login_user1.SetUser(1, "Zoe_1", "Zoe", "Zoe@gm.com");
        Dictionary<string, object> userDetails1 = login_user1.GetUser();
        foreach (var kvp in userDetails1) {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        };
        
        login_user1.Logout();

        var login_user2 = UserSession.Instance;
        login_user2.SetUser(2, "Ben_1", "Ben", "Ben@gm.com");
        Dictionary<string, object> userDetails2 = login_user2.GetUser();
        foreach (var kvp in userDetails2) {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }

        login_user2.Logout();

    }
}
