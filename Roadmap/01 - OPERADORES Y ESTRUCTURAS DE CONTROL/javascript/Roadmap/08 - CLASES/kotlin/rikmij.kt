class Tablet(private val model: String, private val color: String,
             private val screen: Float, private val ram: String) {

    private val brand = "Lenovo"

    fun presentarse(): String{
        return "$brand $model: color $color, pantalla $screen\", RAM $ram"
    }
}


class MyQueue<E>(private val cola: ArrayList<E>) {
    
    fun addComponent(vararg elem: E){
        for (e in elem){
            cola.addLast(e)
        }
    }

    fun removeComponent(){
        cola.removeFirst()
    }

    fun peekComponent(): E{
        return cola.first()
    }

    fun printQueue(): ArrayList<E>{
        return cola
    }
}


class MyStack<E>(private val pila: ArrayList<E>) {

    fun addComponent(vararg elem: E){
        for (e in elem){
            pila.addLast(e)
        }
    }

    fun removeComponent(){
        pila.removeLast()
    }

    fun peekComponent(): E{
        return pila.last()
    }

    fun printStack(): ArrayList<E>{
        return pila
    }
}


fun main() {
    val tablet1 = Tablet("Tab M10", "Gris", 10.6f, "4GB")
    val tablet2 = Tablet("Tab P12", "Gris", 12.7f, "8GB")
    val tablet3 = Tablet("Tab K10", "Azul", 10.3f, "4GB")

    println(tablet1.presentarse())
    println(tablet2.presentarse())
    println(tablet3.presentarse())


    println("${"\n"+"~".repeat(7)} EJERCICIO EXTRA ${"~".repeat(7)}")
    println("-> QUEUES")
    val colaList = ArrayList<String>()
    val queue = MyQueue(colaList)

    queue.addComponent("Uno")
    queue.addComponent("Dos", "Tres")
    queue.addComponent("Cuatro", "Cinco", "Seis")
    println(queue.printQueue())

    queue.removeComponent()
    println(queue.printQueue())

    println(queue.peekComponent())

    println("-> STACKS")
    val pilaList = ArrayList<Int>()
    val stack = MyStack(pilaList)

    stack.addComponent(1, 2, 3)
    stack.addComponent(4, 5)
    println(stack.printStack())

    stack.removeComponent()
    println(stack.printStack())

    println(stack.peekComponent())
}
