import java.util.ArrayDeque

class estudiante(val nombre: String, var edad: Int, val ciudad: String) {
    //Se definen parametros opcionales dentro de la clase
    var carrera:String = ""
    //Funcion de comportamiento del objeto
    fun show(){
        println("el estudiante se llama $nombre tiene $edad años y vive en la ciudad de $ciudad y estudia la carrera de $carrera")
    }
}

fun main(){

    //Se construye el objeto dando como paarametros los datos requeridos por la clase, algo muy similar a las funciones
    var estudianteNuevo = estudiante("Santiago", 24, "Bogota")
    //Se llama un comportamiento del objeto
    estudianteNuevo.show()
    //Se puede interactuar con las variables definidas dentro de la clase
    estudianteNuevo.carrera = "Programacion"
    estudianteNuevo.show()
    //Se pueden editar tanto como los parametros ingresados como las variables de la clase siempre y cuando estendefinidas como variables y no como valores (definidas como var)
    estudianteNuevo.edad = 25
    estudianteNuevo.show()
    //No se pueden modificar las variables creadas en una funcion ya estas son exclusivas de cada una, si se necesita tener una variable que se deba editar debe estar definida al nivel de la clase

    //Ejecuciones ejercicio extra

    //Stack
    //Stack Definition
    var tempStack = ArrayDeque<String>()
    tempStack.add("Esto es")
    tempStack.add("un")
    tempStack.add("Stack")

    //Build stack object
    var buildStack = stack(tempStack)

    //Add in stack
    buildStack.addStack("Esta es una adicion en la pila")

    //Erase in stack
    buildStack.deleteStack()

    //Show all stack items
    buildStack.showAllStack()

    //Show stack size
    buildStack.showSizeStack()

    //Queue
    //Queue definition
    var tempQueue = ArrayDeque<String>()
    tempQueue.add("Esto es")
    tempQueue.add("una")
    tempQueue.add("cola")

    //Build queue object
    var buildQueue = queue(tempQueue)

    //Add in queue
    buildQueue.addQueue("Esta es una adicion en la cola")

    //Erase in queue
    buildQueue.deleteQueue()

    //Show all queue items
    buildQueue.showAllQueue()

    //Show queue size
    buildQueue.showSizeQueue()



}

//Ejercicio extra
//Stack
class stack(var stackItems: ArrayDeque<String>){

    fun addStack(item: String){
        stackItems.push(item)
        println("Se ha agregado el item $item a la pila")
    }

    fun deleteStack(){
        val erasedItem = stackItems.pop()
        println("Se ha eliminado el ultimo elemento ingresado de la pila: $erasedItem")
    }

    fun showAllStack(){
        println("A continuacion se mostraran todos los datos de la pila")
        stackItems.forEachIndexed{index, value -> println("${index+1}. $value")}
    }

    fun showSizeStack(){
        println("La pila contiene un total de ${stackItems.size} registros")
    }
}

//Queue
class queue(var queueItems: ArrayDeque<String>){

    fun addQueue(item: String){
        queueItems.offer(item)
        println("Se ha agregado el item $item a la cola")
    }

    fun deleteQueue(){
        val erasedItem = queueItems.poll()
        println("Se ha eliminado el primer elemento ingresado de la cola: $erasedItem")
    }

    fun showAllQueue(){
        println("A continuacion se mostraran todos los datos de la cola")
        queueItems.forEachIndexed{index, value -> println("${index+1}. $value")}
    }

    fun showSizeQueue(){
        println("La pila contiene un total de ${queueItems.size} registros")
    }
}