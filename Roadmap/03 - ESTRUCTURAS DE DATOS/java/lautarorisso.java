import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class LogicaJava03 {
    
    private static final Map<String, String> agenda = new HashMap<>();
    private static final Scanner teclado =new Scanner(System.in);
    
    public static void main(String[] args) {
    
        // 1.
        // Array
        int[] numeros = new int[3];

        // Inserción / actualización
        numeros[0] = 10;
        numeros[1] = 5;

        // Borrado (no existe, se reasigna)
        numeros[1] = 0;

        // Ordenación
        Arrays.sort(numeros);

        // Mostrar
        System.out.println(Arrays.toString(numeros));
        
        // ArrayList
        
        List<String> nombres = new ArrayList<>();

        // Inserción
        nombres.add("Ana");
        nombres.add("Pedro");

        // Actualización
        nombres.set(1, "Lucía");

        // Borrado
        nombres.remove("Pedro");

        // Ordenación
        Collections.sort(nombres);

        // Mostrar
        System.out.println(nombres);

        // LinkedList
        List<Integer> edades = new LinkedList<>();

        edades.add(30);
        edades.add(20);

        edades.set(0, 35);
        edades.remove(1);

        Collections.sort(edades);

        System.out.println(edades);

        // HashSet
        Set<String> paises = new HashSet<>();

        paises.add("Argentina");
        paises.add("Brasil");
        paises.add("Argentina"); // duplicado, no entra

        paises.remove("Brasil");

        // ❌ No hay actualización directa (se borra y se agrega)
        paises.remove("Argentina");
        paises.add("Uruguay");

        // Ordenación → convertir a lista
        List<String> ordenados = new ArrayList<>(paises);
        Collections.sort(ordenados);

        System.out.println(ordenados);
        
        // TreeSet
        Set<Integer> numeros2 = new TreeSet<>();

        numeros2.add(50);
        numeros2.add(10);

        numeros2.remove(10);

        // Ya está ordenado
        System.out.println(numeros);
        
        // HashMap
        
        Map<String, Integer> personas = new HashMap<>();

        // Inserción
        personas.put("Roberto", 25);
        personas.put("Ana", 30);

        // Actualización
        personas.put("Roberto", 40);

        // Borrado
        personas.remove("Ana");

        // Ordenación por clave
        Map<String, Integer> ordenado = new TreeMap<>(personas);

        System.out.println(ordenado);

        // TreeMap
        Map<Integer, String> ranking = new TreeMap<>();

        ranking.put(3, "Bronce");
        ranking.put(1, "Oro");
        ranking.put(2, "Plata");

        ranking.remove(3);

        System.out.println(ranking);

        // Queue
        Queue<String> cola = new LinkedList<>();

        cola.add("Cliente 1");
        cola.add("Cliente 2");

        cola.poll(); // elimina el primero

        System.out.println(cola);

        // Stack
        Stack<Integer> pila = new Stack<>();

        pila.push(10);
        pila.push(20);

        pila.pop(); // elimina el último

        System.out.println(pila);
        
        
        // EXTRA : Agenda de contactos
        int opcion;
        
        do {
            mostrarMenu();
            opcion = leerOpcion();

            switch (opcion) {
                case 1 -> insertarContacto();
                case 2 -> buscarContacto();
                case 3 -> actualizarContacto();
                case 4 -> eliminarContacto();
                case 5 -> System.out.println("Programa finalizado.");
                default -> System.out.println("Opción inválida");
            }

        } while (opcion != 5);

        teclado.close();
    }
    
    private static void mostrarMenu() {
        System.out.println("\n--- AGENDA DE CONTACTOS ---");
        System.out.println("1. Insertar contacto");
        System.out.println("2. Buscar contacto");
        System.out.println("3. Actualizar contacto");
        System.out.println("4. Eliminar contacto");
        System.out.println("5. Salir");
        System.out.print("Elegí una opción: ");
    }

    private static int leerOpcion() {
        while (!teclado.hasNextInt()) {
            System.out.print("Ingresá un número válido: ");
            teclado.next();
        }
        int opcion = teclado.nextInt();
        teclado.nextLine(); // limpiar buffer
        return opcion;
    }
    
    private static String leerTelefono() {
        String telefono;
        
        while (true) {
            System.out.print("Teléfono (solo números, máx 11 dígitos): ");
            telefono = teclado.nextLine();
            
            if (telefono.length() == 0) {
            System.out.println("Error: no puede estar vacío.");
            continue;
            }

            if (telefono.length() > 11) {
                System.out.println("Error: máximo 11 dígitos.");
                continue;
            }

            boolean esNumerico = true;

            for (int i = 0; i < telefono.length(); i++) {
                char c = telefono.charAt(i);

                if (c < '0' || c > '9') {
                    esNumerico = false;
                    break;
                }
            }

            if (!esNumerico) {
                System.out.println("Error: solo números.");
                continue;
            }

            break;
        }

        return telefono;
    }
    
    private static void insertarContacto() {
        System.out.print("Nombre: ");
        String nombre = teclado.nextLine();

        if (agenda.containsKey(nombre)) {
            System.out.println("Ese contacto ya existe.");
            return;
        }

        String telefono = leerTelefono();
        agenda.put(nombre, telefono);
        System.out.println("Contacto agregado.");
    }
    
    private static void buscarContacto() {
        System.out.print("Nombre a buscar: ");
        String nombre = teclado.nextLine();

        if (agenda.containsKey(nombre)) {
            System.out.println("Teléfono: " + agenda.get(nombre));
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }
    
    private static void actualizarContacto() {
        System.out.print("Nombre a actualizar: ");
        String nombre = teclado.nextLine();

        if (!agenda.containsKey(nombre)) {
            System.out.println("El contacto no existe.");
            return;
        }

        System.out.print("Escribe telefono nuevo: ");
        String nuevoTelefono = leerTelefono();
        agenda.put(nombre, nuevoTelefono);
        System.out.println("Contacto actualizado.");
    }

    private static void eliminarContacto() {
        System.out.print("Nombre a eliminar: ");
        String nombre = teclado.nextLine();

        if (agenda.remove(nombre) != null) {
            System.out.println("Contacto eliminado.");
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }
}
