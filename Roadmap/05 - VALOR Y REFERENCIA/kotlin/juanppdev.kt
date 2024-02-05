fun main() {
    // Asignación de variables por valor
    var a = 10
    var b = a
    println("Asignación por valor:")
    println("a: $a, b: $b")

    // Modificación de variable por valor
    b = 20
    println("Después de modificar b:")
    println("a: $a, b: $b")
    println()

    // Asignación de variables por referencia
    val listaOriginal = mutableListOf(1, 2, 3)
    val listaReferencia = listaOriginal
    println("Asignación por referencia:")
    println("Original: $listaOriginal, Referencia: $listaReferencia")

    // Modificación de variable por referencia
    listaReferencia.add(4)
    println("Después de modificar la lista por referencia:")
    println("Original: $listaOriginal, Referencia: $listaReferencia")
    println()

    // Función con parámetro por valor
    val originalX = 5
    val resultadoX = duplicarPorValor(originalX)
    println("Función con parámetro por valor:")
    println("Original: $originalX, Resultado: $resultadoX")

    // Función con parámetro por referencia (mutableList)
    val originalList = mutableListOf(1, 2, 3)
    duplicarPorReferencia(originalList)
    println("Función con parámetro por referencia:")
    println("Original: $originalList")
}

fun duplicarPorValor(x: Int): Int {
    return x * 2
}

fun duplicarPorReferencia(lista: MutableList<Int>) {
    for (i in 0 until lista.size) {
        lista[i] *= 2
    }
}

// Ejercicio extra
fun main() {
    // Programa con parámetros por valor
    val a = 5
    val b = 10
    val resultadoValor = intercambiarPorValor(a, b)
    println("Programa con parámetros por valor:")
    println("a: $a, b: $b")
    println("Resultado: $resultadoValor")
    println()

    // Programa con parámetros por referencia
    val listaOriginal = mutableListOf(1, 2, 3)
    val listaReferencia = mutableListOf(4, 5, 6)
    intercambiarPorReferencia(listaOriginal, listaReferencia)
    println("Programa con parámetros por referencia:")
    println("Original: $listaOriginal")
    println("Referencia: $listaReferencia")
}

fun intercambiarPorValor(x: Int, y: Int): Pair<Int, Int> {
    // Intercambio de valores
    val temp = x
    val resultadoX = y
    val resultadoY = temp
    return Pair(resultadoX, resultadoY)
}

fun intercambiarPorReferencia(lista1: MutableList<Int>, lista2: MutableList<Int>) {
    // Intercambio de listas
    val temp = ArrayList(lista1)
    lista1.clear()
    lista1.addAll(lista2)
    lista2.clear()
    lista2.addAll(temp)
}
