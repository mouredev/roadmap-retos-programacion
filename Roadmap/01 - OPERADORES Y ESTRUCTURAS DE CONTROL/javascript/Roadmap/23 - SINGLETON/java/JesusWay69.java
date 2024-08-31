package roadmap.ejercicio_23;

/*
* EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 */
public class JesusWay69 {

    private static JesusWay69 jesusway69;// Variable estática para recibir la unica instancia del Singleton

    private JesusWay69() {
        System.out.println("Creando objeto...");
    }

    public static JesusWay69 getJesusway69() {

        if (jesusway69 == null) { //Condicional para crear la instancia si es null
            jesusway69 = new JesusWay69();//en caso de ser la primera vez es null y se llama al constructor
        }
        return jesusway69;// Retorna el objeto único creado
    }

    public static void main(String[] args) {
        JesusWay69 instance1 = JesusWay69.getJesusway69();//Creamos un objeto instancia1
        JesusWay69 instance2 = JesusWay69.getJesusway69();// y otro objeto instancia2
        System.out.println("Instancia1 = " + instance1);//Observamos que el objeto generado en esta instancia
        System.out.println("Instancia2 = " + instance2);// es el mismo que el generado en la siguiente instancia

        Session sessionJesus = Singleton.getInstance(1, "Jesusway69", "Jesus", "jesusway60@midominio.es");
        Session sessionJose = Singleton.getInstance(2, "Pepe84", "Jose", "pepepepe@midominio.es");

        System.out.println("\nSesión de Jesús = " + sessionJesus + "\nID = " + sessionJesus.id
                + "\nName = " + sessionJesus.name + "\nUsername = " + sessionJesus.username + "\nemail = " + sessionJesus.email);
        //Al imprimir los datos solo recupera los datos de la primera instancia que es la de Jesus
        System.out.println("\nSesión de Jose = " + sessionJose + "\nID = " + sessionJose.id
                + "\nName = " + sessionJose.name + "\nUsername = " + sessionJose.username + "\nemail = " + sessionJose.email);
        //Aunque intentemos imprimir los datos de Jose seguirá imprimiendo los de Jesus porque la sesión es la misma
        
        System.out.println("\nBorrando sesion: " + sessionJesus);
        Session close = Singleton.deleteInstance();
        System.out.println("Sesión borrada, valor actual = " + close);
        //Una vez borrados los datos de la sesión podemos hacer una instancia nueva en este caso de Ana
        Session sessionAna = Singleton.getInstance(3, "Ana57", "Ana", "anagarcia@midominio.es");
        System.out.println("Nueva instancia para sesión de " + sessionAna.name + " = " + sessionAna);
        //Imprime correctamente los datos de Ana al haber borrado la sesión anterior de Jesus
        System.out.println("\nSesión de Ana = " + sessionAna + "\nID = " + sessionAna.id
                + "\nName = " + sessionAna.name + "\nUsername = " + sessionAna.username + "\nemail = " + sessionAna.email);

    }

}

/*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */
class Session {

    public int id;
    public String username;
    public String name;
    public String email;

    public Session(int id, String username, String name, String email) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.email = email;
    
    }

}

class Singleton {

    private static Session session = null;

    public synchronized static Session getInstance(int id, String username, String name, String email) {
        if (session == null) {
            session = new Session(id, username, name, email); // instar el Singleton si no hay todavía
        }
        return session;
    }

    public synchronized static Session deleteInstance() {
        if (session != null) {
            session = null;
        }

        return session;
    }

}
