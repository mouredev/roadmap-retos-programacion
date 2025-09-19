public class AnaLauDB {
    public static void main(String[] args) {
        // Ejemplo de uso de bucles
        for (int i = 0; i <= 10; i++) {
            System.out.println("Número (for): " + i);
        }

        // Ejemplo de uso de un bucle while
        int j = 0;
        while (j <= 10) {
            System.out.println("Número (while): " + j);
            j++;
        }

        // Ejemplo de uso de un bucle do-while
        int k = 0;
        do {
            System.out.println("Número (do-while): " + k);
            k++;
        } while (k <= 10);
        System.out.println("          ");

        // DIFICULTAD EXTRA
        System.out.println("DIFICULTAD EXTRA");
        // 4. For-each sobre un array
        int[] numeros = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        for (int n : numeros) {
            System.out.println("for-each: " + n);
            System.out.println("          ");
        }

        // 5. Iterando con Streams (Java 8+)
        java.util.stream.IntStream.rangeClosed(1, 10)
                .forEach(x -> System.out.println("stream: " + x));
        System.out.println("          ");

        // 6. Iterando con recursividad
        imprimirRecursivo(1, 10);
        System.out.println("          ");

        // 7. Iterando con java.util.Iterator
        java.util.List<Integer> lista = java.util.Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        java.util.Iterator<Integer> it = lista.iterator();
        while (it.hasNext()) {
            System.out.println("iterator: " + it.next());
        }
        System.out.println("          ");
    }

    // Método recursivo para imprimir del a al b
    public static void imprimirRecursivo(int a, int b) {
        if (a > b)
            return;
        System.out.println("recursivo: " + a);
        imprimirRecursivo(a + 1, b);
    }
}
