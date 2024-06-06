import Foundation

struct Stack<T> {
    var stack = [T]()

    init(array: [T]) {
        stack = array
    }

    init() {

    }

    mutating func push(e: T) {
        stack.append(e)
    }

    mutating func get() -> T? {
        guard !stack.isEmpty else {
            return nil
        }

        return stack.last
    }

    mutating func pop() -> T {
        return stack.removeLast()
    }

    mutating func clean() {
        stack.removeAll()
    }
}

struct Queue<T> {
    var queue = [T]()

    init(array: [T]) {
        queue = array
    }

    init() {

    }

    mutating func enqueue(e: T) {
        queue.insert(e, at: 0)
    }

    mutating func get() -> T? {
        guard !queue.isEmpty else {
            return nil
        }

        return queue.first
    }

    mutating func dequeue() -> T {
        return queue.removeFirst()
    }

    mutating func clean() {
        queue.removeAll()
    }
}

func browser() {

    var backward: Stack<String> = Stack()
    var forward: Stack<String> = Stack()

    var quite = false

    while !quite {
        print()
        if let web = backward.get() {
            print("Web: \(web)")
        } else {
            print("Web:")
        }
        print("1. Go to a website")
        print("2. Go back")
        print("3. Go forward")
        print("4. Quite")

        if let input = readLine() {
            switch input {
                case "1": 
                    print("Web: ")
                    if let web = readLine() {
                        goWebSite(web: web)
                    } else {
                        print("Wrong input")
                    }
                case "2":
                    goBackward()
                case "3":
                    goForward()
                case "4":
                    quite = true
                default:
                    print("Wrong input")        
            }
        }
    }

    func goBackward() {
        if backward.stack.count != 0 {
            let actualWeb = backward.pop()
            forward.push(e: actualWeb)
        }
    }

    func goForward() {
        if forward.stack.count != 0 {
            let actualWeb = forward.pop()
            backward.push(e: actualWeb)
        }
    }

    func goWebSite(web: String) {
        backward.push(e: web)
        forward.clean()
    }
}

func printer() {
    var printer: Queue<String> = Queue()

    var quite = false

    while !quite {

        if let word = readLine() {

            switch word {
                case "imprimir":
                    if printer.queue.count != 0 {
                        print("> \(printer.dequeue())")
                    }
                case "quite":
                    quite = true
                default:
                    printer.enqueue(e: word)
                    
            }
        }
    }
}

// browser()
printer()