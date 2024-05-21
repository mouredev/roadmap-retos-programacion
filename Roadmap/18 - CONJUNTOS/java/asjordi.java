import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        operaciones();
        operacionesConjuntos();
    }

    /**
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
    static void operaciones(){
        List<Integer> lista = new LinkedList<>(List.of(1, 2, 3, 4, 5));

        System.out.println("Lista original: " + lista);

        // Añade un elemento al final
        lista.add(6);

        // Añade un elemento al principio
        lista.add(0, 0);

        // Añade varios elementos en bloque al final
        lista.addAll(List.of(7, 8, 9));

        // Añade varios elementos en bloque en una posición concreta
        lista.addAll(0, List.of(-3, -2, -1));

        // Elimina un elemento en una posición concreta
        lista.remove(0);

        // Actualiza el valor de un elemento en una posición concreta
        lista.set(0, -10);

        // Comprueba si un elemento está en un conjunto
        var containsNumber = lista.contains(5);

        System.out.println("Lista modificada: " + lista);

        // Elimina todo el contenido del conjunto
        lista.clear();

        System.out.println("Lista vacía: " + lista);
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Muestra ejemplos de las siguientes operaciones con conjuntos:
     * - Unión.
     * - Intersección.
     * - Diferencia.
     * - Diferencia simétrica.
     */
    static void operacionesConjuntos(){
        // Crear dos conjuntos de números para realizar las operaciones
        Set<Integer> conjunto1 = new HashSet<>(Set.of(1, 2, 3, 4, 5));
        Set<Integer> conjunto2 = new HashSet<>(Set.of(4, 5, 6, 7, 8));

        // UNIÓN
        Set<Integer> union = new HashSet<>(conjunto1);
        union.addAll(conjunto2);

        System.out.println("Unión: " + union);

        // INTERSECCIÓN
        Set<Integer> interseccion = new HashSet<>(conjunto1);
        interseccion.retainAll(conjunto2);

        System.out.println("Intersección: " + interseccion);

        // DIFERENCIA
        Set<Integer> diferencia = new HashSet<>(conjunto1);
        diferencia.removeAll(conjunto2);

        System.out.println("Diferencia: " + diferencia);

        // DIFERENCIA SIMÉTRICA
        Set<Integer> diferenciaSimetrica = new HashSet<>(conjunto1);
        diferenciaSimetrica.addAll(conjunto2);
        Set<Integer> tmp = new HashSet<>(conjunto1);
        tmp.retainAll(conjunto2);
        diferenciaSimetrica.removeAll(tmp);

        System.out.println("Diferencia simétrica: " + diferenciaSimetrica);
    }

}
