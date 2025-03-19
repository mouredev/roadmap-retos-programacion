import Foundation
// Reto #07 PILAS Y COLAS

// PILAS
/* 
Una pila o stack es una estructura de datos
que almacena los elementos bajo el principio
LI-FO (Last in First Out) -> último en entrar,
primero en salir.

Tiene dos func básicas, Push/Pop.
Push: Se encarga de agregar un elemento a la
pila. Se inserta en la parte superior.
Pop: Saca el elemento y lo retorna.
*/

class Stack {
    var stack: [AnyObject]

    init() {
        stack = [AnyObject]()
    }

    func push(object: AnyObject) -> Bool {
        return stack.append(object)
    }

    func pop() -> AnyObject? {
        if !isEmpty() {
            return stack.removeLast()
        } else {
            return nil 
        }
    }

    func isEmpty() -> Bool {
        return stack.isEmpty
    }

    func peek() -> AnyObject {
        return stack.last
    }

    func size() -> Int {
        return stack.count
    }
} 

// COLAS
/*
Las colas o queues se rigen por el principio
FI-FO (First In-First Out), primero en entrar,
primero en salir.
*/

class Queue {
    var queue: [AnyObject]

    init() {
        queue = [AnyObject]()
    }

    func enqueue(object: AnyObject) -> Bool {
        return queue.append(object)
    }

    func dequeue() -> AnyObject? {
        if !isEmpty() {
            return queue.removeFirst()
        } else {
            return nil 
        }
    }

    func isEmpty() -> Bool {
        return queue.isEmpty
    }

    func peek() -> AnyObject? {
        return queue.first
    }

    func size() -> Int {
        return queue.count
    }
}


// 🧩 DIFICULTAD EXTRA 🧩 - SIMULADOR DE NAVEGADOR WEB.
var webSites: [String] = []
var stackProgramContinue = true
var step: Int = 1

showStackMenu()

while stackProgramContinue {
    if let input = readLine() {
        switch input {
            case inpuWeb(web: input):
                webSites.append(input)
                if let last = webSites.last {
                    print(last)
                }

            case "Back":
                if webSites.isEmpty {
                    print("Not pages found")
                    continue
                }
                step += 1
                if step == webSites.count + 1 {
                    step = webSites.count
                    print("Not more pages")
                } else {
                    print(webSites[webSites.count - step])
                }

            case "Forward":
                if webSites.isEmpty {
                    print("Not pages found")
                    continue
                }
                step -= 1
                if step == 0 {
                    step = 1
                    print("Not more pages")
                } else {
                    print(webSites[webSites.count - step])
                }
            
            case "Exit":
                stackProgramContinue = false
            default:
                print("Invalid option")
        }
    }
}

func inputWebSite(web name: String) -> String {
    var firstChar = ""
    var lastChar: String = ""
    var lastCharReversed: String = ""

    for char in name {
        firstChar.append(char)
        if firstChar.count == 4 {
            break
        }
    }

    for char: Character in name.reversed() {
        lastCharReversed.append(char)
        if lastCharReversed.count == 4 {
            break
        }
    }

    for char: Character in lastCharReversed.reversed() {
        lastChar.append(char)
    }

    if firstChar == "www." && lastChar == ".com" {
        return name
    }

    return "Invalid Website"
}

func showStackMenu() {
    print("\nInput a option.\n")
    print("[WebSite]")
    print("[Back]")
    print("[Forward]")
    print("[Exit]")
}

// 🧩 DIFICULTAD EXTRA 🧩 - SIMULADOR DE IMPRESORA.
var docs: [String] = []
var queueProgramContinue: Bool = true

showQueueMenu()

while queueProgramContinue {
    if let input = readLine() {

        switch input {
            case inputDocument(doc: input):
                docs.append(input)
            case "Print":
                if docs.isEmpty {
                    print("Not Docs for print")
                } else {
                    if let first = docs.first {
                        print(first)
                    }
                    docs.removeFirst()
                }
            case "Exit":
                queueProgramContinue = false
            default:
                print("Invalid option")
        }
    }
}

func inputDocument(doc name: String) -> String {
    if name.contains(".pdf") {
        return name
    }

    return "Invalid Document"
}

func showQueueMenu() {
    print("\nInput an option\n")
    print("[.pdf File]")
    print("[Print]")
    print("Exit")
}