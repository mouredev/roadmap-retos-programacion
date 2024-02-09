/*
EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.

* DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la
sucesión de Fibonacci (la función recibe la posición).
 */

fun countBack(counter: Int) {
    if (counter > 0){
        print("$counter, ")
        countBack(counter-1)
    }else if (counter == 0){
        println(counter)
    }
}

fun factorial(num: Int): Int {
    return if (num > 0){
        num * factorial(num-1)
    }else{
        1
    }
}

fun fibonacci(num: Int): Int {
    return when (num-1){
        1 -> 1
        2 -> 2
        else -> fibonacci(num-2) + fibonacci(num-1)
    }
}


fun main() {
    countBack(100)

    println("\n ${"~".repeat(7)} EJERCICIO EXTRA ${"~".repeat(7)}")
    println("--> FACTORIAL")
    println(factorial(5))
    println("--> FIBONACCI")
    println(fibonacci(9))
}
