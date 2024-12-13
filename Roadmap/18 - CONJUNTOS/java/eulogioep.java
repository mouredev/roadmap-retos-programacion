import java.util.*;

public class eulogioep {
    public static void main(String[] args) {
        // TEORÍA: Los conjuntos en Java
        /*
         * En Java, un Set es una colección que no puede contener elementos duplicados.
         * Hay tres implementaciones principales de Set:
         * 1. HashSet - La más rápida, no mantiene orden
         * 2. TreeSet - Mantiene los elementos ordenados
         * 3. LinkedHashSet - Mantiene el orden de inserción
         * 
         * Para este ejercicio, usaremos principalmente HashSet para las operaciones básicas
         * y luego mostraremos ejemplos con otros tipos para las operaciones adicionales.
         */

        // PARTE 1: OPERACIONES BÁSICAS CON CONJUNTOS
        System.out.println("PARTE 1: OPERACIONES BÁSICAS");
        
        // Creación de un conjunto
        Set<String> conjunto = new HashSet<>();
        System.out.println("Conjunto inicial: " + conjunto);

        // 1. Añadir un elemento al final
        // NOTA: En un HashSet no hay "final" como tal, ya que no mantiene orden
        conjunto.add("Elemento1");
        System.out.println("Después de añadir un elemento: " + conjunto);

        // 2. Añadir un elemento al principio
        // NOTA: Como HashSet no mantiene orden, es igual que añadir al final
        conjunto.add("Elemento2");
        System.out.println("Después de añadir otro elemento: " + conjunto);

        // 3. Añadir varios elementos en bloque al final
        List<String> elementosNuevos = Arrays.asList("Elemento3", "Elemento4", "Elemento5");
        conjunto.addAll(elementosNuevos);
        System.out.println("Después de añadir varios elementos: " + conjunto);

        // 4. Añadir elementos en una posición concreta
        // NOTA: HashSet no permite insertar en posiciones específicas
        // Para demostrar esto, usaremos una LinkedList temporalmente
        List<String> listaOrdenada = new LinkedList<>(conjunto);
        listaOrdenada.addAll(2, Arrays.asList("ElementoA", "ElementoB"));
        conjunto = new HashSet<>(listaOrdenada);
        System.out.println("Después de 'insertar' en posición específica: " + conjunto);

        // 5. Eliminar un elemento
        conjunto.remove("Elemento3");
        System.out.println("Después de eliminar 'Elemento3': " + conjunto);

        // 6. Actualizar un elemento
        // NOTA: En un Set no se pueden actualizar elementos directamente
        // Hay que eliminar el viejo y añadir el nuevo
        if (conjunto.remove("Elemento4")) {
            conjunto.add("Elemento4Actualizado");
        }
        System.out.println("Después de actualizar 'Elemento4': " + conjunto);

        // 7. Comprobar si un elemento está en el conjunto
        boolean contiene = conjunto.contains("Elemento1");
        System.out.println("¿Contiene 'Elemento1'? " + contiene);

        // 8. Eliminar todo el contenido
        conjunto.clear();
        System.out.println("Después de limpiar el conjunto: " + conjunto);

        // PARTE 2: OPERACIONES EXTRA CON CONJUNTOS
        System.out.println("\nPARTE 2: OPERACIONES EXTRA");
        
        Set<Integer> conjunto1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        Set<Integer> conjunto2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8));
        
        // 1. Unión
        Set<Integer> union = new HashSet<>(conjunto1);
        union.addAll(conjunto2);
        System.out.println("Unión: " + union);
        
        // 2. Intersección
        Set<Integer> interseccion = new HashSet<>(conjunto1);
        interseccion.retainAll(conjunto2);
        System.out.println("Intersección: " + interseccion);
        
        // 3. Diferencia
        Set<Integer> diferencia = new HashSet<>(conjunto1);
        diferencia.removeAll(conjunto2);
        System.out.println("Diferencia (conjunto1 - conjunto2): " + diferencia);
        
        // 4. Diferencia simétrica
        Set<Integer> diferenciaSimetrica = new HashSet<>(conjunto1);
        diferenciaSimetrica.addAll(conjunto2);           // Unión
        Set<Integer> temp = new HashSet<>(conjunto1);
        temp.retainAll(conjunto2);                       // Intersección
        diferenciaSimetrica.removeAll(temp);             // Unión - Intersección
        System.out.println("Diferencia simétrica: " + diferenciaSimetrica);
    }
}