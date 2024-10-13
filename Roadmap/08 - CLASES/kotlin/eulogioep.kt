// Clase principal para demostrar el concepto de clase
class Persona(var nombre: String, var edad: Int) {
    // Inicializador
    init {
        println("Se ha creado una nueva Persona: $nombre")
    }

    // Función para imprimir los atributos
    fun imprimirDatos() {
        println("Nombre: $nombre, Edad: $edad")
    }
}

// Implementación de una Pila (Stack - LIFO)
class Pila<T> {
    private val elementos = mutableListOf<T>()

    fun agregar(elemento: T) {
        elementos.add(elemento)
    }

    fun eliminar(): T? {
        if (estaVacia()) return null
        return elementos.removeAt(elementos.size - 1)
    }

    fun numeroElementos(): Int = elementos.size

    fun estaVacia(): Boolean = elementos.isEmpty()

    fun imprimir() {
        println("Contenido de la Pila:")
        for (i in elementos.size - 1 downTo 0) {
            println(elementos[i])
        }
    }
}

// Implementación de una Cola (Queue - FIFO)
class Cola<T> {
    private val elementos = mutableListOf<T>()

    fun agregar(elemento: T) {
        elementos.add(elemento)
    }

    fun eliminar(): T? {
        if (estaVacia()) return null
        return elementos.removeAt(0)
    }

    fun numeroElementos(): Int = elementos.size

    fun estaVacia(): Boolean = elementos.isEmpty()

    fun imprimir() {
        println("Contenido de la Cola:")
        elementos.forEach { println(it) }
    }
}

fun main() {
    // Demostración de la clase Persona
    println("--- Demostración de la clase Persona ---")
    val persona = Persona("Alice", 30)
    persona.imprimirDatos()
    
    persona.edad = 31
    persona.nombre = "Alicia"
    persona.imprimirDatos()

    // Demostración de la Pila
    println("\n--- Demostración de la Pila ---")
    val pila = Pila<String>()
    pila.agregar("Primero")
    pila.agregar("Segundo")
    pila.agregar("Tercero")
    
    println("Número de elementos en la pila: ${pila.numeroElementos()}")
    pila.imprimir()
    
    println("Elemento eliminado: ${pila.eliminar()}")
    println("Nuevo número de elementos: ${pila.numeroElementos()}")
    pila.imprimir()

    // Demostración de la Cola
    println("\n--- Demostración de la Cola ---")
    val cola = Cola<Int>()
    cola.agregar(1)
    cola.agregar(2)
    cola.agregar(3)
    
    println("Número de elementos en la cola: ${cola.numeroElementos()}")
    cola.imprimir()
    
    println("Elemento eliminado: ${cola.eliminar()}")
    println("Nuevo número de elementos: ${cola.numeroElementos()}")
    cola.imprimir()
}