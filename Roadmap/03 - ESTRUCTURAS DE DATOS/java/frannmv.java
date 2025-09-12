import java.util.Scanner;
import java.util.HashMap;

public class frannmv {

    public enum Operaciones {
        BUSCAR(1),
        INSERTAR(2),
        ACTUALIZAR(3),
        ELIMINAR(4),
        MOSTRAR(5),
        EXIT(6);

        private final int valor;

        Operaciones(int valor) {
            this.valor = valor;
        }
    }

    public static Scanner keyboard = new Scanner(System.in);
    public static HashMap<String, Long> agenda = new HashMap<>();
    public static long numTelefono;
    public static String nombre;

    public static void main(String[] args) {

        while (true) {

            mostrarMenu();

            switch (operacionElegida()) {

                case BUSCAR:
                    System.out.println("Ingrese el nombre del contacto a buscar:");
                    nombre = keyboard.nextLine();
                    buscar(nombre);
                    break;

                case ELIMINAR:
                    System.out.println("Ingrese el nombre del contacto a eliminar: ");
                    nombre = keyboard.nextLine();
                    eliminar(nombre);
                    break;

                case INSERTAR:
                    insertar();
                    break;

                case ACTUALIZAR:
                    actualizar();
                    break;

                case MOSTRAR:
                    mostrar();
                    break;

                case EXIT:
                    System.out.println("Hasta luego, vuelva prontos!");
                    System.exit(0);
                    break;

                case null:
                    System.out.println("Ingrese un numero valido!");

            }
        }
    }

    private static void mostrarMenu() {
        for (Operaciones operacion : Operaciones.values()) {
            System.out.println(operacion.valor + ". " + operacion);
        }
    }

    private static Operaciones obtenerOperacion(int valor) {
        for (Operaciones operacion : Operaciones.values()) {
            if (valor == operacion.valor) {
                return operacion;
            }
        }
        return null;
    }

    private static Operaciones operacionElegida() {

        int valor = keyboard.nextInt();
        keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer
        return obtenerOperacion(valor);
    }

    private static boolean existeContacto(String nombre) {
        return agenda.containsKey(nombre);
    }

    private static void buscar(String nombre) {

        if (existeContacto(nombre)) {
            System.out.println("El numero de " + nombre + " es: " + agenda.get(nombre));
        } else {
            System.out.println("El usuario no se encuentra en el sistema! ");
        }
    }

    private static void eliminar(String nombre) {

        if (existeContacto(nombre)) {
            agenda.remove(nombre);
            System.out.println("Contacto Eliminado!");
        } else {
            System.out.println("Ingrese un nombre de usuario valido!");
        }
    }

    private static boolean cumpleCondiciones(long telefono) {
        String telStr = Long.toString(telefono);
        return telStr.length() <= 11;
    }

    private static void insertar() {
        System.out.println("Agregue el nombre del contacto: ");
        nombre = keyboard.nextLine();

        System.out.println("Agregue el telefono del contacto: ");

        numTelefono = keyboard.nextLong();
        keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer

        if (cumpleCondiciones(numTelefono)) {
            agenda.put(nombre, numTelefono);
        } else {
            System.out.println("El numero de telefono tiene que tener al menos un digito y menos que 11 digitos");
        }

    }

    private static void actualizar() {
        System.out.println("Que persona desea actualizar?");
        nombre = keyboard.nextLine();
        if (existeContacto(nombre)) {
            System.out.println("Ingrese el nuevo numero: ");
            numTelefono = keyboard.nextLong();
            keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer

            agenda.replace(nombre, numTelefono);
            System.out.println("Contacto actualizado!");
        } else {
            System.out.println("El usuario no se encuentra en el sistema!");
        }
    }

    private static void mostrar() {
        System.out.println(agenda);
    }
}
