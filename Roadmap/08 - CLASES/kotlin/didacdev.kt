fun main() {
    var queue = Queue<Int>()
    var stack = Stack<Int>()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.printQueue()
    println(queue.size())
    println(queue.get())
    println(queue.dequeue())
    queue.printQueue()
    println(queue.size())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.printStack()
    println(stack.size())
    println(stack.get())
    println(stack.pop())
    stack.printStack()
    println(stack.size())
}

class Stack<T>(initialStack: List<T> = emptyList()) {

    private var stack: MutableList<T> = initialStack.toMutableList()

    fun push(e: T) {
        stack.add(0, e)
    }

    fun get(): T? {
        return this.stack.firstOrNull()
    }

    fun pop(): T? {
        return if (stack.isNotEmpty()) {
            stack.removeFirst()
        } else {
            null
        }
    }

    fun clear() {
        stack.clear()
    }

    fun size(): Int {
        return stack.size
    }

    fun printStack() {
        println(stack)
    }
}

class Queue<T>(initialQueue: List<T> = emptyList()) {

    private var queue: MutableList<T> = initialQueue.toMutableList()

    fun enqueue(e: T) {
        queue.addLast(e)
    }

    fun get(): T? {
        return this.queue.firstOrNull()
    }

    fun dequeue(): T? {
        return if (queue.isNotEmpty()) {
            queue.removeFirst()
        } else {
            null
        }
    }

    fun clear() {
        queue.clear()
    }

    fun size(): Int {
        return queue.size
    }

    fun printQueue() {
        println(queue)
    }
}