
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.Vector;

public class reto_3 {

    private static HashMap<String, String> contacto = new HashMap();

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // Array
        int[] array = new int[5];
        array[0] = 1;
        array[1] = 2;
        array[2] = 3;
        array[1] = 20; // Actualización
        array[2] = 0; // "Borrado"
        Arrays.sort(array); // Ordenación
        System.out.println("Array: " + Arrays.toString(array));

        // Matriz
        int[][] matrix = new int[3][3];
        matrix[0][0] = 1;
        matrix[0][1] = 2;
        matrix[0][2] = 3;
        matrix[1][0] = 4;
        matrix[1][1] = 5;
        matrix[1][2] = 6;
        matrix[2][0] = 7;
        matrix[2][1] = 8;
        matrix[2][2] = 9;
        matrix[1][1] = 50; // Actualización
        matrix[2][0] = 0; // "Borrado"

        // Ordenación por filas
        for (int i = 0; i < matrix.length; i++) {
            Arrays.sort(matrix[i]);
        }

        System.out.println("Matriz ordenada por filas:");
        for (int i = 0; i < matrix.length; i++) {
            System.out.println(Arrays.toString(matrix[i]));
        }

        // ArrayList
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(1);
        arrayList.add(2);
        arrayList.add(3);
        arrayList.set(1, 20); // Actualización
        arrayList.remove(Integer.valueOf(3)); // Borrado
        Collections.sort(arrayList); // Ordenación
        System.out.println("ArrayList: " + arrayList);

        // LinkedList
        LinkedList<String> linkedList = new LinkedList<>();
        linkedList.add("A");
        linkedList.add("B");
        linkedList.add("C");
        linkedList.set(1, "Z"); // Actualización
        linkedList.remove("C"); // Borrado
        Collections.sort(linkedList); // Ordenación
        System.out.println("LinkedList: " + linkedList);

        // HashMap
        HashMap<Integer, String> hashMap = new HashMap<>();
        hashMap.put(1, "Uno");
        hashMap.put(2, "Dos");
        hashMap.put(3, "Tres");
        hashMap.put(2, "Veinte"); // Actualización
        hashMap.remove(3); // Borrado
        System.out.println("HashMap: " + hashMap);

        // HashSet
        HashSet<String> hashSet = new HashSet<>();
        hashSet.add("A");
        hashSet.add("B");
        hashSet.add("C");
        hashSet.add("B"); // No se añadirá porque ya existe
        hashSet.remove("C"); // Borrado
        // Ordenación (conversión a lista y ordenación)
        ArrayList<String> sortedList = new ArrayList<>(hashSet);
        Collections.sort(sortedList);
        System.out.println("HashSet: " + sortedList);

        // TreeMap
        TreeMap<Integer, String> treeMap = new TreeMap<>();
        treeMap.put(1, "Uno");
        treeMap.put(2, "Dos");
        treeMap.put(3, "Tres");
        treeMap.put(2, "Veinte"); // Actualización
        treeMap.remove(3); // Borrado
        System.out.println("TreeMap: " + treeMap);

        // TreeSet
        TreeSet<String> treeSet = new TreeSet<>();
        treeSet.add("A");
        treeSet.add("B");
        treeSet.add("C");
        treeSet.add("B"); // No se añadirá porque ya existe
        treeSet.remove("C"); // Borrado
        System.out.println("TreeSet: " + treeSet);

        // Vector
        Vector<Integer> vector = new Vector<>();
        vector.add(1);
        vector.add(2);
        vector.add(3);
        vector.set(1, 20); // Actualización
        vector.remove(Integer.valueOf(3)); // Borrado
        Collections.sort(vector); // Ordenación
        System.out.println("Vector: " + vector);

        // PriorityQueue
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(3);
        priorityQueue.add(1);
        priorityQueue.add(2);
        priorityQueue.add(20); // Inserción
        priorityQueue.remove(2); // Borrado
        System.out.println("PriorityQueue (ordenada automáticamente): ");
        while (!priorityQueue.isEmpty()) {
            System.out.print(priorityQueue.poll() + " \n\n");

        }
        boolean exit = false;
        while (!exit) {
            try {
                System.out.println("*******Libreta de contactos******* \n" + //
                        "");
                System.out.println("***Ingresa el numero de la accion que deseas realizar*** \n" + //
                        "");

                System.out.println("1: Registrar contacto");
                System.out.println("2: buscar contacto ");
                System.out.println("3: Actualizar contacto");
                System.out.println("4: Eliminar contacto");
                System.out.println("5: salir");

                int option = input.nextInt();

                switch (option) {
                    case 1:
                        register();
                        break;
                    case 2:
                        find();
                        break;
                    case 3:
                        update();
                        break;
                    case 4:
                        delete();
                        break;
                    case 5:
                        exit = true;
                        break;
                    default:
                        break;
                }
            } catch (InputMismatchException e) {
                System.out.println("Ingrese una opcion valida");
                input.nextLine();
            }
        }

    }

    public static void register() {
        Scanner input = new Scanner(System.in);

        System.out.println("Nombre");
        String name = input.nextLine();

        System.out.println("Numero de telefono");
        String numberOfPhone = input.nextLine();

        while (numberOfPhone.length() > 11 || !esNumerico(numberOfPhone)) {

            System.out.print("Número de teléfono inválido. Ingresa un número maximo de 11 dígitos: ");
            numberOfPhone = input.nextLine();

            break;

        }
        contacto.put(numberOfPhone, name);
    }

    private static String find() {
        Scanner input = new Scanner(System.in);

        try {
            System.out.println("Número de teléfono:");
            String numberOfPhone = input.nextLine();

            if (contacto.containsKey(numberOfPhone) && esNumerico(numberOfPhone)) {
                String name = contacto.get(numberOfPhone);
                System.out.println("Contacto encontrado:");
                System.out.println("Nombre: " + name);
                System.out.println("Número de teléfono: " + numberOfPhone);
                return numberOfPhone;
            } else if (!esNumerico(numberOfPhone)) {
                System.out.println("Ingresa un número entero válido.");
            } else {
                System.out.println("No se encontró ningún contacto para el número " + numberOfPhone);
            }
        } catch (NoSuchElementException e) {
            System.out.println("Error: No se encontró ningún contacto.");
        }
        return null;
    }

    private static void update() {
        Scanner input = new Scanner(System.in);

        String currentNumberOfPhone = find();
        String newNumberOfPhone = "";

        if (currentNumberOfPhone != null) {
            System.out.println("Ingresa el nuevo numero de telefono");
            newNumberOfPhone = input.nextLine();

            while (newNumberOfPhone.length() > 11 || !esNumerico(newNumberOfPhone)) {

                System.out.print("Número de teléfono inválido. Ingresa un número maximo de 11 dígitos: ");
                newNumberOfPhone = input.nextLine();

                break;

            }

        }

        System.out.println("Ingresa el nuevo nombre");
        String newName = input.nextLine();

        contacto.remove(currentNumberOfPhone);
        contacto.put(newNumberOfPhone, newName);
        System.out.println("Contacto actualizado con éxito.");

    }

    private static void delete() {
        String deleteNumberOfPhone = find();

        contacto.remove(deleteNumberOfPhone);

        System.out.println("contacto eliminado con exito");
    }

    private static boolean esNumerico(String cadena) {
        try {
            Long.parseLong(cadena);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

}
