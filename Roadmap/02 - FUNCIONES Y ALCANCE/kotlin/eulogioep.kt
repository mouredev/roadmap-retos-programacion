// Variable global
var globalVar = "Soy una variable global"

fun main() {
    // Función sin parámetros ni retorno
    fun saludar() {
        println("Hola, mundo!")
    }
    saludar()

    // Función con un parámetro y sin retorno
    fun saludarPersona(nombre: String) {
        println("Hola, $nombre!")
    }
    saludarPersona("Alice")

    // Función con múltiples parámetros y retorno
    fun sumar(a: Int, b: Int): Int {
        return a + b
    }
    println("La suma de 3 y 5 es: ${sumar(3, 5)}")

    // Función con retorno implícito
    fun multiplicar(a: Int, b: Int) = a * b
    println("El producto de 4 y 6 es: ${multiplicar(4, 6)}")

    // Función dentro de otra función
    fun operacionesMatematicas() {
        fun restar(a: Int, b: Int) = a - b
        println("La resta de 10 y 3 es: ${restar(10, 3)}")
    }
    operacionesMatematicas()

    // Uso de función predefinida en Kotlin
    val lista = listOf(1, 2, 3, 4, 5)
    println("La suma de la lista es: ${lista.sum()}")

    // Demostración de variable local vs global
    fun demoVariables() {
        val localVar = "Soy una variable local"
        println(localVar)
        println(globalVar)
    }
    demoVariables()

    // Modificación de variable global
    globalVar = "He cambiado"
    println(globalVar)

    // DIFICULTAD EXTRA
    fun fizzBuzz(firstWord: String, secondWord: String): Int {
        var count = 0
        for (i in 1..100) {
            when {
                i % 3 == 0 && i % 5 == 0 -> println("$firstWord$secondWord")
                i % 3 == 0 -> println(firstWord)
                i % 5 == 0 -> println(secondWord)
                else -> {
                    println(i)
                    count++
                }
            }
        }
        return count
    }

    val resultado = fizzBuzz("Fizz", "Buzz")
    println("Se imprimieron números $resultado veces")
}