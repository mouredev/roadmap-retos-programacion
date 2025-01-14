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

import java.util.Collections; // Colecciones de Java
import java.util.Arrays;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashSet;
import java.util.TreeSet;
import java.util.HashMap;
import java.util.TreeMap;
import java.util.InputMismatchException; // Para excepciones
import java.util.Scanner;

public class Alextc35 {
    private static Scanner sc = new Scanner(System.in); // Inicializamos Scanner para recoger inputs

    public static void main(String[] args) {
        // ---- ARRAY UNIDIMENSIONAL ----
        System.out.println("----- ARRAY UNIDIMENSIONAL -----");

        // Creación de un arreglo unidimensional de enteros con 5 elementos
        int[] numbers = new int[5];

        // Inserción de valores en el arreglo
        int value = 1;
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = value++;
        }

        // Alternativa de inserción
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;

        // Actualización de un elemento
        numbers[2] = 35; // Cambia el valor del índice 2 a 35

        // Borrar un elemento (sobreescribir con 0)
        numbers[4] = 0;

        // Ordenar el arreglo
        Arrays.sort(numbers);

        // Imprimir el arreglo
        System.out.println("Array Unidimensional:");
        for (int indice : numbers) {
            System.out.println(indice);
        }

        // ---- ARRAY BIDIMENSIONAL ----
        System.out.println("\n----- ARRAY BIDIMENSIONAL -----");

        // Creación de un arreglo bidimensional de enteros con 3 filas y 4 columnas
        int[][] matriz = new int[3][4];

