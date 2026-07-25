/**
 * Clase que demuestra diferentes mecanismos de iteración en Java
 * 
 * En programación, la iteración es el proceso de repetir un bloque de código
 * múltiples veces. Java ofrece varios mecanismos para realizar iteraciones,
 * cada uno con sus propias características y casos de uso ideales.
 */
public class eulogioep {
    public static void main(String[] args) {
        System.out.println("Demostración de diferentes mecanismos de iteración en Java\n");
        
        // 1. Bucle for tradicional
        System.out.println("1. Usando bucle for tradicional:");
        /*
         * El bucle for es uno de los más comunes y versátiles.
         * Sintaxis: for (inicialización; condición; incremento)
         * - inicialización: se ejecuta una vez al principio
         * - condición: se evalúa antes de cada iteración
         * - incremento: se ejecuta al final de cada iteración
         */
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println("\n");

        // 2. Bucle while
        System.out.println("2. Usando bucle while:");
        /*
         * El bucle while se ejecuta mientras una condición sea verdadera.
         * Es útil cuando no sabemos exactamente cuántas iteraciones necesitamos.
         */
        int contador = 1;
        while (contador <= 10) {
            System.out.print(contador + " ");
            contador++;
        }
        System.out.println("\n");

        // 3. Bucle do-while
        System.out.println("3. Usando bucle do-while:");
        /*
         * Similar al while, pero garantiza que el código se ejecute al menos una vez
         * ya que la condición se evalúa al final de cada iteración.
         */
        int num = 1;
        do {
            System.out.print(num + " ");
            num++;
        } while (num <= 10);
        System.out.println("\n");

        // EXTRA: Más mecanismos de iteración

        // 4. forEach con array
        System.out.println("4. Usando forEach con array:");
        /*
         * El bucle forEach es una forma más moderna y legible de iterar
         * sobre colecciones o arrays.
         */
        int[] numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        for (int numero : numeros) {
            System.out.print(numero + " ");
        }
        System.out.println("\n");

        // 5. Stream forEach
        System.out.println("5. Usando Stream forEach:");
        /*
         * Los Streams, introducidos en Java 8, ofrecen una forma funcional
         * de procesar colecciones de datos.
         */
        java.util.stream.IntStream.rangeClosed(1, 10)
            .forEach(n -> System.out.print(n + " "));
        System.out.println("\n");

        // 6. Iterator
        System.out.println("6. Usando Iterator:");
        /*
         * Los Iterators son objetos que permiten recorrer una colección
         * y eliminar elementos durante la iteración si es necesario.
         */
        java.util.List<Integer> lista = new java.util.ArrayList<>();
        for (int i = 1; i <= 10; i++) lista.add(i);
        
        java.util.Iterator<Integer> iterator = lista.iterator();
        while (iterator.hasNext()) {
            System.out.print(iterator.next() + " ");
        }
        System.out.println("\n");

        // 7. Stream iterate
        System.out.println("7. Usando Stream.iterate:");
        /*
         * Otra forma de usar Streams para generar una secuencia infinita
         * y limitarla según necesitemos.
         */
        java.util.stream.Stream.iterate(1, n -> n + 1)
            .limit(10)
            .forEach(n -> System.out.print(n + " "));
        System.out.println("\n");
    }
}