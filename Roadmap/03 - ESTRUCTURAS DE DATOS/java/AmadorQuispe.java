import java.util.Arrays;
import java.util.Stack;
import java.util.TreeMap;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Map;
import java.util.Optional;
import java.util.Properties;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Queue;
import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.TreeSet;
import java.util.stream.Stream;

public class AmadorQuispe {
    // Arrays, son del mismo tipo y de tamaño fijo
    // Se acceden por un indice
    public static void arrays() {
        // Crear
        int[] integers = new int[5]; // crea un array con valores por defecto 0
        // String[] names = { "Amador", "AMsoft", "AMcodex" }; otro forma de inicializar
        // Agregar
        integers[0] = 3;
        integers[1] = 5;
        integers[2] = 6;
        integers[3] = 7;
        integers[4] = 8;
        for (int n : integers) {
            System.out.println(n);
        }
        // modificar
        integers[2] = 12;
        System.out.println("Array modificado");
        for (int n : integers) {
            System.out.println(n);
        }
        // Eliminar
        // No es posible eliminar, podemos asignar su valor por defecto.

        // ordenar
        // se puede usar la clase Arrays del lenguaje.
        Arrays.sort(integers);
        System.out.println("Array ordenado");
        for (int n : integers) {
            System.out.println(n);
        }
    }

    // Array de Arrays
    public static void matriz() {
        // creación y inserción
        int[][] numbers = { { 1, 2 }, { 2, 2 }, { 2, 3 } };
        // modificación
        numbers[0][1] = 8;
        // Eliminación
        // No es posible eliminar
        // ordenar
        Arrays.sort(numbers);
    }

    // ArrayList, pueden cambiar de tamaño durante la ejecución del programa
    public static void arrayList() {
        // Initialization.
        ArrayList<String> studentNames = new ArrayList<>();
        // Insertar
        studentNames.add("Pedro");
        studentNames.add("Juan");
        studentNames.add("Pepe");
        studentNames.add("Amador");
        // Modificar, se puede modificar por el indice
        studentNames.set(0, "Pedro F"); // modificar el valor del indice 0
        // Eliminar, se puede eliminar por el indice
        studentNames.remove(0);// Elimina por el indice 0

        // Ordenar
        studentNames.sort(Comparator.naturalOrder()); // ordena en orden alfabético
        for (String name : studentNames) {
            System.out.println(name);
        }
    }

    // LinkedList, Una clase que añade métodos adicionales y permite disponer de una
    // lista doblemente enlazada en la que las inserciones y modificaciones de la
    // lista sean muy rápidas
    public static void linkedList() {
        // Initialization.
        LinkedList<String> studentNames = new LinkedList<>();
        // Insertar
        studentNames.add("Pedro");
        studentNames.add("Juan");
        studentNames.add("Pepe");
        studentNames.add("Amador");
        studentNames.addFirst("Mia");// inserta al inicio

        // Modificar, se puede modificar por el indice
        studentNames.set(0, "Pedro F"); // modificar el valor del indice 0

        // Eliminar, se puede eliminar por el indice
        studentNames.remove("Pedro");// Elimina por el indice 0
        studentNames.removeLast();// Elimina el ultimo
        // Ordenar
        studentNames.sort(Comparator.naturalOrder()); // ordena en orden alfabético
        for (String name : studentNames) {
            System.out.println(name);
        }
    }

    // Stack, representa una pila en la que el último elemento agregado es el
    // primero en ser eliminado
    public static void stack() {
        Stack<String> studentNames = new Stack<>();
        // Agregar
        studentNames.push("Pedro");
        studentNames.push("Juan");
        studentNames.push("Pepe");
        studentNames.add("Amador");
        System.out.println("Contenido inicial de la pila: " + studentNames);
        // Modificar.
        studentNames.set(0, "Pedro F");
        System.out.println("Contenido modificado de la pila: " + studentNames);
        // Eliminar
        studentNames.pop();
        System.out.println("Contenido post eliminación de la pila: " + studentNames);
        // ordenar, es posible ordenar pero no es necesaria
        studentNames.sort(Comparator.naturalOrder());
        System.out.println("Ordenado: " + studentNames);
    }

