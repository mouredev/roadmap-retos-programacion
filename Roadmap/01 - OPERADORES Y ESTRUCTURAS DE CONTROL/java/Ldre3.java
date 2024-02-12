import java.util.stream.IntStream;

public class Ldre3 {
    public static void main(String[] args) {
        // EJERCICIO:
        // * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
        // *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
        // *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

        // Operador de suma y asignacion
        int suma = 1 + 2;
        System.out.println(suma);
        // Operador logico
        System.out.println(true && false);
        System.out.println(true || false);
        // Operador de comparacion
        System.out.println(1 == 2);
        System.out.println(1 != 2);
        // Operador de identidad
        System.out.println("Hola" instanceof String);


        // * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
        // *   que representen todos los tipos de estructuras de control que existan
        // *   en tu lenguaje:
        // *   Condicionales, iterativas, excepciones...
        // * - Debes hacer print por consola del resultado de todos los ejemplos.

        // Estructura condicional
        if (1 == 2) {
            System.out.println("1 es igual a 2");
        } else {
            System.out.println("1 no es igual a 2");
        }
        // Estructura iterativa
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }
        while (true) {
            System.out.println("Hola");
            break;
        }

        // Excepciones
        try {
            int a = 1 / 0;
        } catch (Exception e) {
            System.out.println("No se puede dividir entre 0");
        }
        // switch case
        int x = 1;
        switch (x) {
            case 1:
                System.out.println("x es 1");
                break;
            case 2:
                System.out.println("x es 2");
                break;
            default:
                System.out.println("x no es ni 1 ni 2");
                break;
        }



        // Imprimir numeros comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        IntStream.range(10, 56).filter(v -> v%2 == 0 && v!=16 && v%3!=0)
                .forEach(System.out::println);
    }
}