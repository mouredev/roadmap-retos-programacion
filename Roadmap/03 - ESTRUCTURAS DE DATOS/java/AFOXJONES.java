
import java.util.*;
public class AFOXJONES{
        // Mapa para almacenar los contactos (nombre -> número de teléfono)
    private static Map<String, String> contacts = new HashMap<>();
    private static final int MAX_PHONE_DIGITS = 11; // Límite de dígitos del número de teléfono


    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args){

          // 1. Array
        System.out.println("Array:");
        int[] array = {5, 3, 8, 1};
        System.out.println("Original: " + Arrays.toString(array));
        array[1] = 10; // Actualización
        System.out.println("Actualizado: " + Arrays.toString(array));
        Arrays.sort(array); // Ordenación
        System.out.println("Ordenado: " + Arrays.toString(array));

        // 2. ArrayList (Lista)
        System.out.println("\nArrayList:");
        List<Integer> arrayList = new ArrayList<>(Arrays.asList(5, 3, 8, 1));
        System.out.println("Original: " + arrayList);
        arrayList.add(7); // Inserción
        System.out.println("Añadido 7: " + arrayList);
        arrayList.remove(Integer.valueOf(3)); // Borrado
        System.out.println("Borrado 3: " + arrayList);
        arrayList.set(1, 10); // Actualización
        System.out.println("Actualizado: " + arrayList);
        arrayList.sort(Comparator.naturalOrder()); // Ordenación
        System.out.println("Ordenado: " + arrayList);

        // 3. HashSet (Conjunto)
        System.out.println("\nHashSet:");
        Set<Integer> hashSet = new HashSet<>(Arrays.asList(5, 3, 8, 1));
        System.out.println("Original: " + hashSet);
        hashSet.add(7); // Inserción
        System.out.println("Añadido 7: " + hashSet);
        hashSet.remove(3); // Borrado
        System.out.println("Borrado 3: " + hashSet);
        // No admite ordenación directamente; convertir a lista
        List<Integer> sortedSet = new ArrayList<>(hashSet);
        Collections.sort(sortedSet);
        System.out.println("Ordenado: " + sortedSet);

        // 4. HashMap (Mapa)
        System.out.println("\nHashMap:");
        Map<String, Integer> hashMap = new HashMap<>();
        hashMap.put("A", 5); // Inserción
        hashMap.put("B", 3);
        hashMap.put("C", 8);
        System.out.println("Original: " + hashMap);
        hashMap.put("B", 10); // Actualización
        System.out.println("Actualizado B: " + hashMap);
        hashMap.remove("A"); // Borrado
        System.out.println("Borrado A: " + hashMap);
        // No admite ordenación directamente; usar TreeMap
        Map<String, Integer> sortedMap = new TreeMap<>(hashMap);
        System.out.println("Ordenado: " + sortedMap);

        // 5. Queue (Cola)
        System.out.println("\nQueue:");
        Queue<Integer> queue = new LinkedList<>(Arrays.asList(5, 3, 8, 1));
        System.out.println("Original: " + queue);
        queue.add(7); // Inserción
        System.out.println("Añadido 7: " + queue);
        queue.poll(); // Borrado (primer elemento)
        System.out.println("Borrado primer elemento: " + queue);

        // 6. Stack (Pila)
        System.out.println("\nStack:");
        Stack<Integer> stack = new Stack<>();
        stack.push(5); // Inserción
        stack.push(3);
        stack.push(8);
        stack.push(1);
        System.out.println("Original: " + stack);
        stack.pop(); // Borrado (último elemento)
        System.out.println("Borrado último elemento: " + stack);
        stack.push(7); // Inserción
        System.out.println("Añadido 7: " + stack);

        extra();

    
    }

    public static void extra(){
          Scanner scanner = new Scanner(System.in);
        boolean running = true;

        System.out.println("Bienvenido a la Agenda de Contactos");

        while (running) {
            System.out.println("\n¿Qué deseas hacer?");
            System.out.println("1. Insertar contacto");
            System.out.println("2. Buscar contacto");
            System.out.println("3. Actualizar contacto");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Mostrar todos los contactos");
            System.out.println("6. Salir");
            System.out.print("Selecciona una opción: ");
            
            String option = scanner.nextLine();

            switch (option) {
                case "1":
                    insertContact(scanner);
                    break;
                case "2":
                    searchContact(scanner);
                    break;
                case "3":
                    updateContact(scanner);
                    break;
                case "4":
                    deleteContact(scanner);
                    break;
                case "5":
                    showAllContacts();
                    break;
                case "6":
                    running = false;
                    System.out.println("¡Hasta luego!");
                    break;
                default:
                    System.out.println("Opción no válida. Inténtalo de nuevo.");
            }
        }

        scanner.close();
    }

    // Método para insertar un contacto
    private static void insertContact(Scanner scanner) {
        System.out.print("Introduce el nombre del contacto: ");
        String name = scanner.nextLine().trim();

        if (contacts.containsKey(name)) {
            System.out.println("El contacto ya existe.");
            return;
        }

        System.out.print("Introduce el número de teléfono: ");
        String phone = scanner.nextLine().trim();

        if (isValidPhone(phone)) {
            contacts.put(name, phone);
            System.out.println("Contacto agregado correctamente.");
        } else {
            System.out.println("Número de teléfono no válido. Debe ser numérico y tener hasta " + MAX_PHONE_DIGITS + " dígitos.");
        }
    }

    // Método para buscar un contacto
    private static void searchContact(Scanner scanner) {
        System.out.print("Introduce el nombre del contacto a buscar: ");
        String name = scanner.nextLine().trim();

        if (contacts.containsKey(name)) {
            System.out.println("Contacto encontrado: " + name + " -> " + contacts.get(name));
        } else {
            System.out.println("No se encontró ningún contacto con ese nombre.");
        }
    }

    // Método para actualizar un contacto
    private static void updateContact(Scanner scanner) {
        System.out.print("Introduce el nombre del contacto a actualizar: ");
        String name = scanner.nextLine().trim();

        if (contacts.containsKey(name)) {
            System.out.print("Introduce el nuevo número de teléfono: ");
            String newPhone = scanner.nextLine().trim();

            if (isValidPhone(newPhone)) {
                contacts.put(name, newPhone);
                System.out.println("Contacto actualizado correctamente.");
            } else {
                System.out.println("Número de teléfono no válido.");
            }
        } else {
            System.out.println("No se encontró ningún contacto con ese nombre.");
        }
    }

    // Método para eliminar un contacto
    private static void deleteContact(Scanner scanner) {
        System.out.print("Introduce el nombre del contacto a eliminar: ");
        String name = scanner.nextLine().trim();

        if (contacts.containsKey(name)) {
            contacts.remove(name);
            System.out.println("Contacto eliminado correctamente.");
        } else {
            System.out.println("No se encontró ningún contacto con ese nombre.");
        }
    }

    // Método para mostrar todos los contactos
    private static void showAllContacts() {
        if (contacts.isEmpty()) {
            System.out.println("No hay contactos en la agenda.");
        } else {
            System.out.println("Lista de contactos:");
            contacts.forEach((name, phone) -> System.out.println(name + " -> " + phone));
        }
    }

    // Método para validar un número de teléfono
    private static boolean isValidPhone(String phone) {
        return phone.matches("\\d{1," + MAX_PHONE_DIGITS + "}");
    }
}