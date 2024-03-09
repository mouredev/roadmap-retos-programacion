class NoInputError(error: String): Exception(error)

fun calculator(n1: Int, n2: Int) {
    println("Tienes los números $n1 y $n2. ¿Qué quieres hacer con ellos?")
    println("1.- Sumar\n" +
            "2.- Restar\n" +
            "3.- Multiplicar\n" +
            "4.- Dividir")

    val input = readln()

    try {
        if (input == ""){
            throw NoInputError("Debes ingresar algo")
        }
        val choose = input.toInt()
        when (choose){
            1 -> println(n1 + n2)
            2 -> println(n1 - n2)
            3 -> println(n1 * n2)
            4 -> println(n1 / n2)
            else -> println("Este número está fuera del rango. Ingrese un número del 1 al 4")
        }
        println("Felicidades, no ha habido ningún error")
        
    }catch (e: ArithmeticException){
        println("Ha habido un fallo con las operaciones. Recuerda que no se puede dividire entre 0")
    }
    catch (e: NoInputError){
        println("No has introducido nada. Debes introducir algo")
    }
    catch (e: NumberFormatException) {
        println("Ingresa un número")
    }
    finally {
        println("Hasta aquí llegó el programa")
    }
}


fun main() {
    try {
        println(10 / 0)
    } catch (e: ArithmeticException) {
        println("Estás intentando dividir entre cero. No se puede")
    }

    try {
        val lista = listOf(1, 2, 3, 4)
        println(lista[5])
    } catch (e: ArrayIndexOutOfBoundsException){
        println("Esta lista no tiene tantos elementos")
    }

    println("${"\n" + "~".repeat(7)} EJERCICIO EXTRA ${"~".repeat(7)}")
    calculator(21, 7)
}
