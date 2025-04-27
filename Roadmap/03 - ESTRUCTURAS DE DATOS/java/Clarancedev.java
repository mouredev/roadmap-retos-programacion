/**
 * @author clarancedev
 * @version 1.0 - 2025/04/15
 */

import java.util.Arrays;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Collections;
import java.util.Stack;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.HashMap;
import java.util.Scanner;

public class Clarancedev {

    // TIPOS DE ESTRUCTURAS DE DATOS

    public static void exampleArray() {

        /*
        ARRAYS
        - Almacena valores de un mismo tipo
        - Se accede a los valores mediante un índice
        - Tamaño fijo determinado al crearse, sin poder modificarse después
        */

        // Creación
        int[] array1 = new int[5];
        int[] array2 = {1, 2, 3, 4, 5};

        // Inserción de valores indicando la posición
        array1[0] = 10;
        array1[1] = 20;
        array1[2] = 30;
        array1[3] = 40;
        array1[4] = 50;

        // Cambio de valor de una posición
        array2[0] = 0;

        // Recorrer un array
        for (int i = 0; i < array1.length; i++) {
            System.out.println(array1[i]);
        }
        System.out.println("Cómo recorre un bucle for-each un array:");
        for (int i : array2) {
            System.out.println(i); // 0, 20, 30, 40, 50
        }

        // Imprimir array
        System.out.println(Arrays.toString(array1)); // 0, 20, 30, 40, 50

        // Imprimir posición
        System.out.println("Impresión de una posición de un array: " + array1[0]);
    }

    public static void exampleArrayList() {

        /*
        ARRAYLIST
        - Almacena datos de un mismo tipo, pero también objetos
        - Tamaño dinámico
        - Puntos fuertes: rápido para consultas y actualizaciones
        - Puntos débiles: lento para inserciones y borrados en posiciones concretas
        */

        // Creación
        java.util.ArrayList<Integer> arrayList = new java.util.ArrayList<>();

        // Inserción de valores (se añaden al final de la lista)
        arrayList.add(10);
        arrayList.add(20);
        arrayList.add(30);

        // Otros tipos de inserción
        arrayList.add(2, 100); // Valores en posiciones posteriores se moverán de posición (n + 1)
        arrayList.addFirst(0); // También aplicable con .remove y .set
        arrayList.addLast(40); // También aplicable con .remove y .set

        // Borrado de un valor
        arrayList.remove(1);

        // Actualización ([índice], [valor])
        arrayList.set(4, 25);

        // Ordenación
        java.util.Collections.sort(arrayList);

        // Se recorren de la misma forma que un array
        for (int i = 0; i < arrayList.size(); i++) {
            System.out.println(arrayList.get(i));
        }

        // Imprimir lista + posición concreta
        System.out.println(arrayList + "\n" + arrayList.get(1));
    }

    public static void exampleLinkedList() {
        /*
        LINKEDLIST
        - Almacena datos de un mismo tipo, pero también objetos
        - Tamaño dinámico
        - Puntos fuertes: rápido para inserciones y borrados en posiciones concretas
        - Puntos débiles: lento para consultas y actualizaciones
        */

        // Creación
        java.util.LinkedList<Integer> linkedList = new java.util.LinkedList<>();

        // Inserción de valores (se añaden al final de la lista)
        linkedList.add(10);
        linkedList.add(20);
        linkedList.add(30);

        // Otros tipos de inserción
        linkedList.add(2, 100); // Valores en posiciones posteriores se moverán de posición (n + 1)
        linkedList.addFirst(0); // También aplicable con .remove y .set
        linkedList.addLast(40); // También aplicable con .remove y .set

        // Borrado de un valor
        linkedList.remove(1);

        // Actualización ([indice], [valor])
        linkedList.set(4, 25);

        // Ordenación de la lista
        java.util.Collections.sort(linkedList);

        // Se recorren de la misma forma que un array
        for (int i = 0; i < linkedList.size(); i++) {
            System.out.println(i);
        }

        // Imprimir lista + posición concreta
        System.out.println(linkedList + "\n" + linkedList.get(1));
    }