    // HashSet, permite añadir elementos no repetidos al grupo
    public static void hashSet() {
        // initialization
        HashSet<String> setStudents = new HashSet<>();
        // inserción
        setStudents.add("Mia");
        setStudents.add("Pepe");
        setStudents.add("Amador");
        setStudents.add("Carlos");
        setStudents.add("Mia"); // Se intenta agregar duplicado.
        System.out.println("Lista inicial " + setStudents);
        // modificación
        // No es posible modificar, lo que se puede hacer es eliminar y insertar
        // Eliminación
        setStudents.remove("Pepe");
        System.out.println("Lista post eliminación " + setStudents);
        // ordenar
        // Siempre se guardan en desorden, java usa hash para fácil acceso
    }

    // TreeSet, permite añadir elementos no repetidos al grupo pero ordenados (orden
    // natural)
    public static void treeSet() {
        // initialization
        TreeSet<String> setStudents = new TreeSet<>((s1, s2) -> Integer.compare(s1.length(), s2.length()));
        // inserción
        setStudents.add("Mia");
        setStudents.add("Pepe");
        setStudents.add("Amador");
        setStudents.add("Carlos");
        setStudents.add("Mia"); // Se intenta agregar duplicado.
        System.out.println("Lista inicial " + setStudents);
        // modificación
        // No es posible modificar, lo que se puede hacer es eliminar y insertar

        // Eliminación
        setStudents.remove("Pepe");
        System.out.println("Lista post eliminación " + setStudents);
        // ordenar
        // Siempre se guardan en desorden, java usa hash para fácil acceso

    }

    // Queue, para manejar colas, primero en entrar, primero en salir
    public static void deQueue() {
        Queue<String> cola = new ArrayDeque<>();
        // Agregar elementos a la cola
        cola.offer("Mia");
        cola.offer("Amador");
        cola.offer("Carlos");
        // Mostrar la cola
        System.out.println("Cola: " + cola);

        // Obtener y eliminar el primer elemento de la cola
        String primerElemento = cola.poll();
        System.out.println("Primer elemento obtenido y eliminado: " + primerElemento);

        // Mostrar la cola después de la operación de poll
        System.out.println("Cola después de poll: " + cola);

        // Obtener el primer elemento sin eliminarlo
        String primerElementoPeek = cola.peek();
        System.out.println("Primer elemento obtenido sin eliminar: " + primerElementoPeek);

        // Mostrar la cola después de peek
        System.out.println("Cola después de peek: " + cola);
        cola.remove();

    }

    // HashMap, Un diccionario es una colección de pares clave-valor
    public static void hashMap() {
        // Initialization un HashMap
        HashMap<String, Integer> hashMap = new HashMap<>();

        // Agregar elementos al HashMap
        hashMap.put("Uno", 1);
        hashMap.put("Dos", 2);
        hashMap.put("Tres", 3);
        // Modificar un elemento del HashMap
        hashMap.put("Uno", 4);
        // Imprimir todos los elementos del HashMap
        System.out.println("Elementos del HashMap " + hashMap);
        // Eliminar un elemento del HashMap
        hashMap.remove("Uno");
        System.out.println("Elementos del HashMap post Eliminación " + hashMap);
        // Obtener un valor usando una clave
        int valorDos = hashMap.get("Dos");
        System.out.println("Valor asociado a 'Dos': " + valorDos);
        // Ordenar
        // !No se garantiza orden
    }

    // HashMap, Un diccionario es una colección de pares clave-valor, con orden
    // natural o personalizado
    public static void treeMap() {
        // Crear un TreeMap
        TreeMap<String, Integer> treeMap = new TreeMap<>();
        treeMap.put("Uno", 1);
        treeMap.put("Dos", 2);
        treeMap.put("Tres", 3);
        treeMap.put("Cero", 0);
        // Mostrar todo los elementos
        System.out.println("Mostrar todo los elementos " + treeMap);
        // Modificar
        treeMap.put("Cero", 9);
        System.out.println("Mostrar todo los elementos, con mod " + treeMap);
        // Eliminar elemento del TreeMap
        treeMap.remove("Cero");
        System.out.println("Mostrar elementos post eliminación " + treeMap);
    }

    // Properties, gestiona pares clave-valor, diseñada para cadenas de texto. Usada
    // para
    // configuraciones y archivos de propiedades en aplicaciones Java.
    public static void properties() {
        Properties properties = new Properties();
        // Agregar elementos a properties
        properties.setProperty("app-name", "App");
        properties.setProperty("app-language", "ES");
        System.out.println("Mostrar elementos " + properties);
        // Modificar
        properties.setProperty("app-name", "App Gestion");
        System.out.println("Mostrar modificado " + properties);
        // Eliminar
        properties.remove("app-name");
        System.out.println("Mostrar post eliminación " + properties);
        // Ordenación
        // No se garantiza orden.
    }

