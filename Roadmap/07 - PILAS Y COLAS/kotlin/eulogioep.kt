// Implementación de una pila (stack - LIFO) utilizando una lista mutable
class Stack<T> {
    private val elements = mutableListOf<T>()

    fun push(item: T) {
        elements.add(item)
    }

    fun pop(): T? {
        if (isEmpty()) return null
        return elements.removeAt(elements.size - 1)
    }

    fun peek(): T? {
        return elements.lastOrNull()
    }

    fun isEmpty(): Boolean {
        return elements.isEmpty()
    }
}

// Implementación de una cola (queue - FIFO) utilizando una lista mutable
class Queue<T> {
    private val elements = mutableListOf<T>()

    fun enqueue(item: T) {
        elements.add(item)
    }

    fun dequeue(): T? {
        if (isEmpty()) return null
        return elements.removeAt(0)
    }

    fun peek(): T? {
        return elements.firstOrNull()
    }

    fun isEmpty(): Boolean {
        return elements.isEmpty()
    }
}

// Simulación de navegador web utilizando la pila
class WebBrowser {
    private val backStack = Stack<String>()
    private val forwardStack = Stack<String>()
    private var currentPage: String? = null

    fun navigateTo(url: String) {
        currentPage?.let { backStack.push(it) }
        currentPage = url
        while (!forwardStack.isEmpty()) {
            forwardStack.pop()
        }
        println("Navegando a: $url")
    }

    fun goBack() {
        if (!backStack.isEmpty()) {
            currentPage?.let { forwardStack.push(it) }
            currentPage = backStack.pop()
            println("Retrocediendo a: $currentPage")
        } else {
            println("No hay páginas anteriores")
        }
    }

    fun goForward() {
        if (!forwardStack.isEmpty()) {
            currentPage?.let { backStack.push(it) }
            currentPage = forwardStack.pop()
            println("Avanzando a: $currentPage")
        } else {
            println("No hay páginas para avanzar")
        }
    }
}

// Simulación de impresora compartida utilizando la cola
class SharedPrinter {
    private val documentQueue = Queue<String>()

    fun addDocument(document: String) {
        documentQueue.enqueue(document)
        println("Documento '$document' añadido a la cola de impresión")
    }

    fun printNextDocument() {
        val document = documentQueue.dequeue()
        if (document != null) {
            println("Imprimiendo: $document")
        } else {
            println("No hay documentos en la cola de impresión")
        }
    }
}

fun main() {
    // Demostración del navegador web
    println("--- Simulación de Navegador Web ---")
    val browser = WebBrowser()
    browser.navigateTo("google.com")
    browser.navigateTo("openai.com")
    browser.goBack()
    browser.goForward()
    browser.navigateTo("kotlin.com")
    browser.goBack()
    browser.goForward()

    println("\n--- Simulación de Impresora Compartida ---")
    val printer = SharedPrinter()
    printer.addDocument("Informe1.pdf")
    printer.addDocument("Foto.jpg")
    printer.printNextDocument()
    printer.addDocument("Contrato.docx")
    printer.printNextDocument()
    printer.printNextDocument()
    printer.printNextDocument()
}