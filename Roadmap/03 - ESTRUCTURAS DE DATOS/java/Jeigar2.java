import java.util.*;

public class Jeigar2 {
    /*
     * EJERCICIO:
     * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
     * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
     *
     * DIFICULTAD EXTRA (opcional):
     * Crea una agenda de contactos por terminal.
     * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
     * - Cada contacto debe tener un nombre y un número de teléfono.
     * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
     *   los datos necesarios para llevarla a cabo.
     * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
     *   (o el número de dígitos que quieras)
     * - También se debe proponer una operación de finalización del programa.
     */

    public enum Acciones {
        B("Buscar"),
        I("Insertar"),
        A("Actualizar"),
        E("Eliminar"),
        L("Listar"),
        C("Contar"),
        S("Salir");

        private final String valor;

        Acciones(String valor) {
            this.valor = valor;
        }

        public String getValor() {
            return valor;
        }
    }

    public enum Datos {
        N("Nombre"),
        T("Teléfono"),
        A("Ambos"),
        S("Salir");

        private final String valor;

        Datos(String valor) {
            this.valor = valor;
        }

        public String getValor() {
            return valor;
        }
    }

    // Se decide que la colección sea un HashMap
    // Se guarda como key el nombre y luego el teléfono, existiendo el contacto duplicado
    // Ventaja, es muy rápido buscar por ambos atributos: nombre, teléfono
    // Desventaja, al actualizar hay que borrar ambos elementos y volver a insertar.
    //   si hay un error no hay transaccionalidad, por lo que puede que esto de errores al contar o buscar o listar
    //   TODO: Al borrar si da error, hay que revisar donde ha dado el error y ver como recuperar la coherencia
    private HashMap<String, Jeigar2Contacto> contactos;

    public static void main(String[] args) {
        Jeigar2 app = new Jeigar2();
        app.iniciar();
    }

    public void iniciar(){
        contactos =  new HashMap();
        String opcion;
        Acciones accion = null;
        // Nota: Solo se puede cerrar el Scanner una vez, aunque se use en muchos sitios
        Scanner scanner = new Scanner(System.in);
        do {
            imprimirMenu();
            opcion = scanner.next();
            try {
                accion = Acciones.valueOf(opcion.toUpperCase()); // Paso a Mayúsculas
                switch (accion) {
                    case B:
                         buscarContacto();
                        break;
                    case I:
                        insertarContacto();
                        break;
                    case A:
                        actualizarContacto();
                        break;
                    case E:
                        eliminarContacto();
                        break;
                    case C:
                        contarContactos();
                        break;
                    case L:
                        listarContactos();
                        break;
                }
            } catch (IllegalArgumentException e){
                System.out.println("Error. Operación no reconocida.");
            }
        } while (accion != null && accion != Acciones.S);
        scanner.close();
    }

    private void imprimirMenu(){
        Arrays.stream(Acciones.values()).forEach(item -> System.out.println(String.format("(%s)%s", item.name(), item.getValor().substring(1))));
        System.out.print("Seleccione la inicial de la operación a realizar: ");
    }

    public Jeigar2Contacto buscarContacto() {
        Jeigar2Contacto contacto = null;
        if(contactos.isEmpty()) {
            System.out.println("La lista de contactos está vacía.");
        } else {
            contacto = getJeigar2Contacto("buscar");
            if(contacto == null){
                System.out.println("Este contacto no existe");
            } else {
                System.out.println("encontrado: " + contacto.toString());
            }
        }
        return contacto;
    }

    private Jeigar2Contacto getJeigar2Contacto(String accion) {
        Scanner scannerGet = new Scanner(System.in);
        Jeigar2Contacto contacto = null;
        System.out.println(String.format("Procedemos a %s un contacto", accion));
        if(contactos.isEmpty()) {
            System.out.println("La lista de contactos está vacía.");
        } else {
            System.out.println("Introduce un nombre o numero de teléfono");
            String valor = scannerGet.nextLine();
            contacto = contactos.get(valor);
        }
        return contacto;
    }

