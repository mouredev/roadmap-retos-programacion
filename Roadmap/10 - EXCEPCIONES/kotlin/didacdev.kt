class MyException(message: String): Exception(message)

fun divideBy(numbers: List<Int>, divisor: Int, size: Int) {
    require(numbers.size != 0) { throw MyException("The list is empty")}
    require(divisor != 0) { "El divisor no puede ser cero" }
    require(numbers.size == size) { "El tamaño de la lista no es el esperado" }

    for (index in 0 until size) {
        println(numbers[index] / divisor)
    }

    println("No error found")
}

fun main() {
    try {
        divideBy(listOf(1, 2, 3), 2, 3)
    } catch(e: MyException) {
        println("${e.message}")
    } catch(e: Exception) {
        println("Error $e")
    } finally {
        print("Ejecución finalizada")
    }
}