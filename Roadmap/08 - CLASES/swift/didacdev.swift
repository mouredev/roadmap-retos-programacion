import Foundation 

struct Stack<T> {
    private var stack = [T]()

    init(array: [T]) {
        stack = array
    }

    init() {

    }

    mutating func push(e: T) {
        stack.insert(e, at: 0)
    }

    mutating func get() -> T? {
        if let e = stack.first {
            return e
        } else {
            return nil
        }
    }

    mutating func pop() -> T? {
        if stack.first != nil {
            return stack.removeFirst()
        } else {
            return nil
        }

    }

    mutating func clean() {
        stack.removeAll()
    }

    mutating func size() -> Int{
        return stack.count
    }

    mutating func printStack() {
        print(stack)
    }
}

struct Queue<T> {
    private var queue = [T]()

    init(array: [T]) {
        queue = array
    }

    init() {

    }

    mutating func enqueue(e: T) {
        queue.append(e)
    }

    mutating func get() -> T? {
        if let e = queue.first {
            return e
        } else {
            return nil
        }
    }

    mutating func dequeue() -> T? {
        if queue.first != nil {
            return queue.removeFirst()
        } else {
            return nil
        }
    }

    mutating func clean() {
        queue.removeAll()
    }

    mutating func size() -> Int {
        return queue.count
    }

    mutating func printQueue() {
        print(queue)
    }
}

var queue: Queue<Int> = Queue()
var stack: Stack<Int> = Stack()

queue.enqueue(e: 1)
queue.enqueue(e: 2)
queue.enqueue(e: 3)
queue.enqueue(e: 4)
queue.enqueue(e: 5)
queue.printQueue()
print(queue.size())
print(queue.get())
print(queue.dequeue())
queue.printQueue()
print(queue.size())

stack.push(e: 1)
stack.push(e: 2)
stack.push(e: 3)
stack.push(e: 4)
stack.push(e: 5)
stack.printStack()
print(stack.size())
print(stack.get())
print(stack.pop())
stack.printStack()
print(stack.size())
