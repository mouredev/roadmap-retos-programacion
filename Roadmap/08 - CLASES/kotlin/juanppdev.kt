/*
EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
*/

// Definición de la clase
class Persona(var nombre: String, var edad: Int) {
    // Inicializador
    init {
        println("Se ha creado una persona llamada $nombre, de $edad años.")
    }

    // Función para imprimir los atributos
    fun imprimirDatos() {
        println("Nombre: $nombre, Edad: $edad")
    }
}

// Creación de un objeto de la clase
val persona1 = Persona("Juan", 25)

// Modificación de los atributos
persona1.nombre = "Juan Carlos"
persona1.edad = 30

// Impresión de los atributos
persona1.imprimirDatos()


/*
DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
*/

// Clase Pila
class Pila<T> {
    private var elementos: MutableList<T> = mutableListOf()

    // Función para añadir un elemento
    fun agregar(elemento: T) {
        elementos.add(elemento)
    }

    // Función para eliminar y retornar el último elemento
    fun eliminar(): T? {
        return if (elementos.isEmpty()) {
            null
        } else {
            elementos.removeAt(elementos.size - 1)
        }
    }

    // Función para retornar el número de elementos
    fun tamaño(): Int {
        return elementos.size
    }

    // Función para imprimir todos los elementos
    fun imprimir() {
        println("Pila: $elementos")
    }
}

// Clase Cola
class Cola<T> {
    private var elementos: MutableList<T> = mutableListOf()

    // Función para añadir un elemento
    fun agregar(elemento: T) {
        elementos.add(elemento)
    }

    // Función para eliminar y retornar el primer elemento
    fun eliminar(): T? {
        return if (elementos.isEmpty()) {
            null
        } else {
            elementos.removeAt(0)
        }
    }

    // Función para retornar el número de elementos
    fun tamaño(): Int {
        return elementos.size
    }

    // Función para imprimir todos los elementos
    fun imprimir() {
        println("Cola: $elementos")
    }
}

// Creación de objetos de las clases
val pila1 = Pila<Int>()
val cola1 = Cola<Int>()

// Añadir elementos a las estructuras
pila1.agregar(1)
pila1.agregar(2)
pila1.agregar(3)

cola1.agregar(1)
cola1.agregar(2)
cola1.agregar(3)

// Imprimir elementos
pila1.imprimir()
cola1.imprimir()