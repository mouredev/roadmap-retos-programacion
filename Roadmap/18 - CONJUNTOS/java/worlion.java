/*
 * EJERCICIO:
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

import java.util.LinkedList;
import java.util.List;

public class worlion {

    public static void main(String[] args) {

        playWithLists();
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
     * 
     * }
     * 
     * /*
     * DIFICULTAD EXTRA (opcional):
     * Muestra ejemplos de las siguientes operaciones con conjuntos:
     * - Unión.
     * - Intersección.
     * - Diferencia.
     * - Diferencia simétrica.
     */

    private static void log(String message) {
        System.out.println(message);
    }
}
