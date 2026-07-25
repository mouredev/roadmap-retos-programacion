package retosProgramacion;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;
import java.util.TreeMap;
import java.util.TreeSet;

public class RetoCuatro {

    public static void main(String[] args) {
/*
        //Array (No hay borrado)
        int[] numeros = {1, 2, 3, 4, 5};
        numeros[0] = 0; //Inserción
        numeros[0] = 10; //Actualización
        Arrays.sort(numeros); //Ordenación
        System.out.println(numeros[0]); //Acceso

        //ArrayList
        ArrayList<String> lista = new ArrayList<>();
        lista.add("Kilian"); //Inserción
        lista.add("Hernández");
        lista.add("Chirino");
        lista.add(1, "Daniel"); //Inserción en una posición determinada
        lista.set(0, "Kili"); //Actualización
        lista.remove(1); //Borrado
        Collections.sort(lista); //Ordenación (alfabética)
        System.out.println(lista);

        //LinkedList
        LinkedList<String> lista2 = new LinkedList<>();
        lista2.add("Elena"); //Inserción
        lista2.addFirst("Ele");
        lista2.addLast("Espino");
        lista2.add(2, "González");
        lista2.set(0, "Elenita"); //Actualización
        lista2.remove(0); //Borrado
        Collections.sort(lista2); //Ordenación
        System.out.println(lista2);

        //HashSet (No hay actualización...sería borrar y añadir de nuevo)
        HashSet<String> lista3 = new HashSet<>();
        lista3.add("Kilian"); //Inserción
        lista3.add("Elena");
        lista3.add("Daniel");
        lista3.remove("Daniel"); //Borrado
        System.out.println(lista3);
        List<String> sortedList = new ArrayList(lista3); //Ordenación(hay que convertirla en una ArrayList)
        Collections.sort(sortedList);
        System.out.println(sortedList);

        //TreeSet (No hay actualización...sería borrar y añadir de nuevo. | Se ordena automáticamente.)
        TreeSet<String> lista4 = new TreeSet<>();
        lista4.add("Real Madrid"); //Inserción
        lista4.add("Barcelona");
        lista4.add("Las Palmas");
        lista4.remove("Barcelona"); //Borrado
        System.out.println(lista4);

        //TreeMap (Se ordena automáticamente)
        TreeMap<Integer, String> lista7 = new TreeMap<>();
        lista7.put(1, "Real Madrid"); //Inserción
        lista7.put(0, "Barcelona");
        lista7.replace(0, "Las Palmas"); //Actualización
        lista7.remove(0); //Borrado
        System.out.println(lista7);

        //HashMap
        HashMap<String, String> lista5 = new HashMap<>();
        lista5.put("Subcampeón ", " Real Madrid"); //Inserción
        lista5.put("Campeón ", " Las Palmas");
        lista5.put("Último ", " Barcelona");
        lista5.replace("Último ", " Tenerife"); //Actualización
        lista5.remove("Último "); //Borrado
        System.out.println(lista5);
        TreeMap<String, String> sortedMap = new TreeMap<>(lista5); //Ordenación (Convirtiéndolo a un TreeMap)
        System.out.println(sortedMap);

        //Stack
        Stack<String> pila = new Stack<>();
        pila.push("Pedri"); //Inserción
        pila.push("Yeremi");
        pila.remove("Pedri");
        pila.push("Ayoze"); //Actualización (Borrar y añadir)
        pila.sort(String::compareTo); //Ordenación
        pila.pop(); //Borrado del último elemento
        System.out.println(pila);

        //Queue
        Queue<String> cola = new LinkedList<>();
        cola.add("Valerón"); //Inserción
        cola.add("Silva");
        cola.remove("Silva");
        cola.add("Viera"); //Actualización (Borrar y añadir)
        LinkedList<String> sortedCola = new LinkedList<>(cola); //Ordenación
        sortedCola.sort(String::compareTo);
        cola.poll(); //Borrado del primer elemento
        System.out.println(cola);
        System.out.println(sortedCola);

        //PriorityQueue (no permite actualización, ni ordenación)
        PriorityQueue<String> lista6 = new PriorityQueue<>();
        lista6.add("España"); //Inserción
        lista6.add("Alemania");
        lista6.remove("Alemania"); //Borrado
        lista6.add("Inglaterra");
        lista6.add("Francia");
        System.out.println(lista6);
*/
        agenda();

    }

    //Dificultad Extra
    public static void agenda() {
        
        Scanner leer = new Scanner(System.in);
        
        HashMap<String, Long> memoria = new HashMap<>();
        
        boolean flujo = true;
        
        
        
        while (flujo) {
        System.out.println(
                "\n"
                + "--------AGENDA--------\n"
                + "1.Buscar Contacto\n"
                + "2.Insertar Contacto\n"
                + "3.Actualizar Contacto\n"
                + "4.Eliminar Contacto\n"
                + "5.Salir de la Agenda\n"
                + "Elige una de las opciones:\n");

        int opcion = leer.nextInt();       

        switch (opcion) {
            case 1:
                System.out.println("Introduce el nombre: \n");
                String name = leer.next();
                if (memoria.containsKey(name)) {
                    System.out.printf("Su numero es: \n" + memoria.get(name));
                } else {
                    System.out.println("El contacto no existe");
                }
                break;
            case 2:
                System.out.print("Ingrese el nombre: \n");
                name = leer.next();
                System.out.print("Ingrese el número: \n");
                Long numero = leer.nextLong();
                if(numero.toString(numero).length() == 9) {
                    memoria.put(name, numero);
                    System.out.println("Contacto insertado");
                }else {
                    System.out.println("Error: El número debe tener 9 dígitos");
                }
                break;
            case 3:
                System.out.println("Ingrese el nombre del contacto que quiere actualizar: \n");
                name = leer.next();
                System.out.println("Ingrese su nuevo número: \n");
                numero = leer.nextLong();
                if(numero.toString(numero).length() == 9 && memoria.containsKey(name)){
                    memoria.replace(name, numero);
                    System.out.println("Contacto actualizado");
                }else {
                    System.out.println("Error: El nombre debe existir en la agenda y el nuevo número debe tener 9 dígitos");
                }
                break;
            case 4:
                System.out.println("Ingrese el nombre: \n");
                name = leer.next();
                if(memoria.containsKey(name)) {
                    memoria.remove(name);
                    System.out.println("Contacto borrado");
                }else {
                    System.out.println("Error: El contacto no existe en la agenda");
                }
                break;
            case 5:
                System.out.println("Salió de la Agenda");
                flujo = false;
                break;
            default:
                System.out.println("Error: Elige una opción del 1 al 5");
        }
          
    }
        leer.close();

 }

}


/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
