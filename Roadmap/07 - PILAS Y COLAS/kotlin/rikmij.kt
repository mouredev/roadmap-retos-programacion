import java.util.*

fun lifoWeb() {
    val webs = ArrayDeque<String>()
    val deletedWebs = mutableListOf<String>()

    do{
        print("\n¿Quieres buscar una web, avanzar a la siguiente web (adelante) o volver a la anterior (atrás)?\n")
        val action = readln().lowercase()
        if (action != "adelante" && action != "atrás" && action != "esc"){
            webs.add(action)
            println("Estás en la web ${webs.peekLast()}")
        }

        try {
            if (action == "atrás") {
                val del = webs.removeLast()
                deletedWebs.addLast(del)
                if (webs.size == 0) {
                    println("No hay webs previas.")
                } else {
                    println("Estás en la web ${webs.peekLast()}")
                }
            }
        } catch(e: NoSuchElementException){
            println("No hay webs previas. Estás en ${webs.peekLast()}")
        }
        try {
            if (action == "adelante") {
                val adit = deletedWebs.removeLast()
                webs.addLast(adit)

                println("Estás en la web ${webs.peekLast()}")

            }
        } catch(e: NoSuchElementException){
            println("Estás en la web más reciente: ${webs.peekLast()}")
        }
    }while (action != "esc")
}


fun fifoPrint() {
    val prints = ArrayDeque<String>()

    do{
        println("\n¿Quieres imprimir el documento (imprimir) o quieres añadir un elemento a la cola?")
        println("\"Next\" para siguiente documento, \"Prev\" para el anterior. \"Esc\" para salir")
        val option = readln().lowercase()

        if (option != "imprimir"){
            prints.add(option)
            println("Documento \"${prints.peekFirst()}\"")
        }else{
            if (prints.size > 0) {
                println("Documento \"${prints.peekFirst()}\" imprimiéndose")
                prints.removeFirst()
            }else{
                println("No hay más documentos en cola")
            }
        }
    } while(option != "esc")
}


fun main() {
    println("\n --> Ejemplo stack - LIFO")
    val exampleStack = Stack<String>()

    exampleStack.add("Primero")
    exampleStack.add("Segundo")
    exampleStack.add("Tercero")
    println(exampleStack)

    val last = exampleStack.peek()  //peek busca, pero no elimina
    println("-> $last")
    println(exampleStack)

    val popped = exampleStack.pop()
    println("-> $popped")
    println(exampleStack)

    println("\n --> Ejemplo queue - FIFO")
    val exampleQueue: Queue<Int> = LinkedList()
    exampleQueue.add(1)
    exampleQueue.add(2)
    exampleQueue.add(3)
    println(exampleQueue)

    val first = exampleQueue.peek()   //peek aquí accede al primer elemento por ser una cola
    println("-> $first")
    println(exampleQueue)

    val polled = exampleQueue.poll()
    println("-> $polled")
    println(exampleQueue)

    println("\n ${"~".repeat(7)} EJERCICIOS EXTRA ${"~".repeat(7)}")
    println("--> EJERCICIO LIFO WEB")
    lifoWeb()
    println("\n--> EJERCICIO FIFO IMPRESORA")
    fifoPrint()
}
