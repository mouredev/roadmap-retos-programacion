fun holaMundo() {
    println("Hola Mundo")
}

fun saludo (nombre: String) {
    println("Hola $nombre")
}

fun suma(a: Int, b: Int): Int {
    return a + b
}

// Funcion declarada dentro de funcion

fun funcionInterna() {
    println("Funcion fuera de funcion")
    fun inner() {
        println("Funcion dentro de funcion")
    }
    inner()
}

fun extra(a: String, b: String): Int {
    var contNum = 0
    for (i in 1..100) {
        if (i % 15 == 0) {
            println(a+b)
        }
        else if (i % 3 == 0) {
            println(a)
        }
        else if (i % 5 == 0) {
            println(b)
        }
        else {
            println(i)
            contNum++
        }
    }
    return contNum
}

fun main() {
    holaMundo()
    saludo("Miguel")
    println(suma(5, 5))
    funcionInterna()
    println("Ejemplo de funcion del sistema es hacer que la cadena 'hola' salga en mayusculas: ${"hola".toUpperCase()}")
    println("La cantidad de numeros impresos es ${extra("Fizz", "Buuz")}")
}