/*
 * Decoradores en Kotlin (Versión simplificada)
 *
 * Los decoradores son un patrón de diseño estructural que permite añadir
 * nuevas funcionalidades a objetos existentes sin alterar su estructura.
 * En Kotlin, podemos implementar decoradores de manera sencilla utilizando
 * funciones de orden superior.
 *
 * En esta implementación, nos centraremos en decorar funciones específicas
 * en lugar de intentar crear un decorador genérico para cualquier tipo de función.
 */

// Función que queremos decorar
fun operation(x: Int, y: Int): Int = x + y

// Decorador simple
fun decorateOperation(func: (Int, Int) -> Int, before: () -> Unit, after: () -> Unit): (Int, Int) -> Int {
    return { x, y ->
        before()
        val result = func(x, y)
        after()
        result
    }
}

// Decorador para contar llamadas a función
fun countCallsOperation(func: (Int, Int) -> Int): (Int, Int) -> Int {
    var count = 0
    return { x, y ->
        count++
        println("La función ha sido llamada $count veces")
        func(x, y)
    }
}

fun main() {
    // Ejemplo de uso del decorador simple
    val decoratedOperation = decorateOperation(
        ::operation,
        before = { println("Antes de la operación") },
        after = { println("Después de la operación") }
    )

    println("Resultado: ${decoratedOperation(5, 3)}")

    // Ejemplo de uso del decorador que cuenta llamadas
    val countedOperation = countCallsOperation(::operation)

    repeat(3) {
        println("Resultado: ${countedOperation(it, it + 1)}")
    }
}