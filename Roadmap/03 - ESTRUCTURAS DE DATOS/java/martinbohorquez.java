import java.util.*;
import java.util.stream.Collectors;

/**
 * 03 ESTRUCTURAS DE DATOS
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    /**
     * Arrays
     */
    private static final int[] array = new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; //array con datos inicializados
    private static final int[] array2 = new int[10]; //array con longitud
    /**
     * List: {@code ArrayList}, {@code LinkedList}, {@code Vector}, {@code Stack}<p>
     * Unlike sets, lists typically allow duplicate elements, null elements.<p>
     * An ordered collection, where the user has precise control over where in the list
     * each element is inserted. The user can access elements by their integer index
     * (position in the list), and search for elements in the list.<p>
     * {@code iterator}, {@code add}, {@code remove}, {@code equals}, and
     * {@code hashCode} methods.
     */
    private static final List<String> lista = new ArrayList<>();//Mutable
    private static final List<String> listaInmutable = List.of("Martin", "Zuckerberg");//Inmutable
    private static final List<String> listaMutable = new ArrayList<>(Arrays.asList("Martin", "Zuckerberg"));//Mutable
    /**
     * Set: {@code HashSet}, {@code LinkedHashSet}, {@code TreeSet}<p>
     * A collection that contains no duplicate elements.  More formally, sets
     * contain no pair of elements {@code e1} and {@code e2} such that
     * {@code e1.equals(e2)}, and at most one null element.<p>
     * {@code TreeSet} sorted based on natural ordering or custom comparator
     */
    private static final Set<String> conjunto = new HashSet<>();
    private static final Set<String> conjuntoInmutable = Set.of("Martin", "Zuckerberg");//Inmutable
    private static final Set<String> conjuntoMutable = new HashSet<>(Arrays.asList("Martin", "Zuckerberg"));

    /**
     * Map: {@code HashMap}, {@code LinkedHashMap}, {@code HashTable}, {@code TreeMap}<p>
     * An object that maps keys to values. A map cannot contain duplicate keys;
     * each key can map to at most one value.
     * <p>This interface takes the place of the {@code Dictionary} class, which
     * was a totally abstract class rather than an interface.
     * <p>{@code TreeMap} sorted based on natural ordering or custom comparator
     */
    private static final Map<String, String> diccionario = new HashMap<>();
    private static final Map<String, Integer> diccionarioSingleton = Collections.singletonMap("uno", 1);
    private static final Map<String, Integer> diccionarioInmutable = Map.of(
            "uno", 1,
            "dos", 2,
            "tres", 3
    );//Inmutable
    private static final Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
    private static final Map<String, Integer> treeMap = new TreeMap<>();//Ordered
    private static Scanner scan;

    public static void main(String[] args) {
        System.out.println("LIST");
        /*
         * List
         */
        Collections.addAll(lista, "Martin", "Karl");
        ListIterator<String> listIterator = lista.listIterator();

        listIterator.next(); //ListIterator
        listIterator.add("Mike"); //add()

        Iterator<String> iterator = lista.iterator(); //Iterator
        while (iterator.hasNext()) {
            String elemento = iterator.next();
            if (elemento.equals("Karl")) {
                iterator.remove(); //remove()
            }
        }
//        lista.add("Martin"); //inserción
        lista.add("Castle"); //inserción
        lista.set(2, "Pepe"); //actualización
        System.out.println(lista);
        System.out.println(lista.getClass().getSimpleName()); //ArrayList

        System.out.println(listaInmutable.getClass().getSimpleName()); //List12

        listaMutable.add("Moy"); //inserción
        listaMutable.set(2, "Xavi"); //actualización
        listaMutable.add("Kathe"); //inserción
        listaMutable.add("Martin");
        listaMutable.remove("Zuckerberg"); //borrado
        listaMutable.sort(String::compareTo);
        System.out.println(listaMutable);
        listaMutable.removeIf(s -> s.equals("Martin"));
        listaMutable.add("Franklin");
        Collections.sort(listaMutable);// Collections.sort()
        listaMutable.add(null);

        listaMutable.forEach(System.out::println);
        System.out.println(listaMutable.reversed());
        System.out.println(listaMutable.getClass().getSimpleName()); //ArrayList

        /*
         * Set
         * No se puede Actualizar
         * No se puede Ordenar
         */
        System.out.println("\nSET");
        Collections.addAll(conjunto, "Patrick", "Sam", "Jim");
        conjunto.add("Sam"); //inserción
        System.out.println(conjunto.getClass().getSimpleName());
        System.out.println(conjunto);
        conjunto.remove("Patrick"); //borrado
        System.out.println(conjunto.contains("Peter"));
        System.out.println(conjunto);
        System.out.println(conjuntoInmutable.getClass().getSimpleName());
        System.out.println(conjuntoInmutable.size());
        conjuntoInmutable.forEach(System.out::println);
        conjuntoMutable.add("Sam");
        System.out.println(conjuntoMutable.getClass().getSimpleName());
        System.out.println(conjuntoMutable);

        /*
         * Map: clave-valor (key, value)
         * Las llaves (keys) son únicas dentro del diccionario.
         */
        diccionario.put("clave1", "valor1"); //inserción
        diccionario.put("clave2", "valor2");
        diccionario.put("clave3", "valor3");
        diccionario.put("clave2", "nuevoValor2"); // Sobrescribe "valor2"
        Map<String, String> diccionarioOrdenado = diccionario.entrySet().stream()
                .sorted(Map.Entry.comparingByValue())//ordenación byValue
                .collect(Collectors.toMap(
                        Map.Entry::getKey,
                        Map.Entry::getValue,
                        (e1, e2) -> e1,
                        LinkedHashMap::new
                ));
        System.out.println(diccionarioOrdenado);
        diccionario.remove("clave1"); //borrado
        diccionario.replace("clave3", "nuevoValor3"); //actualización
        System.out.println(diccionario.getClass().getSimpleName());
        System.out.println(diccionario);
        System.out.println(diccionario.keySet());
        System.out.println(diccionario.get("clave2"));  // Imprime "nuevoValor2"
        System.out.println(diccionario.get("clave3"));  // Imprime "nuevoValor3"

        System.out.println(diccionarioSingleton.getClass().getSimpleName());
        System.out.println(diccionarioSingleton);

        System.out.println(diccionarioInmutable.getClass().getSimpleName());
        diccionarioInmutable.forEach((m, n) -> System.out.println("Key es: " + m.toUpperCase() + ", value es : " + n));

        //LinkedHashMap
        linkedHashMap.put("uno", 1);
        linkedHashMap.put("tres", 3);
        linkedHashMap.put("dos", 2);
        System.out.println(linkedHashMap);

        // Ordenar por claves
        Map<String, Integer> mapaOrdenado = new TreeMap<>(linkedHashMap);

        System.out.println(mapaOrdenado);

        //TreeMap
        treeMap.put("uno", 1);
        treeMap.put("tres", 3);
        treeMap.put("dos", 2);

        System.out.println(treeMap);

        /*
         * DIFICULTAD EXTRA
         */
        HashMap<String, Long> contactos = new HashMap<>();

        //etiqueta de bucle
        outerloop:
        while (true) {
            System.out.println("""
                    Bienvenido a la agente de contactos, tiene las siguientes opciones:
                    1. Buscar un contacto
                    2. Crear un contacto
                    3. Actualizar un contacto
                    4. Eliminar un contacto
                    5. Salir
                    """);

            System.out.print("Elige una opción: ");
            int option = 0;
            try {
                scan = new Scanner(System.in);
                option = scan.nextInt();
            } catch (InputMismatchException ignored) {
            }
            String name = "";

            if (option > 0 && option < 5) {
                name = getName();
            }

            switch (option) {
                case 1 -> {
                    Long number = contactos.get(name);
                    getResult(number,
                            "El número de teléfono de " + name + " es " + number + "\n",
                            "El contacto " + name + " no existe en la agenda!\n");
                }
                case 2 -> {
                    boolean flag = contactos.containsKey(name);
                    contactos.put(name, getPhone());
                    Long number = flag ? null : contactos.get(name);
                    getResult(number,
                            "El contacto " + name + " ha sido registrado!\n",
                            "El contacto " + name + " ya se encuentra registrado. Si desea actualizar usa la opción 3!\n");

                }
                case 3 -> getResult(contactos.replace(name, getPhone()),
                        "El contacto " + name + " ha sido actualizado!\n",
                        "El contacto " + name + " no existe en la agenda!\n");
                case 4 -> getResult(contactos.remove(name),
                        "El contacto " + name + " ha sido eliminado!\n",
                        "El contacto " + name + " no existe en la agenda!\n");
                case 5 -> {
                    System.out.println("Saliendo de la agenda!");
                    break outerloop;
                }
                default -> System.out.println("Opción no válida! Debe elegir una opción del 1 al 5.\n");
            }
        }
    }

    public static String getName() {
        scan = new Scanner(System.in);
        System.out.print("Indique su nombre: ");
        return scan.next();
    }

    public static Long getPhone() {
        Long numero = Long.MIN_VALUE;
        while (true) {
            try {
                System.out.print("Indique su numero de teléfono: ");
                scan = new Scanner(System.in);
                numero = scan.nextLong();
                if (numero.toString().length() > 11 && numero > 0L) {
                    System.out.println("Debe introducir un número de teléfono con un máximo de 11 dígitos!\n");
                } else {
                    break;
                }
            } catch (InputMismatchException e) {
                System.out.println("Número de teléfono no válido!\n");
            }
        }
        return numero;
    }

    public static void getResult(Long result, String success) {
        if (result != null) {
            System.out.println(success);
        } else {
            System.out.println("Operación fallida");
        }
    }

    public static void getResult(Long result, String success, String failed) {
        if (result != null) {
            System.out.println(success);
        } else {
            System.out.println(failed);
        }
    }
}
