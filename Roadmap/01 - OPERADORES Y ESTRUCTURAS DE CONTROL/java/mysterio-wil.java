/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

// Nota: El nombre de la clase debe ser válido en Java. Usamos mysterio_wil.
public class mysterio_wil {
    public static void main(String[] args) {

        System.out.println("### OPERADORES ###");

        // Operadores Aritméticos
        System.out.println("\n--- Aritméticos ---");
        int a = 10;
        int b = 3;
        System.out.println("Suma: 10 + 3 = " + (a + b));
        System.out.println("Resta: 10 - 3 = " + (a - b));
        System.out.println("Multiplicación: 10 * 3 = " + (a * b));
        System.out.println("División: 10 / 3 = " + (a / b));
        System.out.println("Módulo: 10 % 3 = " + (a % b));

        // Operadores Lógicos
        System.out.println("\n--- Lógicos ---");
        System.out.println("AND (true && false): " + (true && false));
        System.out.println("OR (true || false): " + (true || false));
        System.out.println("NOT (!true): " + (!true));

        // Operadores de Comparación
        System.out.println("\n--- Comparación ---");
        System.out.println("Igualdad (10 == 3): " + (10 == 3));
        System.out.println("Desigualdad (10 != 3): " + (10 != 3));
        System.out.println("Mayor que (10 > 3): " + (10 > 3));

        // Operadores de Asignación
        System.out.println("\n--- Asignación ---");
        int x = 5;
        System.out.println("Asignación simple: x = " + x);
        x += 2;
        System.out.println("Suma y asignación: x += 2 -> x = " + x);

        // Operador de Pertenencia (instanceof)
        System.out.println("\n--- Pertenencia (instanceof) ---");
        String texto = "Hola";
        System.out.println("¿'texto' es una instancia de String? " + (texto instanceof String));

        // Operadores de Bits
        System.out.println("\n--- Bits ---");
        int p = 10; // 1010
        int q = 3;  // 0011
        System.out.println("AND a nivel de bits (10 & 3): " + (p & q));
        System.out.println("OR a nivel de bits (10 | 3): " + (p | q));

        /*
         * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
         *   que representen todos los tipos de estructuras de control que existan
         *   en tu lenguaje:
         *   Condicionales, iterativas, excepciones...
         */

        System.out.println("\n### ESTRUCTURAS DE CONTROL ###");

        // Condicionales
        System.out.println("\n--- Condicionales (if, else if, else) ---");
        int edad = 18;
        if (edad < 18) {
            System.out.println("Eres menor de edad.");
        } else if (edad == 18) {
            System.out.println("Tienes 18 años.");
        } else {
            System.out.println("Eres mayor de edad.");
        }

        // Iterativas
        System.out.println("\n--- Iterativas (for) ---");
        for (int i = 1; i <= 3; i++) {
            System.out.println(i);
        }

        System.out.println("\n--- Iterativas (while) ---");
        int contador = 3;
        while (contador > 0) {
            System.out.println(contador);
            contador--;
        }

        // Excepciones
        System.out.println("\n--- Excepciones (try, catch, finally) ---");
        try {
            int resultado = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Se capturó una excepción aritmética: " + e.getMessage());
        } finally {
            System.out.println("Este bloque (finally) se ejecuta siempre.");
        }

        /*
         * DIFICULTAD EXTRA (opcional):
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni móltiplos de 3.
         */

        System.out.println("\n### DIFICULTAD EXTRA ###");
        System.out.println("Números entre 10 y 55, pares, no 16 y no móltiplos de 3:");
        for (int numero = 10; numero <= 55; numero++) {
            if (numero % 2 == 0 && numero != 16 && numero % 3 != 0) {
                System.out.println(numero);
            }
        }
    }
}
