/* EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */


fun main() {

    val yo = Alumno("Adrian", 29, true)
    yo.verDatos()

    yo.edad = 30
    yo.aprobado = false

    yo.verDatos()

    val stack = Stack<Int>()
    println("Creando pila...")
    stack.push(3)
    stack.push(5)
    stack.push(7)
    stack.printStack()
    println("Tamaño: ${stack.size()}")
    println("Eliminado: ${stack.pop()}")
    stack.printStack()

    val queue = Queue<String>()
    println("Creando cola...")
    queue.push("Perro")
    queue.push("Gato")
    queue.push("Mono")
    queue.printQueue()
    println("Tamaño: ${queue.size()}")
    println("Eliminado: ${queue.pop()}")
    queue.printQueue()

}

class Alumno(
    val nombre: String,
    var edad: Int,
    var aprobado: Boolean
) {
    init {
        println("Alumno $nombre creado")
    }

    fun verDatos() {
        println("Nombre: $nombre")
        println("Edad: $edad")
        println("Aprobado: ${if (aprobado) "Si" else "No"}")
    }
}

/* DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */
class Queue<T> {
    private val queue = ArrayDeque<T>()

    fun push(element: T){
        queue.addLast(element)
    }

    fun pop(): T?{
        return queue.removeFirstOrNull()
    }

    fun size(): Int {
        return queue.size
    }

    fun printQueue(){
        println(queue)
    }
}

class Stack<T> {
    private val stack = ArrayDeque<T>()

    fun push(element: T){
        stack.addLast(element)
    }

    fun pop(): T? {
        return stack.removeLastOrNull()
    }

    fun size(): Int {
        return stack.size
    }

    fun printStack(){
        println(stack)
    }
}

