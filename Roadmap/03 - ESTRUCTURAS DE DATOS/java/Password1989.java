package org.roadmap.java.ejercicio.tres;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class Password1989 {

	// Mapa para almacenar los contactos (nombre como clave y teléfono como valor)
    private static final HashMap<String, String> contacts = new HashMap<>();
    private static final Scanner scanner = new Scanner(System.in);

    // Constante para la opción de salir
    private static final int OPTION_EXIT = 6;

    // Bucle principal de la agenda
    public static void runAgenda() {
        boolean exit = false;
        while (!exit) {
            showMenu();
            int option = readOption();
            exit = processOption(option);
        }
    }

    // Mostrar menú
    private static void showMenu() {
        System.out.println("\n--- Agenda de Contactos ---");
        System.out.println("1. Insertar contacto");
        System.out.println("2. Buscar contacto");
        System.out.println("3. Actualizar contacto");
        System.out.println("4. Eliminar contacto");
        System.out.println("5. Mostrar todos los contactos");
        System.out.println("6. Salir");
        System.out.print("Elige una opción: ");
    }

    // Leer opción del usuario
    private static int readOption() {
        int option = scanner.nextInt();
        scanner.nextLine(); // Limpieza del buffer
        return option;
    }

    // Procesar la opción elegida
    private static boolean processOption(int option) {
        switch (option) {
            case 1:
                insertContact();
                break;
            case 2:
                searchContact();
                break;
            case 3:
                updateContact();
                break;
            case 4:
                deleteContact();
                break;
            case 5:
                showAllContacts();
                break;
            case OPTION_EXIT:
                System.out.println("Adiós!");
                return true;
            default:
                System.out.println("Opción no válida.");
        }
        return false;
    }

    // Insertar un contacto
    private static void insertContact() {
        String name = inputNonEmptyString("Introduce nombre: ");
        String phone = inputValidPhoneNumber();

        if (contacts.containsKey(name)) {
            System.out.println("El contacto ya existe.");
        } else {
            contacts.put(name, phone);
            System.out.println("Contacto añadido.");
        }
    }

    // Buscar un contacto (verificar si el mapa está vacío)
    private static void searchContact() {
        if (contacts.isEmpty()) {
            System.out.println("La agenda está vacía. No hay contactos para buscar.");
            return;
        }

        String name = inputNonEmptyString("Introduce nombre a buscar: ");

        if (contacts.containsKey(name)) {
            System.out.println("Nombre: " + name + ", Teléfono: " + contacts.get(name));
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }

    // Actualizar un contacto (verificar si el mapa está vacío)
    private static void updateContact() {
        if (contacts.isEmpty()) {
            System.out.println("La agenda está vacía. No hay contactos para actualizar.");
            return;
        }

        String name = inputNonEmptyString("Introduce nombre del contacto a actualizar: ");

        if (contacts.containsKey(name)) {
            String newPhone = inputValidPhoneNumber();
            contacts.put(name, newPhone);
            System.out.println("Contacto actualizado.");
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }

    // Eliminar un contacto (verificar si el mapa está vacío)
    private static void deleteContact() {
        if (contacts.isEmpty()) {
            System.out.println("La agenda está vacía. No hay contactos para eliminar.");
            return;
        }

        String name = inputNonEmptyString("Introduce nombre del contacto a eliminar: ");

        if (contacts.remove(name) != null) {
            System.out.println("Contacto eliminado.");
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }

    // Mostrar todos los contactos
    private static void showAllContacts() {
        if (contacts.isEmpty()) {
            System.out.println("No hay contactos en la agenda.");
        } else {
            System.out.println("--- Lista de Contactos ---");
            contacts.forEach((name, phone) -> 
                System.out.println("Nombre: " + name + ", Teléfono: " + phone));
        }
    }

    // Leer una cadena no vacía del usuario
    private static String inputNonEmptyString(String prompt) {
        String input;
        do {
            System.out.print(prompt);
            input = scanner.nextLine().trim();
            if (input.isEmpty()) {
                System.out.println("El valor no puede estar vacío. Inténtalo de nuevo.");
            }
        } while (input.isEmpty());
        return input;
    }

    // Validar y leer un número de teléfono válido (solo dígitos, hasta 11 caracteres)
    private static String inputValidPhoneNumber() {
        String phone;
        do {
            System.out.print("Introduce un número de teléfono (solo dígitos, máximo 11): ");
            phone = scanner.nextLine().trim();
            if (!phone.matches("\\d{1,11}")) {
                System.out.println("Número de teléfono no válido. Debe contener solo dígitos y hasta 11 caracteres.");
            }
        } while (!phone.matches("\\d{1,11}"));
        return phone;
    }
	
	public static void main(String[] args) {
		
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
		 
		
		// Creación de una lista
        ArrayList<Integer> list = new ArrayList<>();

        // Inserción
        list.add(5);
        list.add(2);
        list.add(8);
        System.out.println("Lista después de inserción: " + list);

        // Borrado
        list.remove(Integer.valueOf(2)); // Eliminar el valor 2
        System.out.println("Lista después de borrado: " + list);

        // Actualización
        list.set(1, 2); // Cambiar el elemento en el índice 1 por 10
        System.out.println("Lista después de actualización: " + list);

        // Ordenación
        Collections.sort(list);
        System.out.println("Lista ordenada: " + list);
        
        // Creación de un conjunto
        HashSet<String> set = new HashSet<>();

        // Inserción
        set.add("Rojo");
        set.add("Azul");
        set.add("Verde");
        System.out.println("Conjunto después de inserción: " + set);

        // Borrado
        set.remove("Azul");
        System.out.println("Conjunto después de borrado: " + set);

        // Actualización (no hay actualización directa, se debe eliminar y volver a insertar)
        set.remove("Rojo");
        set.add("Amarillo");
        System.out.println("Conjunto después de actualización: " + set);

        // Ordenación (no aplicable a HashSet, pero se puede convertir en una lista)
        System.out.println("Conjunto (no ordenado por defecto): " + set);
        
        // Creación de una lista enlazada
        LinkedList<Integer> queue = new LinkedList<>();

        // Inserción (en cola)
        queue.add(3);
        queue.add(1);
        queue.add(4);
        System.out.println("Cola después de inserción: " + queue);

        // Borrado (de la cabeza)
        queue.remove();
        System.out.println("Cola después de borrado: " + queue);

        // Actualización
        queue.set(0, 7); // Cambia el primer elemento a 7
        System.out.println("Cola después de actualización: " + queue);

        // Ordenación
        Collections.sort(queue);
        System.out.println("Cola ordenada: " + queue);
        
        // Creación de una pila
        Stack<String> stack = new Stack<>();

        // Inserción (empujar en la pila)
        stack.push("Uno");
        stack.push("Dos");
        stack.push("Tres");
        System.out.println("Pila después de inserción: " + stack);

        // Borrado (pop, sacar de la pila)
        stack.pop();
        System.out.println("Pila después de borrado: " + stack);

        // Actualización (no hay actualización directa)
        stack.set(0, "Cuatro");
        System.out.println("Pila después de actualización: " + stack);
        
        // Creación de un mapa
        HashMap<Integer, String> map = new HashMap<>();

        // Inserción
        map.put(1, "Manzana");
        map.put(2, "Banana");
        map.put(3, "Cereza");
        System.out.println("Mapa después de inserción: " + map);

        // Borrado
        map.remove(2); // Eliminar la entrada con clave 2
        System.out.println("Mapa después de borrado: " + map);

        // Actualización
        map.put(1, "Durazno"); // Cambiar el valor de la clave 1
        System.out.println("Mapa después de actualización: " + map);

        // No hay ordenación para HashMap, ya que no mantiene orden.
        
         */
		runAgenda();
	}
}
