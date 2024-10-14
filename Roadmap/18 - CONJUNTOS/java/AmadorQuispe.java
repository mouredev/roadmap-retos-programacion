/* ╔══════════════════════════════════════╗
   ║ Autor:  Amador Q                     ║
   ║ Web  : https://amsoft.dev            ║
   ║ 2024                                 ║
   ╚══════════════════════════════════════╝
*/

import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        List<String> conjunto = new LinkedList<>();

        // Añade un elemento al final.
        conjunto.add("C");
        conjunto.add("D");
        conjunto.add("E");
        conjunto.add("J");
        conjunto.add("K");

        System.out.println(conjunto);

        // Agregar al inicio
        conjunto.add(0, "A");
        System.out.println(conjunto);

        // Agregar en posición concreta
        conjunto.add(1, "B");
        System.out.println(conjunto);

        // Añade varios elementos en bloque al final.
        List<String> bloque = new LinkedList<>();
        bloque.add("L");
        bloque.add("M");
        bloque.add("N");
        bloque.add("O");
        conjunto.addAll(bloque);
        System.out.println(conjunto);

        // Añade varios elementos en bloque en una posición concreta.
        List<String> bloque1 = new LinkedList<>();
        bloque1.add("F");
        bloque1.add("G");
        bloque1.add("H");
        bloque1.add("I");
        conjunto.addAll(5, bloque1);
        System.out.println(conjunto);

        // Elimina un elemento en una posición concreta.
        conjunto.remove(0);
        System.out.println(conjunto);

        // Actualiza el valor de un elemento en una posición concreta
        conjunto.set(0, "A");
        System.out.println(conjunto);

        // Comprueba si un elemento está en un conjunto.
        System.out.println("¿Está la letra 'B'? " + conjunto.contains("B"));

        // Elimina todo el contenido del conjunto.
        conjunto.clear();

        // EXTRA
        extra();
    }

    static void extra() {
        Set<String> conjuntoA = new LinkedHashSet<>(List.of("A", "B", "C", "D"));
        System.out.println("Conjunto A: " + conjuntoA);

        Set<String> conjuntoB = new LinkedHashSet<>(List.of("C", "D", "E", "F"));
        System.out.println("Conjunto B: " + conjuntoB);

        // Unión
        Set<String> union = new LinkedHashSet<>(conjuntoA);
        union.addAll(conjuntoB);
        System.out.println("Unión: " + union);

        // Intersección
        Set<String> interseccion = new LinkedHashSet<>(conjuntoA);
        interseccion.retainAll(conjuntoB);
        System.out.println("Intersección: " + interseccion);

        // Diferencia (A - B)
        Set<String> diferenciaAB = new LinkedHashSet<>(conjuntoA);
        diferenciaAB.removeAll(conjuntoB);
        System.out.println("Diferencia (A - B): " + diferenciaAB);

        // Diferencia simétrica (A Δ B)
        Set<String> diferenciaSimetrica = new LinkedHashSet<>(conjuntoA);
        diferenciaSimetrica.addAll(conjuntoB);
        Set<String> interseccionRemoval = new LinkedHashSet<>(conjuntoA);
        interseccionRemoval.removeAll(conjuntoB);
        diferenciaSimetrica.removeAll(interseccionRemoval);
        System.out.println("Diferencia simétrica (A Δ B): " + diferenciaSimetrica);
    }
}
