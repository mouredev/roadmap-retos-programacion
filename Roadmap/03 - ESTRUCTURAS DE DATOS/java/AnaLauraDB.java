import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.HashMap;
import java.util.Scanner;

public class AnaLauraDB {
    public static void main(String[] args) {
        // creación de todas las estructuras soportadas por defecto

        // Arreglos
        int[] num = new int[10];
        for (int i = 0; i < num.length; i++) {
            num[i] = i + 1; // inicializar el arreglo con ceros
            System.out.println("Elemento del arreglo num: " + num[i]);
        }

        // Pilas y colas
        Stack<Integer> pilas = new Stack<>();
        pilas.push(99); // ejemplo de uso: agregar un elemento
        int elementoPila = pilas.pop(); // obtener y eliminar el elemento
        System.out.println("Elemento de la pila: " + elementoPila);

        Queue<Integer> colas = new LinkedList<>();
        colas.add(42); // ejemplo de uso: agregar un elemento
        int elementoCola = colas.poll(); // obtener y eliminar el elemento
        System.out.println("Elemento de la cola: " + elementoCola);

        // Matrices y diccionarios
        int[][] matriz = new int[2][2];
        // Llenar la matriz con valores de ejemplo
        int valor = 1;
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = valor++;
            }
        }
        System.out.println("Elemento de la matriz: " + matriz[0][0]);
        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        final int MAX_DIGITS = 11;

        while (running) {

            HashMap<String, String> Contactos = new HashMap<>();
            // Ejemplo de uso: agregar un contacto y obtenerlo
            Contactos.put("Ana", "555451234");
            Contactos.put("Richard", "555569878");
            Contactos.put("Juan", "555098765");
            Contactos.put("Gabi", "5522153042");
            Contactos.put("Toño", "555123456");
            Contactos.put("Ale", "555987654");
            String telefono = Contactos.get("Ana");
            System.out.println("Teléfono de Ana: " + telefono);

            System.out.println("\nOperaciones disponibles:");
            System.out.println("1. Buscar contacto");
            System.out.println("2. Insertar contacto");
            System.out.println("3. Actualizar contacto");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Salir");
            System.out.print("Selecciona una opción: ");
            String opcion = scanner.nextLine();

            switch (opcion) {
                case "1": // Buscar
                    System.out.print("Nombre del contacto a buscar: ");
                    String nombreBuscar = scanner.nextLine();
                    if (Contactos.containsKey(nombreBuscar)) {
                        System.out.println("Teléfono de " + nombreBuscar + ": " + Contactos.get(nombreBuscar));
                    } else {
                        System.out.println("Contacto no encontrado.");
                    }
                    break;
                case "2": // Insertar
                    System.out.print("Nombre del nuevo contacto: ");
                    String nombreInsertar = scanner.nextLine();
                    System.out.print("Número de teléfono: ");
                    String telefonoInsertar = scanner.nextLine();
                    if (!telefonoInsertar.matches("\\d{1," + MAX_DIGITS + "}")) {
                        System.out.println("Número inválido. Debe ser numérico y máximo " + MAX_DIGITS + " dígitos.");
                    } else {
                        Contactos.put(nombreInsertar, telefonoInsertar);
                        System.out.println("Contacto agregado.");
                    }
                    break;
                case "3": // Actualizar
                    System.out.print("Nombre del contacto a actualizar: ");
                    String nombreActualizar = scanner.nextLine();
                    if (Contactos.containsKey(nombreActualizar)) {
                        System.out.print("Nuevo número de teléfono: ");
                        String telefonoActualizar = scanner.nextLine();
                        if (!telefonoActualizar.matches("\\d{1," + MAX_DIGITS + "}")) {
                            System.out
                                    .println("Número inválido. Debe ser numérico y máximo " + MAX_DIGITS + " dígitos.");
                        } else {
                            Contactos.put(nombreActualizar, telefonoActualizar);
                            System.out.println("Contacto actualizado.");
                        }
                    } else {
                        System.out.println("Contacto no encontrado.");
                    }
                    break;
                case "4": // Eliminar
                    System.out.print("Nombre del contacto a eliminar: ");
                    String nombreEliminar = scanner.nextLine();
                    if (Contactos.containsKey(nombreEliminar)) {
                        Contactos.remove(nombreEliminar);
                        System.out.println("Contacto eliminado.");
                    } else {
                        System.out.println("Contacto no encontrado.");
                    }
                    break;
                case "5": // Salir
                    running = false;
                    System.out.println("Programa finalizado.");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        }
        scanner.close();

    }

}
