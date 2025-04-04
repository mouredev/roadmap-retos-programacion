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

class Alumno(
    val nombre: String,
    val edad: Int,
    val aprobado: Boolean
) {
    init {
        println("Alumno $nombre creado")
    }

    fun verDatos(){
        println("Nombre: $nombre")
        println("Edad: $edad")
        println("Aprobado: ${if aprobado "Si" else "No"}")
    }
}