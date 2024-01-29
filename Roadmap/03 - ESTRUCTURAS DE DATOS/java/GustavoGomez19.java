import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

class GustavoGomez192 {
    public static void main(String[] args) {
        // Punto 1: Ejemplos de las estructuras de datos en Java
        // Arrays: Conjuntos ordenados del mismo tipo de datos
        Integer[] numeros = new Integer[5];
        // Punto 2: operaciones de inserción, borrado, actualización y ordenación.
        // INSERCIÓN
        numeros[0] = 1;
        numeros[1] = 2;
        numeros[2] = 3;
        numeros[3] = 4;
        numeros[4] = 5;
        for (int i = 0; i < numeros.length; i++) {
            System.out.println(numeros[i]);
        }
        System.out.println();
        // BORRADO
        int indiceEliminar = 1;
        // Se marca la posición como null para "eliminar"
        numeros[indiceEliminar] = null;
        for (int i = 0; i < numeros.length; i++) {
            System.out.println(numeros[i]);
        }
        System.out.println();
        // ACTUALIZACIÓN
        numeros[4] = 10;
        for (int i = 0; i < numeros.length; i++) {
            System.out.println(numeros[i]);
        }
        // ORDENACIÓN
        int[] ordenarArrays = { 20, 10, 50, 60, 40 };
        // se imprime el arreglo desordenado
        for (int i = 0; i < ordenarArrays.length; i++) {
            System.out.println("Números" + ordenarArrays[i]);
        }
        System.out.println();
        // se imprime el arreglo ordenado
        Arrays.sort(ordenarArrays);
        for (int i = 0; i < ordenarArrays.length; i++) {
            System.out.println("Números" + ordenarArrays[i]);
        }
        System.out.println();

        // Punto 1: Ejemplos de las estructuras de datos en Java
        /*
         * Listas (lists): Las listas pueden crecer o decrecer dinámicamente
         * Se implementan por la clases en el paquete 'java.util' como 'arrayLists'
         * y 'linkedList'
         */
        List<String> nombres = new ArrayList<String>();
        // Punto 2: operaciones de inserción, borrado, actualización y ordenación.
        // INSERCIÓN
        nombres.add("Gustavo");
        nombres.add("Katerine");
        System.out.println(nombres);
        System.out.println("Tamaño de la lista antes de borrar un elemento: " + nombres.size());
        // BORRADO
        nombres.remove(0);
        System.out.println(nombres);
        System.out.println("Tamaño de la lista despues de borrar un elemento : " + nombres.size());
        // ACTUALIZACIÓN
        System.out.println("Lista antes de actualizar un elemento : " + nombres);
        nombres.set(0, "María José");
        System.out.println("Lista después de actualizar un elemento : " + nombres);
        // ORDENACIÓN
        List<Integer> ordenarLista = new ArrayList<Integer>();
        ordenarLista.add(50);
        ordenarLista.add(21);
        ordenarLista.add(105);
        ordenarLista.add(10);
        System.out.println("Lista desordenada: " + ordenarLista);
        Collections.sort(ordenarLista);
        System.out.println("Lista ordenada: " + ordenarLista);

        // Punto 1: Ejemplos de las estructuras de datos en Java
        /*
         * Queue (colas): Son interfaces que se extienden de la interfaz 'Collection'
         * Proporcionan métodos especificos para manipular los elementos.
         * 'linkedList' puede utilizarse como una Queue
         */
        Queue<String> apellidos = new LinkedList<>();
        // Punto 2: operaciones de inserción, borrado, actualización y ordenación.
        // INSERCIÓN
        apellidos.add("Gómez");
        apellidos.add("Gil");
        apellidos.add("Quiñones");
        apellidos.add("Marin");
        apellidos.offer("Ardila");
        System.out.println(apellidos);
        // BORRADO
        apellidos.remove("Marin");
        System.out.println(apellidos);
        System.out.println();
        /*
         * ACTUALIZACIÓN. Para actualizar un cola no se hace directamente en la cola
         * por motivo de que está diseñadas para trabajar con la lógia FIFO, una forma
         * de actualizar un valor es creando una lista enlazada 'LinkedList'
         */
        System.out.println("Cola antes de actualizar: " + apellidos);
        LinkedList<String> listaTemporal = new LinkedList<>(apellidos);
        // Actualizar el valor
        listaTemporal.set(1, "Villa");
        apellidos.clear();
        apellidos.addAll(listaTemporal);
        System.out.println("Cola después de actualizar: " + apellidos);
        /*
         * ORDENACIÓN. Para ordenar los datos de una cola no se hace directamente en la
         * cola
         * por motivo de que está diseñadas para trabajar con la lógia FIFO, una forma
         * de ordenar los valores es creando una lista enlazada 'LinkedList'
         */
        System.out.println();
        Queue<Integer> ordenarCola = new LinkedList<>();
        ordenarCola.add(50);
        ordenarCola.add(10);
        ordenarCola.add(30);
        ordenarCola.add(5);
        System.out.println("Cola antes de ordenar: " + ordenarCola);
        // Ordenar cola
        List<Integer> ordenar = new LinkedList<>(ordenarCola);
        ordenarCola.clear();
        Collections.sort(ordenar);
        ordenarCola.addAll(ordenar);
        System.out.println("Cola después de ordenar: " + ordenarCola);

        // Punto 1: Ejemplos de las estructuras de datos en Java
        /*
         * Conjuntos (set): Son interfaces que se extienden de 'Collection'
         * Representan conjuntos de elementos unicos, pueden ser 'HashSet' y 'TreeSet'
         */
        Set<String> animales = new HashSet<String>();
        System.out.println();
        // Punto 2: operaciones de inserción, borrado, actualización y ordenación.
        // INSERCIÓN
        animales.add("Perro");
        animales.add("Gato");
        animales.add("Tigre");
        animales.add("Lobo");
        System.out.println("Inserción: " + animales);
        // BORRADO
        animales.remove("Gato");
        System.out.println("Borrado" + animales);
        // ACTUALIZACIÓN --> para actualizar un dato se realizan los pasos de 'remove' y
        // 'add'
        System.out.println("Antes de actualizar: " + animales);
        animales.remove("Lobo");
        animales.add("Zorro");
        System.out.println("Despué de actualizar: " + animales);
        // ORDENACIÓN --> para ordenar un HasHSet se debe convertir a una lista
        Set<Integer> oredenarHashSet = new HashSet<>();
        oredenarHashSet.add(50);
        oredenarHashSet.add(10);
        oredenarHashSet.add(30);
        oredenarHashSet.add(5);
        System.out.println("Antes de ordenar: " + oredenarHashSet);
        // Se convierte el 'HashSet' en lista
        List<Integer> hashSetOrdenado = new ArrayList<>(oredenarHashSet);
        Collections.sort(hashSetOrdenado);
        System.out.println("Después de ordenar: " + hashSetOrdenado);
        System.out.println();

        // Punto 1: Ejemplos de las estructuras de datos en Java
        Set<String> mascotas = new TreeSet<String>();
        // Punto 2: operaciones de inserción, borrado, actualización y ordenación.
        // INSERCIÓN
        mascotas.add("Roko");
        mascotas.add("Gael");
        mascotas.add("Raymond");
        mascotas.add("Benji");
        System.out.println("Inserción: " + mascotas);
        // BORRADO
        mascotas.remove("Raymond");
        System.out.println("Borrado: " + mascotas);
        // ACTUALIZACIÓN
        System.out.println("Antes de actualizar: " + mascotas);
        mascotas.remove("Gael");
        mascotas.add("Larry");
        System.out.println("Después de actualizar: " + mascotas);
        // ORDENACIÓN
        Set<String> treeSetOrdenado = new TreeSet<>(Comparator.comparing(String::length));
        treeSetOrdenado.add("Gustavo");
        treeSetOrdenado.add("María");
        treeSetOrdenado.add("Katerine");
        treeSetOrdenado.add("José");
        System.out.println("Ordenado con base a la longitud de cada String: " + treeSetOrdenado);

        /*
         * Mapas (Maps): Interfaces que representan asociaciones clave - valor
         * Pueden ser 'HashMap' y 'TreeMap'
         */
        Map<String, Integer> razas = new HashMap<>();
        Map<String, Integer> carros = new TreeMap<>();

        /*
         * Pilas (Stacks): La clase 'Stack' es una subclase de 'vector' que implementa
         * una pila
         * Se pueden implementar con el uso de 'Deque'
         */
        Deque<String> pila = new ArrayDeque<>();

        /*
         * Colas de prioridad (Priority Queues): Son implementadas por la interfaz
         * 'PriorityQueue'
         * Representan colas donde elementos tiene una proridad asociada.
         */
        PriorityQueue<Integer> priority = new PriorityQueue<>();

        /*
         * Deques (Double-Ended Queues): Son onterfaces que extiendne de la interfaz
         * 'Queue'
         * Permiten la manipulación de elementos desde ambos extremos 'ArrayDeque' es
         * una
         * implementación muy común
         */
        Deque<String> deque = new ArrayDeque<>();

        // Dificultad extra
        System.out.println("----------------------------------------------");
        System.out.println("** AGENDA ELECTRÓNICA **");
        Scanner name = new Scanner(System.in);
        Scanner number = new Scanner(System.in);
        Scanner option = new Scanner(System.in);
        Scanner buscar = new Scanner(System.in);
        Scanner actualizar = new Scanner(System.in);
        Scanner actualizarNum = new Scanner(System.in);

        Map<String, Long> agenda = new HashMap<>();
        // List<Long> numContacto = new ArrayList<>();
        System.out.println("Seleccione una opción: " + "\n" +
                "-----+-----+-----+-----+" + "\n" +
                "1. Agregar contacto" + "\n" +
                "2. Buscar contacto" + "\n" +
                "3. Actualizar contacto" + "\n" +
                "4. Borrar contacto" + "\n" +
                "5. Salir" + "\n" +
                "-----+-----+-----+-----+");

        int opcion = option.nextInt();

        while (opcion != 5) {
            if (opcion == 1) {
                System.out.print("Ingrese el nombre del contacto: ");
                String nombre = name.nextLine();
                System.out.print("Ingrese el número del contacto: ");
                Long numero = number.nextLong();
                agenda.put(nombre, numero);
                System.out.println("Agenda" + agenda);
                System.out.println("-----*-----*-----*-----*-----");
            } else if (opcion == 2) {
                System.out.print("Ingrese el nombre del contacto a buscar: ");
                String buscarNombre = buscar.nextLine();
                Long numberFind = agenda.get(buscarNombre);
                if (numberFind != null) {
                    System.out.println("Resultado de la búsqueda: ");
                    System.out.println("Nombre: " + buscarNombre + "\n" + "Número: " + numberFind);
                } else {
                    System.out.println("Resultado de la búsqueda: ");
                    System.out.println("El nombre ingresado no está en la agenda de contactos.");
                }
                System.out.println();
            } else if (opcion == 3) {
                System.out.print("Ingrese el nombre del contacto a actualizar: ");
                String actualizarContacto = actualizar.nextLine();
                System.out.print("Ingrese el nuevo núnero: ");
                Long nuevoNumero = actualizarNum.nextLong();
                agenda.put(actualizarContacto, nuevoNumero);
                System.out.println("Contacto actualizado." + actualizarContacto);
                System.out.println("Agenda" + agenda);
                System.out.println("-----*-----*-----*-----*-----");
            } else if (opcion == 4) {
                System.out.print("Ingrese el nombre del contacto a elimina: ");
                String eliminarContaco = actualizar.nextLine();
                agenda.remove(eliminarContaco);
                System.out.println("Contacto elimina: " + eliminarContaco);
                System.out.println("Agenda" + agenda);
                System.out.println("-----*-----*-----*-----*-----");
            } else if (opcion > 5) {
                System.out.println("Opción no valida. Intente de nuevo");
                System.out.println("-----*-----*-----*-----*-----");
            }
            System.out.println("Seleccione una opción: " + "\n" +
                    "-----+-----+-----+-----+" + "\n" +
                    "1. Agregar contacto" + "\n" +
                    "2. Buscar contacto" + "\n" +
                    "3. Actualizar contacto" + "\n" +
                    "4. Borrar contacto" + "\n" +
                    "5. Salir" + "\n" +
                    "-----+-----+-----+-----+");

            opcion = option.nextInt();

        }
        System.out.println("-----*-----*-----*-----*-----");
        System.out.println("Contactos registrados en la agenda" + "\n" +
                agenda);

    }
}