    public void insertarContacto() {
        System.out.println("Procedemos a insertar un contacto");
        insertarContacto("");
    }
    public void insertarContacto(String nombre) {
        boolean nombreInvalido = true;
        Scanner scannerInsertar = new Scanner(System.in);
        String nombreInterno = null;
        Jeigar2Contacto contacto = null;
        if(nombre == null || nombre.isBlank() || nombre.isEmpty()) {
            do {
                System.out.println("Introduce un nombre (obligatorio, no puede ser un valor vacío o espacios en blanco)");
                nombreInterno = scannerInsertar.nextLine();
                nombreInvalido = (nombreInterno == null || nombreInterno.isEmpty() || nombreInterno.isBlank());
            } while (nombreInvalido);

        } else {
            nombreInterno = nombre;
        }
        System.out.println("Introduce un numero de teléfono (solo números, menor o igual a " + Jeigar2Contacto.MAX_DIGITOS_TELEFONO + " dígitos)");
        String telefono = scannerInsertar.nextLine();
        try {
            contacto = new Jeigar2Contacto(nombreInterno.trim(), telefono);
        } catch (TelefonoException ex) {
            System.err.println("Error de validación. " + ex.getMessage());
            insertarContacto(nombreInterno);
        }
        try {
            insertarContacto(contacto);
        } catch (ContactoDuplicadoException exception) {
            System.err.println(exception.getMessage());
            insertarContacto();
        }
    }

    public void insertarContacto(Jeigar2Contacto contacto) throws ContactoDuplicadoException{
        if (contacto != null) {
            System.out.println("insertando: " + contacto);
            if(contactos.containsKey(contacto.getNombre()) || contactos.containsKey(contacto.getTelefono())) {
                throw new ContactoDuplicadoException();
            } else {
                contactos.put(contacto.getNombre(), contacto);
                contactos.put(contacto.getTelefono(), contacto);
            }
        }
    }

    public void actualizarContacto() {
        actualizarContacto(null);
    }

    public void actualizarContacto(Jeigar2Contacto contacto) {
        String opcion = "";
        Datos datos = null;
        Jeigar2Contacto contactoInterno = null;
        Jeigar2Contacto contactoNuevoNombre = null;
        Jeigar2Contacto contactoNuevoTelefono = null;
        Jeigar2Contacto contactoNuevo = null;
        if (contactos.isEmpty()){
            System.out.println("La lista de contactos está vacía.");
        } else {
            if (contacto == null) {
                contactoInterno = getJeigar2Contacto("actualizar");
            } else {
                contactoInterno = contacto;
            }
            System.out.println("Datos Antes: " + contactoInterno.toString());
            Arrays.stream(Datos.values()).forEach(item -> System.out.println(String.format("(%s)%s", item.name(), item.getValor().substring(1))));
            System.out.print("Seleccione la inicial de la operación a realizar: ");
            Scanner scannerActualizar = new Scanner(System.in);
            opcion = scannerActualizar.nextLine();
            try {
                datos = Datos.valueOf(opcion.toUpperCase()); // Paso a mayúsculas
                switch (datos) {
                    case N:
                        contactoNuevoNombre = actualizaNombreContacto(contactoInterno);
                        System.out.println("Datos Actualizados: " + contactoNuevoNombre.toString());
                        break;
                    case T:
                        contactoNuevoTelefono = actualizaTelefonoContacto(contactoInterno);
                        System.out.println("Datos Actualizados: " + contactoNuevoTelefono.toString());
                        break;
                    case A:
                        contactoNuevoNombre = actualizaNombreContacto(contactoInterno);
                        contactoNuevoTelefono = actualizaTelefonoContacto(contactoInterno);
                        try {
                            contactoNuevo = new Jeigar2Contacto(contactoNuevoNombre.getNombre(), contactoNuevoTelefono.getTelefono());
                        } catch (TelefonoException e) {
                        } // No hacer nada porque ya está validado el telefono antes
                        System.out.println("Datos Actualizados: " + contactoNuevo.toString());
                        break;
                }
            } catch (IllegalArgumentException e) {
                System.err.println("Error. Operación no reconocida. " + e.getMessage());
            } catch (ContactoDuplicadoException | ContactoNoEncontradoException exception) {
                System.err.println("Error. No se realiza la actualización. " + exception.getMessage());
            }
        }
    }

    private Jeigar2Contacto actualizaTelefonoContacto(Jeigar2Contacto contacto) throws ContactoNoEncontradoException, ContactoDuplicadoException {
        Scanner scannerActualizar = new Scanner(System.in);
        Jeigar2Contacto contactoNuevo = null;
        Jeigar2Contacto contactoRecuperado = contactos.get(contacto.getTelefono());
        if (contactoRecuperado != null) {
            boolean telefonoValido = false;
            String nombre = contactoRecuperado.getNombre();
            String telefono = null;
            do {
                System.out.println("Introduce un numero de teléfono (solo números, menor o igual a " + Jeigar2Contacto.MAX_DIGITOS_TELEFONO + " dígitos");
                telefono = scannerActualizar.nextLine();
                try {
                    contactoNuevo = new Jeigar2Contacto(nombre, telefono);
                    telefonoValido = true;
                } catch (TelefonoException ex) {
                    System.out.println("Error de validación. " + ex.getMessage());
                }
            } while (!telefonoValido);
            eliminarContacto(contactoRecuperado);
            insertarContacto(contactoNuevo);
        } else {
            throw new ContactoNoEncontradoException("Actualizando Telefono");
        }
        return contactoNuevo;
    }

