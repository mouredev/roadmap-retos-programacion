fun main() {
    // Asignación por valor
    val a = 1
    var b = a
    b = 2
    println("a = $a")
    println("b = $b")

    // Asignación por referencia
    val c = mutableListOf(1, 2, 3)
    val d = c
    d.add(4)
    println("c = $c")
    println("d = $d")

    // llamada a función con parámetros por valor
    println("a after function call = ${functionWithParametersByValue(a)}")

    // llamada a función con parámetros por referencia
    println("c after function call = ${functionWithParametersByReference(c)}")

    // ---------- Reto ----------

    // Intercambio de valores por valor
    println("Swap by value: ${swapByValue(a, b)}")

    // Intercambio de valores por referencia
    println("Swap by reference: ${
        swapByReference(mutableListOf(1, 2, 3), mutableListOf(4, 5, 6))
    }")
}

// función con parámetros por valor
fun functionWithParametersByValue(a: Int): Int {
    return a + 1
}

// función con parámetros por referencia
fun functionWithParametersByReference(a: MutableList<Int>): MutableList<Int> {
    a.add(1)
    return a
}

fun swapByValue(a: Int, b: Int): Pair<Int, Int> {
    return Pair(b, a)
}

fun swapByReference(
    a: MutableList<Int>,
    b: MutableList<Int>,
): Pair<MutableList<Int>, MutableList<Int>> {
    return Pair(b, a)
}