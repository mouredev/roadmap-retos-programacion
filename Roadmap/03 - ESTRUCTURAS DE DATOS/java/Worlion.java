import java.util.TreeMap;
import java.util.LinkedList;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Queue;

public class Worlion {

    public static void main(String[] args) {
        System.out.println("Estructuras de datos en Java");
        estructurasDeDatos();
    }

    /*
    * EJERCICIO: Estructuras de datos en Java
    */

    private static void estructurasDeDatos() {
        // Ejemplos de creación de estructuras de datos en Java
        // Arrays
        int [] numbers = new int[5];

        // ArrayList
        ArrayList<String> listaCadenas = new ArrayList<>();
        System.out.println("Lista: " +listaCadenas);

        //HashMap
        HashMap<Integer, String> mapaEnteroCadena = new HashMap<>();
        System.out.println("Mapa: " +mapaEnteroCadena);

        //HashSet 
        HashSet<String> conjuntoCadenas = new HashSet<>();
        System.out.println("Conjunto: " +conjuntoCadenas);

        // LinkedList
        LinkedList<Integer> listaEnteros = new LinkedList<>();
        System.out.println("Lista: " +listaEnteros);

        // TreeMap
        TreeMap<String, Integer> mapaCadenaEntero = new TreeMap<>();
        System.out.println("Mapa: " +mapaCadenaEntero);

        // Cola
        Queue<Integer> cola = new LinkedList<>();
        System.out.println("Cola: " +cola);

        // inserción 
        listaCadenas.add("Hola");
        listaCadenas.add("Mundo");
        listaCadenas.add("Java");
        listaCadenas.add("Estructuras de datos");

        System.out.println("Lista tras la inserción: " +listaCadenas);
        
        //borrado, 
        listaCadenas.remove("Java");
        System.out.println("Lista tras borrado: " +listaCadenas);
        
        //actualización 
        listaCadenas.set(2, "Java");
        System.out.println("Lista tras actualización: " +listaCadenas);
        
        //ordenación.
        listaCadenas.sort(null);
        System.out.println("Lista ordenada: " +listaCadenas);
    }



/*
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
}
