fun exchangeValue(a: Int, b: Int): Pair<Int, Int> {
    return Pair(b, a)
}


fun exchangeByReference(a: Int, b: Int): Pair<Int, Int> {
    return Pair(a, b)
}

fun main() {
    // Variables por valor
    val originalNumber = 5
    var referenceNumber = originalNumber

    println("Asignación por valor:")
    println("Original: $originalNumber, Nuevo valor: $referenceNumber")

    // Modificación del valor
    referenceNumber = 50
    println("Modificando el valor por referencia:")
    println("Original: $originalNumber, Nuevo valor: $referenceNumber")

    // Asignación por referencia
    data class Person(var name: String)

    val person1 = Person("Juan")
    val person2 = person1  // Asignación por referencia

    println(person1.name) // Imprimirá "Pedro", ya que se modificó el objeto referenciado por 'Person1'
    println("Asignación por referencia:")
    println("Original: $person1, Referencia: $person2")

    // Modificación por referencia
    person2.name = "Pedro"
    println("Modificación por referencia:")
    println("Original: $person1, Referencia: $person2")

    // función con parámetro por valor
    println("Función con parámetro por valor")


    fun multiplyValue(num: Int) {
        println(num * 2) // Esto modifica una copia de 'numero'
    }

    fun modifyName(person: Person) {
        person.name = "Carlos" // Esto modifica el objeto referenciado por 'persona'
    }

    val x = 5
    multiplyValue(x)
    println(x) // Imprimirá 5, ya que 'x' no se modifica dentro de la función

    val person = Person("Juan")
    modifyName(person)
    println(person.name) // Imprimirá "Carlos", ya que se modificó el objeto referenciado por 'persona'

    val originalA = 10
    val originalB = 20

    val (newA, newB) = exchangeValue(originalA, originalB)

    println("Valores originales: A=$originalA, B=$originalB")
    println("Valores intercambiados: A=$newA, B=$newB")

    val firstValue = 1
    val secondValue = 15

    val (newFirstValue, newSecondValue) = exchangeByReference(firstValue, secondValue)
    println("Valores originales: A= ${firstValue}, B= $secondValue")
    println("Valores intercambiados: A=$newFirstValue , B=$newSecondValue")
}