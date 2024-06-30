/** #03 - Java -> Jesus Antonio Escamilla */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        array();
        list();
        map();
        set();
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

    //Pendiente

    /**-----DIFICULTAD EXTRA-----*/
}