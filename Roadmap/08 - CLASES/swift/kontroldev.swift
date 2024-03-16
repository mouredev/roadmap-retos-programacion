import Foundation


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

// Definición de la clase Libro
class Libro {
    var titulo: String
    var autor: String
    var paginas: Int
    
    // Inicializador de la clase Libro
    init(titulo: String, autor: String, paginas: Int) {
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    }
    
    // Función para imprimir los atributos del libro
    func imprimirDetalles() {
        print("Título: \(titulo)")
        print("Autor: \(autor)")
        print("Número de páginas: \(paginas)")
    }
}

// Creación de una instancia de Libro
var miLibro = Libro(titulo: "El insondable sonido del silencio.", autor: "N_Mu", paginas: 429)

// Impresión de los detalles del libro utilizando la función imprimirDetalles()
miLibro.imprimirDetalles()

// Modificación de los atributos del libro
miLibro.titulo = "La niña del por qué"
miLibro.autor = "N Mu"
miLibro.paginas = 282

// Impresión de los detalles del libro actualizados
miLibro.imprimirDetalles()


// DIFICULTAD EXTRA (opcional)

// Definición de la clase Pila
class Pila<T> {
    var elementos: [T] = []
    
    // Función para añadir un elemento a la pila
    func push(_ elemento: T) {
        elementos.append(elemento)
    }
    
    // Función para eliminar y retornar el elemento en la cima de la pila
    func pop() -> T? {
        return elementos.popLast()
    }
    
    // Función para retornar el número de elementos en la pila
    func count() -> Int {
        return elementos.count
    }
    
    // Función para imprimir todo el contenido de la pila
    func imprimirContenido() {
        print("Contenido de la pila:")
        for elemento in elementos {
            print(elemento)
        }
    }
}

// Definición de la clase Cola
class Cola<T> {
    var elementos: [T] = []
    
    // Función para añadir un elemento a la cola
    func enqueue(_ elemento: T) {
        elementos.append(elemento)
    }
    
    // Función para eliminar y retornar el primer elemento de la cola
    func dequeue() -> T? {
        if elementos.isEmpty {
            return nil
        } else {
            return elementos.removeFirst()
        }
    }
    
    // Función para retornar el número de elementos en la cola
    func count() -> Int {
        return elementos.count
    }
    
    // Función para imprimir todo el contenido de la cola
    func imprimirContenido() {
        print("Contenido de la cola:")
        for elemento in elementos {
            print(elemento)
        }
    }
}

// Ejemplo de uso de las clases Pila y Cola
var pila = Pila<Int>()
pila.push(1)
pila.push(2)
pila.push(3)
pila.imprimirContenido()

print("Número de elementos en la pila: \(pila.count())")

var cola = Cola<String>()
cola.enqueue("A")
cola.enqueue("B")
cola.enqueue("C")
cola.imprimirContenido()

print("Número de elementos en la cola: \(cola.count())")

