/**
 * Implementación del patrón Singleton en Java
 * Archivo: eulogioep.java
 */
public class eulogioep {
    /**
     * Ejemplo básico del patrón Singleton
     */
    public static class BasicSingleton {
        // Instancia privada estática
        private static BasicSingleton instance;

        // Constructor privado
        private BasicSingleton() {}

        // Método público para obtener la instancia (synchronized para thread-safety)
        public static synchronized BasicSingleton getInstance() {
            if (instance == null) {
                instance = new BasicSingleton();
            }
            return instance;
        }
    }

    /**
     * Clase para representar los datos del usuario
     */
    public static class User {
        private final int id;
        private final String username;
        private final String name;
        private final String email;

        public User(int id, String username, String name, String email) {
            this.id = id;
            this.username = username;
            this.name = name;
            this.email = email;
        }

        // Getters
        public int getId() { return id; }
        public String getUsername() { return username; }
        public String getName() { return name; }
        public String getEmail() { return email; }

        @Override
        public String toString() {
            return "User{" +
                    "id=" + id +
                    ", username='" + username + '\'' +
                    ", name='" + name + '\'' +
                    ", email='" + email + '\'' +
                    '}';
        }
    }

    /**
     * Implementación del Singleton para la sesión de usuario
     * Utiliza inicialización lazy y es thread-safe
     */
    public static class UserSession {
        // Instancia volátil privada estática
        private static volatile UserSession instance;
        // Datos del usuario actual
        private User currentUser;

        // Constructor privado
        private UserSession() {
            if (instance != null) {
                throw new RuntimeException("Use getInstance() method to create");
            }
        }

        // Método público para obtener la instancia (implementación thread-safe con double-checked locking)
        public static UserSession getInstance() {
            if (instance == null) {
                synchronized (UserSession.class) {
                    if (instance == null) {
                        instance = new UserSession();
                    }
                }
            }
            return instance;
        }

        // Método para establecer el usuario actual
        public void setUser(User user) {
            if (user == null) {
                throw new IllegalArgumentException("User cannot be null");
            }
            this.currentUser = user;
        }

        // Método para obtener el usuario actual
        public User getUser() {
            return currentUser;
        }

        // Método para cerrar la sesión
        public void logout() {
            this.currentUser = null;
        }
    }

    /**
     * Método principal para demostrar el uso del patrón Singleton
     */
    public static void main(String[] args) {
        try {
            // Ejemplo básico
            BasicSingleton singleton1 = BasicSingleton.getInstance();
            BasicSingleton singleton2 = BasicSingleton.getInstance();
            System.out.println("Singleton básico - ¿Misma instancia? " + (singleton1 == singleton2));

            // Ejemplo de sesión de usuario
            System.out.println("\nProbando sesión de usuario:");
            
            // Obtener instancia de sesión
            UserSession session = UserSession.getInstance();

            // Crear y establecer usuario
            User user = new User(1, "john_doe", "John Doe", "john@example.com");
            session.setUser(user);
            System.out.println("Usuario actual: " + session.getUser());

            // Obtener otra referencia a la sesión
            UserSession anotherSession = UserSession.getInstance();
            System.out.println("¿Misma sesión? " + (session == anotherSession));
            System.out.println("Usuario desde otra referencia: " + anotherSession.getUser());

            // Cerrar sesión
            session.logout();
            System.out.println("Después de logout: " + session.getUser());

            // Intentar crear una nueva instancia directamente (esto lanzará una excepción)
            // new UserSession(); // Esto lanzaría una RuntimeException

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}