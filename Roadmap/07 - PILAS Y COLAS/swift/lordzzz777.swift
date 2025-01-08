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


// Implementación de pila (stack) utilizando un array
struct Stack<T>{
    private var elements = [T]()
    
     mutating func push(_ element: T ) {
       elements.append(element)
    }
    
    mutating func pop() -> T? {
        return elements.popLast()
    }
    
     func peek() -> T? {
        return elements.last
    }
    
    func isEmptyElement() -> Bool {
        return elements.isEmpty
    }
    
    
}

// Implementación de cola (queue) utilizando un array
struct Queue<T> {
    private var elements = [T]()
    
    mutating func enqueue(_ element: T){
        elements.append(element)
    }
    
    mutating func dequeue() -> T? {
           if elements.isEmpty {
               return nil
           } else {
               return elements.removeFirst()
           }
       }
    
    func isEmptyQueue() -> Bool {
        return elements.isEmpty
    }
}

// Simulación de un navegador web
func isWebBrowser(){
    var historyBack = Stack<String>()
    var historyForward = Stack<String>()
    
    var currentWebsite = "Homepage"
    
    while true {
        print("ingresa una acción (adelante, atrás o una URL):")
        let input = readLine() ?? ""
        
        switch input.lowercased() {
        case "adelante":
            if !historyForward.isEmptyElement(){
                historyBack.push(currentWebsite)
                currentWebsite = historyForward.pop()!
            }else {
                print("No hay paginas adelante en el historial")
            }
        case "atras":
            if !historyBack.isEmptyElement(){
                historyForward.push(currentWebsite)
                currentWebsite = historyForward.pop()!
            }else {
                print("No hay paginnas atras del historia.")
            }
        default:
            historyBack.push(currentWebsite)
            currentWebsite = input
            historyForward = Stack<String>()
        }
        print("Pagina actual \(currentWebsite)")
    }
}

// probar funcion de simulación de Web
isWebBrowser()

// Simulación de una Impresora
func isPrint(){
    var printQueue = Queue<String>()
    
    while true {
        print("Ingrsa una acción (imprimiendo documento...):")
        
        let input = readLine() ?? ""
        
        if input.lowercased() == "imprimir" {
            if let document = printQueue.dequeue(){
                print("imprimiendo documento \(document)")
            }else {
                print("No hay documento en la cola de impresión")
            }
        }else {
            printQueue.enqueue(input)
            print("Documento agregado a la cola.")
        }
    }
}

// probar funcion de simulación de inpresión
isPrint()
