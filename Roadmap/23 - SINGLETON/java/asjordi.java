/**
 * SINGLETON es un patrón de diseño creacional que nos permite asegurarnos
 * de que una clase tenga una única instancia, a la vez que proporciona un
 * punto de acceso global a dicha instancia.
 * ¿Cómo se implementa?
 * 1. Agregar un campo estático privado a la clase para guardar la instancia Singleton.
 * 2. Declarar un método de creación estático público para obtener la instancia Singleton.
 * 3. Implementar una inicialización diferida dentro del método de estático. Debe crear un nuevo objeto
 * en su primer llamada y colocarlo dentro del campo estático. Debe devolver siempre la misma instancia.
 * 4. Declarar el constructor de la clase como privado. El método estático de la clase todavía podrá llamar al constructor.
 * 5. Modificar todos los clientes de la clase para que usen el método de creación estático, y no el constructor.
 */
public class Main {

    public static void main(String[] args) {
        var s1 = Singleton.getInstance("FOO");
        var s2 = Singleton.getInstance("BAR");
        System.out.println(s1.getValue());
        System.out.println(s2.getValue());

        var session = UserSession.getInstance(1, "asjordi", "Jordi", "me@asjordi.dev");
        System.out.println(session.getId());
    }

    /**
     * EJERCICIO:
     * Explora el patrón de diseño "singleton" y muestra cómo crearlo
     * con un ejemplo genérico.
     */
    static class Singleton {
        private static Singleton instance;
        private String value;

        private Singleton(String value) {
            this.value = value;
        }

        public static Singleton getInstance(String value) {
            if (instance == null) instance = new Singleton(value);
            return instance;
        }

        public String getValue() {
            return value;
        }

        public void setValue(String value) {
            this.value = value;
        }
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Utiliza el patrón de diseño "singleton" para representar una clase que
     * haga referencia a la sesión de usuario de una aplicación ficticia.
     * La sesión debe permitir asignar un usuario (id, username, nombre y email),
     * recuperar los datos del usuario y borrar los datos de la sesión.
     */
    static class UserSession {
        private static UserSession instance;
        private Integer id;
        private String username;
        private String name;
        private String email;

        private UserSession(Integer id, String username, String name, String email) {
            this.id = id;
            this.username = username;
            this.name = name;
            this.email = email;
        }

        public static UserSession getInstance(Integer id, String username, String name, String email) {
            if (instance == null) instance = new UserSession(id, username, name, email);
            return instance;
        }

        public void deleteSession() {
            if (instance != null) instance = null;
        }

        public void deleteUserData() {
            if (instance != null) {
                setId(null);
                setUsername(null);
                setName(null);
                setEmail(null);
            }
        }

        public Integer getId() {
            return id;
        }

        public String getUsername() {
            return username;
        }

        public String getName() {
            return name;
        }

        public String getEmail() {
            return email;
        }

        public void setId(Integer id) {
            this.id = id;
        }

        public void setUsername(String username) {
            this.username = username;
        }

        public void setName(String name) {
            this.name = name;
        }

        public void setEmail(String email) {
            this.email = email;
        }
    }
}
