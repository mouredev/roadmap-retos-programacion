/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

open class LuisRetos {

    var a = 10
    var b = a

    fun byValue(a: int, b: Int) {
        a = 20
        b = 30
        println("Valor de a: $a")
        println("Valor de b: $b")
    }

    val listOne = mutableListOf(1, 2, 3)
    val listTwo = listOne
    fun byReference(a: IntArray, b: IntArray) {
        listTwo.add(4)
        println("Valor de listOne: $listOne")
    }
}

fun main() {
    val retos = LuisRetos()
    retos.byValue()
    retos.byReference()
}