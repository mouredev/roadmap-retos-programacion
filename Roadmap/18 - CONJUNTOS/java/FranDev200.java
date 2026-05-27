import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class FranDev200 {


    static void main() {

        /*

        EJERCICIO:
        * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
        * operaciones (debes utilizar una estructura que las soporte):
        * - Añade un elemento al final.
        * - Añade un elemento al principio.
        * - Añade varios elementos en bloque al final.
        * - Añade varios elementos en bloque en una posición concreta.
        * - Elimina un elemento en una posición concreta.
        * - Actualiza el valor de un elemento en una posición concreta.
        * - Comprueba si un elemento está en un conjunto.
        * - Elimina todo el contenido del conjunto.

         */

        ArrayList<Integer> lista = new ArrayList<>();
        lista.add(1);
        lista.add(2);
        lista.add(3);
        lista.add(5);

        System.out.println("Lista inicial");
        System.out.println(lista);

        // Añadir un elemento al final
        lista.addLast(4);
        System.out.println("Número añadido al final de la lista [4]:");
        System.out.println(lista);

        // Añadir un elemento al principio
        lista.addFirst(0);
        System.out.println("Número añadido al principio de la lista [0]:");
        System.out.println(lista);

        // Añade varios elementos en bloque al final
        ArrayList<Integer> bloqueAniadir = new ArrayList<>();
        bloqueAniadir.add(7);
        bloqueAniadir.add(8);
        bloqueAniadir.add(9);
        lista.addAll(lista.size(), bloqueAniadir);
        System.out.println("Bloque añadido al final de la lista [7, 8, 9]:");
        System.out.println(lista);

        // Añade varios elementos en bloque en una posicion concreta
        ArrayList<Integer> bloqueAniadir2 = new ArrayList<>();
        bloqueAniadir2.add(3);
        bloqueAniadir2.add(3);
        bloqueAniadir2.add(3);
        lista.addAll(lista.indexOf(5), bloqueAniadir2);
        System.out.println("Bloque añadido en una posicion especifica de la lista [3, 3, 3] | Pos -> Donde este el 5:");
        System.out.println(lista);

        // Elimina un elemento de una posicion concreta
        lista.remove(8);
        System.out.println("Elemento de una posicion concreta eliminado [8]:");
        System.out.println(lista);

        // Actualizacion de un elemento
        lista.set(4, 4);
        System.out.println("Elemento de una posicion concreta actualizado [4]:");
        System.out.println(lista);

        // Comprobar si un elemento esta en la lista
        System.out.println("¿Está el 34 en la lista?");
        System.out.println(lista.contains(34));

        // Limpiar la lista
        lista.clear();
        System.out.println("Contenido de la lista despues de limpiarla");

        /*
        DIFICULTAD EXTRA (opcional):
        * Muestra ejemplos de las siguientes operaciones con conjuntos:
        * - Unión.
        * - Intersección.
        * - Diferencia.
        * - Diferencia simétrica.
         */

        System.out.println("\nEjercicio Extra");
        Set<String> listaUnion = new HashSet<>();
        Set<String> listaInterseccion = new HashSet<>();
        Set<String> listaDiferencia = new HashSet<>();
        Set<String> listaDiferenciaSimetrica = new HashSet<>();
        Set<String> listaDiferenciaSimetricaCoincidentes = new HashSet<>();

        Set<String> alumnosFisica = new HashSet<>();
        Set<String> alumnosBiologia = new HashSet<>();

        alumnosFisica.add("Manuel");
        alumnosFisica.add("Inma");
        alumnosFisica.add("Mario");

        alumnosBiologia.add("Laura");
        alumnosBiologia.add("Manuel");
        alumnosBiologia.add("Carlos");

        System.out.println("\nAlumnos de la clase de Física: " + alumnosFisica);
        System.out.println("Alumnos de la clase de Biologia: " + alumnosBiologia);

        // UNION
        listaUnion.addAll(alumnosFisica);
        listaUnion.addAll(alumnosBiologia);
        System.out.println("===== ||");
        System.out.println("UNION ||");
        System.out.println("===== ||");
        System.out.println("Todos los alumnos que hay: " + listaUnion);

        // INTERSECCION
        listaInterseccion.addAll(alumnosFisica);
        listaInterseccion.retainAll(alumnosBiologia);
        System.out.println("============ ||");
        System.out.println("INTERSECCION ||");
        System.out.println("============ ||");
        System.out.println("Alumnos comunes de ambas asignaturas: " + listaInterseccion);

        // DIFERENCIA
        listaDiferencia.addAll(alumnosFisica);
        listaDiferencia.removeAll(alumnosBiologia);
        System.out.println("=================== ||");
        System.out.println("DIFERENCIA (Física) ||");
        System.out.println("=================== ||");
        System.out.println("Alumnos que solo van a física: " + listaDiferencia);

        listaDiferencia.clear();

        listaDiferencia.addAll(alumnosBiologia);
        listaDiferencia.removeAll(alumnosFisica);
        System.out.println("===================== ||");
        System.out.println("DIFERENCIA (Biologia) ||");
        System.out.println("===================== ||");
        System.out.println("Alumnos que solo van a biología: " + listaDiferencia);

        // DIFERENCIA SIMETRICA
        listaDiferenciaSimetrica.addAll(alumnosFisica);
        listaDiferenciaSimetrica.addAll(alumnosBiologia);
        listaDiferenciaSimetricaCoincidentes.addAll(alumnosFisica);
        listaDiferenciaSimetricaCoincidentes.retainAll(alumnosBiologia);
        listaDiferenciaSimetrica.removeAll(listaDiferenciaSimetricaCoincidentes);
        System.out.println("===================== ||");
        System.out.println("DIFERENCIA (Biologia o Física) ||");
        System.out.println("===================== ||");
        System.out.println("Alumnos que solo van a biología o a física: " + listaDiferenciaSimetrica);

    }

}
