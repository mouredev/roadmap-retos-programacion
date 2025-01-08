fun main() {
    println("Diferentes mecanismos de iteración en Kotlin:")

    // 1. Usando un bucle for con un rango
    println("\n1. Usando for con rango:")
    for (i in 1..10) {
        print("$i ")
    }
    println()

    // 2. Usando un bucle while
    println("\n2. Usando while:")
    var j = 1
    while (j <= 10) {
        print("$j ")
        j++
    }
    println()

    // 3. Usando forEach con una lista
    println("\n3. Usando forEach con lista:")
    (1..10).toList().forEach { print("$it ") }
    println()

    // 4. Usando repeat
    println("\n4. Usando repeat:")
    repeat(10) { print("${it + 1} ") }
    println()

    // 5. Usando do-while
    println("\n5. Usando do-while:")
    var k = 1
    do {
        print("$k ")
        k++
    } while (k <= 10)
    println()

    // 6. Usando un iterador
    println("\n6. Usando un iterador:")
    val iterator = (1..10).iterator()
    while (iterator.hasNext()) {
        print("${iterator.next()} ")
    }
    println()

    // 7. Usando secuencias
    println("\n7. Usando secuencias:")
    (1..10).asSequence().forEach { print("$it ") }
    println()

    // 8. Usando un bucle for con índices
    println("\n8. Usando for con índices:")
    for (index in 0 until 10) {
        print("${index + 1} ")
    }
    println()

    // 9. Usando takeWhile
    println("\n9. Usando takeWhile:")
    generateSequence(1) { it + 1 }
        .takeWhile { it <= 10 }
        .forEach { print("$it ") }
    println()

    // 10. Usando fold
    println("\n10. Usando fold:")
    (1..10).fold("") { acc, i -> "$acc$i " }.also { print(it) }
    println()
}