    private Jeigar2Contacto actualizaNombreContacto(Jeigar2Contacto contacto) throws ContactoNoEncontradoException, ContactoDuplicadoException {
        Scanner scannerActualizar = new Scanner(System.in);
        Jeigar2Contacto contactoNuevo = null;
        Jeigar2Contacto contactoRecuperado = contactos.get(contacto.getNombre());
        if(contactoRecuperado != null) {
            System.out.println("Introduce un nombre");
            String nombre = scannerActualizar.nextLine();
            String telefono = contactoRecuperado.getTelefono();
            try {
                contactoNuevo = new Jeigar2Contacto(nombre, telefono);
            }catch (TelefonoException ex){
                // No hacer nada porque el teléfono es el mismo
            }
            eliminarContacto(contactoRecuperado);
            insertarContacto(contactoNuevo);
        } else {
            throw new ContactoNoEncontradoException("Actualizando nombre");
        }
        return contactoNuevo;
    }

    public void eliminarContacto() {
        System.out.println("Procedemos a eliminar un contacto");
        Jeigar2Contacto contacto = getJeigar2Contacto("eliminar");;
        if (contacto == null) {
            System.out.println("El contacto no existe");
        } else {
            eliminarContacto(contacto);
        }
    }

    public void eliminarContacto(Jeigar2Contacto contacto) {
        System.out.println("Borraremos: " + contacto.toString());
        contacto = contactos.remove(contacto.getNombre());
        if(contacto != null) {
            System.out.println("Borrado por nombre: " + contacto.toString());
        } else {
            System.out.println("No se pudo borrar por nombre");
        }
        contacto = contactos.remove(contacto.getTelefono());
        if(contacto != null) {
            System.out.println("Borrado por teléfono: " + contacto.toString());
        } else {
            System.out.println("No se pudo borrar por teléfono");
        }
    }

    public void contarContactos() {
        System.out.println("Total contacto: " + contactos.size()/2); // Muestra la mitad porque está duplicado por teléfono y nombre
    }

    public void listarContactos(){
        HashMap<String, Jeigar2Contacto> contactosUnicos =  new HashMap<>();
        if (contactos.isEmpty()){
            System.out.println("La lista de contactos está vacía.");
        } else {
            //recorre todos
            contactos.forEach((cadena, contacto) -> {
                // solo introduce los nombres por lo que los teléfonos no los mete
                if(!contactosUnicos.containsKey(contacto.nombre)){
                    contactosUnicos.put(contacto.nombre, contacto);
                }
            });
            // recorre todos, pero solo hay la mitad los que tienen nombre
            contactosUnicos.forEach((cadena, contacto) -> {
                System.out.println(contacto.toString());
            });
        }
    }


    class Jeigar2Contacto {
        public static final int MAX_DIGITOS_TELEFONO = 11;

        private String nombre;
        private String telefono;

        public Jeigar2Contacto(String nombre, String telefono) throws TelefonoException{
            this.nombre = nombre;
            this.setTelefono(telefono);
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public String getTelefono() {
            return telefono;
        }

        public void setTelefono(String telefono) throws TelefonoException {
            try {
                if (telefono == null || telefono.length() == 0) {
                    throw new TelefonoException("debe tener un valor");
                }
                if (telefono.length() > MAX_DIGITOS_TELEFONO) {
                    throw new TelefonoException(String.format("no puede superar los %d dígitos", MAX_DIGITOS_TELEFONO));
                }
                Long.parseLong(telefono); // Solo para forzar la validacion de que sea numérico
                this.telefono = telefono;
            } catch (NumberFormatException e){
                throw new TelefonoException("No permite valores que no sean dígitos");
            }
        }

        @Override
        public String toString() {
            return "Contacto{" +
                    "nombre='" + nombre + '\'' +
                    ", telefono='" + telefono + '\'' +
                    '}';
        }
    }

    class TelefonoException extends Exception{
        TelefonoException(){
            super();
        }

        TelefonoException(String mensaje){
            super("Error: El teléfono " + mensaje);
        }
    }

    class ContactoDuplicadoException extends Exception {
        ContactoDuplicadoException() {
            super("Contacto duplicado, los nombres deben ser únicos y los teléfonos también ");
        }

        ContactoDuplicadoException(String mensaje){
            super("Error: contacto duplicado. " + mensaje);
        }
    }

    class ContactoNoEncontradoException extends Exception {
        ContactoNoEncontradoException() {
            super("Contacto no encontrado.");
        }

        ContactoNoEncontradoException(String mensaje){
            super("Error: contacto no encontrado. " + mensaje);
        }
    }

}