        // Inserción de valores en la matriz
        value = 1;
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = value++;
            }
        }

        // Actualización de un elemento
        matriz[1][2] = 70; // Cambia el valor en la fila 1, columna 2 a 70

        // Borrar un elemento (sobreescribir con 0)
        matriz[2][3] = 0;

        // Imprimir la matriz
        System.out.println("Array Bidimensional:");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }

        // ---- ARRAY MULTIDIMENSIONAL ----
        System.out.println("\n----- ARRAY MULTIDIMENSIONAL -----");

        // Creación de un arreglo tridimensional de enteros con dimensiones 2x3x4
        int[][][] cube = new int[2][3][4];

        // Inserción de valores en el arreglo tridimensional
        value = 1;
        for (int i = 0; i < cube.length; i++) {
            for (int j = 0; j < cube[i].length; j++) {
                for (int k = 0; k < cube[i][j].length; k++) {
                    cube[i][j][k] = value++;
                }
            }
        }

        // Actualización de un elemento
        cube[1][2][3] = 99; // Cambia el valor en la capa 1, fila 2, columna 3 a 99

        // Borrar un elemento (sobreescribir con 0)
        cube[0][0][0] = 0;

        // Imprimir el arreglo tridimensional
        System.out.println("Array Multidimensional:");
        for (int i = 0; i < cube.length; i++) {
            for (int j = 0; j < cube[i].length; j++) {
                for (int k = 0; k < cube[i][j].length; k++) {
                    System.out.print(cube[i][j][k] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }

        // ---- ARRAYLIST ----
        System.out.println("----- ARRAYLIST -----");
        /*
         * Admite duplicados y es ordered.
         * 
         * Los elementos tienen un índice asociado que indica
         * la posición dentro de la lista, comienza en 0.
         * 
         * Acceso en modo aleatorio rápido pero lento secuencialmente.
         * 
         * No es sincronizada.
         */

        // Creación de un ArrayList de cadenas
        ArrayList<String> list = new ArrayList<>();

        // Inserción de elementos
        list.add("Banana");
        list.add("Apple");
        list.add("Cherry");

        // Actualización de un elemento
        list.set(1, "Blueberry"); // Cambia "Apple" por "Blueberry"

        // Ordenar la lista
        Collections.sort(list);

        // Borrar un elemento
        list.remove("Cherry");

        // Imprimir la lista
        System.out.println("ArrayList:");
        System.out.println(list);

        /*
         * ----- Métodos -----
         * ----- list.add(elemento)
         * Añade un elemento primitivo(autoboxing) o referenciado.
         * Lo coloca al final.
         * Devuelve un boolean si se modificó la colección.
         * 
         * ----- list.add(posicion, elemento)
         * Añade el elemento en una posición dada.
         * Las anteriores han de estar ocupadas.
         * Desplaza hacia arriba al resto.
         * Devuelve void.
         * 
         * ----- list.addAll(Collection)
         * Añadir todo el contenido de un Collection a la colección actual.
         * 
         * ----- list.set(posicion, elemento)
         * Introduce un elemento en la posición indicada.
         * Si ya estaba ocupada, despalza hacia arriba a los otros.
         * 
         * ----- list.add(null)
         * Podemos añadir null.
         * 
         * ----- list.get(posicion)
         * Obtener el elemento de la posición indicada.
         * Recuperamos Object, luego hacer Casting (salvo que usemos genéricos).
         * 
         * ----- list.contains(elemento)
         * Comprueba si el elemento existe.
         * Devuelve un true / false (podemos tener más de 1, luego utilizar bucle
         * WHILE).
         * 
         * ----- list.indexOf(elemento)
         * Primera posición que cupa un determinado elemento (puede haber varios),
         * -1 si no lo encuentra.
         * 
         * ----- list.lastIndexOf(elemento)
         * Última posición que ocupa un determinado elemento (puede haber varios),
         * -1 si no lo encuentra.
         * 
         * ----- list.isEmpty()
         * Booleano que nos dice si hay elementos (también se toman en cuenta los null).
         * 
         * ----- list.size()
         * Tamaño del ArrayList.
         * También cuenta los null.
         * 
         * ----- list.iterator()
         * Obtener iterador para recorrer elementos (hasNext() - next()).
         * 
         * ----- list.toArray()
         * Obtener un Array de Object con los elementos contenidos en la colección.
         * 
         * ----- list.remove(posicion)
         * Devuelve el elemento contenido en una determinada posición
         * y a continuaciñon lo elimina de la colección.
         * 
         * ----- list.remove(Objeto)
         * Elimina el objeto de la posición (podemos tener más de 1).
         * Devuelve true si la lista ha sido modificada.
         * 
         * ----- list.clear()
         * Borra todo, incluidos los null.
         */

        // ---- LINKEDLIST ----
        System.out.println("\n----- LINKEDLIST -----");
        /*
         * Lista simplemente enlazada.
         * Cada elemento dispone de la dirección del elemento que le sigue en la lista.
         * 
         * Acceso secuencial rápido tanto para lectura como para escritura,
         * pero lento en acceso aleatorio.
         * 
         * Permite duplicados y no está sincronziada.
         * Es ordered.
         */

        // Creación de un LinkedList de cadenas
        LinkedList<String> linkedList = new LinkedList<>();

        // Inserción de elementos
        linkedList.add("Banana");
        linkedList.add("Apple");
        linkedList.add("Cherry");

        // Actualización de un elemento
        linkedList.set(1, "Blueberry"); // Cambia "Apple" por "Blueberry"

        // Ordenar la lista
        linkedList.sort(null); // Ordena usando el orden natural de los elementos

        // Borrar un elemento
        linkedList.remove("Cherry");

        // Imprimir la lista
        System.out.println("LinkedList:");
        System.out.println(linkedList);

        /*
         * Métodos similares al de ArrayList, incorpora métodos propios.
         * ----- Métodos -----
         * ----- linkedList.addFirst(elemento)
         * Añade el elemento al principio de la colección.
         * 
         * ----- linkedList.offerFirst(elemento)
         * Lo mismo (java 6).
         * 
         * ----- linkedList.addLast(elemento)
         * Añade el elemento al final de la colección
         * 
         * ----- linkedList.offerLast(elemento)
         * Lo mismo (java 6).
         * 
         * ----- linkedList.peekFirst()
         * Obtiene el primer elemento sin borrarlo de la colección
         * 
         * ----- linkedList.peekLast()
         * Obtiene el último elemento sin borrarlo de la colección
         * 
         * ----- linkedList.pollFirst()
         * Extrae el primer elemento de la colección.
         * (extraer == obtener y luego quitarlo de la colección).
         * Desplaza al resto de elementos.
         * 
         * ----- linkedList.pollLast()
         * Extrae el último elemento de la colección.
         * (Desplaza al resto de elementos).
         * 
         * ----- linkedList.push(elemento)
         * Introduce el elemento al principio de la colección.
         * Desplaza al resto.
         * Pila tipo LIFO.
         * 
         * ----- linkedList.pop()
         * Extrae el último elemento de la colección.
         * Pila tipo LIFO.
         */

        // ---- VECTOR ----
        // System.out.println("\n----- VECTOR -----");
        /*
         * De las tres implementaciones de la interfaz List,
         * es la única que está sincronizada.
         * También permite duplicados y es ordered.
         * 
         * Si no es necesario controla la concurrencia en multiacceso,
         * sería mejor utilizar un ArrayList.
         * Dicho control sacrifica buena parte del rendimiento de la clase.
         */

        /*
         * ----- Métodos -----
         * ----- v.capacity()
         * Obtiene la capacidad inicial con la que se ha creado la instancia de la clase
         * Vector.
         * 
         * ----- v.size()
         * Obtiene el número total de elementos contenido en el vector
         * (posiciones realmente oocupadas, no la capacidad inicial)
         * 
         * ----- v.elementAt(posicion)
         * Obtiene el elemento contenido en la posición indicada.
         * Se recupera como Object, salvo que se haya usado genéricos.
         * 
         * ----- v.get(posicion)
         * Igual que el anterior.
         * 
         * ----- v.firstElement()
         * Obtiene el primer elemento de la colección
         * 
         * ----- v.lastElement()
         * Obtiene el último elemento de la colección
         * 
         * ----- v.add(posicion, elemento)
         * Añade el elemento en la posición indicada.
         * Operación NO SINCRONIZADA.
         * 
         * ----- v.insertElementAt(elemento, posicion)
         * Igual que el anterior, pero esta vez la operación
         * ES SINCRONIZADA.
         * 
         * ----- v.elements()
         * Devuelve un Enumeration que contiene los elementos de la colección.
         * 
         * ----- v.iterator()
         * Devuelve un Iterator con el que poder recorrer los elementos de la colección
         * (secuencial, hacia abajo, necesita recarga).
         * 
         * ----- v.removeElementAt(posicion)
         * Elimina el elemento de la posición indicada.
         * Devuelve void.
         * Operación sincronizada.
         * 
         * ----- v.indexOf(elemento)
         * Devuelve la posición que ocupa un determinado elemento
         * (podemos tener más de 1).
         * 
         * ----- v.removeAllElements()
         * Elimina todos los elementos de la colección
         */

        // ---- HASHSET ----
        System.out.println("\n----- HASHSET -----");
        // No es ordered.

        // Creación de un HashSet de cadenas
        HashSet<String> set = new HashSet<>();

        // Inserción de elementos
        set.add("Banana");
        set.add("Apple");
        set.add("Cherry");

        // Intentar insertar un elemento duplicado
        set.add("Apple"); // No se agregará porque "Apple" ya está en el set

        // Borrar un elemento
        set.remove("Cherry");

        // Imprimir el conjunto
        System.out.println("HashSet:");
        System.out.println(set);

        // Los métodos más importantes son los ya vistos en la interface List.

        // ---- TREESET ----
        System.out.println("\n----- TREESET -----");
        /*
         * Los SortedSet (y en los Map, los denominados SortedMap)
         * organizan sus elementos como una ordenación natural.
         * Dicha ordenación es automática.
         * 
         * No permite mezclar tipos de datos incompatibles.
         * Es sorted.
         */

        // Creación de un TreeSet de cadenas (se mantiene ordenado)
        TreeSet<String> treeSet = new TreeSet<>();

        // Inserción de elementos
        treeSet.add("Banana");
        treeSet.add("Apple");
        treeSet.add("Cherry");

        // Borrar un elemento
        treeSet.remove("Cherry");

        // Imprimir el conjunto
        System.out.println("TreeSet:");
        System.out.println(treeSet);

        /*
         * ----- Métodos -----
         * ----- treeSet.descendingIterator()
         * Obtiene un iterator de recorrido descendente (el normal tiene recorrido
         * ascendete).
         * 
         * ----- treeSet.ceiling(elemento)
         * Devuelve el mismo o el siguiente mayor que se encuentre en la colección
         * respecto al elemento indicado.
         * 
         * ----- treeSet.first()
         * Obtiene el primer elemento.
         * 
         * ----- treeSet.floor(elemento)
         * Obtiene el elemento de la colección que sea igual o el más próximo por
         * defecto, con respecto al indicado.
         * 
         * ----- treeSet.higher(elemento)
         * Obtiene el elemento de la colección que sea igual o el más próximo por
         * exceso, con respecto al indicado.
         * 
         * ----- treeSet.headSet(elemento)
         * Obtiene un subconjunto inferior en ordenación al elemento indicado.
         * 
         * ----- treeSet.tailSet(elemento)
         * Obtiene un subconjunto superior en ordenación al elemento indicado.
         */

        // ---- HASHTABLE ----
        // System.out.println("\n----- HASHTABLE -----");
        /*
         * Esta colección es de tipo sincronizada, al igual que ocurría con Vector en
         * las listas.
         * 
         * No se admite null, ni para el campo key ni para el campo value (HashMap si lo
         * permite).
         */

        /*
         * ----- Métodos -----
         * ----- ht.put(clave, valor)
         * Introduce el elemento de la colección.
         * Si la clave ya existe, se devuelve el valor antiguo
         * y luego se reemplaza con el nuevo.
         * 
         * ----- ht.containsKey(clave)
         * Devuelve un booleano que indica si la clave existe.
         * 
         * ----- ht.containsValue(valor)
         * Devuelve un booleano que indica si el valor existe.
         * 
         * ----- ht.get(clave)
         * Devuelve el valor asociado a la clave indicada.
         * 
         * ----- ht.keys()
         * Devuelve un Enumeration con las claves de la colección.
         * 
         * ----- ht.values()
         * Devuelve un Collection con los valores de la colección.
         * (Obtener de aquí el Iterator ***).
         * 
         * ----- ht.elements()
         * Devuelve un Enumeration con los valores de la colección.
         * 
         * ----- ht.values().iterator()
         * *** devuelve un Iterador para recorrer la colección.
         * Se ha de obtener primero el Collection correspondiente y de él, el Iterator.
         * 
         * ----- ht.remove(clave)
         * Devuelve el valor y a continuación elimina el registro que coincida con la
         * clave indicada.
         * Si la clave no existe no ocurre nada.
         */

        // ---- HASHMAP ----
        System.out.println("\n----- HASHMAP -----");
        /*
         * A diferencia de Hashtable, sí se permite null en el campo clave
         * y en el campo valor.
         */

        // Creación de un HashMap de cadenas a enteros
        HashMap<String, Integer> map = new HashMap<>();

        // Inserción de pares clave-valor
        map.put("Banana", 1);
        map.put("Apple", 2);
        map.put("Cherry", 3);

        // Actualización de un valor
        map.put("Apple", 4); // Cambia el valor de "Apple" a 4

        // Borrar un elemento
        map.remove("Cherry");

        // Imprimir el mapa
        System.out.println("HashMap:");
        System.out.println(map);

        /*
         * Mismos métodos que Hashtable.
         * 
         * NO TIENE elements()
         * que devolvía un Enumeration
         * con los valores de la colección !!!!!
         */

        // ---- LINKEDHASHMAP ----
        // System.out.println("\n----- LINKEDHASHMAP -----");
        // Un mapa que se basa en una lista enlazada

        // Los métodos son los ya vistos hasta ahora.

        // ---- TREEMAP ----
        System.out.println("\n----- TREEMAP -----");
        // Mapa ordenado. Elementos de menor a mayor.

        // Creación de un TreeMap de cadenas a enteros (mantiene el orden de las claves)
        TreeMap<String, Integer> treeMap = new TreeMap<>();

        // Inserción de pares clave-valor
        treeMap.put("Banana", 1);
        treeMap.put("Apple", 2);
        treeMap.put("Cherry", 3);

        // Actualización de un valor
        treeMap.put("Apple", 4);

        // Borrar un elemento
        treeMap.remove("Cherry");

        // Imprimir el mapa
        System.out.println("TreeMap:");
        System.out.println(treeMap);

        /*
         * ----- Métodos -----
         * ----- treeMap.descendingMap()
         * Obtiene un NavigableMap para recorrer la colección
         * en orden inverso al natural. (mayor a menor).
         * 
         * ----- treeMap.firstKey()
         * Obtiene la primera clave de la colección
         * 
         * ----- treeMap.lastKey()
         * Obtiene la última clave de la colección
         * 
         * ----- treeMap.floorKey(clave)
         * Obtiene la clave indicada o la más próxima a ésta por defecto.
         * 
         * ----- treeMap.lowerKey(clave)
         * Igual que la anterior.
         * 
         * ----- treeMap.higherKey(clave)
         * Obtiene la clave indicada o la más próxima a ésta por exceso.
         */

        // ----- OPCIONAL -----
        HashMap<String, Integer> miAgenda = new HashMap<>();
        menu(miAgenda);
        sc.close();
    }
    // AGENDA
    // menú
    public static void menu(HashMap<String, Integer> map) {
        int opcion;
        System.out.println("\n----- AGENDA DE CONTACTOS -----");
        System.out.println("\t1. BÚSQUEDA");
        System.out.println("\t2. INSERCIÓN");
        System.out.println("\t3. ACTUALIZACIÓN");
        System.out.println("\t4. ELIMINACIÓN");
        System.out.println("\t5. SALIR");
        System.out.print("Elige su opción [1-5]: ");

        opcion = getValidIntInput(1, 5);

        agenda(map, opcion);
    }

    public static void agenda(HashMap<String, Integer> map, int opcion) {
        switch (opcion) {
            case 1:
                busquedaAgenda(map);
                break;
            case 2:
                insercionAgenda(map);
                break;
            case 3:
                actualizacionAgenda(map);
                break;
            case 4:
                eliminacionAgenda(map);
                break;
            case 5:
                System.out.println("\n----- Fin del programa -----\n");
                break;
        }
    }

    // 1
    public static void busquedaAgenda(HashMap<String, Integer> map) {
        int opcion = 0;
        String nombre;

        while (opcion != 3) {
            System.out.println("\n----- MIS CONTACTOS -----");
            System.out.println("\t1. VER (TODOS)");
            System.out.println("\t2. BUSCAR POR NOMBRE");
            System.out.println("\t3. SALIR");
            System.out.print("Elige su opción [1-3]: ");

            opcion = getValidIntInput(1, 3);

            switch (opcion) {
                case 1:
                    System.out.println(map);
                    break;
                case 2:
                    System.out.print("\nEscribe el nombre del contacto\n> ");
                    nombre = sc.next();
                    if (map.containsKey(nombre)) {
                        System.out.println("Número de contacto: " + map.get(nombre)); // da el teléfono
                    } else {
                        System.out.println("Contacto no encontrado.");
                    }
                    break;
                case 3:
                    menu(map);
            }
        }
    }

    // 2
    public static void insercionAgenda(HashMap<String, Integer> map) {
        String nombre;
        int telefono;

        System.out.print("\nInserta el nombre del contacto\n> ");
        nombre = sc.next();

        System.out.print("Inserta el número de teléfono del contacto");
        telefono = getValidNumber();

        map.put(nombre, telefono); // Clave-Valor

        menu(map);
    }

    // 3
    public static void actualizacionAgenda(HashMap<String, Integer> map) {
        String nombre;
        int telefono;

        System.out.print("\nIntroduzca el nombre del contacto a editar\n> ");
        nombre = sc.next();

        if (map.containsKey(nombre)) {
            System.out.print("Introduzca el nuevo número del contacto");
            telefono = getValidNumber();
            map.put(nombre, telefono); // Se actualiza el número del contacto
        } else {
            System.out.println("Contacto no encontrado.");
        }
        menu(map);
    }

    // 4
    public static void eliminacionAgenda(HashMap<String, Integer> map) {
        String nombre;

        System.out.print("\nEscribe el nombre del contacto a borrar\n> ");
        nombre = sc.next();
        if (map.containsKey(nombre)) {
            System.out.println(nombre + " ha sido borrado...");
            map.remove(nombre);
        } else {
            System.out.println("Contacto no encontrado.");
        }
        menu(map);
    }

    private static int getValidNumber() {
        while (true) {
            try {
                System.out.print("\n> ");
                int input = sc.nextInt();
                if (Integer.toString(input).length() >= 9) {
                    return input;
                } else {
                    System.out.println("El mínimo son 9 dígitos.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Número inválido. Por favor, introduce un número válido.");
                sc.next();
            }
        }
    }

    // Validador de Inputs (int) con Scanner
    private static int getValidIntInput(int min, int max) {
        while (true) {
            try {
                System.out.print("\n> ");
                int input = sc.nextInt();
                if (input >= min && input <= max) {
                    return input;
                } else {
                    System.out.println(
                            "\nOption out of bounds. Please enter a number between " + min + " and " + max + ".\n");
                }
            } catch (InputMismatchException e) {
                System.out.println("\nInvalid input. Please enter a valid integer.\n");
                sc.next(); // Clear invalid input
            }
        }
    }
}
