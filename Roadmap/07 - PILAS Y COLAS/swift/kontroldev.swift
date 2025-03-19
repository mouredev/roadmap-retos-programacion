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
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

// Implementación de una pila (stack) utilizando un array
struct Stack<Element> {
    private var elements: [Element] = []
    
    mutating func push(_ element: Element) {
        elements.append(element)   // añadir un elemento
    }
    
    mutating func pop() -> Element? {
        return elements.popLast()
    }
    
    func peek() -> Element? {
        return elements.last
    }
    
    var isEmpty: Bool {
        return elements.isEmpty
    }
    
    var count: Int {
        return elements.count
    }
}


// Implementación de una cola (queue) utilizando un array
struct Queue<Element> {
    private var elements: [Element] = []
    
    mutating func enqueue(_ element: Element) {
        elements.append(element)
    }
    
    mutating func dequeue() -> Element? {
        if elements.isEmpty {
            return nil
        } else {
            return elements.removeFirst()
        }
    }
    
    func peek() -> Element? {
        return elements.first
    }
    
    var isEmpty: Bool {
        return elements.isEmpty
    }
    
    var count: Int {
        return elements.count
    }
}

// Ejemplo de uso
var stack = Stack<Int>()
stack.push(1)
stack.push(2)
stack.push(3)

print("Elementos de la pila:")
while let element = stack.pop() {
    print(element)
}

var queue = Queue<String>()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")

print("\nElementos de la cola:")
while let element = queue.dequeue() {
    print(element)
}


// DIFICULTAD EXTRA (opcional)
struct WebBrowser {
    private var historyStack = Stack<String>()
    private var forwardStack = Stack<String>()
    private var currentPage: String?
    
    mutating func navigate(to page: String) {
        if let currentPage = currentPage {
            historyStack.push(currentPage)
            forwardStack = Stack<String>()
        }
        currentPage = page
        print("Navegando a la página: \(page)")
    }
    
    mutating func goBack() {
        if let page = historyStack.pop() {
            forwardStack.push(currentPage!)
            currentPage = page
            print("Retrocediendo a la página anterior: \(page)")
        } else {
            print("No hay páginas anteriores para retroceder.")
        }
    }
    
    mutating func goForward() {
        if let page = forwardStack.pop() {
            historyStack.push(currentPage!)
            currentPage = page
            print("Avanzando a la página siguiente: \(page)")
        } else {
            print("No hay páginas siguientes para avanzar.")
        }
    }
}

var browser = WebBrowser()

browser.navigate(to: "www.example.com")
browser.navigate(to: "www.google.com")
browser.navigate(to: "www.openai.com")

browser.goBack()
browser.goForward()
browser.goBack()
browser.goBack()


struct SharedPrinter {
    private var printQueue = Queue<String>()
    
    mutating func enqueueDocument(_ document: String) {
        printQueue.enqueue(document)
        print("Se ha añadido el documento '\(document)' a la cola de impresión.")
    }
    
    mutating func printDocument() {
        if let document = printQueue.dequeue() {
            print("Imprimiendo el documento: \(document)")
        } else {
            print("La cola de impresión está vacía.")
        }
    }
}

var printer = SharedPrinter()

printer.enqueueDocument("Documento 1")
printer.enqueueDocument("Documento 2")
printer.enqueueDocument("Documento 3")

printer.printDocument()
printer.printDocument()
printer.printDocument()
printer.printDocument()

