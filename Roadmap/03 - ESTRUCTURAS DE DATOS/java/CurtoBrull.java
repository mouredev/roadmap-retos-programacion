import java.util.ArrayList;
import java.util.BitSet;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.InputMismatchException;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Stack;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.concurrent.ConcurrentHashMap;

public class CurtoBrull {
    public static void main(String[] args) {

        // Creación de todas las estructuras soportadas por defecto en tu lenguaje.
        // Array
        int[] array = {1, 2, 3, 4, 5};
        // ArrayList
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(1);
        // Map
        HashMap<String, Integer> map = new HashMap<>();
        map.put("key1", 1);
        // HashSet
        HashSet<Integer> hashSet = new HashSet<>();
        hashSet.add(1);
        // LinkedList
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.add(1);
        //TreeMap
        TreeMap<String, Integer> treeMap = new TreeMap<>();
        treeMap.put("key1", 1);
        // TreeSet
        TreeSet<Integer> treeSet = new TreeSet<>();
        treeSet.add(1);
        // LinkedHashMap
        LinkedHashMap<String, Integer> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put("key1", 1);
        // Stack
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        // PriorityQueue
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(1);
        // BitSet
        BitSet bitSet = new BitSet();
        bitSet.set(1);
        // Vector
        Deque<Integer> vector = new LinkedList<>();
        vector.add(1);
        // HashTable
        Hashtable<String, Integer> hashTable = new Hashtable<>();
        hashTable.put("key1", 1);
        // ConcurrentHashMap
        ConcurrentHashMap<String, Integer> concurrentHashMap = new ConcurrentHashMap<>();
        concurrentHashMap.put("key1", 1);
        // Etc...

        // Utiliza operaciones de inserción, borrado, actualización y ordenación.
        // Actualizar en ArrayList
        arrayList.set(0, 2);
        // Insertar en ArrayList
        arrayList.add(2);
        // Borrar en ArrayList
        arrayList.remove(1);
        // Ordenar en ArrayList
        arrayList.sort(null);

        // Agenda
        agenda();
    }

    /**
     * Función para simular una agenda telefónica
     * Permite buscar, insertar, actualizar y eliminar contactos
     */
    public static void agenda() {
        HashMap<String, Integer> agenda = new HashMap<>();
        boolean exitProgram = false;
        while (!exitProgram) {
            System.out.println("1. Buscar contacto");
            System.out.println("2. Insertar contacto");
            System.out.println("3. Actualizar contacto existente");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Salir");

            // Leer la opción del usuario por teclado
            Scanner scanner = new Scanner(System.in);
            int option = scanner.nextInt();

            switch (option) {
                case 1 -> searchContact(agenda, scanner);
                case 2 -> insertContact(agenda, scanner);
                case 3 -> updateContact(agenda, scanner);
                case 4 -> deleteContact(agenda, scanner);
                case 5 -> {
                    System.out.println("Saliendo...");
                    exitProgram = true;
                }
            }

        }

    }

    /**
     * Función para buscar un contacto en la agenda
     *
     * @param agenda  contacto de la agenda a buscar
     * @param scanner scanner para leer la entrada del usuario
     */
    public static void searchContact(HashMap<String, Integer> agenda, Scanner scanner) {
        System.out.println("Ingrese el nombre del contacto a buscar");
        String searchName = scanner.next();
        if (agenda.containsKey(searchName)) {
            System.out.println("El número de " + searchName + " es " + agenda.get(searchName) + "\n");
        } else {
            System.out.println("No se ha encontrado el contacto\n");
        }
    }

    /**
     * Función para insertar un contacto en la agenda
     *
     * @param agenda contacto de la agenda a insertar
     * @param scanner scanner para leer la entrada del usuario
     */
    public static void insertContact(HashMap<String, Integer> agenda, Scanner scanner) {
        System.out.println("Ingrese el nombre del contacto a insertar");
        String insertName = scanner.next();
        int insertNumber = validateNumber(scanner);
        if (insertNumber != -1) {
            if (agenda.containsKey(insertName)) {
                System.err.println("El contacto ya existe\n");
            } else {
                agenda.put(insertName, insertNumber);
                System.out.println("El contacto " + insertName + " ha sido añadido con el número " + insertNumber + "\n");
            }
        }
    }

    /**
     * Función para actualizar un contacto en la agenda
     *
     * @param agenda contacto de la agenda a actualizar
     * @param scanner scanner para leer la entrada del usuario
     */
    public static void updateContact(HashMap<String, Integer> agenda, Scanner scanner) {
        System.out.println("Ingrese el nombre del contacto a actualizar");
        String oldName = scanner.next();
        if (!agenda.containsKey(oldName)) {
            System.err.println("El contacto no existe\n");
            return;
        }
        System.out.println("Ingrese el nuevo nombre del contacto");
        String newName = scanner.next();
        int updateNumber = validateNumber(scanner);
        if (updateNumber != -1) {
            agenda.remove(oldName);
            agenda.put(newName, updateNumber);
            System.out.println("El contacto " + oldName + " ha sido actualizado a " + newName + " con el número " + updateNumber + "\n");
        }
    }

    /**
     * Función para eliminar un contacto en la agenda
     *
     * @param agenda contacto de la agenda a eliminar
     * @param scanner scanner para leer la entrada del usuario
     */
    public static void deleteContact(HashMap<String, Integer> agenda, Scanner scanner) {
        System.out.println("Ingrese el nombre del contacto a eliminar");
        String deleteName = scanner.next();
        if (!agenda.containsKey(deleteName)) {
            System.err.println("El contacto no existe\n");
            return;
        }
        agenda.remove(deleteName);
        System.out.println("El contacto " + deleteName + " ha sido eliminado\n");
    }

    /**
     * Función para validar un número de teléfono
     *
     * @param scanner scanner para leer la entrada del usuario
     * @return número de teléfono validado
     */
    public static int validateNumber(Scanner scanner) {
        int number = -1;
        boolean validNumber = false;
        while (!validNumber) {
            System.out.println("Ingrese el número del contacto");
            try {
                number = scanner.nextInt();
                // Comprobar si el número es válido utilizando regex
                if (!String.valueOf(number).matches("[0-9]{1,11}")) {
                    System.err.println("El número de teléfono no es válido\n");
                } else {
                    validNumber = true;
                }
            } catch (InputMismatchException e) {
                System.err.println("Error: Debes ingresar un número válido\n");
                scanner.next();
            }
        }
        return number;
    }
}
