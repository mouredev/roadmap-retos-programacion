fun main() {
    println("Imprimiendo números del 100 al 0:")
    imprimirNumeros(100)

    println("\nCalculando factoriales:")
    for (i in 0..5) {
        println("Factorial de $i: ${factorial(i)}")
    }

    println("\nCalculando elementos de la sucesión de Fibonacci:")
    for (i in 0..10) {
        println("Fibonacci($i) = ${fibonacci(i)}")
    }
}

// Función recursiva para imprimir números del 100 al 0
fun imprimirNumeros(n: Int) {
    if (n >= 0) {
        print("$n ")
        imprimirNumeros(n - 1)
    }
}

// Función recursiva para calcular el factorial de un número
fun factorial(n: Int): Long {
    return when {
        n < 0 -> throw IllegalArgumentException("El factorial no está definido para números negativos")
        n == 0 || n == 1 -> 1
        else -> n * factorial(n - 1)
    }
}

// Función recursiva para calcular el valor de un elemento en la sucesión de Fibonacci
fun fibonacci(n: Int): Int {
    return when {
        n < 0 -> throw IllegalArgumentException("La posición en la secuencia de Fibonacci debe ser no negativa")
        n == 0 -> 0
        n == 1 -> 1
        else -> fibonacci(n - 1) + fibonacci(n - 2)
    }
}