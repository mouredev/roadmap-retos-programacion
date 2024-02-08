// Función sin parámetros ni retorno
fun printHello() {
    println("Hello")
}

// Función con un parámetro
fun printMessage(message: String) {
    println(message)
}

// Función con varios parámetros
fun printSum(a: Int, b: Int) {
    println("La suma de $a y $b es ${a + b}")
}

// Función con retorno
fun sum(a: Int, b: Int): Int {
    return a + b
}

// Función dentro de una función
fun outerFunc() {
    fun innerFunction() {
        println("Esta es una función interna")
    }
    innerFunction()
}

// Variable global
var globalVar = "Soy una variable global"

fun main() {
    printHello()
    printMessage("Este es un mensaje")
    printSum(5, 10)
    println("La suma de 5 y 10 es ${sum(5, 10)}")
    outerFunc()
    // Variable local
    val localVar = "Soy una variable local"
    println(localVar)
    println(globalVar)
    println(reto02("Fizz", "Buzz"))
}

fun reto02(a: String, b: String): Int {
    var num = 0
    for (i in 1..100) {
        when {
            i % 3 == 0 && i % 5 == 0 -> println("$a$b")
            i % 5 == 0 -> println(b)
            i % 3 == 0 -> println(a)
            else -> num++
        }
    }
    return num
}