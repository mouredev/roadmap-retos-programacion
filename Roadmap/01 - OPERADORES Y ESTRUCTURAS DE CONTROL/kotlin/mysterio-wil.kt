/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

fun main() {
    println("### OPERADORES ###")

    // Operadores Aritméticos
    println("\n--- Aritméticos ---")
    val a = 10
    val b = 3
    println("Suma: 10 + 3 = ${a + b}")
    println("Resta: 10 - 3 = ${a - b}")
    println("Multiplicación: 10 * 3 = ${a * b}")
    println("División: 10 / 3 = ${a / b}")
    println("Módulo: 10 % 3 = ${a % b}")

    // Operadores Lógicos
    println("\n--- Lógicos ---")
    println("AND (true && false): ${true && false}")
    println("OR (true || false): ${true || false}")
    println("NOT (!true): ${!true}")

    // Operadores de Comparación
    println("\n--- Comparación ---")
    println("Igualdad (10 == 3): ${10 == 3}")
    println("Desigualdad (10 != 3): ${10 != 3}")

    // Operadores de Asignación
    println("\n--- Asignación ---")
    var x = 5
    x += 2
    println("Suma y asignación: x += 2 -> x = $x")

    // Operadores de Pertenencia
    println("\n--- Pertenencia (in) ---")
    val rango = 1..5
    println("¿El número 3 está en el rango 1..5? ${3 in rango}")

    // Operadores de Bits
    println("\n--- Bits ---")
    val p = 10
    val q = 3
    println("AND a nivel de bits (10 and 3): ${p and q}")
    println("OR a nivel de bits (10 or 3): ${p or q}")

    /*
     * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
     *   que representen todos los tipos de estructuras de control que existan
     *   en tu lenguaje:
     *   Condicionales, iterativas, excepciones...
     */

    println("\n### ESTRUCTURAS DE CONTROL ###")

    // Condicionales
    println("\n--- Condicionales (if, else) ---")
    val edad = 18
    if (edad < 18) {
        println("Eres menor de edad.")
    } else {
        println("Eres mayor de edad.")
    }

    // When (similar a switch)
    println("\n--- Condicionales (when) ---")
    when (edad) {
        in 0..17 -> println("Menor de edad (con when)")
        18 -> println("Justo 18 años (con when)")
        else -> println("Mayor de edad (con when)")
    }

    // Iterativas
    println("\n--- Iterativas (for) ---")
    for (i in 1..3) {
        println(i)
    }

    println("\n--- Iterativas (while) ---")
    var contador = 3
    while (contador > 0) {
        println(contador)
        contador--
    }

    // Excepciones
    println("\n--- Excepciones (try, catch) ---")
    try {
        val division = 10 / 0
    } catch (e: ArithmeticException) {
        println("Se capturó una excepción: ${e.message}")
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea un programa que imprima por consola todos los números comprendidos
     * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
     */

    println("\n### DIFICULTAD EXTRA ###")
    for (numero in 10..55) {
        if (numero % 2 == 0 && numero != 16 && numero % 3 != 0) {
            println(numero)
        }
    }
}