    public static void agenda() {

    }

    public static void main(String[] args) {
        // Arrays
        arrays();
        matriz();
        // Listas
        arrayList();
        linkedList();
        stack();
        // Sets
        hashSet();
        treeSet();
        // --Queue (Colas)
        deQueue();
        // --Map (mapas)
        hashMap();
        treeMap();
        properties();
        // Opcional - Agenda
        Agenda agenda = new Agenda();
        while (true) {
            String optSelect = agenda.showMenu();
            if (!Character.isDigit(optSelect.charAt(0))) {
                System.out.println("Introduzca un número");
            } else {
                int numSelect = optSelect.charAt(0) - '0';
                switch (agenda.getOperation(numSelect)) {
                    case INSERT:
                        agenda.insert();
                        break;
                    case SEARCH:
                        agenda.search();
                        break;
                    case DELETE:
                        agenda.delete();
                        break;
                    case UPDATE:
                        agenda.update();
                        break;
                    case SHOW:
                        agenda.show();
                        break;
                    case EXIT:
                        System.out.println("!!! Hasta luego, vuelva pronto!");
                        System.exit(0);
                        break;
                    default:
                        System.out.println("Ingresa una opción valida");
                        break;
                }
            }
        }

    }
}

class Agenda {
    public enum operations {
        SEARCH(1),
        INSERT(2),
        UPDATE(3),
        DELETE(4),
        SHOW(5),
        EXIT(6);

        private final int value;

        operations(int value) {
            this.value = value;
        }
    }

    private Map<String, Long> agenda = new HashMap<>();
    String optSelect;
    private Scanner sc = new Scanner(System.in);

    public String showMenu() {
        System.out.println("-----------------------");
        System.out.println("<<< MENU DE AGENDA  >>>");
        System.out.println("-----------------------");
        System.out.println("Introduce el número de la opción que quieres realizar");
        for (operations ope : operations.values()) {
            System.out.println(ope.value + "> " + ope);
        }
        System.out.print("Ingrese la opción :");
        optSelect = sc.next();
        sc.nextLine();
        return optSelect;
    }

    public operations getOperation(int value) {
        Optional<operations> op = Stream.of(operations.values()).filter(o -> o.value == value).findFirst();
        return op.isPresent() ? op.get() : null;
    }

    public void insert() {
        String name;
        Long number;
        do {
            System.out.print("Ingresa el nombre del contacto :");
            name = sc.next();
            if (name.trim().length() < 3) {
                System.out.println("! El nombre no puede ser vació");
            }
        } while (name.trim().length() < 3);

        do {
            System.out.print("Ingresa el número del contacto :");
            number = sc.nextLong();
            if (Long.toString(number).length() > 11) {
                System.out.println("! El número debe ser máximo de 11");
            }
        } while (Long.toString(number).length() > 11);

        agenda.put(name, number);
        System.out.println("(- Contacto agregado correctamente");
    }

    public void search() {
        System.out.print("Ingresa el contacto a buscar :");
        String name = sc.next();
        if (agenda.containsKey(name)) {
            System.out.println("El numero de " + name + " es: " + agenda.get(name));
        } else {
            System.out.println("El usuario no se encuentra en el sistema! ");
        }
    }

    public void delete() {
        System.out.print("Ingresa el contacto a eliminar :");
        String name = sc.next();
        if (agenda.containsKey(name)) {
            agenda.remove(name);
            System.out.println("Contacto Eliminado!");
        } else {
            System.out.println(String.format("El usuario %s no se encuentra en el sistema!", name));
        }
    }

    public void update() {
        System.out.print("Que contacto desea actualizar? :");
        String name = sc.next();
        if (agenda.containsKey(name)) {
            Long number;
            do {
                System.out.print("Ingresa el nuevo número del contacto :");
                number = sc.nextLong();
                if (Long.toString(number).length() > 11) {
                    System.out.println("! El número debe ser máximo de 11");
                }
            } while (Long.toString(number).length() > 11);
            agenda.replace(name, number);
            System.out.println("(- Contacto actualizado!");
        } else {
            System.out.println("! El usuario no se encuentra en el sistema!");
        }
    }

    public void show() {
        System.out.println("Tus contactos");
        System.out.println("----------------");
        agenda.forEach((c, n) -> {
            System.out.println(String.format("%s : %d", c, n));
        });
        System.out.println("----------------");
    }
}
