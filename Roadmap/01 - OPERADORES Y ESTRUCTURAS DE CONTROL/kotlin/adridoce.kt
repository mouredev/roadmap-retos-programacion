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

 fun main() {
    // Operadores Aritmeticos
    println("Operadores Aritmeticos:")
    val suma = 10 + 5
    println("10 + 5 = $suma")

    val resta = 10 - 5
    println("10 - 5 = $resta")

    val multiplicacion = 10 * 5
    println("10 * 5 = $multiplicacion")

    val division = 10 / 5
    println("10 / 5 = $division")

    val modulo = 10 % 5
    println("10 % 5 = $modulo")

    // Operadores de asignacion
    println("Operadores de asignacion:")
    var x = 10
    println("x = 10 -> $x")

    x += 5
    println("x += 5 -> $x")

    x -= 2
    println("x -= 2 -> $x")

    x *= 2
    println("x *= 2 -> $x")

    x /= 4
    println("x /= 4 -> $x")

    x %= 2
    println("x %= 2 -> $x")

    // Operadores de comparacion
    val a = 5
    val b = 10

    println("$a == $b -> ${a == b}")
    println("$a != $b -> ${a != b}")
    println("$a < $b -> ${a < b}")
    println("$a > $b -> ${a > b}")
    println("$a <= $b -> ${a <= b}")
    println("$a >= $b -> ${a >= b}")

    // Operadores logicos
    val c = true
    val d = false

    println("$c && $d -> ${c && d}")
    println("$c || $d -> ${c && d}")
    println("$c ! $d -> ${c && d}")

    //Operadores de incremento y decremento
    var contador = 5
    println("Contador: $contador")
    contador++
    println("Contador++ = $contador")
    contador--
    println("Contador-- = $contador")

    //Operadores de rango
    val rangoInclusivo = 1..5
    println("Rango inclusivo: $rangoInclusivo")
    val rangoExclusivo = 1 until 5
    println("Rango exclusivo: $rangoExclusivo")

    //Estructuras de Control de Selección
    val numero = 10
    if (numero > 0) println("Es positivo") else println("Es negativo o cero")

    val dia = 6
    when (dia) {
        1 -> println("Lunes")
        2 -> println("Martes")
        3 -> println("Miercoles")
        4 -> println("Jueves")
        5 -> println("Viernes")
        6 -> println("Sabado")
        7 -> println("Domingo")
        else -> println("Día no válido")
    }

    // Estructuras de control de iteracion
    for (i in 1..5) {
        println(i)
    }

    var iterador = 0
    while (iterador < 5) {
        println(iterador)
        iterador++
    }

    var y = 0
    do {
        println(y)
        y++
    } while (y < 5)

    // Estructuras de control de saltos

    for (i in 1..10) {
        if (i == 5) break
        println(i)
    }

    for (i in 1..10) {
        if (i % 2 == 0) continue
        println(i)
    }

    try {
        val valor = 4/0
    } catch (e: ArithmeticException){
        println("Excepción aritmética: $e")
    }

    // Reto extra: 
    // Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

    retoExtra()
}

fun retoExtra() {
    for (i in 10..55) {
        if (i % 2 != 0 || i == 16 || i % 3 = 0) continue else println(i)
    }
}