import java.util.ArrayDeque

class queues{
    fun main() {

        //Definicion
        var pilaCola =
            ArrayDeque<Int>() //Esta definicon puede toamr comportamientos tanto de pila como de cola, se debe importar la siguiente dependencia import java.util.ArrayDeque

        //Pilas - Stacks LIFO(Last in, First Out)

        //Insercion de datos
        pilaCola.push(1)
        pilaCola.push(2)
        pilaCola.push(3)

        //Eliminacion
        var itemEliminadoPila = pilaCola.pop()
        println("En las pilas se elimina el ultimo elemento en ser ingresado al objeto en este caso se elimino $itemEliminadoPila dejando la pila de la siguiente forma $pilaCola")

        //Obtener elementos
        var obItemPila = pilaCola.peek()
        println("Al consultar elementos en las pilas se llama al ultimo elemento en la misma, con .peek() por lo que de nuestra pila el ultimo elemento es $obItemPila")

        //Colas - queue FIFO(First In, First Out)

        //Insercion de datos
        pilaCola.offer(4)
        pilaCola.offer(5)
        pilaCola.offer(6)

        //Eliminacion
        var itemEliminadoCola = pilaCola.poll()
        println("En las colas se elimina el primer elemento en ser ingresado al objeto en este caso se elimino $itemEliminadoCola dejando la cola de la siguiente forma $pilaCola")

        //Obtener elementos
        var obItemCola = pilaCola.last()
        println("Al consultar elementos en las colas se llama al ultimo elemento en la misma, con .last() por lo que de nuestra pila el ultimo elemento es $obItemCola")

        //Operaciones Comunes

        //Consulta de elementos por indice
        var obItemPilaCola = pilaCola.elementAt(0)
        println("Si se desea obtener un item especifico se puede usar .elementAt() donde en los parentesis dejaremos la posicion que deseamos obtener, en este caso obtenderemos la 0 = $obItemPilaCola")
    }

    //Ejercicio Extra #1 navegacion y adicion de paginas
    var pages = ArrayDeque<String>()
    var index = 0

    fun newPage(item: String){
        pages.push(item)
        println("Se ha agregado la pagina")
        start()
    }

    fun nextPage(){
        if(index == pages.indices.last){
            println("Se encuentra en la ultima pagina: ${pages.elementAt(index)} no puede avanzar mas")
            start()
        }else{
            index++
            println("Se encuentra en la siguiente pagina: ${pages.elementAt(index)}")
            start()
        }
    }

    fun previousPage(){
        if(index == 0){
            println("Se encuentra en la primera pagina: ${pages.elementAt(index)} no puede retroceder mas")
            start()
        }else{
            index--
            println("Se encuentra en la siguiente pagina: ${pages.elementAt(index)}")
            start()
        }
    }
    fun start() {
        var action: String?
        if (pages.size == 0) {
            println("No tiene paginas registradas, por favor registre el nombre de su primera pagina")
            newPage(readLine()!!)

        } else {
            println("Escriba la accion que desea realizar, si desea ir hacia adelante escriba 'adelante', si desea ir hacia atras escriba 'atras' y si escribe una palabra diferente se agregara como una pestaña nueva, enc aso que desee finalizar escriba 'finalizar'")
            action = readLine()
            when (action) {
                "atras" -> nextPage()
                "adelante" -> previousPage()
                "finalizar"-> return
                else -> newPage(action!!)
            }
        }
    }

    //Ejercicio Extra #2 impresiones en cola
    var documents = ArrayDeque<String>()

    fun begin() {
        var action: String?
        if (documents.size == 0) {
            println("No tiene documentos para imprimir, por favor registre el nombre de su primer documento")
            newDocument(readLine()!!)
        } else {
            println("Escriba la accion que desea realizar, Si desea agregar un nuevo documento a la cola ingrese el nombre del documento, si desea imprimir el documento escriba 'Imprimir' y si desea finalizar escriba 'Finalizar'")
            action = readLine()
            when (action) {
                "imprimir" -> printDocument()
                "finalizar"-> return
                else -> newDocument(action!!)
            }
        }
    }

    fun newDocument(item: String){
        documents.offer(item)
        println("Se ha agregado el documento a la cola")
        begin()
    }

    fun printDocument(){
        var printedDocument = documents.pop()
        println("Ha imprimido el siguiente documento $printedDocument")
        begin()
    }


    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val obj = queues()
            obj.main()
            obj.start()
            obj.begin()
        }
    }
}