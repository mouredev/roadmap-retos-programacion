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

public class JimsimroDev {

  public static class ConfiguracionGlobal {

    private static ConfiguracionGlobal config;

    private ConfiguracionGlobal() {
    }

    public static ConfiguracionGlobal getConfig() {
      return (config == null) ? config = new ConfiguracionGlobal() : config;
    }
  }

  // Extra
  public static class SesionUsuario {
    private static SesionUsuario instancia;
    private Long id;
    private String username;
    private String nombre;
    private String email;

    private SesionUsuario() {
    }

    public static SesionUsuario getInstancia() {
      return instancia == null ? instancia = new SesionUsuario() : instancia;
    }

    public void registrarUsuario(Long id, String username, String nombre, String email) {
      this.id = id;
      this.username = username;
      this.nombre = nombre;
      this.email = email;
    }

    public String mostrarDatosUsuario() {
      if (this.id == null) {
        return "No hay usuario registrado.";
      }
      return String.format("ID: %d - Username: %s - Nombre: %s - Email: %s", this.id, this.username, this.nombre,
          this.email);
    }

    public void cerrarSesion() {
      this.id = null;
      this.username = null;
      this.nombre = null;
      this.email = null;
    }
  }

  public static void main(String[] args) {
    ConfiguracionGlobal config1 = ConfiguracionGlobal.getConfig();
    ConfiguracionGlobal config2 = ConfiguracionGlobal.getConfig();
    System.out.println(config1 == config2);

    // Extra
    System.out.println("Creando una nueva instancia de SesionUsuario...");
    var sesion1 = SesionUsuario.getInstancia();
    sesion1.registrarUsuario(1L, "jimsimro", "Jim Simro", "prueba@gmail.com");

    var sesion2 = SesionUsuario.getInstancia();

    System.out.println(sesion2.mostrarDatosUsuario());
    System.out.println(sesion1.mostrarDatosUsuario());

    System.out.println("Creando una nueva instancia de SesionUsuario...");
    sesion2.registrarUsuario(2L, "jhoans", "Jhoan", "prueba2@gmail.com");
    System.out.println(sesion2.mostrarDatosUsuario());
    System.out.println(sesion1.mostrarDatosUsuario());

    System.out.println("Creando una nueva instancia de SesionUsuario...");
    var sesion3 = SesionUsuario.getInstancia();
    System.out.println(sesion3.mostrarDatosUsuario());
    System.out.println(sesion2.mostrarDatosUsuario());
    System.out.println(sesion1.mostrarDatosUsuario());

    sesion2.cerrarSesion();

    System.out.println(sesion2.mostrarDatosUsuario());
    System.out.println(sesion1.mostrarDatosUsuario());
  }
}
