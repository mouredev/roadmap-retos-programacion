import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class JimsimroDev {

    /*
     * EJERCICIO:
     * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
     * números del 1 al 10 mediante iteración.
     */

    public static void iterarNumber(int i) {
        if (i <= 10) {
            System.out.printf("Iteraciones %d %n", i);
            iterarNumber(i + 1);
        }
    }

    public static void iterarNumber() {
        iterarNumber(1);
    }

    public static void main(String[] args) {
        /*
         * DIFICULTAD EXTRA (opcional):
         * Escribe el mayor número de mecanismos que posea tu lenguaje
         * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
         */

        //Iterar texto con for
        String texto = "java";
        System.out.println("Iterar texto con for:");
        for (int i = 0; i < texto.length(); i++) {
            System.out.printf("Caracter %d: %s %n", i, texto.charAt(i));
        }

        //Iterar arreglo con for
        System.out.println("Iterar arreglo con for:");
        String[] array = { "a", "b", "c", "d", "e" };
        for (int i = 0; i < array.length; i++) {
            System.out.printf("Elemento %d: %s %n", i, array[i]);
        }

        //Iterar lista con lambda
        System.out.println("Iterar lista con lambda:");
        List<String> list = List.of("Java", "Kotlin", "Elixir", "PHP", "Zig");
        list.stream().forEach(System.out::println); //con referencia a metodo
        list
            .stream()
            .forEach(element -> System.out.printf("Elemento: %s %n", element));

        Map<Integer, Object> map = new HashMap<>();
        map.put(1, "Java");
        map.put(2, "Kotlin");
        map.put(3, "Elixir");
        map.put(4, "PHP");

        //Recorrer pares indice valor del diccionario
        System.out.println("Recorrer pares clave-valor del diccionario:");
        for (Iterator it = map.entrySet().iterator(); it.hasNext();) {
            Map.Entry entry = (Map.Entry) it.next();
            System.out.printf(
                "Clave: %d Valor: %s %n",
                entry.getKey(),
                entry.getValue()
            );
        }

        //Recorrer valor del diccionario con for
        System.out.println("Recorrer valores del diccionario:");
        for (Iterator it = map.keySet().iterator(); it.hasNext();) {
            System.out.printf("Valor: %s %n", map.get(it.next()));
        }

        //Recorrer clave del diccionario con for
        System.out.println("Recorrer claves del diccionario:");
        for (Iterator it = map.keySet().iterator(); it.hasNext();) {
            System.out.printf("Clave: %s %n ", it.next());
        }

        //Recorrer pares clave-valor del diccionario con lambda
        System.out.println(
            "Recorrer pares clave-valor del diccionario con lambda:"
        );

        map.forEach((key, value) ->
            System.out.printf("Clave: %d Valor: %s %n", key, value)
        );

        //Iterar hata 10 con for
        System.out.println("Iteraciones con for:");
        for (int i = 1; i <= 10; i++) {
            System.out.printf("Iteraciones %d %n", i);
        }

        //Iterar hasta 10 con while
        System.out.println("Iteraciones con while:");
        int iteraciones = 1;
        while (iteraciones <= 10) {
            System.out.printf("Iteraciones %d %n", iteraciones);
            iteraciones++;
        }

        System.out.println("Iteraciones con recursividad:");
        iterarNumber();
    }
}
