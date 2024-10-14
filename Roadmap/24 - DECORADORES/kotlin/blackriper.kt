

/*
Patron decorador
Es un patron de diseño estructural que agrega funcionalidades a objetos existentes, sin modificar su comportamiento original.
esto se logra utilizandp objetos encapsulados  que contienen estas funcionalidades.

cuando queremos agregar funcionalidades a un objeto la primera solucion es usar la herencia
pero la herencia tiene  varias limitaciones

la herencia es estatica no se puede alterar su comportamiento en tiempo de ejecucion
y solo se puede sustituir un objeto por otro creando una subclase diferente.

las subclases solo pueden tener una clase padre la mayoria de los lenguajes no permiten la herencia multiple
y la herencia multiple solo permite una subclase por clase padre. hay lenguajes como python que permiten la herencia multiple.

una forma de mitigar esto es usando la composicion esto en palabra simples es un objeto que contiene otro objeto al
cual le delega una parte del trabajo

para mas informacion revisa https://refactoring.guru/design-patterns/decorator

*/

//ejemplo de patron decorador

//1.- primero creamos una interface que defina la funcionalidad que queremos agregar
interface ChrimasTree{
   fun decorate():String
}

//2.- creamos la clase que implementa la interface
class PineTree: ChrimasTree{
    override fun decorate() ="Christmas tree"

}

// alternativa 1 usando composicion

//3.- creaamos una clase abstracta para que actue como  decorador de nuestro objeto
abstract class TreeDecorator(protected val tree: ChrimasTree): ChrimasTree{
    override fun decorate()=tree.decorate()

}


//4.- ahora creamos el metodo que va ser decorado por nuestro decorador
class BubbleLight(tree: ChrimasTree): TreeDecorator(tree) {
    override fun decorate() = tree.decorate() + decoratedWithBubbleLight()
    private fun decoratedWithBubbleLight() = " decorating with Bubble Light"
}

//alternativa 2 usando delegacion de kotlin
class Garlans(private val tree: ChrimasTree): ChrimasTree by tree{
    override fun decorate(): String {
        return tree.decorate() + decoratedWithGarlands()
    }

    private fun decoratedWithGarlands() = " decorated with Garland"
}

fun christmasTreeWithDecorator() {
    println("using composition")
    val christmasTree = BubbleLight(PineTree())
    val decoratedChristmasTree = christmasTree.decorate()
    println(decoratedChristmasTree)

    println("using delegation")
    val decoratedChristmasTree2 = Garlans(PineTree()).decorate()
    println(decoratedChristmasTree2)

}

//ejercicio extra

interface Counter{
    fun counterInvokes()
}

class Count: Counter{
   private  var count = 0
    override fun counterInvokes() {
        count++
        println("the funcion was invoked $count times")
    }
}

class Hello(private val counter: Counter): Counter by counter{
    override fun counterInvokes() {
        hello()
        counter.counterInvokes()
    }
    private fun hello() {
        println("hello")
    }
}




fun main() {
    christmasTreeWithDecorator()

    val hello = Hello(Count())
    hello.counterInvokes()
    hello.counterInvokes()
}