
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por
 * defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y
 * eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere
 * realizar, y a continuación
 * los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y
 * con más de 11 dígitos.
 * (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
/**
 * JuanCamiloFVX
 */
import java.util.*;

public class JuanCamiloFVX {

    // INICIALIZACIÓN:
    // Array
    static int[] array = new int[4]; // Inicializa un array de tamaño 4 con valores por defecto (0, 0, 0, 0).

    // ArrayList
    static ArrayList<String> arrayList = new ArrayList<>(); // Inicializa un ArrayList vacío. []

    // Map
    static Map<Integer, String> map = new HashMap<>(); // Inicializa un HashMap vacío. {}

    // Stack
    static Stack<Integer> stack = new Stack<>(); // Inicializa una pila vacía. []<=>

    // Queue
    static Queue<Integer> queue = new LinkedList<>(); // Inicializa una cola vacía. <-[]<-

    public static void main(String[] args) {
        imprimirContenidos();
        insertar();
        imprimirContenidos();
        borrar();
        imprimirContenidos();
        actualizar();
        imprimirContenidos();
        ordenar();
        imprimirContenidos();
        agendaContactos();
    }

    static void insertar() {
        // Array
        array[0] = 2;
        array[1] = 3;
        array[2] = 5;
        array[3] = 6;

        // ArrayList
        arrayList.add("uno");
        arrayList.add("dos");
        arrayList.add("tres");
        arrayList.add("cuatro");

        // Map
        map.put(0, "uno");
        map.put(1, "dos");

        // Stack
        stack.push(1);
        stack.push(2);
        stack.push(3);

        // Queue
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
    }

    static void ordenar() {
        // Array
        Arrays.sort(array); // Ordena el array.

        // ArrayList
        Collections.sort(arrayList); // Ordena el ArrayList.

        // Map - No tiene un método para ordenarlo.

        // Stack - No es necesario ordenar un Stack ya que representa una pila.

        // Queue - No es necesario ordenar una Queue ya que representa una cola.
    }

    static void borrar() {
        // Array
        array[0] = 0;

        // ArrayList
        arrayList.remove("dos");

        // Map
        map.remove(1);

        // Stack
        stack.pop(); // Elimina el elemento superior de la pila.

        // Queue
        if (!queue.isEmpty()) {
            queue.poll(); // Elimina el elemento frontal de la cola si no está vacía.
        }
    }

    static void actualizar() {
        // Array
        array[0] = 7;

        // ArrayList
        arrayList.set(0, "UNO"); // Actualiza el primer elemento del ArrayList.

        // Map
        map.put(0, "UNO"); // Actualiza el valor asociado a la clave 0 en el mapa.

        // Stack
        if (!stack.isEmpty()) {
            stack.pop(); // Elimina el elemento superior de la pila.
            stack.push(99); // Inserta el valor 99 en la pila.
        }

        // Queue
        if (!queue.isEmpty()) {
            queue.poll(); // Elimina el elemento frontal de la cola.
            queue.offer(999); // Inserta el valor 999 en la cola.
        }
    }

    static void imprimirContenidos() {
        System.out.println("Array: " + Arrays.toString(array));
        System.out.println("ArrayList: " + arrayList);
        System.out.println("Map: " + map);
        System.out.println("Stack: " + stack);
        System.out.println("Queue: " + queue);
        System.out.println("--------------------------------");
    }

    // DIFICULTAD EXTRA

    static void agendaContactos() {
        Scanner scanner = new Scanner(System.in);
        Map<String, String> agenda = new HashMap<>();

        while (true) {
            System.out.println(" ");
            System.out.println("Agenda de Contactos");
            System.out.println(" ");
            System.out.println("---------------------------");
            System.out.println("| 1: Buscar Contacto      |");
            System.out.println("| 2: Agregar Contacto     |");
            System.out.println("| 3: Actualizar Contacto  |");
            System.out.println("| 4: Eliminar Contacto    |");
            System.out.println("| 5: Salir                |");
            System.out.println("---------------------------");
            System.out.println(" ");
            System.out.print("+ Seleccione una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine(); // Consumir el salto de línea después de la opción

            switch (opcion) {
                case 1:
                    buscarContacto(agenda, scanner);
                    break;
                case 2:
                    insertarContacto(agenda, scanner);
                    break;
                case 3:
                    actualizarContacto(agenda, scanner);
                    break;
                case 4:
                    eliminarContacto(agenda, scanner);
                    break;
                case 5:
                    System.out.println("¡Hasta la proxima!");
                    System.exit(0);
                default:
                    System.out.println("Opción no válida. Inténtalo de nuevo.");
            }
        }
    }

    private static void buscarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el nombre del contacto a buscar: ");
        String nombre = scanner.nextLine();

        if (agenda.containsKey(nombre)) {
            String telefono = agenda.get(nombre);
            System.out.println("Número de teléfono de " + nombre + ": " + telefono);
        } else {
            System.out.println("El contacto no se encuentra en la agenda.");
        }
    }

    private static void insertarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el nombre del contacto: ");
        String nombre = scanner.nextLine();

        // Verificar que el nombre no esté en la agenda
        if (agenda.containsKey(nombre)) {
            System.out.println("El contacto ya existe en la agenda.");
            return;
        }

        System.out.print("Ingrese el número de teléfono: ");
        String telefono = scanner.nextLine();

        // Verificar que el número de teléfono sea numérico y tenga 11 dígitos
        try {
            validarNumeroTelefono(telefono);
        } catch (IllegalArgumentException e) {
            return;
        }

        agenda.put(nombre, telefono);
        System.out.println("Contacto insertado con éxito.");
    }

    private static void actualizarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el nombre del contacto a actualizar: ");
        String nombre = scanner.nextLine();

        if (agenda.containsKey(nombre)) {
            System.out.print("Ingrese el nuevo número de teléfono: ");
            String nuevoTelefono = scanner.nextLine();

            // Verificar que el nuevo número de teléfono sea numérico y tenga 11 dígitos
            try {
                validarNumeroTelefono(nuevoTelefono);
            } catch (IllegalArgumentException e) {
                return;
            }

            agenda.put(nombre, nuevoTelefono);
            System.out.println("Contacto actualizado con éxito.");
        } else {
            System.out.println("El contacto no se encuentra en la agenda.");
        }
    }

    private static void eliminarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el nombre del contacto a eliminar: ");
        String nombre = scanner.nextLine();

        if (agenda.containsKey(nombre)) {
            agenda.remove(nombre);
            System.out.println("Contacto eliminado con éxito.");
        } else {
            System.out.println("El contacto no se encuentra en la agenda.");
        }
    }

    private static void validarNumeroTelefono(String telefono) {
        if (!telefono.matches("\\d{11}")) {
            System.out.println("Número de teléfono no válido. Debe tener 11 dígitos.");
            throw new IllegalArgumentException("Número de teléfono no válido");
        }
    }
}
