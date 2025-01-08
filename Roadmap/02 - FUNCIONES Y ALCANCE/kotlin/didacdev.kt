// Funciones sin parámetros
fun hello() {
    println("hello")
}

// Funciones con parámetros
fun say(person: String, sentence: String) {
    println("$sentence $person")
}

// Argumentos por defecto
fun sayHello(person: String, greet: Boolean = true) {
    if (greet) {
        println("hello $person")
    } else {
        println("bye")
    }
}

// Etiquetas de los argumentos
fun greet(person: String, hometown: String){
    println("hello $person for comming from $hometown")
}

// Parámetros variados
fun greetToPeople(vararg people: String) {
    for (person in people){
        println("hello $person")
    }
}

// Unit return
fun hello(name: String?): Unit {

    if(name != null) {
        println("hello $name")
    } else {
        println("hello there")
    }
}

// Funciones de una sola expresión
fun sumaDos(number: Int): Int = number + 2

// Funciones con retorno
fun sumaUno(number: Int): Int {
    var result = number
    return (result + 1)
}

// Notación infija
infix fun Int.suma(number: Int): Int {
    var result = number
    return (result + 2)
}

// Funciones anidadas
fun sumaDos(number: Int, add: Boolean): Int {
    
    fun suma(number: Int): Int {
        var result = number
        return(result + 2)
    }

    if(add) {
        return suma(number)
    } else {
        return number
    }
}

// Funciones genéricas
fun <T: Number> sumaTres(number: T): Double {
    return number.toDouble() + 3
}

// Tail recursie
tailrec fun sumaUno(number: Int, suma: Boolean): Int = if (suma) (number + 1) else number


// ------------------------- Ejercicio --------------------
fun times(textOne: String, textTwo: String): Int {

    var times = 0

    for (number in 1..100) {

        if(number % 3 == 0) {
            println(textOne)
            times += 1
        } else if (number % 5 == 0) {
            println(textTwo)
            times += 1
        } else if (number % 3 == 0 && number % 5 == 0) {
            println("$textOne $textTwo")
            times += 1
        } else {
            println(number)
        }
    }

    return times
}

fun main() {
    
    hello()
    say("Diego", "hello")
    sayHello("Diego")
    greet(person = "Diego", "Madrid")
    greetToPeople(*arrayOf("Diego", "Pepe"))
    hello("Diego")
    println(sumaDos(2))
    println(sumaUno(1))
    println(2 suma 3)
    println(sumaDos(1, true))
    println(sumaTres(0.1))
    println(sumaUno(3, true))
    println(times("hola", "adios"))
}