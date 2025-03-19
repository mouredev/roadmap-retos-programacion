/*EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */

 class Persona {
    var nombre: String
    var edad: Int
    
    // Inicializador
    init(nombre: String, edad: Int) {
        self.nombre = nombre
        self.edad = edad
    }
    
    // Función para imprimir los atributos
    func imprimirDatos() {
        print("Nombre: \(nombre)")
        print("Edad: \(edad)")
    }
}

// Crear una instancia de la clase
let persona1 = Persona(nombre: "Juan", edad: 25)

// Imprimir los atributos
persona1.imprimirDatos()

// Modificar los atributos
persona1.nombre = "Juan Carlos"
persona1.edad = 26

// Imprimir los atributos modificados
persona1.imprimirDatos()

/*
 DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.*/

 class Pila {
    private var elementos: [Int] = []
    
    // Inicializador
    init() {}
    
    // Función para añadir un elemento
    func push(_ elemento: Int) {
        elementos.append(elemento)
    }
    
    // Función para eliminar un elemento
    func pop() -> Int? {
        if elementos.isEmpty {
            return nil
        } else {
            return elementos.removeLast()
        }
    }
    
    // Función para retornar el número de elementos
    func count() -> Int {
        return elementos.count
    }
    
    // Función para imprimir todo su contenido
    func imprimir() {
        print("Pila: \(elementos)")
    }
}

class Cola {
    private var elementos: [Int] = []
    
    // Inicializador
    init() {}
    
    // Función para añadir un elemento
    func enqueue(_ elemento: Int) {
        elementos.append(elemento)
    }
    
    // Función para eliminar un elemento
    func dequeue() -> Int? {
        if elementos.isEmpty {
            return nil
        } else {
            return elementos.removeFirst()
        }
    }
    
    // Función para retornar el número de elementos
    func count() -> Int {
        return elementos.count
    }
    
    // Función para imprimir todo su contenido
    func imprimir() {
        print("Cola: \(elementos)")
    }
}

// Crear instancias de las clases
let pila1 = Pila()
let cola1 = Cola()

// Añadir elementos a las estructuras
pila1.push(1)
pila1.push(2)
cola1.enqueue(1)
cola1.enqueue(2)

// Imprimir los elementos de las estructuras
pila1.imprimir()
cola1.imprimir()

// Eliminar elementos de las estructuras
let elementoPila = pila1.pop()
let elementoCola = cola1.dequeue()

// Imprimir los elementos eliminados
print("Elemento eliminado de la pila: \(elementoPila ?? 0)")
print("Elemento eliminado de la cola: \(elementoCola ?? 0)")

// Imprimir los elementos restantes de las estructuras
pila1.imprimir()
cola1.imprimir()