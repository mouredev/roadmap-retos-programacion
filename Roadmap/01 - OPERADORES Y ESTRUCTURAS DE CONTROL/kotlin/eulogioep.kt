fun main() {
    // Operadores aritméticos
    println("Operadores aritméticos:")
    println("5 + 3 = ${5 + 3}")
    println("10 - 4 = ${10 - 4}")
    println("6 * 2 = ${6 * 2}")
    println("15 / 3 = ${15 / 3}")
    println("17 % 5 = ${17 % 5}")

    // Operadores de asignación
    var x = 10
    println("\nOperadores de asignación:")
    println("x = $x")
    x += 5
    println("x += 5: $x")
    x -= 3
    println("x -= 3: $x")
    x *= 2
    println("x *= 2: $x")
    x /= 4
    println("x /= 4: $x")

    // Operadores de comparación
    println("\nOperadores de comparación:")
    println("5 > 3: ${5 > 3}")
    println("5 < 3: ${5 < 3}")
    println("5 >= 5: ${5 >= 5}")
    println("5 <= 4: ${5 <= 4}")
    println("5 == 5: ${5 == 5}")
    println("5 != 4: ${5 != 4}")

    // Operadores lógicos
    println("\nOperadores lógicos:")
    println("true && false: ${true && false}")
    println("true || false: ${true || false}")
    println("!true: ${!true}")

    // Operadores de identidad
    val a = Integer(5)
    val b = Integer(5)
    val c = a
    println("\nOperadores de identidad:")
    println("a === b: ${a === b}")
    println("a === c: ${a === c}")
    println("a !== b: ${a !== b}")

    // Operadores de bits
    println("\nOperadores de bits:")
    println("5 and 3: ${5 and 3}")
    println("5 or 3: ${5 or 3}")
    println("5 xor 3: ${5 xor 3}")
    println("5 shl 1: ${5 shl 1}")
    println("5 shr 1: ${5 shr 1}")

    // Estructuras de control
    
    // Condicional if-else
    println("\nCondicional if-else:")
    val numero = 7
    if (numero % 2 == 0) {
        println("$numero es par")
    } else {
        println("$numero es impar")
    }

    // Condicional when (switch)
    println("\nCondicional when:")
    when (numero) {
        in 1..5 -> println("$numero está entre 1 y 5")
        in 6..10 -> println("$numero está entre 6 y 10")
        else -> println("$numero está fuera del rango 1-10")
    }

    // Bucle for
    println("\nBucle for:")
    for (i in 1..5) {
        println("Iteración $i")
    }

    // Bucle while
    println("\nBucle while:")
    var i = 0
    while (i < 5) {
        println("Mientras i < 5, i = $i")
        i++
    }

    // Bucle do-while
    println("\nBucle do-while:")
    var j = 0
    do {
        println("Do-while j < 5, j = $j")
        j++
    } while (j < 5)

    // Manejo de excepciones
    println("\nManejo de excepciones:")
    try {
        val resultado = 10 / 0
        println(resultado)
    } catch (e: ArithmeticException) {
        println("Error: División por cero")
    } finally {
        println("Este bloque siempre se ejecuta")
    }

    // DIFICULTAD EXTRA
    println("\nDIFICULTAD EXTRA:")
    for (num in 10..55) {
        if (num % 2 == 0 && num != 16 && num % 3 != 0) {
            println(num)
        }
    }
}