 fun main (){
    // Creación de un objeto de la clase Car
    val car1 = Car("Toyota", "Corolla", 2020)
    // Impresión de los atributos del objeto
    car1.printCar()
    // Impresión de la cantidad de autos creados
    car1.printCount()

    val car2 = Car("Ford", "Fiesta", 2019)
    car2.printCar()
    car2.printCount()

    // Extra: Creación de un objeto de la clase Pila
    val pila = Pila<String>() // Inicializa un objeto de la clase Pila con tipo de dato String
    pila.push("Elemento 1") // Añade un elemento a la pila
    pila.push("Elemento 2")
    pila.push("Elemento 3")
    pila.printPila() // Imprime el contenido de la pila
    pila.pop() // Elimina el último elemento
    pila.printPila()
    println("Número de elementos: ${pila.size()}") // Imprime el número de elementos

    // Extra: Creación de un objeto de la clase Cola
    val cola = Cola<Int>() // Inicializa un objeto de la clase Cola con tipo de dato Int
    cola.add(1) // Añade un elemento a la cola
    cola.add(2)
    cola.add(3)
    cola.printCola() // Imprime el contenido de la cola
    cola.remove() // Elimina el primer elemento
    cola.printCola()
    println("Número de elementos: ${cola.size()}") // Imprime el número de elementos

 }

 // Clase de ejemplo con inicializador, atributos y función.
 // Una clase en kotlin tiene un constructor primario y puede tener uno o más constructores secundarios.
 // El constructor primario es parte de la declaración de la clase y se encuentra después del nombre de la clase.
 // Si el constructor primario no tiene anotaciones o modificadores, la palabra constructor puede omitirse.
 class Car /*constructor*/ (val brand: String, val model: String, val year: Int) {
    // Los atributos de la clase son brand, model y year

    // Atributo para contar la cantidad de autos creados, es parte de la clase, por lo que es compartido por todos las instancias
    companion object {
        var count = 0
    }

    // Si quieres ejecutar código al momento de la creación del objeto, puedes hacerlo en el bloque init
    init {
        println("Car created")
        count++
    }

    // Función que imprime los atributos del objeto
    fun printCar(){
        println("Car: $brand $model $year")
    }

    // Función que imprime la cantidad de autos creados
    fun printCount(){
        println("Cars created: $count")
    }
 }

 // Extra: Clase Pila
class Pila<T> { // T es un tipo genérico, es decir, puede ser cualquier tipo de dato
    // Atributo privado que almacena los elementos de la pila. Un atributo privado es accesible solo dentro de la clase que lo declara
    private val pila = mutableListOf<T>()
    
    // Función que añade un elemento a la pila
    fun push(element: T){
        pila.add(element)
    }
    
    // Función que elimina el último elemento de la pila
    fun pop(){
        pila.removeAt(pila.size - 1)
    }
    
    // Función que retorna el número de elementos de la pila
    fun size(): Int{
        return pila.size
    }
    
    // Función que imprime el contenido de la pila
    fun printPila(){
        println("Contenido de la Pila: $pila")
    }
}

//Extra: Clase Cola
class Cola<T> {
    private val cola = mutableListOf<T>()
    
    fun add(element: T){
        cola.add(element)
    }
    
    fun remove(){
        cola.removeAt(0)
    }
    
    fun size(): Int{
        return cola.size
    }
    
    fun printCola(){
        println("Contenido de la Cola: $cola")
    }
}