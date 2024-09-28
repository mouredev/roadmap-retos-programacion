// La recursividad es un concepto fundamental en programación que se refiere a la capacidad de una función para llamarse a sí misma.
fun recursive(number: Int) {
    if (number >= 0) {
        println(number)
        recursive(number - 1)
    }
}

fun factorial(number: Int): Int {
    return if (number == 0 || number == 1) {
        1
    } else {
        number * factorial(number - 1)
    }
}

fun fibonacci(position: Int): Int {
    return if (position <= 1) {
        position
    } else {
        fibonacci(position - 1) + fibonacci(position - 2)
    }
}

fun main() {
    println("Función recursiva:")
    recursive(100)

    println("Ingresa el número para calcular el factorial:")
    val number = readln().toInt()
    println("Función factorial de $number es: ${factorial(number)}")

    println("Ingresa la posición que deseas buscar en la sucesión de Fibonacci:")
    val position = readln().toInt()
    println("El valor en la posición $position es: ${fibonacci(position)}")
}