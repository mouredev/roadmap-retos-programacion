
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;
import java.util.Stack;
import java.util.TreeMap;
import java.util.TreeSet;


/**
 * kleyner098
 */
public class kleyner098 {
    /*
     * EJERCICIO:
     * - Muestra ejemplos de creación de todas las estructuras soportadas por
     * defecto en tu lenguaje.
     * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
     */

    // Método main ------
    public static void main(String[] args) {
        // Las estructuras de datos en java se pueden clasificar en estáticas y
        // dinámicas.
        // Estáticas: Arrays, Arrays bidimensionales, Arrays multidimensionales
        // Dinámicas, se pueden dividir en:
        // -List: ArraysList, LinkedList
        // -Queue
        // -Stacks
        // -Set: HashSet, TreeSet, LinkedListSet
        // -Map: HashMap, TreeMap
        // Generalmente la forma de construir un estructura de dato es :
        // tipoDato nombreEstructura = new tipoEstructura

        // Arrays: Estructura de datos de elementos del mismo tipo y tamaño estático

        // Creación de array
        System.out.println("Array ----------------------");
        int[] arrayNumbers = new int[3];
        // Inserción
        for (int i = 0; i < arrayNumbers.length; i++) {
            arrayNumbers[i] = arrayNumbers.length - i - 1;
        }
        System.out.println(Arrays.toString(arrayNumbers));
        // Ordenar
        Arrays.sort(arrayNumbers);
        System.out.println(Arrays.toString(arrayNumbers));
        // Para borrar debemos aplicar métodos que nos permita indentificar el elemnto
        // que deseamos borrar y métodos que nos permitar copiar la tabla sin el
        // elemento
        // Buscamos el indice del elemento que queremos borrar, binarySearch solo
        // funciona con arrays ordenadas
        int indexElement = Arrays.binarySearch(arrayNumbers, 2);
        // Desplazamos todos los elementos despues del elemento que quermos borrar una
        // posición menos
        System.arraycopy(arrayNumbers, indexElement + 1, arrayNumbers, indexElement,
                arrayNumbers.length - indexElement - 1);
        // Copiamos la tabla sin el elemento que hemos borrado y le asignamos una
        // longitud menos
        arrayNumbers = Arrays.copyOf(arrayNumbers, arrayNumbers.length - 1);
        System.out.println(Arrays.toString(arrayNumbers));
        // Actualización
        arrayNumbers[1] = 4;
        System.out.println(Arrays.toString(arrayNumbers));

        // List: Estructura de datos dinámica con datos repetidos y orden relevante en
        // ocasiones.
        // Las dos clase ArrayList y LinkedList ofrecen los mismos métodos y
        // funcionalidades
        // La diferencia entre ArrayList y LinkedList es que la primera ofrece un mayor
        // rendimiento en lectura y modificación de elementos y la sengunda ofrece mayor
        // rendimiento en en inserción y eliminación. Utilizare ArrayList pero le puede
        // sustituir por la clase LinkedList
        System.out.println("List ----------------------");
        ArrayList<Integer> arrayList = new ArrayList<>();
        // Inserción
        arrayList.add(1);
        arrayList.add(7);
        arrayList.add(3);
        System.out.println(arrayList);
        // Borrado
        arrayList.remove(0);
        System.out.println(arrayList);
        // Actualización
        arrayList.set(0, 10);
        System.out.println(arrayList);
        // Ordenación
        Collections.sort(arrayList);
        System.out.println(arrayList);

        // Las colas son estructuras de datos que siguen el principio FIFO (First In,
        // First Out). Se puede utilizar la clase PriorityQueue una cola que ordena los
        // elementos o una Linkedlist que no ordena la cola
        System.out.println("Queue ----------------------");
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        Queue<Integer> queue = new LinkedList<>();
        // Inserción
        priorityQueue.offer(3);
        priorityQueue.offer(1);
        priorityQueue.offer(2);
        queue.offer(3);
        queue.offer(1);
        queue.offer(2);
        System.out.println("PriorityQueue:" + priorityQueue);
        System.out.println("Queue:" + queue);
        // Borrado
        priorityQueue.poll();
        queue.poll();
        System.out.println("PriorityQueue:" + priorityQueue);
        System.out.println("Queue:" + queue);
        // Actualización
        // Debido a que las colas siguen el principio de FIFO, no tiene sentido
        // actualizar un valor
        // Ordenación
        // En el caso de PriorityQueue ordena los elementos según el orden de prioridad.
        // En general, tampoco tiene sentido ordenar las cola ya que los elemntos se
        // procesan según se insertaron

        // La pilas son estructuras de datos que siguen el principio LIFO (Last In,
        // First Out).
        System.out.println("Stack ----------------------");
        Stack<Integer> stack = new Stack<>();
        // Inserción
        stack.push(3);
        stack.push(1);
        stack.push(2);
        System.out.println(stack);
        // Borrado
        stack.pop();
        System.out.println(stack);
        // Actualización
        // Debido a que las pila siguen el principio de LIFO, no tiene sentido
        // actualizar un valor
        // Ordenación
        // En general, tampoco tiene sentido ordenar las cola ya que los elemntos se
        // procesan sengún el ultimo valor introducido

        // Los conjuntos son estructuras de datos que no admiten elementos repetidos y
        // su orden no es relevante
        // Existen tres clase HashSet, TreeSet, LinkedHashSet. La diferencia principal
        // diferencia entre ellos es que HashSet no garantiza el orden de la inserción,
        // TreeSet mantiene los elemento ordenados segun el orden natural y
        // LinkedHashSet mantiene el orden de insersión;
        System.out.println("Set ----------------------");
        Set<String> hashSet = new HashSet<>();
        Set<String> linkedHashSet = new LinkedHashSet<>();
        Set<String> treeSet = new TreeSet<>();
        // Inserción
        hashSet.add("c");
        hashSet.add("a");
        hashSet.add("b");
        hashSet.add("c");
        System.out.println("HashSet: " + hashSet);
        treeSet.add("c");
        treeSet.add("a");
        treeSet.add("b");
        treeSet.add("c");
        System.out.println("TreeSet: " + treeSet);
        linkedHashSet.add("c");
        linkedHashSet.add("a");
        linkedHashSet.add("b");
        linkedHashSet.add("c");
        System.out.println("LinkedHashSet: " + linkedHashSet);
        // Borrado
        hashSet.remove("b");
        System.out.println("HashSet: " + hashSet);
        treeSet.remove("b");
        System.out.println("TreeSet: " + treeSet);
        linkedHashSet.remove("b");
        System.out.println("LinkedHashSet: " + linkedHashSet);
        // Actualizar
        // No se puede actualizar como tal, si queremos actualizar un valor debemos
        // borrar y agragar otro
        // Ordenación
        // No tiene mucho sentido ordenar ningúna de la tres, sobre todo TreeSet y
        // LinkedHasSet porque una ya esta ordenada y la una de las funciones de la otra
        // es mantener el orden de inserción. En el caso de HashSet, podemos hacer una
        // conversión a una lista y ordenarla

        // Los mapas son estructuras de datos donde sus elementos se relacionan en pares
        // de clave/valor. Las claves son únicas, pero pueden tener el mismo valor
        // Existen tres clase HashMap, TreeMap, LinkedHashMap. La diferencia entre ellos
        // es similar a
        // las diferencia entre las clase de Set. En el caso de TreeMap el orden será el
        // ordena narutal creciente de las claves
        System.out.println("Map ----------------------");
        Map<String, Integer> hashMap = new HashMap<>();
        Map<String, Integer> treeMap = new TreeMap<>();
        Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
        // Inserción
        hashMap.put("b", 3);
        hashMap.put("a", 2);
        hashMap.put("c", 3);
        System.out.println("HashMap: " + hashMap);
        treeMap.put("b", 3);
        treeMap.put("a", 2);
        treeMap.put("c", 1);
        System.out.println("HashMap: " + treeMap);
        linkedHashMap.put("b", 2);
        linkedHashMap.put("c", 1);
        linkedHashMap.put("a", 3);
        System.out.println("LinkedHashMap: " + linkedHashMap);
        // Borrado
        hashMap.remove("b");
        System.out.println("HashMap: " + hashMap);
        treeMap.remove("b");
        System.out.println("HashMap: " + treeMap);
        linkedHashMap.remove("b");
        System.out.println("LinkedHashMap: " + linkedHashMap);
        // Actualización
        hashMap.put("c", 1);
        System.out.println("HashMap: " + hashMap);
        treeMap.put("c", 7);
        System.out.println("HashMap: " + treeMap);
        linkedHashMap.put("c", 5);
        System.out.println("HashMap: " + linkedHashMap);
        // Ordenación
        // No tiene sentido ordenarlos y dependiendo del programa usaremos uno u otro

        // Ejercicio extra
        System.out.println();
        agenda();
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea una agenda de contactos por terminal.
     * - Debes implementar funcionalidades de búsqueda, inserción, actualización y
     * eliminación de contactos.
     * - Cada contacto debe tener un nombre y un número de teléfono.
     * - El programa solicita en primer lugar cuál es la operación que se quiere
     * realizar, y a continuación
     * los datos necesarios para llevarla a cabo.
     * - El programa no puede dejar introducir números de teléfono no númericos y
     * con más de 11 dígitos.
     * (o el número de dígitos que quieras)
     * - También se debe proponer una operación de finalización del programa.
     */
    static void agenda() {
        Map<String, Integer> agenda = new HashMap<>();
        Scanner sc = new Scanner(System.in);
        String eleccion;
        int numEleccion = 0;
        // String multilinea
        String option = """
                Introduce el número de la opción que quieres realizar.
                1. Añadir un nuevo contacto
                2. Actualizar un contacto
                3. Buscar contacto
                4. Eliminar contacto
                5. Mostra agenda
                6. Cerrar agenda
                """;
        // Bucle que no terminará hasta que la opción se 5
        while (true) {
            // Mostramos las opciones
            System.out.println(option);
            eleccion = sc.next();
            sc.nextLine();
            // Comprobamos si se a introducido un digito
            if (!(Character.isDigit(eleccion.charAt(0)))) {
                System.out.println("Introduce un número");
            } else {
                // Convertimos el carácter en un int restando el valor del caracter 0, 48 en
                // ASCII
                numEleccion = eleccion.charAt(0) - '0';
                // Comprobamos el digito con las opciones disponibles
                switch (numEleccion) {
                    case 1 -> {
                        addContacto(agenda);
                    }
                    case 2 -> {
                        actualizar(agenda);
                    }
                    case 3 -> {
                        buscar(agenda);
                    }
                    case 4 -> {
                        eliminar(agenda);
                    }
                    case 5 ->{
                        System.out.println(agenda + "\n");
                    }
                    case 6 -> {
                        System.out.println("Agenda cerrada");
                        System.exit(0);
                    }
                    default -> {
                        System.out.println("Introduce un número válido");
                    }
                }
            }
        }

    }

    public static void addContacto(Map<String, Integer> agenda) {
        String nombre;
        String telf;
        int telfNum;
        Scanner sc = new Scanner(System.in);
        do {
            System.out.println("Introduce el nombre del contacto");
            nombre = sc.nextLine();
            if (agenda.containsKey(nombre)) {
                System.out.println("El contacto está en la agenda");
            }
        } while (agenda.containsKey(nombre));

        do {
            System.out.println("Introduce el télefono de contacto del contacto");
            do {
                if(!(sc.hasNextInt())){
                    System.out.println("Error. Introduce un número :");
                    sc.next();
                }
            } while (!(sc.hasNextInt()));
            telfNum = sc.nextInt();
            telf = String.valueOf(telfNum);
            if (telf.length() > 9) {
                System.out.println("El número de teléfono no puede tener mas de 9 digitos");
            }
        } while (telf.length() > 9);

        System.out.println("Contacto añadido\n");
        agenda.put(nombre, telfNum);
    }

    public static void actualizar(Map<String, Integer> agenda){
        String nombre;
        String telf;
        int telfNum;
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce el nombre del contacto");
        nombre = sc.nextLine();
        if(!(agenda.containsKey(nombre))){
            System.out.println("Contacto no encontrado\n");
        }else{
            do {
                System.out.println("Introduce el nuevo télefono de contacto del contacto");
                do {
                    if(!(sc.hasNextInt())){
                        System.out.println("Error. Introduce un número :");
                        sc.next();
                    }
                } while (!(sc.hasNextInt()));
                telfNum = sc.nextInt();
                telf = String.valueOf(telfNum);
                if (telf.length() > 9) {
                    System.out.println("El número de teléfono no puede tener mas de 9 digitos");
                }
            } while (telf.length() > 9);
            System.out.println("Contacto actualizado \n");
            agenda.put(nombre, telfNum);
        }
    }

    public static void buscar(Map<String, Integer> agenda){
        String nombre;
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce el nombre del contacto");
        nombre = sc.nextLine();
        if(!(agenda.containsKey(nombre))){
            System.out.println("Contacto no encontrado");
        }else{
            System.out.println(nombre + "|" + agenda.get(nombre)+"\n");;
        }
    }

    public static void eliminar(Map<String, Integer> agenda){
        String nombre;
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce el nombre del contacto");
        nombre = sc.nextLine();
        if(!(agenda.containsKey(nombre))){
            System.out.println("Contacto no encontrado");
        }else{
            agenda.remove(nombre);
            System.out.println("Contacto eliminado \n");
        }
    }
}