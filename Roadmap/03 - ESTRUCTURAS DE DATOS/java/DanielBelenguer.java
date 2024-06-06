import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet;

public class DanielBelenguer {
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
public static void main(String[] args) {
    // Creación de estructuras de datos en Java

    // Array
    int[] arrayNúmeros = {1,4,6,7,8};
    // Vamos a mostrar el contenido del array de números
    for (int i : arrayNúmeros) {
        System.out.println(i);
    }

    String[] arrayStrings = new String[3];
    arrayStrings[0] = "Hola";
    arrayStrings[1] = "Mundo";
    arrayStrings[2] = "Java!!";
    // Vamos a mostrar el contenido del array de String
    for (String string : arrayStrings) {
        System.out.println(string);
    }

    // Arrays bidimensionales
    int[][] matriz = new int[3][3];
    matriz[0][0] = 1;
    matriz[0][1] = 2;
    matriz[0][2] = 3;
    matriz[1][0] = 4;
    matriz[1][1] = 5;
    matriz[1][2] = 6;
    matriz[2][0] = 7;
    matriz[2][1] = 8;
    matriz[2][2] = 9;
    // Vamos a mostrar el contenido de la matriz
    for (int i = 0; i < matriz.length; i++) {
        for (int j = 0; j < matriz[i].length; j++) {
            System.out.print(matriz[i][j] + " ");
        }
        System.out.println();
    }

    // Listas

    // ArrayList es la lista que se basa en un array, por lo que es más rápido acceder a los elementos pero más lento añadir o eliminar
    ArrayList<Integer> listaNúmeros = new ArrayList<>();
    listaNúmeros.add(3);
    listaNúmeros.add(1);
    listaNúmeros.add(2);
    // Vamos a mostrar el contenido de la lista de números
    for (Integer integer : listaNúmeros) {
        System.out.println(integer);
    }

    // LinkedList es la lista formada por lincks, es decir, cada elemento tiene una referencia al siguiente y al anterior
    LinkedList<String> listaStrings = new LinkedList<>();
    listaStrings.add("Hola");
    listaStrings.add("Mundo");
    listaStrings.add("Java!!");
    // Vamos a mostrar el contenido de la lista de strings
    for (String string : listaStrings) {
        System.out.println(string);
    }


   // Conjuntos

   // HashSet es un conjunto que no permite elementos duplicados. No garantiza el orden de los elementos.
    HashSet<String> conjuntoStrings = new HashSet<>();
    conjuntoStrings.add("Hola");
    conjuntoStrings.add("Mundo");
    conjuntoStrings.add("Java!!");
    // Vamos a mostrar el contenido del conjunto de strings
    for (String string : conjuntoStrings) {
        System.out.println(string);
    }

    //TreeSet es un conjunto que mantiene los elementos ordenados según como tenga el metodo compareTo implementado.
    TreeSet<Integer> conjuntoNúmeros = new TreeSet<>();
    conjuntoNúmeros.add(1);
    conjuntoNúmeros.add(2);
    conjuntoNúmeros.add(3);
    // Vamos a mostrar el contenido del conjunto de números
    for (Integer integer : conjuntoNúmeros) {
        System.out.println(integer);
    }


    // Mapas

    // HashMap es un mapa que no garantiza el orden de los elementos
    HashMap<String, Integer> mapaStringsANúmeros = new HashMap<>();
    mapaStringsANúmeros.put("Uno", 1);
    mapaStringsANúmeros.put("Dos", 2);
    mapaStringsANúmeros.put("Tres", 3);
    // Vamos a mostrar el contenido del mapa de strings a números
    for (String key : mapaStringsANúmeros.keySet()) {
        System.out.println(key + " -> " + mapaStringsANúmeros.get(key));
    }

    // TreeMap es un mapa que mantiene los elementos ordenados según como tenga el metodo compareTo implementado.
    TreeMap<Integer, String> mapaNúmerosAStrings = new TreeMap<>();
    mapaNúmerosAStrings.put(1, "Uno");
    mapaNúmerosAStrings.put(2, "Dos");
    mapaNúmerosAStrings.put(3, "Tres");
    // Vamos a mostrar el contenido del mapa de números a strings
    for (Integer key : mapaNúmerosAStrings.keySet()) {
        System.out.println(key + " -> " + mapaNúmerosAStrings.get(key));
    }


    // LinkedHashMap es un mapa que mantiene el orden de inserción de los elementos
    LinkedHashMap<String, Integer> mapaStringsANúmerosOrdenado = new LinkedHashMap<>();
    mapaStringsANúmerosOrdenado.put("Uno", 1);
    mapaStringsANúmerosOrdenado.put("Dos", 2);
    mapaStringsANúmerosOrdenado.put("Tres", 3);
    // Vamos a mostrar el contenido del mapa de strings a números ordenado
    for (String key : mapaStringsANúmerosOrdenado.keySet()) {
        System.out.println(key + " -> " + mapaStringsANúmerosOrdenado.get(key));
    }


    // Operaciones de inserción, borrado, actualización y ordenación

    // Inserción en un ArrayList
    listaNúmeros.add(4);
    listaNúmeros.add(5);
    // Mostramos el contenido de la lista de números
    for (Integer integer : listaNúmeros) {
        System.out.println(integer);
    }

    // Borrado en una LinkedList
    listaStrings.remove("Mundo");
    // Mostramos el contenido de la lista de strings
    for (String string : listaStrings) {
        System.out.println(string);
    }

    // Actualización en un HashMap
    mapaStringsANúmeros.put("Uno", 10);
    // Mostramos el contenido del mapa de strings a números
    for (String key : mapaStringsANúmeros.keySet()) {
        System.out.println(key + " -> " + mapaStringsANúmeros.get(key));
    }


    // Ordenación en un ArrayList
    listaNúmeros.sort((a, b) -> a - b);
    // Mostramos el contenido de la lista de números
    for (Integer integer : listaNúmeros) {
        System.out.println(integer);
    }


    // Dificultad extra

    // Creacion de menu
    Scanner lector = new Scanner(System.in);
    int opt = 0; // Variable para elegir la opción del menú.
    HashMap<String, Integer> agenda = new HashMap<>(); // Mapa para guardar los contactos
    do{
        System.out.println("""
                Bienvenido a la agenda de contactos
                1. Buscar contacto
                2. Añadir contacto
                3. Actualizar contacto
                4. Eliminar contacto
                5. Salir
                Elija una opción: 
                """);
        opt = lector.nextInt();
        switch(opt){
            case 1:
                System.out.println("Buscar contacto");
                String nombreBuscar = lector.nextLine();
                if(agenda.containsKey(nombreBuscar)){
                    System.out.println("El contacto " + nombreBuscar + " tiene el número " + agenda.get(nombreBuscar));
                }
                break;
            case 2:
                System.out.println("Añadir contacto");
                String nombre = lector.nextLine();
                int telefono = lector.nextInt();
                agenda.put(nombre, telefono);
                System.out.println("Contacto añadido");
                break;
            case 3:
                System.out.println("Actualizar contacto");
                String nombreActualizar = lector.nextLine();
                if(agenda.containsKey(nombreActualizar)){
                    int telefonoActualizar = lector.nextInt();
                    agenda.put(nombreActualizar, telefonoActualizar);
                    System.out.println("Contacto actualizado");
                }
                break;
            case 4:
                System.out.println("Eliminar contacto");
                String nombreEliminar = lector.nextLine();
                if(agenda.containsKey(nombreEliminar)){
                    agenda.remove(nombreEliminar);
                    System.out.println("Contacto eliminado");
                }
                break;
            case 5:
                System.out.println("Saliendo del programa");
                break;
            default:
                System.out.println("Opción no válida");
                break;
        }
        
    }while(opt != 5);
    lector.close();
}
}
