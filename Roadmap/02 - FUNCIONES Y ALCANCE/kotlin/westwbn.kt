// Función sin parámetros
fun withoutParameters() {
    println("Función sin parámetros ni retorno")
}

// Función con parámetros
fun employeeData(name: String, age: Int, salary: Int) {
    println("Nombre: $name \nEdad: $age \nSalario: $$salary")
}

// Función con retorno
fun shoppingList(products: List<String>): String {
    return products.joinToString { it }
}

// Función con otra función en su interior

fun calculator(numberOne: Int, numberTwo: Int) {
    fun sum(numberOne: Int, numberTwo: Int): Int = numberOne + numberTwo
    println(sum(numberOne, numberTwo))
}

// Variable global
val globalVariable = "Kotlin"

// Extra
fun extra(dataOne: String, dataTwo: String): Int {
    var count = 0

    for (number in 1..100) {
        when {
            number % 3 == 0 && number % 5 == 0 -> println("$dataOne$dataTwo")
            number % 3 == 0 -> println(dataOne)
            number % 5 == 0 -> println(dataTwo)
            else -> count++
        }
    }
    return count
}


fun main() {
//    Variable local
    val localVariable = "Programando con:"
    withoutParameters()
    employeeData("Daniel", 48, 1500)
    println(shoppingList(listOf("Fideos", "Aceite", "Arroz", "Carne")))
    calculator(12, 18)
    println("$localVariable $globalVariable")
    println(extra("Fizz", "Buzz"))
}