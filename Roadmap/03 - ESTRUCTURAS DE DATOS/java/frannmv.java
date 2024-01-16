import java.util.Scanner;
import java.util.HashMap;

public class frannmv {

    public enum Operaciones {
        BUSCAR(1),
        INSERTAR(2),
        ACTUALIZAR(3),
        ELIMINAR(4);

        private final int valor;

        Operaciones(int valor) {
            this.valor = valor;
        }
    }
    public static void main(String[] args) {

        int numTelefono,flag = 0, proxOperacion;
        String nombre;
        Scanner keyboard = new Scanner (System.in);
        HashMap<String, Integer> agenda = new HashMap<>();

        while(flag != -1){

            menu();

            proxOperacion = keyboard.nextInt();
            keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer
            Operaciones op = obtenerOperacion(proxOperacion);

            switch (op){
                case BUSCAR:
                    System.out.println("Ingrese el nombre del contacto a buscar:");
                    nombre = keyboard.nextLine();

                    System.out.println("El numero de " + nombre + " es: " + agenda.get(nombre));
                    break;

                case ELIMINAR:
                    System.out.println("Ingrese el nombre del contacto a eliminar: ");
                    nombre = keyboard.nextLine();
                    agenda.remove(nombre);
                    System.out.println("Contacto Eliminado!");
                    break;

                case INSERTAR:
                    System.out.println("Agregue el nombre del contacto: ");
                    nombre = keyboard.nextLine();

                    System.out.println("Agregue el telefono del contacto: ");
                    numTelefono = keyboard.nextInt();
                    keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer

                    agenda.put(nombre, numTelefono);
                    break;

                case ACTUALIZAR:
                    System.out.println("El numero de que persona desea actualizar?:");
                    nombre = keyboard.nextLine();

                    System.out.println("Ingrese el nuevo numero: ");
                    numTelefono= keyboard.nextInt();
                    keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer

                    agenda.replace(nombre,numTelefono);
                    System.out.println("Contacto actualizado!");
                    break;

                default:
                    System.out.println("Ingrese un numero valido!");
            }

            System.out.println(agenda);

            System.out.println("Ingrese:\n" +
                                "1 - Para Continuar\n" +
                                "-1 - Para Finalizar el programa");
            flag = keyboard.nextInt();
            keyboard.nextLine(); // Consumir el caracter \n que deja keyboard.nextInt() en el bufer

        }

        System.out.println(agenda);
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
}