    public static void exampleStack() {

        /*
        STACK (también conocido como PILA)
        - Lógica de manipulación de datos según el principio LIFO (Last-In-First-Out)
        - Solo permite inserción/borrado/consulta sobre último valor almacenado
        - Ideal para almacenar datos temporales y acceder a ellos según LIFO
        */

        // Creación
        Stack<Integer> aStack = new Stack<>();

        // Inserción
        aStack.push(10);
        aStack.push(20);
        aStack.push(30);
        aStack.push(40);
        aStack.push(50);

        // Borrado
        aStack.pop(); // En este caso el valor [50]

        // Consulta (imprimiendo directamente el valor)
        aStack.peek(); // 40

        // Imprimir todos los valores
        System.out.println(aStack); // [10, 20, 30, 40]

        /* OJO:
        * Con la clase predeterminada Stack la impresión de todos
        * los elementos no se hace según la lógica LIFO. Si queremos
        * una impresión LIFO, tenemos las clases Deque + ArrayDeque.
        */

        // Ejemplo Deque implementando ArrayDeque
        Deque<Integer> aDeque = new ArrayDeque<>();

        aDeque.push(10);
        aDeque.push(20);
        aDeque.push(30);
        aDeque.push(40);
        aDeque.push(50);

        aDeque.pop();

        aDeque.peek();

        System.out.println(aDeque); // [40, 30, 20, 10]
    }

    public static void exampleQueue() {

        /*
        QUEUE (también conocido como COLA)
        - Lógica de manipulación de datos según el principio FIFO (First-In-First-Out)
        - Inserción se aplica sobre la siguiente posición
        - Borrado y consulta se aplican sobre la primera posición
        - Ideal para almacenar datos temporales y acceder a ellos según FIFO
        */

        // Creación
        Queue<Integer> aQueue = new ArrayDeque<>();

        // Inserción (Enqueue)
        aQueue.offer(10);
        aQueue.offer(20);
        aQueue.offer(30);
        aQueue.offer(40);
        aQueue.offer(50);

        // Borrado (Dequeue)
        aQueue.poll(); // En este caso el valor [10]

        // Consulta (imprimiendo directamente el valor)
        aQueue.peek(); // 20

        // Imprimir todos los valores
        System.out.println(aQueue); // [20, 30, 40, 50]
    }

    public static void exampleHash() {

        /*
        HASH
        - Las tablas hash almacenan datos en pares clave-valor, sin duplicados
        - Permite acceso rápido a los valores mediante la clave
        - No garantiza el orden de los elementos
        - El HashMap es la implementación más común
        - Ideal para búsquedas rápidas de valores mediante su referencia
        */

        // Creación
        HashMap<String, Integer> hashMap = new HashMap<>();

        // Inserción ([clave], [valor])
        hashMap.put("One", 1);
        hashMap.put("Two", 2);
        hashMap.put("Three", 3);

        // Borrado
        hashMap.remove("Dos");

        // Actualización ([clave], [nuevo valor])
        hashMap.put("Tres", 4);

        // Consulta ([clave])
        System.out.println(hashMap.get("Uno")); // 1

        // Imprimir todos los valores
        System.out.println(hashMap); // {Uno=1, Tres=4}
    }

    /*
    DIFICULTAD EXTRA
    Agenda de contactos utilizando HashMap y desengranando en métodos
    */

    private static final HashMap<String, String> CONTACTS_AGENDA = new HashMap<>(); // Para almacenaje de datos
    private static final Scanner SCN = new Scanner(System.in); // Scanner

    public static void runContactsAgenda() {
        boolean running = false;
        System.out.println("\n-* AGENDA DE CONTACTOS *-");
        while (!running) {
            printMenu();
            int userOption = getOption();
            running = executeOption(userOption);
        }
    }

    // Menú
    private static void printMenu() {
        System.out.println("-----------Opciones:----------");
        System.out.println("------------------------------");
        System.out.println("1. Buscar contacto");
        System.out.println("2. Añadir contacto");
        System.out.println("3. Actualizar contacto");
        System.out.println("4. Eliminar contacto");
        System.out.println("5. Mostrar todos los contactos");
        System.out.println("6. Salir");
        System.out.println("------------------------------");
        System.out.println("Seleccione una opción:");
     }

    // Recoger opción seleccionada
    private static int getOption() {

        int userOption = 0;
        if (SCN.hasNextInt()) {
            userOption = SCN.nextInt();
            SCN.nextLine();
            checkUserOption(userOption);
        } else {
            System.out.println("Formato incorrecto. Debe introducir un número entre 1 y 6:");
            SCN.nextLine();
            getOption();
        }
        return userOption;
    }

    // Controlar input usuario (valor de tipo int entre 1 y 6)
    private static void checkUserOption(int userOption) {

        if (userOption < 1 || userOption > 6) {
            System.out.println("Valor incorrecto. Debe introducir un número entre 1 y 6:");
            getOption();
        }
    }

