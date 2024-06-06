data class Person(var name: String)
data class Number(var value: Int)

fun main() {

    // Asignacion por valor: Crea una copia y la modifica sin afectar al valor original

    val number1 = 5
    var number2 = number1

    number2 += 10
    println("a: $number1 ; b: $number2\n")

    // Asignacion por referencia: Afecta el valor original de la variable

    val person1 = Person("Moure")
    val person2 = person1

    person2.name = "Alejandro"

    println("Person1: ${person1.name} ; Person2: ${person2.name}\n")

    var value = 5
    incrementarPorValor(value)
    println("Fuera de la función: $value\n")  // No cambia el valor original, pero cambia el valor de la copia

    val person3 = Person("AntiguoNombre")
    cambiarNombrePorReferencia(person3)
    println("Nuevo nombre: ${person3.name}\n")  // La funcion afecta al valor original

    //Extra//

    println("Extra!!")

    val originalA = 10
    val originalB = 20
    val intercambio1 = intercambiarPorValor(originalA, originalB)
    println("""
        
        Valores originales: A = ${originalA} ; B = ${originalB}
        Valores intercambiados: A = ${intercambio1.first} ; B = ${intercambio1.second}
        
    """.trimIndent())

    val originalC = Number(20)
    val originalD = Number(40)
    val intercambio2 = intercambiarPorReferencia(originalC, originalD)
    println("""
        
        Valores originales: C = ${originalC.value} ; D = ${originalD.value}
        Valores intercambiados: C = ${intercambio2.first.value} ; D = ${intercambio2.second.value}
        
    """.trimIndent())

}

fun incrementarPorValor(number: Int) {
    println("Dentro de la función: ${number + 1}\n") // No afecta a la variable fuera de la funcion
}

fun cambiarNombrePorReferencia(person: Person) {
    person.name = "NuevoNombre"
}

fun intercambiarPorValor(a: Int, b: Int): Pair<Int, Int>{
    val temporal = a
    val newA = b
    val newB = temporal

    return Pair(newA, newB)
}

fun intercambiarPorReferencia(a: Number, b: Number): Pair<Number,Number>{
    val temporal = a.value
    a.value = b.value
    b.value = temporal

    return Pair(a, b)
}
