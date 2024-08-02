import java.util.*;

public class Maynor06 {

    public static void main(String[] args) {
    /* Java soporta una amplia variedad de estructuras de datos,
    tanto a nivel de las colecciones estándar de la biblioteca Java Collections
    Framework (JCF) como a través de clases y estructuras personalizadas
    que uno mismo puede implementar
     */

//         Arrays
//         estructura de datos fija y ordenada que almacena elementos del mismo tipo

        int[] array = new int[10];
        // colcar un dato en el primer espacio
        array[0] = 1;
        // editarlo
        array[0] = 2;
        // no se puede eliminar en si pero si se puede poner un 0 como que si este no valiera nada
        array[0] = 0;


        // Collections List
        // ArrayList
        // implementación de lista basada en arrays, permite acceso rápido
        // por índice pero es lenta en inserciones / eliminaciones intermedias.

        List<Integer> list = new ArrayList<Integer>();
        // colocar un dato en la lista
        list.add(1);
        // acceder a un elemento
        int num =  list.get(0);
        // modificar un elemento (estamos modificando el valor en el index 0
        list.set(0, 5);
        // eliminar elementos
        list.remove(0);
        // buscar elementos
        list.indexOf(0);
        // obtener el tamaño de la lista
        int sizeList =  list.size();
        // iterar sobre los elementos
        Iterator<Integer> iterator = list.iterator();


        // LinkedList
        // implementacion de lista doblemente enlazada, permite inserciones/ eliminaciones
        // rápidas pero es lenra en acceso por índice.

        List<Integer> integerList = new LinkedList<Integer>();



        // Collections Set
        // HashSet
        // basado en una tabla hash, no permite elemento duplicados y no garantiza
        // el orden de los elementos

        Set<Integer> set = new HashSet<Integer>();


        // LinkedHashSet
        // Basado en una tabla hash y una lista doblemente enlazada, no permite
        // duplicados y mantiene el orden de inserción

        Set<Integer> integerSet = new LinkedHashSet<Integer>();

        // TreeSet
        // basado en un árbol rojo-negro, no permite duplicados y mantiene
        // elementos ordenados.

        Set<Integer> treeIntegers = new TreeSet<Integer>();

        /*
        Operaciones con los tipos de estructuras set
        1. agregar datos
        2. eleiminar datos
        3. verificar si contiene datos
        4. verificar tamaño
        5. iterar sobre los elementos
         */
        set.add(5);
        set.remove(5);
        set.contains(set);
        set.size();
        set.iterator();


        // Collections Queue
        // LinkedList
        // puede ser usada como una cola (FIFO).

        Queue<Integer> queue = new LinkedList<>();


        // PriorityQueue
        // Implementación de cola con prioridad, los elementos son ordenados
        // de acuerdo a su orden natural o mediane un comparador.

        Queue<Integer> queue2 = new PriorityQueue<>();

                /*
        Operaciones con los tipos de estructuras set
        1. agregar datos
        2. eleiminar datos
        3. verificar si contiene datos
        4. verificar tamaño
         */
        queue2.add(1);
        queue2.remove();
        queue2.size();
        queue2.contains(queue2);


        // Collections Deque
        // ArrayDeque
        // Implementación de deque basada en arrays, permite inserciones y
        // eliminaciones en ambos extremos

        Deque<Integer> deque = new ArrayDeque<>();

        // Collections Map

        //HashMap
        // Basado en una tabla hash, permite almacenar pares clave-valor y no
        // garantiza el orden de los elementos

        Map<String, Integer> map = new HashMap<>();

        // LinkedHashMap
        // Basado en una tabla hash y una lista doblemente enlazada,
        // mantiene el orden de inserción

        Map<String , Integer> map2 = new LinkedHashMap<>();

        // TreeMap
        // Basado en un árbol rojo-negro, mantiene los pares clave-valor ordenados.

        Map<String, Integer> map3 = new TreeMap<>();
                /*
        Operaciones con los tipos de estructuras Map
        1. agregar o actualizar pares clave-valor
        2. eleiminar pares clave-valor
        3. acceder a valores
        4. verificar si contiene claves o valores
        5. verificar tamaño
        */
        map.put("primero", 1);
        map.get("primero");
        map.containsKey("primero");
        map.containsValue(1);
        map.size();
        map.remove("primero");


        // OTRAS ESTRUCTURAS DE DATOS
        // Stack
        // La clase "Stack" también está disponible pero no es recomendada por ser heredada
        // de 'Vector' y no estar sincronizada.

        Stack<Integer> stack = new Stack<>();

        // Vector
        // Similar a 'ArrayList' pero sincronizada.

        Vector<Integer> vector = new Vector<>();

        //RETO EXTRA
        Scanner sc = new Scanner(System.in);
        int option = 0;
        String nombre;
        Integer numero;

        Map<String, Integer> contactos = new HashMap<String, Integer>();
        do {
            System.out.println("------------------------> AGENDA DE CONTACTOS <------------------------------");
            System.out.println("1. Crear Contacto");
            System.out.println("2. modificar Contacto");
            System.out.println("3. Listar Contactos");
            System.out.println("4. Eliminar Contacto");
            System.out.println("5. Salir");
            System.out.println("");
            System.out.print("Elige una Opcion: ");
            option = sc.nextInt();


            switch (option) {
                case 1:
                    System.out.println("Cual es el nombre del contacto? ");
                    nombre = sc.next();
                    System.out.println("Cual es el numero del contacto? ");
                    numero = sc.nextInt();
                    contactos.put(nombre, numero);
                    break;

                case 2:
                    System.out.println("Cual es el nombre del contacto que quieres modificar? ");
                    nombre = sc.next();
                    contactos.remove(nombre);
                    System.out.println("que nombre le quieres poner?");
                    nombre = sc.next();
                    System.out.println("cual es el numero que le quieres poner");
                    numero = sc.nextInt();
                    contactos.put(nombre, numero);
                    System.out.println("modificacion con exito!!!");
                    break;
                case 3:
                    for (Map.Entry<String, Integer> entry : contactos.entrySet()) {
                        System.out.println(entry.getKey() + " " + entry.getValue());
                    }
                    break;
                case 4:
                    System.out.println("el contacto es el nombre del contacto que quieres eliminar? ");
                    nombre = sc.next();
                    contactos.remove(nombre);
                    break;
                case 5:
                    System.out.println("Gracias por confiar en nosotros!!");
                    break;
                default:
                    throw new IllegalStateException("Unexpected value: " + option);
            }



        }while (option != 5);

    }
}
