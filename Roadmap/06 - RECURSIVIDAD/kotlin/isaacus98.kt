/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */

fun main(){
    imprimirNumero(100)
    println("\nFactorial")
    println(factorial(10))
    println("\nFibonacci")
    println(fibonacci(10))
}

fun imprimirNumero(numero: Int){
    println(numero)
    if (numero > 1)
        imprimirNumero(numero - 1)
}

fun factorial(numero: Int) : Int {
    if (numero == 1)
        return 1

    val resultado: Int = numero * factorial(numero - 1)

    return resultado
}

fun fibonacci(pos: Int) : Int {
    when {
        pos < 2 -> return pos
        else -> return fibonacci(pos - 1) + fibonacci(pos - 2)
    }
}