import java.util.*;

public class mensius87 {

    public static void main(String[] args) {

        // Listas: colección ordenada y mutable de elementos
        System.out.println("::::::::::::::::::::::::::::::::::::: LISTAS :::::::::::::::::::::::::::::::::::::");

        List<String> listaColores = new ArrayList<>(Arrays.asList("rojo", "verde", "azul", "amarillo", "marrón", "naranja", "blanco", "negro"));

        System.out.println("Lista inicial:");
        System.out.println(listaColores);

        // Inserción en listas
        listaColores.add("violeta");

        System.out.println("Añadido color violeta:");
        System.out.println(listaColores);

        // Actualización del nuevo color (cambio de violeta por fucsia)
        listaColores.set(listaColores.size() - 1, "fucsia");

        System.out.println("Cambiado color violeta por fucsia:");
        System.out.println(listaColores);

        // Borrado del color
        listaColores.remove("fucsia");

        System.out.println("Eliminado color fucsia:");
        System.out.println(listaColores);

        // Ordenado alfabético
        Collections.sort(listaColores);

        System.out.println("Lista ordenada:");
        System.out.println(listaColores + "\n");

        // Tuplas: colección ordenada e inmutable
        System.out.println("::::::::::::::::::::::::::::::::::::: TUPLAS :::::::::::::::::::::::::::::::::::::");

        List<String> tuplaPaises = Arrays.asList("España", "Portugal", "USA", "Alemania", "Suecia");

        System.out.println("Tupla inicial:");
        System.out.println(tuplaPaises);

        // Ordenar tupla (indirectamente)
        Collections.sort(tuplaPaises);

        System.out.println("Tupla ordenada:");
        System.out.println(tuplaPaises + "\n");

        // Conjuntos: colección desordenada y mutable de elementos únicos
        System.out.println("::::::::::::::::::::::::::::::::::::: CONJUNTOS :::::::::::::::::::::::::::::::::::::");

        Set<Integer> conjuntoNumeros = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));

        System.out.println("Conjunto inicial:");
        System.out.println(conjuntoNumeros);

        // Añadir un elemento
        conjuntoNumeros.add(10);
        System.out.println("Conjunto con añadido:");
        System.out.println(conjuntoNumeros);

        // Eliminar un elemento
        conjuntoNumeros.remove(2);
        System.out.println("Conjunto eliminando el nº2:");
        System.out.println(conjuntoNumeros + "\n");

        // Diccionarios: colección desordenada y mutable de pares clave-valor
        System.out.println("::::::::::::::::::::::::::::::::::::: DICCIONARIOS :::::::::::::::::::::::::::::::::::::");

        Map<String, String> diccionarioSpaEng = new HashMap<>();
        diccionarioSpaEng.put("manzana", "apple");
        diccionarioSpaEng.put("hola", "Hello");
        diccionarioSpaEng.put("silla", "chair");

        System.out.println("Diccionario original:");
        System.out.println(diccionarioSpaEng);

        // Añadir un elemento
        diccionarioSpaEng.put("mundo", "world");
        System.out.println("Diccionario con añadido:");
        System.out.println(diccionarioSpaEng);

        // Modificar un elemento
        diccionarioSpaEng.put("mundo", "world");
        System.out.println("Diccionario con corrección:");
        System.out.println(diccionarioSpaEng);

        // Eliminar un elemento
        diccionarioSpaEng.remove("silla");
        System.out.println("Diccionario con elemento eliminado:");
        System.out.println(diccionarioSpaEng);

        // Ordenar diccionario
        Map<String, String> diccionarioOrdenado = new TreeMap<>(diccionarioSpaEng);
        System.out.println("Diccionario ordenado:");
        System.out.println(diccionarioOrdenado + "\n");

        System.out.println("::::::::::::::::::::::::::::::::::::: EXTRA :::::::::::::::::::::::::::::::::::::");

        // Agenda de contactos
        Map<String, Integer> agenda = new HashMap<>();

        Scanner scanner = new Scanner(System.in);
        int opcionElegida = 0;

        while (opcionElegida != 6) {

            // Creación del menú y bucle
            System.out.println("""

            ### Agenda Telefónica ###

            ¿Qué deseas hacer?:

            [1] - Buscar
            [2] - Añadir
            [3] - Modificar
            [4] - Eliminar
            [5] - Ver todos los contactos
            [6] - Salir
            """);

            opcionElegida = scanner.nextInt();

            switch (opcionElegida) {
                case 1:
                    buscarContacto(agenda);
                    break;
                case 2:
                    anadirContacto(agenda, scanner);
                    break;
                case 3:
                    modificarContacto(agenda, scanner);
                    break;
                case 4:
                    eliminarContacto(agenda, scanner);
                    break;
                case 5:
                    verContactos(agenda);
                    break;
                case 6:
                    System.out.println("\nGracias por utilizar la agenda. Hasta pronto!!!");
                    break;
            }
        }
    }

    private static void buscarContacto(Map<String, Integer> agenda) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce el nombre del contacto a buscar: ");
        String contactoABuscar = scanner.nextLine();

        if (agenda.containsKey(contactoABuscar)) {
            System.out.println(contactoABuscar + ": " + agenda.get(contactoABuscar) + "\n");
        } else {
            System.out.println("El contacto no existe, inténtalo de nuevo.\n");
        }
    }

    private static void anadirContacto(Map<String, Integer> agenda, Scanner scanner) {
        System.out.print("Introduce el nombre del contacto: ");
        String nombre = scanner.next();

        System.out.print("Introduce el número de 9 cifras: ");
        int numero = scanner.nextInt();

        while (String.valueOf(numero).length() != 9 || agenda.containsValue(numero)) {

            if (String.valueOf(numero).length() != 9) {
                System.out.print("Error. Tiene que tener 9 cifras: ");
                numero = scanner.nextInt();
            } else if (agenda.containsValue(numero)) {
                System.out.print("Error. El número " + numero + " ya existe en la agenda: ");
                numero = scanner.nextInt();
            }
        }

        agenda.put(nombre, numero);
        System.out.println(nombre + " se ha agregado a la agenda correctamente.\n");
    }

    private static void modificarContacto(Map<String, Integer> agenda, Scanner scanner) {
        System.out.print("Introduce el nombre del contacto a modificar: ");
        String contactoAModificar = scanner.next();

        if (!agenda.containsKey(contactoAModificar)) {
            System.out.println("El nombre no existe en la agenda, inténtalo de nuevo.\n");
            modificarContacto(agenda, scanner);
        } else {
            agenda.remove(contactoAModificar);

            System.out.print("Introduce el nuevo nombre del contacto: ");
            String nombre = scanner.next();

            System.out.print("Introduce el nuevo número de 9 cifras: ");
            int numero = scanner.nextInt();

            while (String.valueOf(numero).length() != 9 || agenda.containsValue(numero)) {

                if (String.valueOf(numero).length() != 9) {
                    System.out.print("Error. Tiene que tener 9 cifras: ");
                    numero = scanner.nextInt();
                } else if (agenda.containsValue(numero)) {
                    System.out.print("Error. El número " + numero + " ya existe en la agenda: ");
                    numero = scanner.nextInt();
                }
            }

            agenda.put(nombre, numero);
            System.out.println(contactoAModificar + " se ha modificado correctamente.\n");
        }
    }

    private static void eliminarContacto(Map<String, Integer> agenda, Scanner scanner) {
        System.out.print("Introduce el nombre del contacto a eliminar: ");
        String contactoAEliminar = scanner.next();

        if (agenda.containsKey(contactoAEliminar)) {
            agenda.remove(contactoAEliminar);
            System.out.println("El contacto " + contactoAEliminar + " se ha eliminado correctamente.\n");
        } else {
            System.out.println("El contacto no existe, inténtalo de nuevo.\n");
        }
    }

    private static void verContactos(Map<String, Integer> agenda) {
        Map<String, Integer> agendaOrdenada = new TreeMap<>(agenda);

        for (Map.Entry<String, Integer> entry : agendaOrdenada.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
