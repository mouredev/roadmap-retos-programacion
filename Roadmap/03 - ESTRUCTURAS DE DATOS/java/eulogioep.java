import java.util.*;

public class eulogioep {

    public static void main(String[] args) {
        // Ejemplos de estructuras de datos en Java
        ejemplosEstructurasDatos();

        // Agenda de contactos
        agendaContactos();
    }

    public static void ejemplosEstructurasDatos() {
        // ArrayList: Lista dinámica
        List<String> arrayList = new ArrayList<>();
        arrayList.add("Java");
        arrayList.add("Python");
        arrayList.add("C++");
        System.out.println("ArrayList: " + arrayList);

        // LinkedList: Lista enlazada
        List<String> linkedList = new LinkedList<>();
        linkedList.add("Rojo");
        linkedList.add("Verde");
        linkedList.add("Azul");
        System.out.println("LinkedList: " + linkedList);

        // HashSet: Conjunto sin duplicados y sin orden
        Set<Integer> hashSet = new HashSet<>();
        hashSet.add(1);
        hashSet.add(2);
        hashSet.add(2); // No se añade por ser duplicado
        System.out.println("HashSet: " + hashSet);

        // TreeSet: Conjunto ordenado
        Set<Integer> treeSet = new TreeSet<>();
        treeSet.add(3);
        treeSet.add(1);
        treeSet.add(2);
        System.out.println("TreeSet: " + treeSet); // Imprime en orden

        // HashMap: Mapa clave-valor
        Map<String, Integer> hashMap = new HashMap<>();
        hashMap.put("Uno", 1);
        hashMap.put("Dos", 2);
        hashMap.put("Tres", 3);
        System.out.println("HashMap: " + hashMap);

        // Operaciones
        arrayList.remove("Python"); // Borrado
        linkedList.set(1, "Amarillo"); // Actualización
        Collections.sort(arrayList); // Ordenación

        System.out.println("ArrayList después de operaciones: " + arrayList);
        System.out.println("LinkedList después de operaciones: " + linkedList);
    }

    public static void agendaContactos() {
        Scanner scanner = new Scanner(System.in);
        Map<String, String> agenda = new HashMap<>();

        while (true) {
            System.out.println("\n--- Agenda de Contactos ---");
            System.out.println("1. Buscar contacto");
            System.out.println("2. Añadir contacto");
            System.out.println("3. Actualizar contacto");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Mostrar todos los contactos");
            System.out.println("6. Salir");
            System.out.print("Seleccione una opción: ");

            int opcion = scanner.nextInt();
            scanner.nextLine(); // Consumir el salto de línea

            switch (opcion) {
                case 1:
                    buscarContacto(agenda, scanner);
                    break;
                case 2:
                    anadirContacto(agenda, scanner);
                    break;
                case 3:
                    actualizarContacto(agenda, scanner);
                    break;
                case 4:
                    eliminarContacto(agenda, scanner);
                    break;
                case 5:
                    mostrarContactos(agenda);
                    break;
                case 6:
                    System.out.println("¡Hasta luego!");
                    return;
                default:
                    System.out.println("Opción no válida.");
            }
        }
    }

    private static void buscarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el nombre del contacto: ");
        String nombre = scanner.nextLine();
        String telefono = agenda.get(nombre);
        if (telefono != null) {
            System.out.println("Teléfono de " + nombre + ": " + telefono);
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }

    private static void anadirContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el nombre del contacto: ");
        String nombre = scanner.nextLine();
        String telefono = solicitarTelefono(scanner);
        agenda.put(nombre, telefono);
        System.out.println("Contacto añadido con éxito.");
    }

    private static void actualizarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el nombre del contacto a actualizar: ");
        String nombre = scanner.nextLine();
        if (agenda.containsKey(nombre)) {
            String telefono = solicitarTelefono(scanner);
            agenda.put(nombre, telefono);
            System.out.println("Contacto actualizado con éxito.");
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }

    private static void eliminarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el nombre del contacto a eliminar: ");
        String nombre = scanner.nextLine();
        if (agenda.remove(nombre) != null) {
            System.out.println("Contacto eliminado con éxito.");
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }

    private static void mostrarContactos(Map<String, String> agenda) {
        if (agenda.isEmpty()) {
            System.out.println("La agenda está vacía.");
        } else {
            for (Map.Entry<String, String> entry : agenda.entrySet()) {
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }
        }
    }

    private static String solicitarTelefono(Scanner scanner) {
        while (true) {
            System.out.print("Ingrese el número de teléfono (máximo 11 dígitos): ");
            String telefono = scanner.nextLine();
            if (telefono.matches("\\d{1,11}")) {
                return telefono;
            }
            System.out.println("Número no válido. Debe ser numérico y tener máximo 11 dígitos.");
        }
    }
}