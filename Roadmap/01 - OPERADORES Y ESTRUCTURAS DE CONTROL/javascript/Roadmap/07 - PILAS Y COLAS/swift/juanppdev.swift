/*
    Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
*/
// Implementación de una pila (stack) utilizando un array
struct Stack<T> {
    private var elements = [T]()
    
    mutating func push(_ element: T) {
        elements.append(element)
    }
    
    mutating func pop() -> T? {
        return elements.popLast()
    }
    
    func peek() -> T? {
        return elements.last
    }
    
    func isEmpty() -> Bool {
        return elements.isEmpty
    }
}

// Implementación de una cola (queue) utilizando un array
struct Queue<T> {
    private var elements = [T]()
    
    mutating func enqueue(_ element: T) {
        elements.append(element)
    }
    
    mutating func dequeue() -> T? {
        if elements.isEmpty {
            return nil
        } else {
            return elements.removeFirst()
        }
    }
    
    func peek() -> T? {
        return elements.first
    }
    
    func isEmpty() -> Bool {
        return elements.isEmpty
    }
}

// Ejemplo de uso de la pila
var stack = Stack<Int>()
stack.push(1)
stack.push(2)
stack.push(3)

while !stack.isEmpty() {
    if let element = stack.pop() {
        print("Elemento extraído de la pila: \(element)")
    }
}

// Ejemplo de uso de la cola
var queue = Queue<String>()
queue.enqueue("Hola")
queue.enqueue("Mundo")

while !queue.isEmpty() {
    if let element = queue.dequeue() {
        print("Elemento extraído de la cola: \(element)")
    }
}



// Extra

// Simulación de un navegador web utilizando una pila
func simulateWebBrowser() {
    var history = Stack<String>()
    
    func navigate(to page: String) {
        print("Navegando a la página: \(page)")
        history.push(page)
    }
    
    func goBack() {
        if let previousPage = history.pop() {
            print("Volviendo a la página anterior: \(previousPage)")
        } else {
            print("No hay páginas anteriores en el historial.")
        }
    }
    
    // Simulación de la navegación
    navigate(to: "Google")
    navigate(to: "Facebook")
    navigate(to: "Twitter")
    
    goBack()
    goBack()
}

// Simulación de una impresora compartida utilizando una cola
func simulateSharedPrinter() {
    var printerQueue = Queue<String>()
    
    func printDocument(_ document: String) {
        print("Imprimiendo documento: \(document)")
    }
    
    func processPrintQueue() {
        if let document = printerQueue.dequeue() {
            printDocument(document)
        } else {
            print("No hay documentos en la cola de impresión.")
        }
    }
    
    // Simulación de la cola de impresión
    printerQueue.enqueue("Documento1.pdf")
    printerQueue.enqueue("Documento2.docx")
    printerQueue.enqueue("Documento3.txt")
    
    processPrintQueue()
    processPrintQueue()
}

// Ejecutar simulaciones
simulateWebBrowser()
simulateSharedPrinter()