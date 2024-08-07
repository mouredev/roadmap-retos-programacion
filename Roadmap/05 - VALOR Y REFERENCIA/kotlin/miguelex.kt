class Persona(var name: String, var age: Int)

fun intercambioPorvalor(num1: Int, num2: Int) : Pair<Int, Int> {
    var aux = num1
    var num1 = num2
    var num2 = aux

    return Pair(num1, num2)
}

fun intercambioPorReferencia(persona1: Persona, persona2: Persona): Pair<Persona, Persona>{
    var aux = persona1
    var persona1 = persona2
    var persona2 = aux

    return Pair(persona1, persona2)
}
fun main() {

    var num1 = 1
    var num2 = num1

    println("Valor de las variables por valor")
    println(num1)
    println(num2)

    num1 = 10

    println("Valor de las variables por valor tras modificar num1")
    println(num1)
    println(num2)

    var persona1 = Persona("Miguel", 25)
    var persona2 = persona1

    println("Valor de las variables por referencia")
    println(persona1.name)
    println(persona2.name)

    persona1.name = "Miguel Angel"

    println("Valor de las variables por referencia")
    println(persona1.name)
    println(persona2.name)

    num1 = 5
    num2 = 10

    println("Valor de num1 antes del intercambio = $num1")
    println("Valor de num2 antes del intercambio = $num2")

    var result: Pair<Int, Int> = intercambioPorvalor(num1, num2)

    println("Intercambio de valores entre $num1 y $num2")
    println("Valor de num1 despues del intercambio = $num1")
    println("Valor de num2 despues del intercambio = $num2")
    println("Valor devuelto para num1 en el intercambio = $result.first")
    println("Valor devuelvo para num2 en el intercambio = $result.second")

    persona1 = Persona("Juan", 30)
    persona2 = Persona("María", 40) 

    println("Valor de persona1 antes del intercambio = ${persona1.name}")
    println("Valor de persona2 antes del intercambio = ${persona2.name}")

    var result2: Pair<Persona, Persona> = intercambioPorReferencia(persona1, persona2)

    println("Intercambio de valores entre ${persona1.name} y ${persona2.name}")
    println("Valor de persona1 despues del intercambio = ${persona1.name}")

    println("Valor de persona2 despues del intercambio = ${persona2.name}")
    println("Valor devuelto para persona1 en el intercambio = ${result2.first.name}")
    println("Valor devuelvo para persona2 en el intercambio = ${result2.second.name}")


}