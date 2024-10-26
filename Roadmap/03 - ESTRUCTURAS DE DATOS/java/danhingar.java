import java.util.*;
import java.util.Map.Entry;

public class danhingar {

    // Lista vacía
    public static List<String> nameList = new ArrayList<>();
    // Lista con valores iniciales
    public static List<String> friendList = new ArrayList<>(Arrays.asList("MATEO", "CRISTINA", "ALBA"));
    // Array vacía
    public static String[] movies = new String[2];
    // Array con valores iniciales
    public static int[] numbers = { 1, 2, 3, 4 };
    // Set vacío
    public static Set<Long> numbers3 = new LinkedHashSet<>();
    // Set con valores iniciales
    public static Set<Long> numbers4 = Set.of(1L, 2L, 3L, 4L);
    // Map vacío
    public static Map<String, Integer> animalsMap = new HashMap<>();
    // Map con valores iniciales
    public static Map<String, Integer> carsMap = Map.of("Ferrari", 2, "Lamborghini", 5, "MCLAREN", 10);

    public static void main(String[] args) {
        System.out.println(nameList);
        System.out.println(friendList);
        System.out.println(movies);
        System.out.println(numbers);
        System.out.println(numbers3);
        System.out.println(numbers4);
        System.out.println(animalsMap);
        System.out.println(carsMap);

        //Agregar elementos
        addElement();
        System.out.println(nameList);
        System.out.println(movies);
        System.out.println(numbers3);
        System.out.println(animalsMap);

        //Actualizar elementos
        updateElement();
        System.out.println(friendList);
        System.out.println(numbers);
        System.out.println(animalsMap);

        //Eliminar elementos
        removeElement();
        System.out.println(friendList);
        System.out.println(numbers3);
        System.out.println(animalsMap);

        //Ordenar elementos
        sortElement();
        System.out.println(friendList);
        System.out.println(numbers);

        // EJERCICIO EXTRA
        agenda();
    }

    private static void addElement() {
        nameList.add("MATILDA");
        movies[0] = "CARS";
        numbers3.add(100L);
        animalsMap.put("LION", 5);
    }

    private static void updateElement() {
        friendList.set(0, "LORENZO");
        numbers[0] = 0;
        animalsMap.replace("LION", 100);
    }

    private static void removeElement() {
        friendList.remove(0);
        numbers3.remove(100L);
        animalsMap.remove("LION");
    }

    private static void sortElement() {
        Collections.sort(friendList);
        Arrays.sort(numbers);
    }

    public static Map<String, String> agenda = new HashMap<>();

    public static Boolean on = Boolean.TRUE;

    private static void agenda() {

        while (on) {
            System.out.println("1. Buscar contacto");
            System.out.println("2. Insertar contacto");
            System.out.println("3. Actualizar contacto");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Mostrar agenda");
            System.out.println("6. Salir");
            System.out.println("-----------------------------");

            System.out.println("Seleccione una opción");

            Scanner scanner = new Scanner(System.in);
            String option = scanner.nextLine();
            if (!option.isBlank()) {

                switch (Integer.parseInt(option)) {
                    case 1:
                        searchContact(scanner);
                        break;
                    case 2:
                        addContact(scanner);
                        break;
                    case 3:
                        updateContact(scanner);
                        break;
                    case 4:
                        removeContact(scanner);
                        break;
                    case 5:
                        showContacts();
                        break;
                    case 6:
                        scanner.close();
                        System.exit(0);
                        on = Boolean.FALSE;
                        break;
                    default:
                        System.out.println("---------------Opción no valida---------------");

                }
            }
        }

    }

    private static void showContacts() {
        System.out.println("Mostrando agenda completa");
        for (Entry<String, String> person : agenda.entrySet()) {
            System.out.println(person.getKey().toUpperCase()+" : "+person.getValue());
        }
        System.out.println("---------Acción completada-------------\n");
    }

    private static void removeContact(Scanner scanner) {
        System.out.println("Introduzca el nombre de contacto que quiere eliminar");
        String name = scanner.nextLine();
        if (!name.isBlank() && !agenda.keySet().contains(name.toUpperCase())) {
            System.out.println("No existe el contacto que quiere eliminar");
        } else {
            agenda.remove(name.toUpperCase());
            System.out.println("Eliminado el contacto " + name.toUpperCase());
        }
        System.out.println("---------Acción completada-------------\n");
    }

    private static void addContact(Scanner scanner) {
        System.out.println("Introduzca el nombre de contacto");
        String name = scanner.nextLine();
        System.out.println("Introduzca el número de teléfono");
        String number = scanner.nextLine();
        if (!name.isBlank() && agenda.containsKey(name.toUpperCase())) {
            System.out.println("Ya existe el contacto " + name+" en la agenda");
        } else if(!number.matches("^\\d{0,11}$")) {
            System.out.println("Número de teléfono no válido " + number);
        }else{
            agenda.put(name.toUpperCase(), number);
            System.out.println(String.format("Añadido el contacto %s , %s", name.toUpperCase(), number));
        }
        System.out.println("---------Acción completada-------------\n");
    }

    private static void searchContact(Scanner scanner) {
        System.out.println("Introduzca un nombre");
        String name = scanner.nextLine();
        if (agenda.get(name.toUpperCase()) != null) {
            System.out.println(String.format("El teléfono de %s es %s", name.toUpperCase(), agenda.get(name.toUpperCase())));
        } else {
            System.out.println("No existe el contacto " + name.toUpperCase());
        }
        System.out.println("---------Acción completada-------------\n");
    }

    private static void updateContact(Scanner scanner) {
        System.out.println("Introduzca el nombre de contacto que quiere actualizar");
        String name = scanner.nextLine();
        System.out.println("Introduzca el nuevo número de teléfono");
        String number = scanner.nextLine();
        if (!name.isBlank() && !agenda.keySet().contains(name.toUpperCase())) {
            System.out.println("No existe el contacto que quiere actualizar");
        } else if (!number.matches("^\\d{0,11}$")) {
            System.out.println("Número de teléfono no válido " + number);
        } else {
            agenda.replace(name.toUpperCase(), number);
            System.out.println(String.format("Actualizado el contacto %s , %s", name.toUpperCase(), number));
        }
        System.out.println("---------Acción completada-------------\n");
    }

}
