import Foundation 

/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
 
// Stacks (Pilas)
struct Stacks<Element> {
    private var numero: [Element] = [] // Array de Elementos 

    mutating func push(_ numero: Element) {
        return numero.push(numero) // Añadir un nuevo elemento 
    }

    mutating func pop() -> Element? {
        return numero.popLast() 
    }

    mutating func peek() -> Element? {
        return numero.last 
    }

    var isEmpty: Bool {
        numero.isEmpty // Verificar si hay un elemento vavio 
    }

    var count: Int {
        numero.count // Contar los eleemntos del array 
    }
}

var numeros = Stack<Int>()
numeros.push(1)
numeros.push(2)
numeros.push(3)

print(nombres)

// Queue (Colas)
struct Queue<Element> {
    private var nombre: [Element] = [] // Array de Elementos 

    mutating func append(_ nombre: Element) { // Añadir un elemento al Array 
        return nombre.append(nombre)
    }

    mutating func pop() -> Element? {
        if nombre.isEmpty {
            return nil 
        } else {
            nombre.removeFirst()
        }
    }

    mutating func peek() -> Element? {
        return nombre.first 
    }

    var isEmpty: Bool {
        return nombre.isEmpty 
    }

    var count: Int {
        return nombre.count 
    }
}

var nombre = Queue<String>()
nombre.append("Juan")
nombre.append("Pedro")

print(nombre)


 
 
