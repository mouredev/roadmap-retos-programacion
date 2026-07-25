import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class agusrosero {
    public static void main(String[] args) {
        // Arrays
        String[] array = new String[3];

        array[0] = "Hola";
        array[1] = "Mundo";
        array[2] = "Java";

        // Lista
        List<String> list = new ArrayList<>();
        list.add("Hola");
        list.add("Mundo");
        list.add("Java");

        list.clear();

        // Set
        Set<String> set = new HashSet<>();

        set.add("Hola");
        set.add("Mundo");
        set.add("Java");

        set.clear();

        // Map
        Map<String, String> hashMap = new HashMap<>();

        hashMap.put("Hola", "Mundo");
        hashMap.put("Java", "Kotlin");

        hashMap.clear();

        /*
         * * DIFICULTAD EXTRA (opcional):
         * Crea una agenda de contactos por terminal.
         * - Debes implementar funcionalidades de búsqueda, inserción, actualización y
         * eliminación de contactos.
         * - Cada contacto debe tener un nombre y un número de teléfono.
         * - El programa solicita en primer lugar cuál es la operación que se quiere
         * realizar, y a continuación
         * los datos necesarios para llevarla a cabo.
         * - El programa no puede dejar introducir números de teléfono no númericos y
         * con más de 11 dígitos.
         * (o el número de dígitos que quieras)
         * - También se debe proponer una operación de finalización del programa.
         */
        System.out.println("*** Agenda de contactos ***");
        System.out.println("1. Buscar contacto");
        System.out.println("2. Insertar contacto");
        System.out.println("3. Actualizar contacto");
        System.out.println("4. Eliminar contacto");
        System.out.println("5. Salir");

        Scanner scanner = new Scanner(System.in);
        int option = 0;
        List<String> contacts = new ArrayList<>();

        while (true) {
            System.out.print("Seleccione una opcion: ");
            option = scanner.nextInt();
            switch (option) {
                case 1:
                    System.out.print("Ingrese un nombre: ");
                    String search = scanner.next();
                    for (String contact : contacts) {
                        if (contact.contains(search)) {
                            System.out.println(contact);
                        } else {
                            System.out.println("Contacto no encontrado");
                        }
                    }
                    break;
                case 2:
                    System.out.print("Ingrese un nombre: ");
                    String name = scanner.next();
                    System.out.print("Ingrese un número de teléfono: ");
                    String phoneNumber = scanner.next();
                    contacts.add(name + " - " + phoneNumber);
                    break;
                case 3:
                    System.out.print("Ingrese el nombre del contacto a actualizar: ");
                    String oldName = scanner.next();
                    System.out.print("Ingrese el nuevo nombre: ");
                    String newName = scanner.next();
                    System.out.print("Ingrese el nuevo número de teléfono: ");
                    String newPhoneNumber = scanner.next();
                    for (String contact : contacts) {
                        if (contact.contains(oldName)) {
                            contacts.remove(contact);
                            contacts.add(newName + " - " + newPhoneNumber);
                        }
                    }
                    break;
                case 4:
                    System.out.print("Ingrese el contacto a eliminar: ");
                    String contact = scanner.next();
                    contacts.remove(contact);
                    break;
                case 5:
                    System.out.println("Saliendo...");
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Opción no válida");
            }
        }
    }
}
