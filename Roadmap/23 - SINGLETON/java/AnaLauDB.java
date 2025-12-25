public class AnaLauDB {

    // Ejemplo genérico de Singleton
    public static class ConfiguracionSingleton {
        // Instancia única (static)
        private static ConfiguracionSingleton instancia;

        // Variable de ejemplo
        private String configuracion;

        // Constructor privado para evitar instanciación externa
        private ConfiguracionSingleton() {
            this.configuracion = "Configuración por defecto";
        }

        // Método público para obtener la instancia única
        public static ConfiguracionSingleton getInstancia() {
            if (instancia == null) {
                instancia = new ConfiguracionSingleton();
            }
            return instancia;
        }

        public String getConfiguracion() {
            return configuracion;
        }

        public void setConfiguracion(String configuracion) {
            this.configuracion = configuracion;
        }
    }

    // DIFICULTAD EXTRA: Singleton para sesión de usuario
    public static class SesionUsuario {
        private static SesionUsuario instancia;

        // Datos del usuario
        private Integer id;
        private String username;
        private String nombre;
        private String email;
        private boolean sesionActiva;

        // Constructor privado
        private SesionUsuario() {
            this.sesionActiva = false;
        }

        // Método para obtener la instancia única
        public static SesionUsuario getInstancia() {
            if (instancia == null) {
                instancia = new SesionUsuario();
            }
            return instancia;
        }

        // Asignar usuario (iniciar sesión)
        public void asignarUsuario(int id, String username, String nombre, String email) {
            this.id = id;
            this.username = username;
            this.nombre = nombre;
            this.email = email;
            this.sesionActiva = true;
            System.out.println("Sesión iniciada para: " + nombre);
        }

        // Recuperar datos del usuario
        public void mostrarDatosUsuario() {
            if (sesionActiva) {
                System.out.println("=== Datos del Usuario ===");
                System.out.println("ID: " + id);
                System.out.println("Username: " + username);
                System.out.println("Nombre: " + nombre);
                System.out.println("Email: " + email);
            } else {
                System.out.println("No hay sesión activa");
            }
        }

        // Borrar datos de la sesión (cerrar sesión)
        public void cerrarSesion() {
            if (sesionActiva) {
                System.out.println("Cerrando sesión de: " + nombre);
                this.id = null;
                this.username = null;
                this.nombre = null;
                this.email = null;
                this.sesionActiva = false;
                System.out.println("Sesión cerrada correctamente");
            } else {
                System.out.println("No hay sesión activa para cerrar");
            }
        }

        // Verificar si hay sesión activa
        public boolean isSesionActiva() {
            return sesionActiva;
        }

        // Getters
        public Integer getId() {
            return id;
        }

        public String getUsername() {
            return username;
        }

        public String getNombre() {
            return nombre;
        }

        public String getEmail() {
            return email;
        }
    }

    public static void main(String[] args) {
        // Ejemplo básico de Singleton
        System.out.println("=== Ejemplo básico de Singleton ===");
        ConfiguracionSingleton config1 = ConfiguracionSingleton.getInstancia();
        ConfiguracionSingleton config2 = ConfiguracionSingleton.getInstancia();

        System.out.println("¿Son la misma instancia? " + (config1 == config2));

        config1.setConfiguracion("Nueva configuración");
        System.out.println("Config1: " + config1.getConfiguracion());
        System.out.println("Config2: " + config2.getConfiguracion());

        System.out.println("\n=== DIFICULTAD EXTRA: Sesión de Usuario ===");

        // Obtener instancia de sesión
        SesionUsuario sesion1 = SesionUsuario.getInstancia();
        SesionUsuario sesion2 = SesionUsuario.getInstancia();

        System.out.println("¿Son la misma instancia de sesión? " + (sesion1 == sesion2));

        // Intentar mostrar datos sin sesión activa
        sesion1.mostrarDatosUsuario();

        // Asignar usuario (iniciar sesión)
        sesion1.asignarUsuario(1, "analau", "Ana Laura", "ana.laura@email.com");

        // Mostrar datos del usuario
        sesion1.mostrarDatosUsuario();

        // Verificar que ambas referencias apuntan al mismo usuario
        System.out.println("\nVerificando desde sesion2:");
        sesion2.mostrarDatosUsuario();

        // Cerrar sesión
        sesion2.cerrarSesion();

        // Intentar mostrar datos después de cerrar sesión
        sesion1.mostrarDatosUsuario();
    }
}
