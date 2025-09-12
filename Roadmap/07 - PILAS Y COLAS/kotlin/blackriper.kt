import java.util.*

/*
   Colas (Primero en Entrar , Primero en Salir)FIFO
   -cada elemento nuevo va al final de la misma
   -primero tiene que salir el primer elemento del mismo y hasta que este salga
    podra salir otro elemento de la lista
*/

fun exampleWithQueue() {
    // lista de actividades para el dia
    val task= listOf("Breakfast","Coworker meeting","buy a food")
    // cola de procesoa a seguir
    val queueTask:Queue<String> = LinkedList<String>()
    queueTask.addAll(task)

    // he desayunado completo por lo tanto debo removerlo de la cola
    val firstTask=queueTask.remove()
    println("I have to do $firstTask")

    // debo mostrar la lista de tareas pendientes
    println("I have to do the following tasks: $queueTask")
}

// reto extra
fun sharedPrinter(){
   val docs= listOf("doc1","doc2","doc3")
   val printerQueue: Queue<String> = LinkedList<String>()
   printerQueue.addAll(docs)

    fun addDocument(){
        println("What document do you want to add?")
        val name= readLine()!!.toString()
        printerQueue.add(name)
        println("The document $name was added to the printer queue")
    }

    fun printDocument(){
        val printerDoc= printerQueue.remove()
        println("The document $printerDoc was printed")
        println("the queue is $printerQueue")
    }

    do {
      var option:String
      println("What do you want to do Add or Print or Exit ?")
      option= readLine()!!.toString()
      when(option){
         "Add" -> addDocument()
         "Print" -> printDocument()
        }
    } while (option != "Exit")

}

/*
  Pila (Last in First Out) LIFO(Ultimo en entrar , primero en salir)
  - el último que entra es el primero que sale
  - apilar coloca un objeto en la pila
  - desapilar saca el último objeto de la pila
  - hasta que se desapila el ultimo elemento  se puede acceder al elemnto que se apilo con anterioridad
  */
fun exampleWithStack(){
    val stackNumber=Stack<Int>()
    stackNumber.push(1)
    stackNumber.push(2)
    stackNumber.push(3)
    println("The stack is $stackNumber")

    val lastNumber=stackNumber.pop()
    println("The last number was $lastNumber")

    println("The stack is $stackNumber")
}

// reto extra
fun webNavigator(){
  val back = Stack<String>()
  val forward = Stack<String>()

  fun navigate(webPage:String){
     if (back.isEmpty()){
         forward.push(webPage)
         println("Navigate to $webPage")
     }
  }
  fun goBack(){
     if (back.size>1){
         forward.push(back.pop())
         println("Go back to ${back.peek()}")
     }else{
         println("Can't go back")
     }
  }
  fun goForward(){
     if (forward.isNotEmpty()){
         back.push(forward.pop())
         println("Go forward to ${forward.peek()}")
     }else{
         println("Can't go forward")
     }
  }
  navigate("google.com")
  navigate("stackoverflow.com")
  navigate("github.com")
  goBack()
  goBack()
  goForward()
}


fun main() {
   //colas
   exampleWithQueue()
   sharedPrinter()
   //pilas
   exampleWithStack()
   webNavigator()
}
