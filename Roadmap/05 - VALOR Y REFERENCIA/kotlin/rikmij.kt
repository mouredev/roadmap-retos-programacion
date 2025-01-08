// EN Kotlin no existe el paso por referencia, nunca se pasa el valor en sí, siempre una copia

fun ejerExtra() {
    fun valueFunction(val1: String, val2: Int): Pair<Int, String>{
        return Pair(val2, val1)
    }
    val val1 = "Tres"
    val val2 = 3
    val (newVal1, newVal2) = valueFunction(val1, val2)

    println("Originalmente val1 era $val1, y val2 era $val2")
    println("Ahora, el nuevo val1 es $newVal1 y el nuevo del 2 es $newVal2")
}

fun main() {
    val value = 1

    var varia = "hola"
    println(varia)
    varia = "adiós"
    println(varia)

    fun value(valor: String): String{
        val valu = "He cambiado"
        return valu
    }
    val valu = "Hola"
    println(value(valu))

    println("\n" + "~".repeat(9) + " EJERCICIO EXTRA " + "~".repeat(9))
    ejerExtra()
}
