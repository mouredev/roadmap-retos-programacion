/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */

using System;

namespace Roadmap23
{
    class Singleton
    {
        private static Singleton? instance;
        private Singleton() { }

        public static Singleton Instance
        {
            get
            {
                instance ??= new Singleton();
                return instance;
            }
        }
    }

    class Program
    {

        // Extra: Clase de sesión de usuario
        class UserSession
        {
            private static UserSession? instance;
            private UserSession()
            {
                Id = 0;
                Username = "";
                Name = "";
                Email = "";
            }

            public static UserSession Instance
            {
                get
                {
                    instance ??= new UserSession();
                    return instance;
                }
            }

            public int Id { get; private set; }
            public string Username { get; private set; }
            public string Name { get; private set; }
            public string Email { get; private set; }

            public void SetUser(int id, string username, string name, string email)
            {
                Id = id;
                Username = username;
                Name = name;
                Email = email;
            }

            public void ClearUser()
            {
                Id = 0;
                Username = "";
                Name = "";
                Email = "";
            }
        }
        static void Main(string[] args)
        {
            Singleton s1 = Singleton.Instance;
            Singleton s2 = Singleton.Instance;

            Console.WriteLine("Are s1 and s2 the same instance?");
            Console.WriteLine(s1 == s2);

            // Extra: Uso de la sesión de usuario
            UserSession session = UserSession.Instance;
            Console.WriteLine("\n *+* Fill user data *+*\n");
            session.SetUser(1, "user", "User Name", "e@mail.com");

            Console.WriteLine("User ID: " + session.Id);
            Console.WriteLine("Username: " + session.Username);
            Console.WriteLine("Name: " + session.Name);
            Console.WriteLine("Email: " + session.Email);

            session.ClearUser();
            Console.WriteLine("\n *+* User data cleared *+*\n");

            Console.WriteLine("User ID: " + session.Id);
            Console.WriteLine("Username: " + session.Username);
            Console.WriteLine("Name: " + session.Name);
            Console.WriteLine("Email: " + session.Email);
        }
    }
}
