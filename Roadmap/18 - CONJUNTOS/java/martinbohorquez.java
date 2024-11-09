import java.util.*;

/**
 * #18 CONJUNTOS
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    public static void main(String[] args) {
        List<Integer> lista = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.printf("La lista mutable: %s%n", lista);
        // Añade un elemento al final.
        lista.add(6);
        System.out.printf("Añadimos un elementos al final de la lista: %s%n", lista);
        // Añade un elemento al principio.
        lista.addFirst(0);
        System.out.printf("Añadimos un elementos al inicio de la lista: %s%n", lista);
        // Añade varios elementos en bloque al final.
        lista.addAll(List.of(7, 8, 9));
        System.out.printf("Añadimos un conjunto de elementos al final de la lista: %s%n", lista);
        // Añade varios elementos en bloque en una posición concreta.
        lista.addAll(4, List.of(31, 32, 33));
        System.out.printf("Añadimos un conjunto de elementos a la lista: %s%n", lista);
        // Elimina un elemento en una posición concreta.
        lista.remove(4);
        System.out.printf("Eliminamos el 5to elemento de la lista: %s%n", lista);
        // Actualiza el valor de un elemento en una posición concreta.
        lista.set(5, 36);
        System.out.printf("Actualizamos el 6to elemento de la lista: %s%n", lista);
        // Comprueba si un elemento está en un conjunto.
        int num = 32;
        System.out.printf("Lista contiene el elemento '%d': %b%n", num, lista.contains(num));
        // Eliminar todos los elementos de la lista.
        lista.clear();
        System.out.printf("Todos los elementos de la lista han sido eliminados: %s%n", lista);

        /*
         * DIFICULTAD EXTRA
         */
        Set<Integer> lista1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        Set<Integer> lista2 = new HashSet<>(Arrays.asList(7, 6, 5, 4, 3));

        Set<Integer> union = new LinkedHashSet<>(lista1);
        union.addAll(lista2);
        System.out.printf("La unión de ambas listas es: %s%n", union);

        Set<Integer> intersection = new LinkedHashSet<>(lista1);
        intersection.retainAll(lista2);
        System.out.printf("La intersección de ambas listas es: %s%n", intersection);

        Set<Integer> difference1 = new LinkedHashSet<>(lista1);
        difference1.removeAll(lista2);
        System.out.printf("La diferencia de lista1 respecto a la lista2 es: %s%n", difference1);

        Set<Integer> difference2 = new LinkedHashSet<>(lista2);
        difference2.removeAll(lista1);
        System.out.printf("La diferencia de lista2 respecto a la lista1 es: %s%n", difference2);

        Set<Integer> symDifference = new LinkedHashSet<>(difference1);
        symDifference.addAll(difference2);
        System.out.printf("La diferencia simétrica de las listas es: %s%n", symDifference);

        symDifference = new LinkedHashSet<>(union);
        symDifference.removeAll(intersection);
        System.out.printf("La diferencia simétrica de las listas es: %s%n", symDifference);


    }
}
