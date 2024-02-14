fun main() {
    val number = 5
    val resultFactorial = factorial(number)
    println("El factorial de $number es $resultFactorial")

    val position = 4
    val resultFibonacci = fibonacci(position)
    println("El valor de la posición $position en la secuencia de Fibonacci es $resultFibonacci")
}

fun factorial(number: Int): Int {

    if (number == 0) {
        return 1
    } else {
        val i = factorial(number - 1)

        return number * i
    }
}

fun fibonacci(position: Int): Int {

    if (position <= 2) {
        return 1
    } else {
        val i = fibonacci(position - 1)
        val j = fibonacci(position - 2)
        return j + i
    }
}