class Stack<T>(initialStack: List<T> = emptyList()) {

    private var stack: MutableList<T> = initialStack.toMutableList()

    fun push(e: T) {
        stack.addLast(e)
    }

    fun get(): T? {
        return this.stack.lastOrNull()
    }

    fun pop(): T? {
        return if (stack.isNotEmpty()) {
            stack.removeLast()
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
}

class Queue<T>(initialQueue: List<T> = emptyList()) {

    private var queue: MutableList<T> = initialQueue.toMutableList()

    fun enqueue(e: T) {
        queue.addLast(e)
    }

    fun get(): T? {
        return this.queue.lastOrNull()
    }

    fun dequeue(): T? {
        return if (queue.isNotEmpty()) {
            queue.removeLast()
        } else {
            null
        }
    }

    fun clear() {
        queue.clear()
    }
}

fun browser() {
    var backward: Stack<String> = Stack()
    var forward: Stack<String> = Stack()

    fun goBackward() {
        val actualWeb = backward.pop() ?: ""
        if (actualWeb != "") {
            forward.push(actualWeb)
        }
    }

    fun goForward() {
        val actualWeb = forward.pop() ?: ""
        if (actualWeb != "") {
            backward.push(actualWeb)
        }
    }

    fun goWebSite(web: String) {
        backward.push(web)
        forward.clear()
    }
    var quite = false

    while (!quite) {
        println()
        var web = backward.get() ?: ""
        println("Web: $web") 
        println("1. Go to a website")
        println("2. Go back")
        println("3. Go forward")
        println("4. Quite")

        val input = readLine() ?: ""
        if (input == "1") {
            println("Web:")
                web = readLine() ?: ""
                if (web != "") {
                    goWebSite(web)
                } else {
                    println("Wrong input")
                }
        } else if (input == "2") {
            goBackward()
        } else if (input == "3") {
            goForward()
        } else if (input == "4") {
            quite = true
        } else {
            println("Wrong input")
        }
    }
}

/* EXTRA */

fun printer() {
    var printer: Queue<String> = Queue()
    var quite = false

    while (!quite) {
        val word = readLine() ?: ""

        if (word != "") {

            if (word == "imprimir") {
                val file = printer.dequeue() ?: ""
                println("> $file")
            } else if (word == "quite") {
                quite = true
            } else {
                printer.enqueue(word)
            }
        }
    }
}

fun main() {
    // browser()
    printer()
}