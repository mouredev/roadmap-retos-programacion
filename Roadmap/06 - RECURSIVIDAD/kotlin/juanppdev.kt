fun recursividad(number) {
    if(number > 0) {
        print("$number")
        recursividad(number - 1)
    } else if (number == 0 ) {
        println(number)
    }
}

recursividad(100)


// Factorial
// Función para calcular el factorial de un número
fun factorial(n: Int): Int {
    return if (n == 0) {
        1
    } else {
        n * factorial(n - 1)
    }
}

// Función para calcular el valor de un elemento en la sucesión de Fibonacci
fun fibonacci(n: Int): Int {
    return if (n <= 1) {
        n
    } else {
        fibonacci(n - 1) + fibonacci(n - 2)
    }
}

// Prueba de las funciones
fun main() {
    val numFactorial = 5
    val numFibonacci = 6

    println("El factorial de $numFactorial es: ${factorial(numFactorial)}")
    println("El valor en la posición $numFibonacci de Fibonacci es: ${fibonacci(numFibonacci)}")
}