    // Ejecución de opción del menú seleccionada por usuario
    private static boolean executeOption(int userOption) {
        boolean running = false;

        switch (userOption) {
            case 1 -> searchContact();
            case 2 -> addContact();
            case 3 -> updateContact();
            case 4 -> deleteContact();
            case 5 -> printAllContacts();
            case 6 -> {
                System.out.println("Cerrando agenda de contactos.");
                running = true;
            }
        }
        return running;
    }

    // Buscar contacto
    private static void searchContact() {
        if (CONTACTS_AGENDA.isEmpty()) {
            System.out.println("La agenda de contactos está vacía.");
        } else {
            System.out.println("Indique el nombre del contacto que desea buscar:");
            String contactName = checkNameInput(SCN.nextLine().trim());

            if (CONTACTS_AGENDA.containsKey(contactName)) {
                System.out.println("El número de teléfono de " + contactName + " es: " + CONTACTS_AGENDA.get(contactName));
            } else {
                System.out.println("El contacto \"" + contactName + "\" no existe.");
            }
        }
    }

    // Añadir contacto
    private static void addContact() {
        System.out.println("Indique el nombre del nuevo contacto: ");
        String name = checkNameInput(SCN.nextLine().trim());
        System.out.println("Indique el número de teléfono de " + name + ":");
        String phoneNumber = checkPhoneNumberInput(SCN.nextLine().trim());
        CONTACTS_AGENDA.put(name, phoneNumber);
        System.out.println("Contacto registrado con los siguientes datos:\n" + name + " - " + phoneNumber);
    }

    // Controlar input usuario para nombre de contacto (valor de tipo String no vacío)
    private static String checkNameInput(String contactName) {

        while (contactName.isEmpty()) {
            System.out.println("El campo no puede estar vacío. Introduzca un nombre válido:");
            contactName = SCN.nextLine().trim();
        }
        return contactName;
    }

    // Controlar input usuario de número de teléfono (valor de tipo String de entre 1 y 11 dígitos)
    private static String checkPhoneNumberInput(String contactPhoneNumber) {

        while (!contactPhoneNumber.matches("\\d{1,11}")) {
            System.out.println("El campo no puede estar vacío, ni tener más de 11 dígitos. Introduzca un número de teléfono válido");
            contactPhoneNumber = SCN.nextLine().trim();
        }
        return contactPhoneNumber;
    }

    // Actualizar contacto
    private static void updateContact() {
        if (CONTACTS_AGENDA.isEmpty()) {
            System.out.println("La agenda de contactos está vacía.");
        } else {
            System.out.println("Indique el nombre del contacto que desea actualizar:");
            String contactName = checkNameInput(SCN.nextLine().trim());

            if (!CONTACTS_AGENDA.containsKey(contactName)) {
                System.out.println("El contacto \"" + contactName + "\" no existe.");
            } else {
                System.out.println("Indique el nuevo número de teléfono para el contacto \"" + contactName + "\":");
                String newContactPhoneNumber = checkPhoneNumberInput(SCN.nextLine().trim());
                CONTACTS_AGENDA.put(contactName, newContactPhoneNumber);
                System.out.println("El nuevo número de teléfono de " + contactName + " es: " + newContactPhoneNumber);
            }
        }
    }

    // Eliminar contacto
    private static void deleteContact() {
        if (CONTACTS_AGENDA.isEmpty()) {
            System.out.println("La agenda de contactos está vacía.");
        } else {
            System.out.println("Indique el nombre del contacto que desea eliminar:");
            String contactName = checkNameInput(SCN.nextLine().trim());

            if (!CONTACTS_AGENDA.containsKey(contactName)) {
                System.out.println("El contacto \"" + contactName + "\" no existe.");
            } else {
                CONTACTS_AGENDA.remove(contactName);
                System.out.println("El contacto \"" + contactName + "\" ha sido eliminado.");
            }
        }
    }

    // Imprimir todos los contactos existentes
    private static void printAllContacts() {
        if (CONTACTS_AGENDA.isEmpty()) {
            System.out.println("La agenda de contactos está vacía.");
        } else {
            System.out.println("Contactos existentes:");
            CONTACTS_AGENDA.forEach((contactName, contactPhoneNumber) -> {
                System.out.println(contactName + " - " + contactPhoneNumber);
            });
        }
    }


    public static void main (String[]args){
        runContactsAgenda();
    }

}
