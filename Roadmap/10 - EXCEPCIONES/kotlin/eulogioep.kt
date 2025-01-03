// Excepción personalizada
class MiExcepcionPersonalizada(message: String) : Exception(message)

fun funcionConExcepciones(numero: Int) {
    when {
        numero < 0 -> throw IllegalArgumentException("El número no puede ser negativo")
        numero == 0 -> throw ArithmeticException("No se puede dividir por cero")
        numero > 100 -> throw MiExcepcionPersonalizada("El número es demasiado grande")
        else -> println("El resultado de 100 / $numero es: ${100 / numero}")
    }
}

fun main() {
    // Ejercicio principal: Manejo de excepciones básico
    println("Ejercicio principal:")
    try {
        val resultado = 10 / 0
        println(resultado)
    } catch (e: ArithmeticException) {
        println("Error capturado: ${e.message}")
    }

    val lista = listOf(1, 2, 3)
    try {
        val elemento = lista[5]
        println(elemento)
    } catch (e: IndexOutOfBoundsException) {
        println("Error capturado: ${e.message}")
    }

    // Dificultad extra: Función con múltiples excepciones
    println("\nDificultad extra:")
    val numeros = listOf(-5, 0, 50, 150)

    for (numero in numeros) {
        try {
            println("Procesando el número: $numero")
            funcionConExcepciones(numero)
            println("No se ha producido ningún error para el número $numero")
        } catch (e: IllegalArgumentException) {
            println("Error capturado (IllegalArgumentException): ${e.message}")
        } catch (e: ArithmeticException) {
            println("Error capturado (ArithmeticException): ${e.message}")
        } catch (e: MiExcepcionPersonalizada) {
            println("Error capturado (MiExcepcionPersonalizada): ${e.message}")
        } finally {
            println("La ejecución ha finalizado para el número $numero")
            println()
        }
    }
}