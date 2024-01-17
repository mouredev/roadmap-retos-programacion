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
    public static Scanner keyboard = new Scanner (System.in);
    public static HashMap<String, Integer> agenda = new HashMap<>();
    public static Operaciones op;
    public static int numTelefono;
    public static String nombre;
    public static void main(String[] args) {

        int flag = 0, proxOperacion;

        while(true){

            menu();

            proxOperacion = keyboard.nextInt();
            keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer
            op = obtenerOperacion(proxOperacion);

            switch (op){
                case BUSCAR:
                    buscar();
                    break;

                case ELIMINAR:
                    eliminar();
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
                    System.exit(0);
                    break;
                default:
                    System.out.println("Ingrese un numero valido!");
            }

        }
    }
    private static void menu(){
        for(Operaciones operacion : Operaciones.values()){
            System.out.println(operacion.valor + ". " + operacion.name());
        }
    }
    private static Operaciones obtenerOperacion(int valor){
        for(Operaciones operacion : Operaciones.values()){
            if(valor == operacion.valor){
                return operacion;
            }
        }
        return null;
    }

    private static void buscar(){

        System.out.println("Ingrese el nombre del contacto a buscar:");
        nombre = keyboard.nextLine();

        System.out.println("El numero de " + nombre + " es: " + agenda.get(nombre));
    }

    private static void eliminar(){

        System.out.println("Ingrese el nombre del contacto a eliminar: ");
        nombre = keyboard.nextLine();
        agenda.remove(nombre);
        System.out.println("Contacto Eliminado!");

    }

    private static void insertar(){
        System.out.println("Agregue el nombre del contacto: ");
        nombre = keyboard.nextLine();

        System.out.println("Agregue el telefono del contacto: ");
        numTelefono = keyboard.nextInt();
        keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer

        agenda.put(nombre, numTelefono);

    }
    private static void actualizar(){
        System.out.println("El numero de que persona desea actualizar?:");
        nombre = keyboard.nextLine();

        System.out.println("Ingrese el nuevo numero: ");
        numTelefono= keyboard.nextInt();
        keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer

        agenda.replace(nombre,numTelefono);
        System.out.println("Contacto actualizado!");
    }

    private static void mostrar(){
        System.out.println(agenda);
    }
}
