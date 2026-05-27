import java.util.Scanner;

public class FranDev200 {


    static class BBDD{

        private static BBDD bbdd;

        private BBDD(){
            System.out.println("Creando conexion a la BBDD.");
        }

        public static BBDD getInstance(){
            if(bbdd == null){
                bbdd = new BBDD();
            }
            return bbdd;
        }

        public void crearBBDD(){
            System.out.println("Crear una Base de Datos");
        }

        public void eliminarBBDD(){
            System.out.println("Eliminar una Base de Datos");
        }

        public void editarBBDD(){
            System.out.println("Editar una Base de Datos");
        }
    }

    static void main() {

        /*

        EJERCICIO:
         * Explora el patrón de diseño "singleton" y muestra cómo crearlo
         * con un ejemplo genérico.

         */

        BBDD bbdd = BBDD.getInstance();
        bbdd.crearBBDD();
        bbdd.editarBBDD();
        bbdd.eliminarBBDD();

        BBDD bbdd2 = BBDD.getInstance();
        bbdd2.crearBBDD();
        bbdd2.editarBBDD();
        bbdd2.eliminarBBDD();

        System.out.println(bbdd == bbdd2); // Nos devuelve True.
        // Esto quiere decir que ambas referencias de los objetos apuntan a la misma direccion de memoria, donde
        // está almacenado el objeto

        /*

        bbdd -------- 0xSWEN34          Ambas referencias, apuntan al mismo objeto, almacenado en esa direccion de memoria
                         /
        bbdd2 ----------/

         */

        // Esto también sirve para logins por ejemplo en aplicaciones.


        /*

        DIFICULTAD EXTRA (opcional):
         * Utiliza el patrón de diseño "singleton" para representar una clase que
         * haga referencia a la sesión de usuario de una aplicación ficticia.
         * La sesión debe permitir asignar un usuario (id, username, nombre y email),
         * recuperar los datos del usuario y borrar los datos de la sesión.

         */

        Scanner sc = new Scanner(System.in);

        Usuario usuario = Usuario.getInstance();

        System.out.println("\n --- EJERCICIO EXTRA ---");
        System.out.println();

        System.out.print("Introduce el ID del usuario: ");
        int id = Integer.parseInt(sc.nextLine());
        System.out.print("Introduce el username del usuario: ");
        String username = sc.nextLine();
        System.out.print("Introduce el nombre del usuario: ");
        String nombre = sc.nextLine();
        System.out.print("Introduce el email del usuario: ");
        String email = sc.nextLine();


        usuario.iniciarSesion(id, username, nombre, email);

        System.out.println("\nInformacion del usuario");
        System.out.println("=======================");
        usuario.infoUsuario();

        Usuario usuario2 = Usuario.getInstance();

        System.out.println("\nInformacion del usuario");
        System.out.println("=======================");
        usuario2.infoUsuario();

        usuario.cerrarSesion();


        System.out.println("\nInformacion del usuario");
        System.out.println("=======================");
        usuario2.infoUsuario();

        /*

        Como podemos comprobar por consola, ambas instancias apuntan al mismo objeto, por eso aunq el nombre de la
        instancia sea diferente y puedan parecer dos objetos diferentes, vemos que el usuario2 tiene datos
        sin haberlos rellenado y además coinciden con los de la instancia usuario.
        También, vemos que al cerrar sesion con la instancia usuario, se borran los datos y si queremos ver
        los datos de usuario2, vemos que todo es null.

         */

    }

    static class Usuario{

        private static Usuario usuario;

        private String username;
        private Integer id;
        private String nombre;
        private String email;

        private Usuario(){
            System.out.println("Creando usuario. Rellene sus datos.");
        }

        public static Usuario getInstance(){

            if(usuario == null){
                usuario = new Usuario();
            }

            return usuario;
        }

        public String getUsername() { return username; }

        public void setUsername(String username) { this.username = username; }

        public Integer getId() { return id; }

        public void setId(Integer id) { this.id = id; }

        public String getNombre() { return nombre; }

        public void setNombre(String nombre) { this.nombre = nombre; }

        public String getEmail() { return email; }

        public void setEmail(String email) { this.email = email; }

        public void infoUsuario(){
            System.out.println("ID: " + getId());
            System.out.println("Nombre: " + getNombre());
            System.out.println("Email: " + getEmail());
            System.out.println("Usuario: " + getUsername());
            System.out.println("----------------");
        }

        public void iniciarSesion(Integer id, String username,
                                  String nombre, String email){
            this.id = id;
            this.username = username;
            this.nombre = nombre;
            this.email = email;

            System.out.println("\nSe ha iniciado sesion con el usuario " + getUsername());

        }

        public void cerrarSesion(){

            System.out.println("\nCerrando sesion...");

            setUsername(null);
            setEmail(null);
            setId(null);
            setNombre(null);

        }
    }

}
