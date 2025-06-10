/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */

class newClass {
    var name = ""
    var username = ""

    init {
        name = "Test 1"
        username = "Test 2"
    }

    fun printDates(): String {
        return "$name, $username"
    }
}

val newClass = newClass()
newClass.name = "Test 1"
newClass.username = "Test 2"

println(newClass.printDates())



