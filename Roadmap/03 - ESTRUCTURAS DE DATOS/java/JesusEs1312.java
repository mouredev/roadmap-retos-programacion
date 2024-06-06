/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

class JesusEs1312 {
    // Ejemplos de creación de estructuras de datos
    public static void main(String[] args) {
        // Creación de un array
        int[] array = new int[10];
        // Creación de una lista
        java.util.List<Integer> lista = new java.util.ArrayList<>();
        // Creación de un conjunto
        java.util.Set<Integer> conjunto = new java.util.HashSet<>();
        // Creación de un mapa
        java.util.Map<String, Integer> mapa = new java.util.HashMap<>();
        // Creación de una cola
        java.util.Queue<Integer> cola = new java.util.LinkedList<>();
        // Creación de una pila
        java.util.Stack<Integer> pila = new java.util.Stack<>();

        // Operaciones de inserción
        for (int i = 0; i < 10; i++) {
            array[i] = i;
            lista.add(i);
            conjunto.add(i);
            mapa.put("Clave " + i, i);
            cola.add(i);
            pila.push(i);
        }

        // Operaciones de borrado
        for (int i = 0; i < 10; i++) {
            lista.remove(0);
            conjunto.remove(i);
            mapa.remove("Clave " + i);
            cola.poll();
            pila.pop();
        }

        // Operaciones de actualización
        for (int i = 0; i < 10; i++) {
            array[i] = i * 2;
            lista.set(i, i * 2);
            conjunto.remove(i);
            conjunto.add(i * 2);
            mapa.put("Clave " + i, i * 2);
            cola.poll();
            cola.add(i * 2);
            pila.pop();
            pila.push(i * 2);
        }

        // Operaciones de ordenación
        java.util.Arrays.sort(array);
        java.util.Collections.sort(lista);
        java.util.List<Integer> listaOrdenada = new java.util.ArrayList<>(conjunto);
        java.util.Collections.sort(listaOrdenada);
        java.util.List<java.util.Map.Entry<String, Integer>> listaOrdenadaMapa = new java.util.ArrayList<>(mapa.entrySet());
        java.util.Collections.sort(listaOrdenadaMapa, new java.util.Comparator<java.util.Map.Entry<String, Integer>>() {
            @Override
            public int compare(java.util.Map.Entry<String, Integer> o1, java.util.Map.Entry<String, Integer> o2) {
                return o1.getValue().compareTo(o2.getValue());
            }
        });
        java.util.Collections.sort((java.util.List<Integer>) cola);
        java.util.Collections.sort(pila);

        // Ejemplo de agenda de contactos
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        java.util.Map<String, String> agenda = new java.util.HashMap<>();
        while (true) {
            System.out.println("1. Buscar contacto");
            System.out.println("2. Añadir contacto");
            System.out.println("3. Actualizar contacto");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Salir");
            System.out.print("Elige una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine();
            switch (opcion) {
                case 1:
                    System.out.print("Introduce el nombre del contacto: ");
                    String nombre = scanner.nextLine();
                    String telefono = agenda.get(nombre);
                    if (telefono != null) {
                        System.out.println("El teléfono de " + nombre + " es " + telefono);
                    } else {
                        System.out.println("No se ha encontrado el contacto");
                    }
                    break;
                case 2:
                    System.out.print("Introduce el nombre del contacto: ");
                    nombre = scanner.nextLine();
                    System.out.print("Introduce el teléfono del contacto: ");
                    telefono = scanner.nextLine();
                    agenda.put(nombre, telefono);
                    System.out.println("Contacto añadido");
                    break;
                case 3:
                    System.out.print("Introduce el nombre del contacto: ");
                    nombre = scanner.nextLine();
                    telefono = agenda.get(nombre);
                    if (telefono != null) {
                        System.out.print("Introduce el nuevo teléfono del contacto: ");
                        telefono = scanner.nextLine();
                        agenda.put(nombre, telefono);
                        System.out.println("Contacto actualizado");
                    } else {
                        System.out.println("No se ha encontrado el contacto");
                    }
                    break;
                case 4:
                    System.out.print("Introduce el nombre del contacto: ");
                    nombre = scanner.nextLine();
                    telefono = agenda.get(nombre);
                    if (telefono != null) {
                        agenda.remove(nombre);
                        System.out.println("Contacto eliminado");
                    } else {
                        System.out.println("No se ha encontrado el contacto");
                    }
                    break;
                case 5:
                    return;
                default:
                    System.out.println("Opción no válida");
            }
        }
    }
}
