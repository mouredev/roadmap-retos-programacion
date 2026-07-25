import java.util.*;
public class Dredux2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        /*
         * EJERCICIO:
         * - Muestra ejemplos de creación de todas las estructuras de datos soportadas por defecto.
         * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
         */

        // Array
        int[] array = {1, 2, 3, 4, 5};
        array[2] = 10; // Actualización
        Arrays.sort(array); // Ordenación

        // List
        List<Integer> lista = new ArrayList<>();
        lista.add(1); // Inserción
        lista.add(2); // Inserción
        lista.remove(0); // Borrado
        lista.set(0, 10); // Actualización
        Collections.sort(lista); // Ordenación

        // Set
        Set<Integer> set = new HashSet<>();
        set.add(1); // Inserción
        set.remove(1); // Borrado

        // Map
        Map<String, Integer> map = new HashMap<>();
        map.put("uno", 1); // Inserción
        map.remove("uno"); // Borrado
        map.put("uno", 10); // Actualización

        EjercicioExtra(sc);
    }

    /* DIFICULTAD EXTRA (opcional):
     * Crea una agenda de contactos por terminal.
     * - Debes implementar funcionalidades de búsqueda, inserción, actualización
     *   y eliminación de contactos.
     * - Cada contacto debe tener un nombre y un número de teléfono.
     * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
     *   y a continuación los datos necesarios para llevarla a cabo.
     * - El programa no puede dejar introducir números de teléfono no númericos y con más
     *   de 11 dígitos (o el número de dígitos que quieras).
     * - También se debe proponer una operación de finalización del programa.
     */

    public static void EjercicioExtra(Scanner sc) {
        Map<String, Integer> agenda = new HashMap<>();
        String nombre;
        int telefono;
        int opcion = 0;
        while (opcion != 5) {
            System.out.println("\n*** Agenda ***");
            System.out.println("1. Buscar Contacto");
            System.out.println("2. Nuevo Contacto");
            System.out.println("3. Actualizar Contacto");
            System.out.println("4. Eliminar Contacto");
            System.out.println("5. Salir");
            System.out.print("Introduce una opción: ");
            try {
                opcion = sc.nextInt();
                if (opcion < 1 || opcion > 5) {
                    System.out.println("ERROR: Opción no válida.");
                    continue;
                }

                switch (opcion) {
                    case 1:
                        System.out.print("Introduce el nombre del contacto: ");
                        nombre = sc.next();
                        if (agenda.containsKey(nombre)) {
                            System.out.println("El número de teléfono de " + nombre + " es " + agenda.get(nombre));
                        } else {
                            System.out.println("El contacto no existe.");
                        }
                        continue;
                    case 2:
                        System.out.print("Introduce el nombre del contacto: ");
                        nombre = sc.next();
                        System.out.print("Introduce el número de teléfono: ");
                        telefono = sc.nextInt();

                        while (String.valueOf(telefono).length() != 9) {
                            System.out.println("Número de teléfono no válido.");
                            System.out.print("Introduce el número de teléfono: ");
                            telefono = sc.nextInt();
                        }

                        agenda.put(nombre, telefono);
                        continue;
                    case 3:
                        System.out.print("Introduce el nombre del contacto: ");
                        nombre = sc.next();
                        if (agenda.containsKey(nombre)) {
                            System.out.print("Introduce el nuevo número de teléfono: ");
                            telefono = sc.nextInt();

                            while (String.valueOf(telefono).length() != 9) {
                                System.out.println("Número de teléfono no válido.");
                                System.out.print("Introduce el número de teléfono: ");
                                telefono = sc.nextInt();
                            }

                            agenda.put(nombre, telefono);
                        } else {
                            System.out.println("El contacto no existe.");
                        }
                        continue;
                    case 4:
                        System.out.print("Introduce el nombre del contacto: ");
                        nombre = sc.next();
                        if (agenda.containsKey(nombre)) {
                            agenda.remove(nombre);
                            System.out.println("Contacto eliminado.");
                        } else {
                            System.out.println("El contacto no existe.");
                        }
                }
                if (opcion == 5) {
                    System.out.println("Saliendo...");
                }
            } catch (InputMismatchException e) {
                System.out.println("ERROR: Opción no válida.");
                sc.next();
            }
        }
    }
}