import java.util.*

/*
  una clase es una estructura  que nos sirve para reprentar objectos del mundo real
  la clase es tratada como un molde para crear objetos y a la vez representa un nuevo tipo de dato.

  las clases contienen los siguientes elementos :
  - atributos (variables)
  - metodos (funciones)
  - constructor (una funcion que se ejecuta cuando se crea una instancia de una clase es la encargada de construir el objeto)
  - propiedades (propiedades generedas con la interacion de atributos y metodos)
  - metodos estaticos (metodos que no requieren de una instancia de la clase y estos no influyen en el comportamiento del objeto)

  mas informacion en https://kotlinlang.org/docs/classes.html#constructors

 */

// ejemplo de clase  una clase se crea con una palabra clave class
// en kotlin los valores que estan dentro de los parestesis son los atributos de la clase
//los parentesis despues del nombre de la clase representan el constructor
class Person(var name: String, var age: Int){

    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

// en kotlin tambien se puede crear una clase con un constructor secuandario
class Animal{
    val name: String
    val specie: String
    constructor(name: String, specie:String){
        this.name = name
        this.specie = specie
    }

   fun fly() {
        println("$name is a $specie and is flying")
    }
}

// los atributos de una clase  se puede limitar su visibilidad con el modificador de acceso public, private o protected
// por defecto los atributos de una clase son publicos asi que no es necesario especificar el modificador
// kotlin cuenta con un  modificador que agrega funcionalidades a nuestras clases  solo tenemos que agregarle el modificador data antes de la palabra class
data class Hokage(private val name: String, private val numberHokage: Int){
    fun hokageData() {
        println("My name is $name and iam the $numberHokage hokage")
    }
}

// ejercicio extra
class QueuePrinter(private val docs: List<String>){
   // atributos  de uso interno
   private val printerQueue: Queue<String> = LinkedList<String>()
   private var option:String=""

   // use inicializer blocks para agregar la lista a la cola
   init {
       this.printerQueue.addAll(docs)
   }
   private fun addDocument(){
        println("What document do you want to add?")
        val name= readLine()!!.toString()
        printerQueue.add(name)
        println("The document $name was added to the printer queue")
    }

   private fun printDocument(){
        val printerDoc= printerQueue.remove()
        println("The document $printerDoc was printed")
        println("the queue is $printerQueue")
    }

    fun sharedPrinter(){
        do {
            println("What do you want to do Add or Print or Exit ?")
            option= readLine()!!.toString().lowercase()
            when(option){
                "add" -> this.addDocument()
                "print" -> this.printDocument()
            }
        } while (option != "exit")
    }

}

class WebNavigator{
    private val back = Stack<String>()
    private  val forward = Stack<String>()

    fun navigate(webPage:String){
        if (back.isEmpty()){
            forward.push(webPage)
            println("Navigate to $webPage")
        }
    }

    fun goBack():String{
        if (back.size>1){
            forward.push(back.pop())
            return "Go back to ${back.peek()}"
        }else{
            return "Can't go back"
        }
    }

    fun goForward():String{
        if (forward.isNotEmpty()){
            back.push(forward.pop())
            return "Go forward to ${forward.peek()}"
        }else{
            return "Can't go forward"
        }
    }

}




fun main() {
    // creando una instancia de la clase  la variable person es un objeto de la clase Person
    val person = Person("John", 25)
    person.greet()
    // modificando atributos de la instancia solo se puede hacer si este atributo es var
    person.age=29
    println(person)
    val bird = Animal("condor", "bird")
    bird.fly()
    // al tener atributos publicos estos son accesibles desde nuestra instancia bird
    println(bird.name)

    val secondHokage=Hokage("Tobirama Senju", 2)
    secondHokage.hokageData()
    //secondHokage.name  genera un error por el modificador privado

    val queuePrinter=QueuePrinter(listOf("doc1","doc2","doc3"))
    queuePrinter.sharedPrinter()

    val webNavigator=WebNavigator()
    webNavigator.navigate("https://www.google.com")
    webNavigator.navigate("https://www.stackoverflow.com")
    webNavigator.navigate("https://www.github.com")
    println(webNavigator.goBack())
    println(webNavigator.goBack())
    println(webNavigator.goForward())

}

