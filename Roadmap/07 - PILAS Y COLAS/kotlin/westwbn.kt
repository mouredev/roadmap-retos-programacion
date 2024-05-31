/*
En Kotlin, <T> es un parámetro de tipo genérico. Estos permiten que las clases y funciones sean reutilizables y
puedan manejar diferentes tipos sin necesidad de duplicar el código para cada tipo específico.
*/
class Stack<T> {
    //    Stack (pila): También conocida como LIFO (Last In, First Out), es una estructura de datos donde el último elemento
    //    que se añade es el primero en ser retirado.
    private val elements = mutableListOf<T>()

    //    Añadir un elemento a la parte superior de la pila.
    fun push(data: T) = elements.add(data)

    //    Retirar el elemento superior de la pila.
    fun pop(): T? = if (elements.isNotEmpty()) elements.removeAt(elements.size - 1) else null

    //    Obtener el elemento superior sin retirarlo.
    fun peek(): T? = elements.lastOrNull()

    //    Muestra el estado de la pila
    fun state(): String = if (elements.isNotEmpty()) elements.joinToString() else "Empty"
}

class Queue<T> {
    private val elements = mutableListOf<T>()

    //    Añadir un elemento al final de la cola.
    fun enqueue(data: T) = elements.add(data)

    //    Retirar el elemento al principio de la cola.
    fun dequeue(): T? = if (elements.isNotEmpty()) elements.removeAt(0) else null

    //    Obtener el elemento al principio de la cola sin retirarlo.
    fun peek(): T? = elements.firstOrNull()

    //    Muestra el estado de la cola
    fun state(): String = if (elements.isNotEmpty()) elements.joinToString() else "Empty"
}


fun main() {
    val lifo = Stack<String>()
    println("---Ejemplos de Stack:---")
    lifo.push("primer plato")
    lifo.push("segundo plato")
    lifo.push("tercer plato")
    lifo.push("cuarto plato")
    println(lifo.state())
    println("Elemento a retirar: ${lifo.pop()}")
    println("Elemento a obtener: ${lifo.peek()}")
    println(lifo.state())

    println("\n---Ejemplos de Queue:---")
    val fifo = Queue<String>()
    fifo.enqueue("cliente 1")
    fifo.enqueue("cliente 2")
    fifo.enqueue("cliente 3")
    fifo.enqueue("cliente 4")
    println(fifo.state())
    println("Elemento a retirar: ${fifo.dequeue()}")
    println("Elemento al principio de la cola: ${fifo.peek()}")
    println(fifo.state())
}