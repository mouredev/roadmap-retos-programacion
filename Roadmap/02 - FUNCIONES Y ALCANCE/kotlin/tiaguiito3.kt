// variable global
val soyGlobal = 1 + 2

fun main(args: Array<String>) {
    reto("fizz", "buzz")
    // Funciones de llamda
    uno()
    dos("Tiago")
    println(tres(4, 4))
    println(cuatro(4, 4))
    cinco()
}

// Reto
fun reto(a: String, b: String): Unit {
    for (i in 1..100) {
        when {
            i % 3 == 0 && i % 5 == 0 -> println("$a$b")
            i % 3 == 0 -> println(a)
            i % 5 == 0 -> println(b)
            else -> println(i)
        }
    }
}


// Funciones en Kotlin: llamada y devolucion de valores

// Funcion con variable local
fun uno () {
    val soyLocal = 1 + 3
    println(soyLocal)
    println(soyGlobal)
}

// Funcion con argumentos
fun dos (name: String) {
    println("Hi $name")
    println(soyGlobal)
}

// Funcion con return
fun tres (a: Int, b: Int):Int {
    println(soyGlobal)
    return a * b
}

// Funcion que devuelve sin return
fun cuatro (a: Int, b: Int):Int = a * b

// Funcion dentro de funcion
fun cinco() {
    fun cincoDos(a:Int){
        println(a)
        println(soyGlobal)
    }
    cincoDos(5)
}