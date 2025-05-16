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

//kotlinc Luis-VB.kt -include-runtime -d Luis-VB.jar
//java -jar Luis-VB.jar

open class LuisRetos {

    fun byValue(a: Int, b: Int) {
        println("Valor de a: $a")
        println("Valor de b: $b")
    }

    fun byReference(listOne: MutableList<Int>, listTwo: MutableList<Int>) {
        listTwo.add(4)
        println("Valor de listOne: $listOne")
    }
}

fun main() {
    val retos = LuisRetos()
    retos.byValue(10, 20)
    val listOne = mutableListOf(1, 2, 3)
    val listTwo = listOne
    retos.byReference(listOne, listTwo)

    var x = 10
    var y = 20
    y += 5

    println("\nPasar por valor:")
    println("x: $x")
    println("y: $y")

    var lista1 = mutableListOf(1, 2, 3)
    var lista2 = lista1
    lista2.add(4)
    println("\nPasar por referencia:")
    println("lista1: $lista1")
    println("lista2: $lista2")

    fun porValor(a: Int) {
        var b = a
        b += 5
        println("Valor de a: $a")
    }
    println("\nFuncion con variables por valor:")
    porValor(34546)

    fun porReferencia(lista: MutableList<Int>) {
        lista.add(4)
        lista.add(5)
        println("Valor de lista: $lista")
        lista.remove(5)
        println("Valor de lista: $lista")
    }
    println("\nFuncion con variables por referencia:")
    porReferencia(mutableListOf(1, 2, 3))
}