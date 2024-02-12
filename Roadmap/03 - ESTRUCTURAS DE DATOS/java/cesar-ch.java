import java.util.*;

public class Main {
    public static void main(String[] args) {

        // Listas
        List<String> lista = new ArrayList<>();

        // Insertamos elementos en la lista
        lista.add("Hola");
        lista.add("Mundo");
        lista.add("Java");

        // Eliminamos elementos de la lista
        lista.remove("Hola");

        // Actualizamos elementos de la lista
        lista.set(0, "Adiós");

        // Ordenamos la lista
        lista.sort(Comparator.naturalOrder());

        // Imprimimos la lista
        System.out.println(lista);

        // Sets
        Set<String> conjunto = new HashSet<>();

        // Insertamos elementos en el conjunto
        conjunto.add("Hola");
        conjunto.add("Mundo");
        conjunto.add("Java");

        // Eliminamos elementos del conjunto
        conjunto.remove("Hola");

        // Imprimimos el conjunto
        System.out.println(conjunto);

        // Maps
        Map<String, Integer> mapa = new HashMap<>();

        // Insertamos elementos en el mapa
        mapa.put("Hola", 1);
        mapa.put("Mundo", 2);
        mapa.put("Java", 3);

        // Eliminamos elementos del mapa
        mapa.remove("Hola");

        crearAgenda();

    }

    public static void crearAgenda() {
        ArrayList<String> nombres = new ArrayList<>();
        ArrayList<String> telefonos = new ArrayList<>();
        boolean run = true;
        Scanner scanner = new Scanner(System.in);

        while (run) {
            System.out.println("Ingrese la operación a realizar:");
            System.out.println("1. Buscar contacto");
            System.out.println("2. Insertar contacto");
            System.out.println("3. Actualizar contacto");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Salir");

            String operacion = scanner.nextLine();

            if ("1".equals(operacion)) {
                if (nombres.isEmpty()) {
                    System.out.println("Agenda vacía");
                    continue;
                }
                System.out.println("Ingrese el nombre del contacto a buscar:");
                String nombreBuscar = scanner.nextLine();
                boolean contactoEncontrado = false;

                for (int i = 0; i < nombres.size(); i++) {
                    if (nombres.get(i).equals(nombreBuscar)) {
                        System.out.println("Contacto encontrado: " + "Nombre: " + nombres.get(i) + ", Teléfono: "
                                + telefonos.get(i));
                        contactoEncontrado = true;
                        break;
                    }
                }

                if (!contactoEncontrado) {
                    System.out.println("Contacto no encontrado");
                }
            } else if ("2".equals(operacion)) {
                System.out.println("Ingrese el nombre del contacto a insertar:");
                String nombreInsertar = scanner.nextLine();
                System.out.println("Ingrese el teléfono del contacto a insertar:");
                String telefonoInsertar = scanner.nextLine();

                if (!telefonoInsertar.matches("^\\d{6,11}$")) {
                    System.out.println("El número de teléfono no es válido.");
                    run = false;
                    break;
                }

                nombres.add(nombreInsertar);
                telefonos.add(telefonoInsertar);
                System.out.println(
                        "Contacto insertado: " + "Nombre: " + nombreInsertar + ", Teléfono: " + telefonoInsertar);
            } else if ("3".equals(operacion)) {
                System.out.println("Ingrese el nombre del contacto a actualizar:");
                String nombreActualizar = scanner.nextLine();
                boolean contactoActualizado = false;

                for (int i = 0; i < nombres.size(); i++) {
                    if (nombres.get(i).equals(nombreActualizar)) {
                        System.out.println("Ingrese el nuevo teléfono del contacto:");
                        String nuevoTelefono = scanner.nextLine();
                        telefonos.set(i, nuevoTelefono);
                        System.out.println("Contacto actualizado: " + "Nombre: " + nombres.get(i) + ", Teléfono: "
                                + telefonos.get(i));
                        contactoActualizado = true;
                        break;
                    }
                }

                if (!contactoActualizado) {
                    System.out.println("Contacto no encontrado");
                }
            } else if ("4".equals(operacion)) {
                System.out.println("Ingrese el nombre del contacto a eliminar:");
                String nombreEliminar = scanner.nextLine();
                boolean contactoEliminado = false;

                for (int i = 0; i < nombres.size(); i++) {
                    if (nombres.get(i).equals(nombreEliminar)) {
                        nombres.remove(i);
                        telefonos.remove(i);
                        System.out.println("Contacto eliminado: " + "Nombre: " + nombreEliminar);
                        contactoEliminado = true;
                        break;
                    }
                }

                if (!contactoEliminado) {
                    System.out.println("Contacto no encontrado");
                }
            } else if ("5".equals(operacion)) {
                run = false;
                System.out.println("Agenda creada: " + nombres);
            } else {
                System.out.println("Operación no válida");
            }
        }

        scanner.close();
        System.out.println("Agenda creada: " + nombres);
    }
}
