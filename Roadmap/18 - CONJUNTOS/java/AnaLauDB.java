import java.util.*;

public class AnaLauDB {
    public static void main(String[] args) {
        // Usamos ArrayList para operaciones de posición
        List<String> lista = new ArrayList<>(Arrays.asList("A", "B", "C"));
        System.out.println("Lista inicial: " + lista);

        // Añadir al final
        lista.add("D");
        System.out.println("Añadir al final: " + lista);

        // Añadir al principio
        lista.add(0, "Inicio");
        System.out.println("Añadir al principio: " + lista);

        // Añadir varios al final
        lista.addAll(Arrays.asList("E", "F"));
        System.out.println("Añadir varios al final: " + lista);

        // Añadir varios en posición concreta (en la posición 2)
        lista.addAll(2, Arrays.asList("X", "Y"));
        System.out.println("Añadir varios en posición 2: " + lista);

        // Eliminar elemento en posición concreta (posición 3)
        lista.remove(3);
        System.out.println("Eliminar elemento en posición 3: " + lista);

        // Actualizar valor en posición concreta (posición 1)
        lista.set(1, "NuevoValor");
        System.out.println("Actualizar valor en posición 1: " + lista);

        // Comprobar si un elemento está en el conjunto
        System.out.println("¿Contiene 'E'? " + lista.contains("E"));

        // Eliminar todo el contenido
        lista.clear();
        System.out.println("Lista tras clear(): " + lista);

        // DIFICULTAD EXTRA: Operaciones de conjuntos
        Set<Integer> conjunto1 = new HashSet<>(Arrays.asList(1, 2, 3, 4));
        Set<Integer> conjunto2 = new HashSet<>(Arrays.asList(3, 4, 5, 6));

        // Unión
        Set<Integer> union = new HashSet<>(conjunto1);
        union.addAll(conjunto2);
        System.out.println("Unión: " + union);

        // Intersección
        Set<Integer> interseccion = new HashSet<>(conjunto1);
        interseccion.retainAll(conjunto2);
        System.out.println("Intersección: " + interseccion);

        // Diferencia
        Set<Integer> diferencia = new HashSet<>(conjunto1);
        diferencia.removeAll(conjunto2);
        System.out.println("Diferencia (conjunto1 - conjunto2): " + diferencia);

        // Diferencia simétrica
        Set<Integer> difSim = new HashSet<>(union);
        difSim.removeAll(interseccion);
        System.out.println("Diferencia simétrica: " + difSim);
    }
}
