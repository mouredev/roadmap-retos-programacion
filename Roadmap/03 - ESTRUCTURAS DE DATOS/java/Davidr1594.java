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
 */

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Davidr1594 {

    public static void main(String[] args) {

        /*
         * Tipos de estructuras en Java
         * 
         * Arrays - Los arrays o arreglos, son colecciones de elementos del mismmo tipo,
         * accesibles a traves
         * son estaticos en tamaño, lo que significa que su tama no puede cambiar
         * después de la creación.
         */
        // Ejemplo
        int[] arreglo = { 1, 2, 3, 4, 5 };
        for (int num : arreglo) {
            System.out.println(num);
        }
        /*
         * ArrayList - Coleccion que contiene un tamaño dinamico, el nombre de una serie
         * de nombres, mostrando
         * la operacion de añadir y obtener la salida de elementos.
         */
        // Ejemplo
        ArrayList<String> nombres = new ArrayList<>();
        nombres.add("David");
        nombres.add("Carlos");
        nombres.add("Daniela");
        nombres.add("Sofia");
        System.out.println(nombres);
        // borrar
        nombres.remove(3);
        // Actualizar
        nombres.set(2, "Daniela");
        // Ordenamiento
        Collections.sort(nombres);
        System.out.println(nombres);

        /*
         * Mapas - Estas estructuras de datos almacenan datos en forma de
         * pares(clave-valor), lo que facilita la
         * busqueda y recuperación eficiente de vaores mediante clave única.
         */
        // Ejemplo
        HashMap<String, Integer> edades = new HashMap<>();
        edades.put("David", 29);
        edades.put("Sofia", 22);
        edades.put("Daniel", 34);
        edades.put("Elvin", 28);
        System.out.println(edades);// muestra todos los datos
        System.out.println(edades.get("David"));// obtener un elemento del diccionario mediante la key.
        for (Map.Entry<String, Integer> entry : edades.entrySet()) {// Recorre todos las key y values
            System.out.println("Nombre: ".concat(entry.getKey()) + " Edad: " + entry.getValue());
        }
        // Para borrar un elemento
        edades.remove("Elvin");
        // Para ver si el hash contiene un elemento
        edades.containsKey("Elvin");
        // Para actualizar valor
        edades.put("David", 30);

        /*
         * Colas - Las colas siguen el princiiop "FIFO"(primero en entrar, primeor en
         * salir). Pueden ser implementadas
         * como PriorityQuere o LinkedList. Son útiles en situaciones donde el orden de
         * llegada es relevante, el ejemplo
         * típico, es la cola de tareas de la bandeja de impresión.
         */
        // Ejemplo
        Queue<String> colas = new ArrayDeque<>();
        colas.add("David");
        colas.add("Daniel");
        colas.add("Daniela");
        System.out.println(colas);
        // Poll elimina y devuelve el primer elemento de la cola
        colas.poll();
        // Peel devuelve el primer elemento de la lista sin eliminarlo
        colas.peek();

        /*
         * Pilas - Ultimo en entrar, primero en salir (FIFO).
         */
        // Ejemplo
        Stack<String> books = new Stack<>();
        books.push("El retrato de Dorian Grey");
        books.push("El Principito");
        books.push("Habitos Atomicos");
        System.out.println(books);
        // Peek Ver el ultimo elemento
        System.out.println(books.peek());
        // Eliminar el ultimo elemento
        books.pop();
        // Buscar elemento
        books.search("El Principito");

        // Ejercicio Extra de Agenda Telefonica
        ejercicioExtra();

    }


    // Funcion principal que llama a las demas funciones del ejercicio Extra
    public static void ejercicioExtra() {
        HashMap<String, Long> agendaTelefonicaMap = new HashMap<>();

        Scanner res = new Scanner(System.in);
        Scanner datos = new Scanner(System.in);

        Long numero;
        String nombre;
        int respuesta = 0;

        System.out.println("\n\n\n");
        System.out.println("-----------Bienvenido a la Agenda Telefonica-----------");

        while (respuesta != 5) {
            System.out.println("\n");
            System.out.println("1. Ver contactos");
            System.out.println("2. Agregar contactos");
            System.out.println("3. Actualizar contacto");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Salir");
            respuesta = res.nextInt();

            if (respuesta == 1) {
                System.out.println("\n\n----------Lista de Contactos-----------\n\n");
                verContactos(agendaTelefonicaMap);

            } else if (respuesta == 2) {
                System.out.println("\n¿Con que nombre quieres agregar el nuevo contaco?");
                nombre = datos.next();
                System.out.println("¿Cual es el numero de este nuevo contacto?");
                numero = datos.nextLong();
                agregarContacto(nombre, numero, agendaTelefonicaMap);

            } else if (respuesta == 3) {
                System.out.println("\nElige el contacto que quieres actualizar por su nombre\n");
                verContactos(agendaTelefonicaMap);
                nombre = datos.next();
                System.out.println("\nIngresa un nuevo nombre: ");
                String nuevoNombre = datos.next();
                System.out.println("\nIngresa nuevo numero: ");
                Long nuevoNumero = datos.nextLong();
                actualizarContacto(nombre,nuevoNombre, nuevoNumero, agendaTelefonicaMap);

            } else if (respuesta == 4) {
                System.out.println("\nElige el contacto que quieres eliminar por su nombre\n");
                verContactos(agendaTelefonicaMap);
                nombre = datos.next();
                eliminarContacto(nombre, agendaTelefonicaMap);
            }
        }
    }

    //Funcion para actualizar contactos
    private static void actualizarContacto(String nombre, String nuevoNombre, Long nuevoNumero, HashMap<String, Long> agendaTelefonicaMap) {
        if (agendaTelefonicaMap.containsKey(nombre)){
            agendaTelefonicaMap.remove(nombre);
            agendaTelefonicaMap.put(nuevoNombre, nuevoNumero);
        }
    }

    //Funcion para eliminar contactos
    private static void eliminarContacto(String nombre, HashMap<String, Long> agendaTelefonicaMap) {
        agendaTelefonicaMap.remove(nombre);
        System.out.println("\n*****Contacto Eliminado****\n");
    }

    // Funcion para ver los contactos
    private static void verContactos(HashMap<String, Long> agendaTelefonicMap) {
        if (agendaTelefonicMap.isEmpty()) {
            System.out.println("Aun no hay ningun contacto guardado\n\n");
        } else {
            for (Map.Entry<String, Long> entry : agendaTelefonicMap.entrySet()) {
                System.out.println("Nombre: ".concat(entry.getKey()) + " Numero: " + entry.getValue());
            }
        }
    }

    // Funcion para guardar un contacto
    private static void agregarContacto(String nombre, Long numero, HashMap<String, Long> agendaTelefonicMap) {
        String numeroCoversion = String.valueOf(numero);
        if (numeroCoversion.length() > 8) {
            System.out.println(
                    "\n***El numero excede la capacidad de cifras aceptadas, ingrese un numero telefonico no mayor a 8 digitos*****");
            return;
        } else {
            agendaTelefonicMap.put(nombre, numero);
            System.out.println("\n**Contacto Guardado**");
        }

    }

}
