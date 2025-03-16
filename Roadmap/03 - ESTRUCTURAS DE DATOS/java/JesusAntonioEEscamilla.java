/** #03 - Java -> Jesus Antonio Escamilla */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class JesusAntonioEEscamilla {
    private static final int MAX_DIGITS = 11;
    public static void main(String[] args) {
    //---EJERCIÓ---
        array();
        list();
        map();
        set();
    //---EXTRA---
        EXTRA();
    }

    public static void array(){
        //.....ARRAYS.....
        // Creando Arreglo
        System.out.println("---ARRAY---");
        int[] arreglo = new int[5];
        
        // INSERCIÓN
        System.out.println("INSERCIÓN");
        arreglo[0] = 20;
        arreglo[1] = 10;
        arreglo[2] = 40;
        arreglo[3] = 30;
        arreglo[4] = 60;
        System.out.println(Arrays.toString(arreglo));

        // BORRANDO
        System.out.println("BORRADO");
        System.out.println("No hay forma directa para borrar un elemento");
        System.out.println("Pero mostrare otra forma de borrar un elemento");
        int indexToRemove = 4;
        for (int i = indexToRemove; i < arreglo.length -1; i++) {
            arreglo[i] = arreglo[i + 1];
        }
        // Reducir el tamaño del array eliminando el último elemento
        arreglo = Arrays.copyOf(arreglo, arreglo.length - 1);
        System.out.println(Arrays.toString(arreglo));

        // ACTUALIZACIÓN
        System.out.println("ACTUALIZACIÓN");
        arreglo[2] = 35;
        System.out.println(Arrays.toString(arreglo));

        // ORDENAMIENTO
        System.out.println("ORDENAMIENTO");
        Arrays.sort(arreglo);
        System.out.println(Arrays.toString(arreglo));
    }

    public static void list(){
        //.....LISTAS.....
        // Creando Lista
        System.out.println("---LISTA---");
        List<String> lista = new ArrayList<>();
        Collections.addAll(lista, "Manzana", "Pera", "Banana", "Cereza", "Melon");
        System.out.println(lista);
        
        // INSERCIÓN
        System.out.println("INSERCIÓN");
        lista.add("Uva");
        System.out.println(lista);
        lista.add(0, "Kiwi");
        System.out.println(lista);

        // BORRANDO
        System.out.println("BORRADO");
        lista.remove("Banana");
        System.out.println(lista);
        String elementoBorrado = lista.remove(2);
        System.out.println(elementoBorrado);
        System.out.println(lista);

        // ACTUALIZACIÓN
        System.out.println("ACTUALIZACIÓN");
        lista.set(2, "Papaya");
        System.out.println(lista);

        // ORDENAMIENTO
        System.out.println("ORDENAMIENTO");
        Collections.sort(lista);
        List<String> listaOrdenada = new ArrayList<>(lista);
        System.out.println("Lista Ordenada: " + listaOrdenada);
    }

    public static void map(){
        //.....HASHMAP.....
        // Creando Arreglo
        System.out.println("---HASHMAP---");
        HashMap<String, Integer> mapa = new HashMap<>();
        
        // INSERCIÓN
        System.out.println("INSERCIÓN");
        mapa.put("Rancheros", 1);
        mapa.put("Palomitas", 10);
        mapa.put("Galletas", 4);
        mapa.put("Pan", 2);
        mapa.put("Coca Cola", 8);
        System.out.println(mapa);

        // BORRANDO
        System.out.println("BORRADO");
        mapa.remove("Pan");
        System.out.println(mapa);

        // ACTUALIZACIÓN
        System.out.println("ACTUALIZACIÓN");
        mapa.put("Galletas", 3);
        System.out.println(mapa);

        // ORDENAMIENTO
        System.out.println("ORDENAMIENTO");
        System.out.println("No hay forma directa para ordenar los elementos");
    }

    public static void set(){
        //.....HASHSET.....
        // Creando Arreglo
        System.out.println("---HASHSET---");
        HashSet<String> conjunto = new HashSet<>();
        
        // INSERCIÓN
        System.out.println("INSERCIÓN");
        conjunto.add("A");
        conjunto.add("B");
        conjunto.add("C");
        conjunto.add("D");
        System.out.println(conjunto);

        // BORRANDO
        System.out.println("BORRADO");
        conjunto.remove("B");
        System.out.println(conjunto);

        // ACTUALIZACIÓN
        System.out.println("ACTUALIZACIÓN");
        conjunto.remove("D");
        System.out.println(conjunto);
        conjunto.add("E");
        System.out.println(conjunto);

        // ORDENAMIENTO
        System.out.println("ORDENAMIENTO");
        System.out.println("No hay forma directa para ordenar los elementos");
    }

    /**-----DIFICULTAD EXTRA-----*/

    public static void EXTRA(){
        Map<String, String> agenda = new HashMap<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            mostrarMenu();
            String option = scanner.nextLine();

            switch (option) {
                case "1":
                    insertarContacto(agenda, scanner);
                    break;
                case "2":
                    buscarContacto(agenda, scanner);
                    break;
                case "3":
                    actualizarContacto(agenda, scanner);
                    break;
                case "4":
                    eliminarContacto(agenda, scanner);
                    break;
                case "5":
                    mostrarTodosContactos(agenda);
                    break;
                case "6":
                    System.out.println("Saliendo del programa.....");
                    scanner.close();
                    return;
                default:
                    System.out.println("Opción ni valida. Intente de nuevo");
                    break;
            }
        }
    }

    private static void mostrarMenu() {
        System.out.println("\nAgenda de Contactos");
        System.out.println("1. Insertar Contacto");
        System.out.println("2. Buscar Contacto");
        System.out.println("3. Actualizar Contacto");
        System.out.println("4. Eliminar Contacto");
        System.out.println("5. Mostrar todos los Contacto");
        System.out.println("6. Salir");
        System.out.print("Seleccione una option: ");
    }

    private static boolean validarTelefono(String telefono){
        return telefono.matches("\\d+") && telefono.length() <= MAX_DIGITS;
    }

    private static void insertarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el Nombre del contacto: ");
        String nombre = scanner.nextLine();
        System.out.print("Ingrese el Teléfono del contacto: ");
        String telefono = scanner.nextLine();

        if (validarTelefono(telefono)) {
            agenda.put(nombre, telefono);
            System.out.println("Contacto " + nombre + " añadido con éxito");
        } else {
            System.out.println("Numero de Teléfono no valido. Debe ser numérico y tener un máximo de " + (MAX_DIGITS - 1) + " dígitos");
        }
    }

    private static void buscarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el Nombre del contacto al buscar: ");
        String nombre = scanner.nextLine();
        if (agenda.containsKey(nombre)) {
            System.out.println("Nombre: " + nombre + ", Teléfono: " + agenda.get(nombre));
        } else {
            System.out.println("Contacto no encontrado");
        }
    }

    private static void actualizarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el Nombre del contacto al actualizar: ");
        String nombre = scanner.nextLine();
        if (agenda.containsKey(nombre)) {
            System.out.print("Ingrese el nuevo numero de telefono: ");
            String nuevoTelefono = scanner.nextLine();
            if (validarTelefono(nuevoTelefono)) {
                agenda.put(nombre, nuevoTelefono);
                System.out.println("Contacto " + nombre + " actualizado con éxito");
            } else {
                System.out.println("Numero de Teléfono no valido. Debe ser numérico y tener un máximo de " + (MAX_DIGITS - 1) + " dígitos");
            }
        } else {
            System.out.println("Contacto no encontrado");
        }
    }

    private static void eliminarContacto(Map<String, String> agenda, Scanner scanner) {
        System.out.print("Ingrese el Nombre del contacto a eliminar: ");
        String nombre = scanner.nextLine();
        if (agenda.containsKey(nombre)) {
            agenda.remove(nombre);
            System.out.println("Contacto " + nombre + " eliminado con éxito");
        } else {
            System.out.println("Contacto no encontrado");
        }
    }

    private static void mostrarTodosContactos(Map<String, String> agenda) {
        if (agenda.isEmpty()) {
            System.out.println("No hay contactos en la agenda");
        } else {
            for (Map.Entry<String, String> entry : agenda.entrySet()) {
                System.out.println("Nombre: " + entry.getKey() + ", Telefono: " + entry.getValue());
            }
        }
    }

    /**-----DIFICULTAD EXTRA-----*/
}