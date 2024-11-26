/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritmeticos, logicos, de comparacion, asignacion, identidad, pertenencia, bits...
 *   (Ten en cuenta cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores tú quieras, crea ejemplos
 *   representen todos los tipos de estructuras de control existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */
package org.example;
class Dredux {
    public static void main(String[] args) {
        //1)
        // Operadores aritmeticos
        int a = 10;
        int b = 5;
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicacion: " + (a * b));
        System.out.println("Division: " + (a / b));
        System.out.println("Modulo: " + (a % b));
        System.out.println();

        // Operadores logicos
        boolean c = true;
        boolean d = false;
        System.out.println("AND: " + (c && d));
        System.out.println("OR: " + (c || d));
        System.out.println("NOT: " + (!c));
        System.out.println();

        // Operadores de comparacion
        System.out.println("Igualdad: " + (a == b));
        System.out.println("Desigualdad: " + (a != b));
        System.out.println("Mayor: " + (a > b));
        System.out.println("Menor: " + (a < b));
        System.out.println("Mayor o igual: " + (a >= b));
        System.out.println("Menor o igual: " + (a <= b));
        System.out.println();

        // Operadores de asignacion
        System.out.println("Asignacion: " + (a = b));
        System.out.println("Suma y asignacion: " + (a += b));
        System.out.println("Resta y asignacion: " + (a -= b));
        System.out.println("Multiplicacion y asignacion: " + (a *= b));
        System.out.println("Division y asignacion: " + (a /= b));
        System.out.println("Modulo y asignacion: " + (a %= b));
        System.out.println();

        // Operadores unitarios
        System.out.println("Incremento: " + (++a));
        System.out.println("Decremento: " + (--a));
        System.out.println("Negacion" + (~a));
        System.out.println("Positivo: " + (+a));
        System.out.println();

        // Operadores de Ternario
        System.out.println("Ternario: " + (a > b ? "a es mayor que b" : "a es menor o igual que b"));
        System.out.println();

        // Operadores de instancia
        String s = "Hola";
        System.out.println("Instancia: " + (s instanceof String));
        System.out.println();

        // Operadores de bits
        System.out.println("AND: " + (a & b));
        System.out.println("OR: " + (a | b));
        System.out.println("XOR: " + (a ^ b));
        System.out.println();



        // 2)
        // Condicionales
        if (a > b) {
            System.out.println("a es mayor que b");
        } else {
            System.out.println("a es menor o igual que b");
        }
        System.out.println();

        // Iterativas
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteracion " + i);
        }
        System.out.println();

        // Excepciones
        try {
            int x = 1 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Division por cero");
        }
        System.out.println();

        // DIFICULTAD EXTRA (opcional):
        // Crea un programa imprima por consola todos los números comprendidos
        // entre 10 y 55 (incluidos), pares, y no son ni el 16 ni múltiplos de 3.

        // 3)
        System.out.println("Numeros pares entre 10 y 55 que no son 16 ni multiplos de 3:");
        for (int i = 10; i <= 55; i++) {
            if (i % 2 != 0 || i == 16 || i % 3 == 0) {
                continue;
            }
            System.out.println(i);
        }
    }
}
