/*
 * EJERCICIO: básico (Conjuntos)
 */

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class worlion {

    public static void main(String[] args) {

        playWithLists();
        dificultadExtra();
    }

    private static void playWithLists() {
        log("\nEjercicio básico: ");
        List<String> myList = new LinkedList<>(List.of("b", "c"));
        log("Lista inicial: " + myList);

        // Añade un elemento al final.
        myList.add("g");
        log("Añado al final la 'g':\n" + myList);
        // Añade un elemento al principio.
        myList.add(0, "a");
        log("Añado al principio la 'a':\n" + myList);
        // Añade varios elementos en bloque al final.
        myList.addAll(List.of("h", "i"));
        log("Añado al final la 'h' y la 'i':\n" + myList);
        // Añade varios elementos en bloque en una posición concreta.
        myList.addAll(3, List.of("D", "e", "f", "g"));
        log("Añado en medio las 'D', 'e', 'f' y 'g':\n" + myList);
        // Elimina un elemento en una posición concreta.
        myList.remove(6);
        log("Elimino el elemento de la posición 6 (la 'g'):\n" + myList);
        // Actualiza el valor de un elemento en una posición concreta.
        myList.set(3, "d");
        log("Modifico el elemento de la posición 3 ('D' por 'd'):\n" + myList);
        // Comprueba si un elemento está en un conjunto.
        log("Compruebo si la 'g' está contenida: --> " + myList.contains("g"));
        log("Compruebo si la 'z' está contenida: --> " + myList.contains("z"));
        // Elimina todo el contenido del conjunto.
        myList.clear();
        log("Elimino todos los elementos:\n" + myList);

    }

    /*
     * DIFICULTAD EXTRA (opcional):
     */


    private static void dificultadExtra() {
        log("\nDificultad extra: ");
        Set<String> set_1 = new HashSet<String>(Set.of("a", "b", "c"));
        log("Conjunto A: "+set_1);  

        Set<String> set_2 = new HashSet<String>(Set.of("c", "e", "f"));
        log("Conjunto A: "+set_2);  

        // Unión.
        Set<String> union = new HashSet<String>(set_1);
        union.addAll(set_2);
        log("Unión: " + union);  

        // Intersección.
        Set<String> intersection = new HashSet<String>(set_1);
        intersection.retainAll(set_2);
        log("Intersección: " + intersection);  

        // Diferencia.
        Set<String> difference = new HashSet<String>(set_1);
        difference.removeAll(set_2);
        log("Diferencia: " + difference);  

        // Diferencia simétrica.
        Set<String> simetricDifference = union;
        simetricDifference.removeAll(intersection);
        log("Intersección: " + simetricDifference);  

    } 

    private static void log(String message) {
        System.out.println(message);
    }
}
