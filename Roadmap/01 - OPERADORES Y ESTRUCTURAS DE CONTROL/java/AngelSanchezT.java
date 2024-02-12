/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

/*
    Como ejecutar la siguiente clase de Java: 
    1. Instalación el JDK.

    2. Validar que este instalado con el comando: java -version

    3. Posicionar la terminal en la carpeta: 
    cd C:\DESARROLLO\git\roadmap-retos-programacion\Roadmap\00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO\java

    4. Compilación de la clase Java, el proceso genera un archivo AngelSanchezT.class
        javac AngelSanchezT.java

    5. Ejecución de la clase Java: (Ejecución del archivo sin la extensión .class)
        java AngelSanchezT
 */

public class AngelSanchezT {
    public static void main(String[] args) {
        // Ejemplos de operadores
        // Aritméticos
        int suma = 5 + 3;
        int resta = 10 - 4;
        int multiplicacion = 6 * 2;
        int division = 8 / 4;
        int modulo = 10 % 3;

        // Lógicos
        boolean and = true && false;
        boolean or = true || false;
        boolean not = !true;

        // De comparación
        boolean igual = (5 == 5);
        boolean noIgual = (4 != 7);
        boolean mayorQue = (10 > 5);
        boolean menorQue = (3 < 9);

        // De asignación
        int x = 10;
        x += 5; // Equivalente a x = x + 5;

        // De identidad
        String cadena1 = "Hola";
        String cadena2 = new String("Hola");
        boolean mismaReferencia = (cadena1 == cadena2);

        // De pertenencia
        int[] arreglo = {1, 2, 3, 4, 5};
        boolean contiene = contieneNumero(arreglo, 3);

        // De bits
        int a = 5;
        int b = 3;
        int resultadoAnd = a & b;
        int resultadoOr = a | b;
        int resultadoXor = a ^ b;
        int resultadoDesplazamiento = a << 1;

        System.out.println("Ejemplos de operadores:");
        System.out.println("Suma: " + suma);
        System.out.println("Resta: " + resta);
        System.out.println("Multiplicación: " + multiplicacion);
        System.out.println("División: " + division);
        System.out.println("Módulo: " + modulo);
        System.out.println("AND lógico: " + and);
        System.out.println("OR lógico: " + or);
        System.out.println("NOT lógico: " + not);
        System.out.println("Igual: " + igual);
        System.out.println("No igual: " + noIgual);
        System.out.println("Mayor que: " + mayorQue);
        System.out.println("Menor que: " + menorQue);
        System.out.println("De asignación (x += 5): " + x);
        System.out.println("De identidad: " + mismaReferencia);
        System.out.println("De pertenencia: Contiene 3 en el arreglo: " + contiene);
        System.out.println("De bits AND: " + resultadoAnd);
        System.out.println("De bits OR: " + resultadoOr);
        System.out.println("De bits XOR: " + resultadoXor);
        System.out.println("Desplazamiento a la izquierda: " + resultadoDesplazamiento);

        // Estructuras de control
        System.out.println("\nEjemplos de estructuras de control:");

        // Condicionales
        int numero = 30;
        if (numero > 20) {
            System.out.println("El número es mayor que 20.");
        } else if (numero == 20) {
            System.out.println("El número es igual a 20.");
        } else {
            System.out.println("El número es menor que 20.");
        }

        // Iterativas
        System.out.println("\nNúmeros entre 10 y 55 (pares, no 16 ni múltiplos de 3):");
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.print(i + " ");
            }
        }

        // Excepciones (simulación de una división por cero)
        try {
            int resultadoDivisionCero = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("\nExcepción atrapada: " + e.getMessage());
        }
    }

    // Método auxiliar para verificar si un número está en un arreglo
    private static boolean contieneNumero(int[] arreglo, int numero) {
        for (int elemento : arreglo) {
            if (elemento == numero) {
                return true;
            }
        }
        return false;
    }
}
